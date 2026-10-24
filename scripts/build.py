#!/usr/bin/env python3
"""Build the catalogue from atlas.json: python3 scripts/build.py path/to/atlas.json

Dedupes across all sections, scrubs credential-like values, splits rows into
open / signup / unreachable and writes README.md, open/, signup/ and data/.
Stdlib only; output is deterministic.
"""
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote, parse_qsl, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SECTIONS = ["apis", "rpc", "portals", "feeds", "cloud"]
GROUPS = ["open", "signup", "unreachable"]
MAX_MD = 350_000  # bytes; GitHub stops rendering much beyond this
DESC_MAX = 220

# ---- secrets scrub ---------------------------------------------------------
# Documented public demo keys / test accounts: BART, Ghost demo site, Europeana,
# Tankerkoenig demo, EPA AQS test login, Google's public Firebase JWK endpoint,
# EU sanctions files public token (base64 of "token-2017").
PUBLIC = {"MW9S-E7SL-26DU-VV8V", "22444f78447824223cefc48062", "api2demo",
          "00000000-0000-0000-0000-000000000002", "test@aqs.api",
          "securetoken@system.gserviceaccount.com", "dG9rZW4tMjAxNw"}
CRED_NAME = re.compile(r"(?:api[_-]?(?:key|token)|access[_-]?(?:key|token)|client[_-]?secret"
                       r"|(?:subscription|service|application|auth)[_-]?key|app[_-]?id"
                       r"|key|token|secret|auth|authorization|password|pass|pwd|wskey)", re.I)
ID_NAME = {"id", "path", "request", "series", "organization", "__t__"}  # long hex ids, not secrets
PARAM = re.compile(r"([?&;])([\w.\-]+)=([^&#\s\"'<>]*)")
EMAIL = re.compile(r"[\w.+-]+@[A-Za-z][\w-]*(?:\.[\w-]+)*\.([A-Za-z]{2,})")
FILE_EXT = {"png", "jpg", "jpeg", "gif", "svg", "pst", "css", "js"}
PATH_TOKEN = re.compile(r"epat_\w+|(?<=nodereal\.io/v1/)[0-9a-f]{32}|(?<=dwellir\.com/)[0-9a-f-]{36}")
# Rows that do not belong in a public catalogue: unresolvable hosts, adult content.
EXCLUDE_NAMES = {"Lustpress API", "Danbooru"}
KNOWN_BAD = {l.split("\t")[0] for l in (ROOT / "scripts/known-bad.tsv").read_text().splitlines() if l and l[0] != "#"}
LOCAL_HOST = re.compile(r"^https?://(?:[\w-]+\.local\b|localhost\b|127(?:\.\d+){3}|10(?:\.\d+){3}|192\.168\.\d+\.\d+)")
PRIVATE_KEY = re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----.*?(?:-----END [A-Z ]*PRIVATE KEY-----|$)", re.S)


def placeholder(v):
    """True for placeholders, documented public keys and short plain values (tag keys, search terms)."""
    v = unquote(v)
    return v in PUBLIC or not (len(v) >= 10 and (re.search(r"\d", v) or v.lower() != v != v.upper())) or bool(re.fullmatch(
        r"[{<\[].*[}>\]]|[A-Z][A-Z_]{0,23}|(?i:x+|0+|demo|test|example|your.*)|\d{1,8}|.?", v))


def scrub(text, where, hits):
    """Replace credential-like values in text; append (where, kind, first 4 chars) to hits."""
    def param(m):
        sep, name, val = m.groups()
        secret = CRED_NAME.fullmatch(name) or (name.lower() not in ID_NAME and re.fullmatch(r"[0-9a-fA-F]{24,}", val))
        if not secret or placeholder(val):
            return m.group()
        hits.append((where, name, val[:4]))
        return f"{sep}{name}=YOUR_KEY"

    def email(m):
        if m.group() in PUBLIC or m.group(1).lower() in FILE_EXT or re.search(r"@(?:[\w-]+\.)*example\.(?:com|org|net)$", m.group()):
            return m.group()
        hits.append((where, "email", m.group()[:4]))
        return "user@example.com"

    def block(m):
        hits.append((where, "private key", m.group()[:4]))
        return "YOUR_KEY"

    def path(m):
        hits.append((where, "path", m.group()[:4]))
        return "YOUR_KEY"

    return EMAIL.sub(email, PARAM.sub(param, PATH_TOKEN.sub(path, PRIVATE_KEY.sub(block, text))))


