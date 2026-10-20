#!/usr/bin/env python3
"""Re-verify every row in data/open.jsonl still works without a key, and prune what doesn't.

python3 scripts/verify_open.py          # probe + prune in one run
python3 scripts/verify_open.py --probe-only   # just write data/verify_result.jsonl

Mindful-of-false-positive/negative rules, learned the hard way on 2026-10-20:
- Each call gets up to 3 attempts with backoff; one attempt succeeding beats any
  number of failed ones, to absorb a transient block or rate limit.
- A keyless row that answers 403 on every attempt is NOT removed: per this repo's
  own documented convention (see README's "Reading a row"), 403 on an unauthenticated
  row usually means the checker got blocked, not that a key is now required. Only a
  confirmed 401 or 402 counts as "needs a key/payment".
- An RPC row that 404s a plain GET is retried once as a JSON-RPC POST (eth_chainId)
  before being called dead: standard JSON-RPC nodes only implement POST, so a bare
  GET recheck is inconclusive for them.
- 2xx/3xx/400/405/406/409/413/415/418/422/429 count as "answered" (alive): the
  server responded, even if this specific probe shape was wrong.
- Only a real connection failure/timeout, or a persistent 404/410/5xx, is "dead".
- Docs-only rows (no "e" example call) are left untouched; there is nothing to call.
"""
import argparse
import asyncio
import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import build  # noqa: E402  (reuse its markdown/table writers)

OPEN_FILE = ROOT / "data" / "open.jsonl"
REMOVED_FILE = ROOT / "data" / "removed_open.jsonl"
RESULT_FILE = ROOT / "data" / "verify_result.jsonl"
README_FILE = ROOT / "README.md"

CONCURRENCY = 40
TIMEOUT = 15
MAX_ATTEMPTS = 3
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
ANSWERED_MALFORMED = {400, 405, 406, 409, 413, 415, 418, 422, 429}
RPC_PROBE_BODY = '{"jsonrpc":"2.0","method":"eth_chainId","params":[],"id":1}'


def parse_call(e):
    parts = e.split(None, 2)
    if parts and parts[0].isupper() and parts[0] in ("GET", "POST", "PUT", "PATCH", "DELETE", "HEAD"):
        return parts[0], parts[1] if len(parts) > 1 else "", parts[2] if len(parts) > 2 else None
    return "GET", e, None


async def curl_status(method, url, body, timeout):
    cmd = ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "--max-time", str(timeout), "-A", UA, "-X", method]
    if body:
        cmd += ["-H", "Content-Type: application/json", "--data-raw", body]
    cmd.append(url)
    try:
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
        out, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout + 5)
        code = out.decode().strip()
        return int(code) if code.isdigit() else 0
    except Exception:
        return 0


async def curl_body(method, url, body, timeout):
    cmd = ["curl", "-s", "--max-time", str(timeout), "-A", UA, "-X", method]
    if body:
        cmd += ["-H", "Content-Type: application/json", "--data-raw", body]
    cmd.append(url)
    try:
        proc = await asyncio.create_subprocess_exec(*cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.DEVNULL)
        out, _ = await asyncio.wait_for(proc.communicate(), timeout=timeout + 5)
        return out.decode(errors="replace").strip()
    except Exception:
        return ""


async def probe_row(idx, row, sem):
    url = row.get("e")
    if not url:
        return {"i": idx, "n": row["n"], "verdict": "keep_docs_only", "detail": "no example call"}

    method, call_url, body = parse_call(url)
    statuses = []
    async with sem:
        for attempt in range(MAX_ATTEMPTS):
            status = await curl_status(method, call_url, body, TIMEOUT)
            statuses.append(status)
            if status and (200 <= status < 400 or status in ANSWERED_MALFORMED):
                return {"i": idx, "n": row["n"], "verdict": "keep", "detail": f"status={status} attempt={attempt + 1}"}
            if attempt < MAX_ATTEMPTS - 1:
                await asyncio.sleep(1.5 * (attempt + 1) + random.random())

        if row["section"] == "rpc" and statuses[-1] in (404, 405) and method == "GET":
            rpc_body = await curl_body("POST", call_url, RPC_PROBE_BODY, TIMEOUT)
            if rpc_body.startswith("{") and rpc_body.endswith("}"):
                return {"i": idx, "n": row["n"], "verdict": "keep", "detail": "rpc POST eth_chainId answered"}

    final = statuses[-1]
    if final in (401, 402):
        return {"i": idx, "n": row["n"], "verdict": "remove_key", "detail": f"statuses={statuses} needs key/payment"}
    if final == 403:
        return {"i": idx, "n": row["n"], "verdict": "keep", "detail": "403-only: checker likely blocked, stays open"}
    return {"i": idx, "n": row["n"], "verdict": "remove_dead", "detail": f"statuses={statuses}"}


