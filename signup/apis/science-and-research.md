# Science & Research APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [BASE (Bielefeld Academic Search Engine) API](https://www.base-search.net/about/en/about_develop.php) | 400M+ docs; API access by IP registration (free) | `https://api.base-search.net/cgi-bin/BaseHttpSearchInterface.fcgi?func=PerformSearch&query=climate` | IP whitelisting required | global | free key | 200 |
| [Biodiversity Heritage Library API](https://www.biodiversitylibrary.org/docs/api3.html) | Digitized biodiversity literature, names, pages (free key) | `https://www.biodiversitylibrary.org/api3?op=PublicationSearch&searchterm=darwin&format=json&apikey=YOUR_KEY` | unknown | global | free key | 401 |
| [BioGRID REST](https://wiki.thebiogrid.org/doku.php/biogridrest) | Genetic and protein interactions | `https://webservice.thebiogrid.org/interactions/?searchNames=true&geneList=TP53&format=json` | Free key | global | free key | 200 |
| [ChemSpider (RSC Compounds API)](https://developer.rsc.org/compounds-v1/apis) | Chemical structures database | `https://api.rsc.org/compounds/v1/records/2157/details?fields=SMILES` | free key, 1000 req/month | global | free key | 403 |
| [CORE](https://core.ac.uk/services#api) | Access the world's Open Access research papers | docs only |  | global | free key | 200 |
| [CORE API](https://core.ac.uk/services/api) | Search 300M+ open access papers | `https://api.core.ac.uk/v3/search/works?q=climate&limit=1` | Free key; limited anonymous | global | free key | 200 |
| [CORE API v3](https://api.core.ac.uk/docs/v3) | 300M+ open access research outputs, full texts (free key) | docs only | free tier rate limits | global | free key | 301 |
| [CWA Earthquake Reports](https://opendata.cwa.gov.tw/dist/opendata-swagger.html) | Taiwan significant earthquake reports (CWA open data, free key) | `https://opendata.cwa.gov.tw/api/v1/rest/datastore/E-A0015-001?Authorization=YOUR_KEY&format=JSON` |  | TW | free key | 401 |
| [Ecosyste.ms Papers](https://papers.ecosyste.ms/docs) | Research papers that mention/cite software packages (ecosyste.ms, CC BY-SA data, AGPL code) | `https://papers.ecosyste.ms/api/v1/papers?per_page=2` | 5000 req/h | global | payment required | 402 |
| [Elsevier Scopus/ScienceDirect APIs](https://dev.elsevier.com/) | Free key for non-commercial abstract/search | docs only | institutional entitlements vary | global | free key | 403 |
| [IEEE Xplore API](https://developer.ieee.org/) | IEEE metadata search (free key) | `https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=robot&apikey=YOUR_KEY` | 200 req/day | global | free key | 403 |
| [KCI Open API (Korea Citation Index)](https://open.kci.go.kr/) | National Research Foundation of Korea KCI API: search Korean scholarly journal articles, article detail, references and citation counts (apiCode articleSearch/articleDetail/referenceSearch/citation); XML. Free key from … | `https://open.kci.go.kr/po/openapi/openApiSearch.kci?apiCode=articleSearch&key=YOUR_KEY&title=deep%20learning` | free key on registration | KR | free key | 200 |
| [Materials Platform for Data Science](https://mpds.io) | Curated experimental data for materials science | docs only |  | global | free key | 200 |
| [Materials Project](https://api.materialsproject.org/docs) | Materials properties (free key) | `https://api.materialsproject.org/docs` | Free key | global | free key | 200 |
| [NCBO BioPortal](https://data.bioontology.org/documentation) | 1000+ biomedical ontologies, annotator | `https://data.bioontology.org/ontologies?apikey=YOUR_KEY` | free account key | global | free key | 401 |
| [Numbers](https://math.tools/api/numbers/) | Number of the day, random number, number facts and anything else you want to do with numbers | docs only |  | global | free key | 200 |
| [OpenDOAR / Sherpa repositories API](https://v2.sherpa.ac.uk/api/) | Directory of open access repositories | docs only | unknown | global | free key | 403 |
| [Pl@ntNet Identification API](https://my.plantnet.org/doc/getting-started/introduction) | Pl@ntNet plant species identification from up to 5 images per request (returns ranked species with scores, GBIF/POWO ids, predicted organ) against regional floras/projects; free tier 500 identifications/day with a self-… | `https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key=YOUR_KEY` | 500 identifications/day free | global | free key | 401 |
| [Research Data Australia getMetadata API](https://documentation.ardc.edu.au/rda/getmetadata-api) | ARDC Research Data Australia registry services: getMetadata (JSON from the Solr index) and getRIFCS (RIF-CS XML) across 100k+ Australian research dataset, party, activity and service records; free API key in URL path. | docs only | fair use | AU | free key | 200 |
| [Sherpa Romeo API](https://v2.sherpa.ac.uk/api/) | Publisher OA/self-archiving policies (free key) | docs only | unknown | global | free key | 403 |
| [Springer Nature Open Access API](https://dev.springernature.com/) | Springer Nature metadata and OA full text (free key) | `https://api.springernature.com/openaccess/json?q=climate&api_key=YOUR_KEY` | 500 req/day free | global | free key | 401 |
| [VedIntel™ AstroAPI](https://vedintelastroapi.com/docs) | Vedic astrology computation — birth charts, dashas, panchang, AI narratives | docs only |  | global | free key | 200 |