# ---- dedupe ----------------------------------------------------------------
def norm_url(url):
    """Lowercase host, no www., scheme/default port/fragment/trailing slash ignored, sorted query."""
    p = urlsplit(url.strip())
    try:
        port = p.port if p.port not in (80, 443) else None
    except ValueError:
        port = None
    host = (p.hostname or "").lower().removeprefix("www.")
    return host, port, p.path.rstrip("/"), tuple(sorted(parse_qsl(p.query, keep_blank_values=True)))


def dup_key(r):
    if "e" in r:  # "POST https://x {body}" keeps method and body in the key
        parts = r["e"].split(None, 2)
        method = parts.pop(0) if parts[0].isupper() else None
        if r["section"] == "rpc" or '"jsonrpc"' in r["e"]:  # one node, however it was probed
            method, parts = None, parts[:1]
        return ("e", method, norm_url(parts[0]), " ".join(parts[1:]))
    return ("u", norm_url(r["u"]), r["n"].lower())


def rank(r, i):
    """Keeper order: specific section, 2xx, verified, longest description, input order."""
    return (r["section"] == "apis", not 200 <= r["s"] < 300, r.get("v") != 1, -len(r["d"]), i)


def dedupe(rows, counts):
    sets = defaultdict(list)
    for i, r in enumerate(rows):
        sets[dup_key(r)].append(i)
    kept = []
    for idxs in sets.values():
        k = min(idxs, key=lambda i: rank(rows[i], i))
        keeper = dict(rows[k])
        for i in idxs:
            if i != k:
                counts["dropped"][rows[i]["section"]] += 1
        if len({rows[i]["a"] for i in idxs}) > 1:
            counts["conflicts"] += 1
            if keeper["a"] != "key" and any(rows[i]["s"] in (401, 402, 403) for i in idxs):
                keeper["a"] = "key"
                counts["to_key"] += 1
        kept.append((k, keeper))
    return [r for _, r in sorted(kept, key=lambda x: x[0])]


def group_of(r):
    if r["s"] == 0:
        return "unreachable"
    return "signup" if r["a"] == "key" or r["s"] in (401, 402) else "open"


# ---- markdown --------------------------------------------------------------
def esc(s):
    return re.sub(r"([\\`|*_\[\]<>&~])", r"\\\1", " ".join((s or "").split()))


def link(name, url):
    if not url.startswith(("http://", "https://")):  # one source row has a mangled "ttp://" url
        return esc(name)
    return f"[{esc(name)}]({re.sub(r'[()|`<>\s]', lambda m: f'%{ord(m.group()):02X}', url)})"


def example(e):
    return "docs only" if e is None else "`" + " ".join(e.split()).replace("`", "%60").replace("|", "\\|") + "`"


AUTH = {"none": "none", "key": "free key", "unknown": "unconfirmed, check docs"}


def row_md(r, wide):
    auth = {401: "key required", 402: "payment required"}.get(r["s"]) if r["a"] != "key" else None
    d = " ".join(r["d"].split())
    cells = [link(r["n"], r["u"]), esc(d if len(d) <= DESC_MAX else d[:DESC_MAX - 1] + "…"),
             example(r.get("e")), esc(r.get("l")), esc(r["r"]), auth or AUTH[r["a"]], str(r["s"])]
    if wide:
        cells = [esc(r["c"]), esc(r["p"])] + cells
    return "| " + " | ".join(cells) + " |"


def sort_key(r, wide):
    return ((r["c"].casefold(),) if wide else ()) + (r["n"].casefold(), r["n"], r.get("e", ""))


