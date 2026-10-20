# Patents & IP APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [EPO Open Patent Services](https://www.epo.org/en/searching-for-patents/data/web-services/ops) | Worldwide patent bibliographic, full-text, family data (free key, 4GB/week) | `https://ops.epo.org/3.2/rest-services/published-data/publication/epodoc/EP1000000/biblio` |  | global | free key | 403 |
| [IP Australia API](https://portal.api.ipaustralia.gov.au/) | Australian trademark/patent search | `https://production.api.ipaustralia.gov.au/public/australian-trade-mark-search-api/v1/` |  | AU | free key | 400 |
| [KIPRIS Plus Patent Search API](https://plus.kipris.or.kr/portal/data/service/List.do?subTab=SC001&entYn=N&menuNo=200100) | Korean Intellectual Property Office KIPRIS Plus REST API: keyword search of Korean patents and utility models (getWordSearch) and bibliographic detail by application number; XML. Development accounts approved automatica… | `https://plus.kipris.or.kr/kipo-api/kipi/patUtiModInfoSearchSevice/getWordSearch?word=battery&ServiceKey=YOUR_KEY` | free dev account quota; production needs review | KR | free key | 200 |
| [Lens.org Scholarly \& Patent API](https://docs.api.lens.org/) | Patents and scholarly works | `https://api.lens.org/patent/search` | free trial/non-commercial token by request | global | free key | 401 |
| [NASA TechTransfer API](https://api.nasa.gov/) | NASA patents, software catalog and spinoffs available for licensing (Technology Transfer portal), keyword search; DEMO\_KEY works, free api.nasa.gov key for higher limits | `https://api.nasa.gov/techtransfer/patent/?engine&api_key=DEMO_KEY` | DEMO\_KEY 30/hour; free key 1000/hour | US | free key | 429 |
| [TIPO](https://tiponet.tipo.gov.tw/Gazette/OpenData/OD/OD05.aspx?QryDS=API00) | Taiwan patent search system api | docs only |  | global | free key | 200 |
| [USPTO Open Data Portal](https://data.uspto.gov/apis/getting-started) | Patent file wrapper and application data | `https://api.uspto.gov/api/v1/patent/applications/search` | Free key via account | US | free key | 200 |
| [USPTO TSDR API](https://developer.uspto.gov/api-catalog/tsdr-data-api) | Trademark status \& documents | `https://tsdrapi.uspto.gov/ts/cd/casestatus/sn78787878/info` |  | US | free key | 401 |
| [USPTO TSDR Case Status API](https://developer.uspto.gov/api-catalog/tsdr-data-api) | USPTO trademark case status and documents by serial/registration number; free USPTO API key required. | `https://tsdrapi.uspto.gov/ts/cd/casestatus/sn76044902/info.json` | key required | US | free key | 401 |
