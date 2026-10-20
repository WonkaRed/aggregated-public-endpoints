# Law & Courts APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [CanLII API](https://github.com/canlii/API_documentation) | Canadian case law and legislation metadata (free key on request) | `https://api.canlii.org/v1/caseBrowse/en/?api_key=KEY` |  | CA | free key | 403 |
| [CNJ DataJud API](https://datajud-wiki.cnj.jus.br/api-publica/) | Brazilian court case metadata from all tribunals (public key in docs) | `https://api-publica.datajud.cnj.jus.br/api_publica_tjsp/_search` | public APIKey in docs | BR | free key | 401 |
| [Court Rules](https://www.courtrules.app/api) | Free reference for U.S. federal court rules, local rules, judge standing orders and court holidays, with a deadline calculator, a public API and an MCP server. | docs only |  | global | free key | 200 |
| [CourtListener Citation Lookup](https://www.courtlistener.com/help/api/rest/citation-lookup/) | Resolve and verify legal citations in text (anti-hallucination) | `https://www.courtlistener.com/api/rest/v4/citation-lookup/` | 60 citations/min | US | free key | 401 |
| [CourtListener Financial Disclosures](https://www.courtlistener.com/help/api/rest/financial-disclosures/) | Federal judges' financial disclosures | `https://www.courtlistener.com/api/rest/v4/financial-disclosures/` | free token | US | free key | 401 |
| [CourtListener Judges (people) API](https://www.courtlistener.com/help/api/rest/judges/) | Judges' positions, education, political affiliations | `https://www.courtlistener.com/api/rest/v4/people/` | free token | US | free key | 401 |
| [CourtListener Oral Arguments](https://www.courtlistener.com/help/api/rest/oral-arguments/) | Oral argument audio from federal appellate courts | `https://www.courtlistener.com/api/rest/v4/audio/` | free token | US | free key | 401 |
| [CourtListener RECAP / PACER archive](https://www.courtlistener.com/help/api/rest/pacer/) | Free mirror of PACER federal dockets and documents via RECAP | `https://www.courtlistener.com/api/rest/v4/dockets/?court=dcd` | free token | US | free key | 401 |
| [eCourtsIndia](https://ecourtsindia.com/api) | Indian court case status, judgments, and hearing schedule API | docs only |  | global | free key | 200 |
| [EUR-Lex webservice (SOAP)](https://eur-lex.europa.eu/content/help/data-reuse/webservice.html) | EUR-Lex expert search webservice | `https://eur-lex.europa.eu/content/help/data-reuse/webservice.html` | free registration | EU | free key | 202 |
| [FBI Crime Data Explorer API](https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/docApi) | UCR/NIBRS crime counts by agency/state; free api.data.gov key | `https://api.usa.gov/crime/fbi/cde/agency/byStateAbbr/VA?API_KEY=DEMO_KEY` |  | US | free key | 200 |
| [Free Law Project Juriscraper data via CourtListener webhooks](https://www.courtlistener.com/help/api/webhooks/) | Push alerts for new dockets/opinions | docs only | free token | US | free key | 200 |
| [govinfo API](https://api.govinfo.gov/docs/) | US GPO: Congressional Record, US Code, CFR, Federal Register, bills, court opinions (USCOURTS) | `https://api.govinfo.gov/collections?api_key=DEMO_KEY` | api.data.gov key; DEMO\_KEY works | US | free key | 200 |
| [Judilibre API (Cour de cassation)](https://www.courdecassation.fr/acces-rapide-judilibre) | Open case law of the Cour de cassation (PISTE key) | `https://api.piste.gouv.fr/cassation/judilibre/v1.0/search?query=contrat` |  | FR | free key | 400 |
| [Korea Law Open API](https://open.law.go.kr/LSO/openApi/guideList.do) | Ministry of Government Legislation law search/text | `https://www.law.go.kr/DRF/lawSearch.do?OC=test&target=law&type=JSON&query=%EB%AF%BC%EB%B2%95` | free OC id | KR | free key | 200 |
| [Légifrance PISTE API](https://piste.gouv.fr/) | French legislation and case law (free PISTE account key) | `https://api.piste.gouv.fr/dila/legifrance/lf-engine-app/` |  | FR | free key | 400 |
| [NZ Legislation API](https://api.legislation.govt.nz/docs/) | New Zealand legislation API | `https://api.legislation.govt.nz/docs/` | free key | NZ | free key | 200 |
| [Statutes at Large (govinfo STATUTE)](https://api.govinfo.gov/docs/) | US Statutes at Large collection via govinfo | `https://api.govinfo.gov/collections/STATUTE/2020-01-01T00:00:00Z?pageSize=5&offsetMark=*&api_key=DEMO_KEY` | DEMO\_KEY | US | free key | 200 |
| [US Courts opinions (govinfo USCOURTS)](https://www.govinfo.gov/app/collection/uscourts) | Federal court opinions collection in govinfo | `https://api.govinfo.gov/collections/USCOURTS/2024-01-01T00:00:00Z?pageSize=5&offsetMark=*&api_key=DEMO_KEY` | DEMO\_KEY | US | free key | 200 |