def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def write_table(group, stem, title, rows, wide):
    """Write rows as <stem>.md, or <stem>-part-N.md chunks when too big. Returns [(file name, rows)]."""
    rows = sorted(rows, key=lambda r: sort_key(r, wide))
    head = ["Category", "Type"] * wide + ["Name", "Description", "Example call", "Limits", "Region", "Auth", "Status"]
    up = "README.md" if wide else "../README.md"
    header = "| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n"
    lines = [row_md(r, wide) + "\n" for r in rows]
    chunks, cur, size = [], [], 0
    for line in lines:
        if cur and size + len(line.encode()) > MAX_MD - 2000:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(line)
        size += len(line.encode())
    chunks.append(cur)
    out = []
    for i, chunk in enumerate(chunks, 1):
        name = f"{stem}.md" if len(chunks) == 1 else f"{stem}-part-{i}.md"
        t = title if len(chunks) == 1 else f"{title} (part {i} of {len(chunks)})"
        write(ROOT / group / name, f"# {t}\n\n[Back to the {group} index]({up})\n\n{header}{''.join(chunk)}")
        out.append((name, len(chunk)))
    return out


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower().replace("&", "and")).strip("-")


def links(files):
    return ", ".join(f"[part {i}]({n})" for i, (n, _) in enumerate(files, 1))


def write_group(group, rows):
    by = defaultdict(list)
    for r in rows:
        by[r["section"]].append(r)
    idx = [f"# {group.capitalize()} endpoints\n",
           {"open": "Endpoints that answered without a signup. Check the Auth column: "
                    "\"unconfirmed, check docs\" means the source did not say whether a key is needed.",
            "signup": "Endpoints that need a free signup or key (or payment, on a 402). "
                      "The example call shows the shape; replace `YOUR_KEY` with your own."}[group] + "\n",
           f"Total: {len(rows):,}. [Back to the main README](../README.md)\n"]
    cats = defaultdict(list)
    for r in by["apis"]:
        cats[r["c"]].append(r)
    assert len({slug(c) for c in cats}) == len(cats), "category slug collision"
    if cats:
        idx.append(f"## APIs ({len(by['apis']):,})\n")
        for c in sorted(cats, key=str.casefold):
            files = write_table(group, f"apis/{slug(c)}", f"{c} APIs", cats[c], False)
            where = f"[{c}]({files[0][0]})" if len(files) == 1 else f"{c}: " + links(files)
            idx.append(f"- {where} ({len(cats[c]):,})")
        idx.append("")
    for sec in SECTIONS[1:]:
        if by[sec]:
            title = "RPC" if sec == "rpc" else sec.capitalize()
            files = write_table(group, sec, title, by[sec], True)
            idx.append(f"## {title} ({len(by[sec]):,})\n\n" +
                       (f"[{sec}.md]({sec}.md)" if len(files) == 1 else links(files)) + "\n")
    write(ROOT / group / "README.md", "\n".join(idx))


README = """# Aggregated Public Endpoints

{total:,} free public endpoints, deduplicated and sorted by what you need to use them: {open:,} work without
a signup, {signup:,} need a free key or signup, and {unreachable:,} did not answer when checked (kept as data only).

## Counts

| Section | Rows in | Duplicates dropped | Open | Signup | Unreachable |
|---|---:|---:|---:|---:|---:|
{counts}

## Contents

- [open/](open/README.md): no signup needed, by category
- [signup/](signup/README.md): needs a free key or signup, by category
- [data/open.jsonl](data/open.jsonl), [data/signup.jsonl](data/signup.jsonl),
  [data/unreachable.jsonl](data/unreachable.jsonl): full records, one JSON object per line, with a `section` field.
  The unreachable rows are not listed in the markdown.

## Reading a row

Each table row is name and docs link, description, one example call, stated limits, region, auth and the HTTP
status the example call returned. A row marked "docs only" has no example call and was never called, so its status is not an API response.

- 2xx: the call was answered.
- 3xx: it redirected; follow the redirect.
- 400, 405, 422: the endpoint answered but the probe was refused or malformed. Read the docs for the right request.
- 401, 402, 403 on a key row: it wants its key (402 is payment). A 403 on a keyless row stays under open and
  usually means the checker was blocked.
- 429: rate limited during the check.
- 0: no answer at all (unreachable).

## Rebuild

`python3 scripts/build.py path/to/atlas.json` regenerates everything in this repository except the script itself.

## Sources

Compiled from community API lists plus original research, live-checked {date}. Descriptions belong to their projects.
"""


