# Aggregated Public Endpoints

30,960 free public endpoints, deduplicated and sorted by what you need to use them: 27,761 work without
a signup, 2,735 need a free key or signup, and 464 did not answer when checked (kept as data only).

## Counts

| Section | Rows in | Duplicates dropped | Open | Signup | Unreachable |
|---|---:|---:|---:|---:|---:|
| apis | 25,870 | 89 | 22,595 | 2,722 | 464 |
| rpc | 1,524 | 1 | 1,518 | 5 | 0 |
| portals | 449 | 1 | 448 | 0 | 0 |
| feeds | 2,346 | 2 | 2,337 | 7 | 0 |
| cloud | 877 | 13 | 863 | 1 | 0 |
| **Total** | 31,066 | 106 | 27,761 | 2,735 | 464 |

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

Compiled from community API lists plus original research, live-checked 2026-10-19. Descriptions belong to their projects.
