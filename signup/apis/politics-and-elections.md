# Politics & Elections APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [ACLED API](https://acleddata.com/acled-api-documentation) | Armed conflict event data (Africa origin, now global; free key with registration) | `https://acleddata.com/api/acled/read?country=Nigeria&limit=5` |  | Africa | free key | 403 |
| [Congress.gov API](https://api.congress.gov/) | Bills, amendments, members, committees, nominations, treaties, Congressional Record | `https://api.congress.gov/v3/bill?api_key=DEMO_KEY&format=json` | 5,000 req/hr; api.data.gov key | US | free key | 200 |
| [CongressInvests](https://congressinvests.com) | Real-time U.S. congressional stock trade disclosures from Senate EFD and House Clerk \| apiKey | docs only |  | global | free key | 200 |
| [Congressional Stock Brain](https://congressionalstockbrain.com) | AI-powered tool scoring U.S. STOCK Act lawmaker trade disclosures for retail investors | docs only |  | global | payment required | 402 |
| [Democracy Club Developers API (WhereDoIVote)](https://developers.democracyclub.org.uk/api/v1/) | Polling stations and ballots by postcode | `https://developers.democracyclub.org.uk/api/v1/postcode/SW1A1AA/?auth_token=YOUR_KEY` | free key | UK | free key | 401 |
| [Disclosed Capitol](https://www.disclosedcapitol.com/data-files/api) | US congressional \& executive-branch stock trade disclosures (STOCK Act + OGE) | docs only |  | global | free key | 200 |
| [FEC](https://api.open.fec.gov/developers/) | Information on campaign donations in federal elections | docs only |  | global | free key | 200 |
| [Google Civic Information API](https://developers.google.com/civic-information) | US divisions, representatives by division, elections and voter info (Representatives endpoint retired Apr 2025) | `https://www.googleapis.com/civicinfo/v2/elections?key=YOUR_KEY` | Google API key | US | free key | 400 |
| [IEC South Africa Results API](https://api.elections.org.za/) | Electoral Commission of SA election results (free registration) | docs only |  | ZA | free key | 200 |
| [LegiScan API](https://legiscan.com/legiscan) | State and federal bill tracking, full text, roll calls | `https://api.legiscan.com/?key=YOUR_KEY&op=getSessionList&state=CA` | 30,000 queries/month free | US | free key | 200 |
| [LegiScan Datasets](https://legiscan.com/datasets) | Weekly bulk JSON/CSV per state session (needs key) | docs only | free key | US | free key | 403 |
| [Manifesto Project API](https://manifesto-project.wzb.eu/information/documents/api) | Party manifesto coding data for 1000+ parties | `https://manifesto-project.wzb.eu/api/v1/list_core_versions?api_key=YOUR_KEY` | free key | global | free key | 200 |
| [NEC Election API (data.go.kr)](https://www.data.go.kr/data/15000864/openapi.do) | National Election Commission results via data.go.kr | docs only | free | KR | free key | 200 |
| [NY Senate Open Legislation API](https://legislation.nysenate.gov/static/docs/html/index.html) | New York bills, members, votes; free key by email | `https://legislation.nysenate.gov/api/3/bills/2025?limit=1` | free key | US-NY | free key | 401 |
| [NY State Senate Open Legislation API](https://legislation.nysenate.gov/static/docs/html/) | New York bills, laws, agendas, calendars | `https://legislation.nysenate.gov/api/3/bills/2023?key=YOUR_KEY` | free key | US-NY | free key | 401 |
| [Open States API v3](https://docs.openstates.org/api-v3/) | State legislators, bills and votes across 50 states | `https://v3.openstates.org/jurisdictions` | Free key; 250 req/day | US | free key | 200 |
| [Open States API v3 (state legislatures)](https://docs.openstates.org/api-v3/) | Bills, votes, legislators for all 50 states + DC + PR via REST | `https://v3.openstates.org/docs` | free key; 250 req/day, 10/min | US | free key | 200 |
| [OpenAustralia API](https://www.openaustralia.org.au/api/) | Hansard, MPs and senators (community, OpenAustralia Foundation) | `https://www.openaustralia.org.au/api/getRepresentatives?key=KEY&output=js` | free key | AU | free key | 200 |
| [OpenFEC API](https://api.open.fec.gov/developers/) | US campaign finance: candidates, committees, contributions, expenditures | `https://api.open.fec.gov/v1/candidates/?api_key=DEMO_KEY&per_page=5` | 1,000 req/hr; api.data.gov key | US | free key | 200 |
| [OpenStates](https://openstates.org/api/) | US state legislature bills and lawmakers | docs only |  | global | free key | 200 |
| [ProPublica Congress](https://projects.propublica.org/api-docs/congress-api/) | Congress data | `https://api.propublica.org/congress/v1/118/senate/members.json` | 5000/day | US | free key | 200 |
| [Regulations.gov API v4](https://open.gsa.gov/api/regulationsgov/) | Rulemaking dockets, documents and public comments | `https://api.regulations.gov/v4/documents?api_key=DEMO_KEY&page[size]=5` | DEMO\_KEY works; free key | US | free key | 200 |
| [They Vote For You API](https://theyvoteforyou.org.au/help/data) | How Australian MPs vote on divisions and policies (OpenAustralia Foundation) | `https://theyvoteforyou.org.au/api/v1/people.json?key=KEY` | free key | AU | free key | 401 |
| [TheyWorkForYou API](https://www.theyworkforyou.com/api/) | UK MPs/Lords/MSPs debates, written answers, votes | `https://www.theyworkforyou.com/api/getMPs?key=YOUR_KEY&output=js` | free key for low volume non-commercial | UK | free key | 200 |
| [UCDP API](https://ucdp.uu.se/apidocs/) | Uppsala Conflict Data Program events and conflicts | `https://ucdpapi.pcr.uu.se/api/gedevents/24.1?pagesize=5` | token now required | global | free key | 401 |