def bare_url(e):
    """The URL of an endpoint string, without a leading HTTP method and trailing body ("POST https://x {...}")."""
    parts = e.split(None, 2)
    return parts[1] if len(parts) > 1 and parts[0].isupper() else e


# Listed URLs (no method or body) in dedupe's normal form, so "POST <url> {body}", a reordered query or a
# trailing slash cannot hide a listed endpoint. Listed POST forms with a body still match only exactly.
KNOWN_BAD_URLS = {norm_url(k) for k in KNOWN_BAD if bare_url(k) == k}


def known_bad(e):
    """Raw or credential-scrubbed endpoint, or its bare URL, listed in scripts/known-bad.tsv."""
    if not e:
        return False
    urls = {bare_url(e)}
    urls |= {scrub(u, "", []) for u in urls}
    return bool({e, scrub(e, "", [])} & KNOWN_BAD or urls & KNOWN_BAD or any(norm_url(u) in KNOWN_BAD_URLS for u in urls))


def main(path):
    atlas = json.loads(Path(path).read_text(encoding="utf-8"))
    assert set(atlas) == {"date", *SECTIONS}, "unexpected atlas sections"
    rows = [{**r, "section": s} for s in SECTIONS for r in atlas[s]
            if r["n"] not in EXCLUDE_NAMES and not known_bad(r.get("e")) and not LOCAL_HOST.match(r.get("e") or r["u"])]
    print(f"excluded {sum(map(len, (atlas[s] for s in SECTIONS))) - len(rows)} rows (adult content, local hosts, known-bad hosts)")
    counts = {"dropped": Counter(), "conflicts": 0, "to_key": 0}
    kept = dedupe(rows, counts)
    hits = []
    for r in kept:
        for f, v in r.items():
            if isinstance(v, str):
                n = len(hits)
                r[f] = scrub(v, f"{r['section']}/{r['n']}/{f}", hits)
                if f == "e" and any(h[1] not in ("email", "private key") for h in hits[n:]):
                    r["a"] = "key"  # the example only worked with a key baked in
    grouped = {g: [r for r in kept if group_of(r) == g] for g in GROUPS}
    dropped = sum(counts["dropped"].values())
    assert len(rows) == sum(map(len, grouped.values())) + dropped, "row identity broken"

    for d in ("open", "signup"):
        shutil.rmtree(ROOT / d, ignore_errors=True)
    for g in GROUPS:
        write(ROOT / "data" / f"{g}.jsonl", "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in grouped[g]))
    write_group("open", grouped["open"])
    write_group("signup", grouped["signup"])
    table = []
    for s in SECTIONS:
        n = Counter(r["section"] for r in rows)[s]
        by = [sum(r["section"] == s for r in grouped[g]) for g in GROUPS]
        table.append(f"| {s} | {n:,} | {counts['dropped'][s]:,} | " + " | ".join(f"{x:,}" for x in by) + " |")
    table.append(f"| **Total** | {len(rows):,} | {dropped:,} | " + " | ".join(f"{len(grouped[g]):,}" for g in GROUPS) + " |")
    write(ROOT / "README.md", README.format(total=len(rows) - dropped, date=atlas["date"], counts="\n".join(table),
                                            **{g: len(grouped[g]) for g in GROUPS}))

    print("\n".join(["section | in | dropped | open | signup | unreachable"] +
                    [t.replace("**", "").replace(",", "") for t in table]))
    print(f"auth conflicts among duplicates: {counts['conflicts']}, resolved to key: {counts['to_key']}")
    print(f"scrubbed {len(hits)} values:")
    for h in hits:
        print("  ", *h)


if __name__ == "__main__":
    main(sys.argv[1])
