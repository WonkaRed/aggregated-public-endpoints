# Aggregated Public Endpoints

31,509 free public endpoints, deduplicated and sorted by what you need to use them: 28,304 work without
a signup, 2,740 need a free key or signup, and 465 did not answer when checked (kept as data only).

## Counts

| Section | Rows in | Duplicates dropped | Open | Signup | Unreachable |
|---|---:|---:|---:|---:|---:|
| apis | 25,895 | 94 | 22,542 | 2,727 | 465 |
| rpc | 2,153 | 1 | 2,118 | 5 | 0 |
| portals | 449 | 1 | 445 | 0 | 0 |
| feeds | 2,346 | 2 | 2,336 | 7 | 0 |
| cloud | 877 | 13 | 863 | 1 | 0 |
| **Total** | 31,720 | 111 | 28,304 | 2,740 | 465 |

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

## Re-verification (2026-10-20)

Every open (no-signup) endpoint was re-called live: up to 3 attempts with backoff, then every endpoint still
failing was independently re-checked with curl, a browser user agent and a longer timeout, and any RPC row that
only 404'd on a plain GET got one more retry as a proper JSON-RPC POST (standard JSON-RPC nodes only implement
POST). 100 endpoints never answered correctly across every attempt and were dropped from the open set: 81 dead
and 19 now needing a key or payment (401/402). A plain 403 on a keyless row was kept either way, per this repo's
own convention that it usually means the checker got blocked, not that a key is now required. Dropped rows and
their reason are in [data/removed_open.jsonl](data/removed_open.jsonl); re-run with
`python3 scripts/verify_open.py` going forward. These 100 are not counted in the "Duplicates dropped" column
above, only subtracted from Open.

## Rebuild

`python3 scripts/build.py path/to/atlas.json` regenerates everything in this repository except the script itself.

## Sources

Compiled from community API lists plus original research, live-checked 2026-10-19. Descriptions belong to their projects.