async def probe_all(rows):
    sem = asyncio.Semaphore(CONCURRENCY)
    tasks = [asyncio.create_task(probe_row(i, row, sem)) for i, row in enumerate(rows)]
    done = 0
    with RESULT_FILE.open("w") as out:
        for fut in asyncio.as_completed(tasks):
            res = await fut
            out.write(json.dumps(res) + "\n")
            done += 1
            if done % 500 == 0 or done == len(rows):
                print(f"{done}/{len(rows)}", file=sys.stderr)


def prune_and_rebuild(open_rows):
    results = {}
    for line in RESULT_FILE.read_text().splitlines():
        if line.strip():
            r = json.loads(line)
            results[r["i"]] = r

    kept, removed = [], []
    for i, row in enumerate(open_rows):
        v = results[i]["verdict"]
        (kept if v in ("keep", "keep_docs_only") else removed).append((row, results[i]) if v not in ("keep", "keep_docs_only") else row)

    removed_rows = [(row, res) for row, res in removed]
    print(f"keeping {len(kept)}, removing {len(removed_rows)}: " +
          str(Counter(res["verdict"] for _, res in removed_rows)))

    REMOVED_FILE.write_text("".join(
        json.dumps({**row, "_removed_reason": res["verdict"], "_removed_detail": res["detail"]}, ensure_ascii=False) + "\n"
        for row, res in removed_rows))
    OPEN_FILE.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in kept))

    for d in ROOT.glob("open/**/*"):
        if d.is_file():
            d.unlink()
    build.write_group("open", kept)

    removed_by_section = Counter(row["section"] for row, _ in removed_rows)
    dead = sum(1 for _, res in removed_rows if res["verdict"] == "remove_dead")
    keyed = sum(1 for _, res in removed_rows if res["verdict"] == "remove_key")

    readme = README_FILE.read_text()
    m = re.search(r"(\d[\d,]*) free public endpoints, deduplicated and sorted by what you need to use them: "
                  r"(\d[\d,]*) work without\na signup", readme)
    assert m, "could not find prose totals in README.md"
    old_total, old_open = (int(x.replace(",", "")) for x in m.groups())
    n = len(removed_rows)
    readme = readme.replace(m.group(0),
                             f"{old_total - n:,} free public endpoints, deduplicated and sorted by what you need to use them: "
                             f"{old_open - n:,} work without\na signup")

    tot = re.search(r"\| \*\*Total\*\* \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|", readme)
    assert tot, "could not find totals row in README.md"
    t_in, t_dup, t_open, t_signup, t_unreach = (int(x.replace(",", "")) for x in tot.groups())
    readme = readme.replace(tot.group(0),
                             f"| **Total** | {t_in:,} | {t_dup:,} | {t_open - n:,} | {t_signup:,} | {t_unreach:,} |")

    for sec in build.SECTIONS:
        k = removed_by_section.get(sec, 0)
        if not k:
            continue
        row_re = re.compile(rf"\| {sec} \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \| ([\d,]+) \|")
        m2 = row_re.search(readme)
        assert m2, f"could not find {sec} row in README.md"
        s_in, s_dup, s_open, s_signup, s_unreach = (int(x.replace(",", "")) for x in m2.groups())
        readme = row_re.sub(f"| {sec} | {s_in:,} | {s_dup:,} | {s_open - k:,} | {s_signup:,} | {s_unreach:,} |", readme, count=1)

    note = (f"## Re-verification\n\n"
            f"Every open (no-signup) endpoint is re-called live by `scripts/verify_open.py`: up to 3 attempts "
            f"with backoff, a 403-only result stays open (the checker likely got blocked, not the endpoint), "
            f"and an RPC row that 404s a GET gets one retry as a proper JSON-RPC POST. {n:,} endpoints failed "
            f"every attempt and were dropped from the open set this run: {dead:,} dead, {keyed:,} now needing a "
            f"key or payment (401/402). Dropped rows and their reason are in "
            f"[data/removed_open.jsonl](data/removed_open.jsonl).\n\n## Rebuild")
    readme = re.sub(r"## Re-verification.*?## Rebuild", note, readme, count=1, flags=re.S) if "## Re-verification" in readme \
        else readme.replace("## Rebuild", note)
    README_FILE.write_text(readme)
    print("README.md updated")


async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe-only", action="store_true", help="only write data/verify_result.jsonl, skip pruning")
    args = ap.parse_args()

    open_rows = [json.loads(line) for line in OPEN_FILE.read_text().splitlines() if line.strip()]
    await probe_all(open_rows)
    if not args.probe_only:
        prune_and_rebuild(open_rows)


if __name__ == "__main__":
    asyncio.run(main())
