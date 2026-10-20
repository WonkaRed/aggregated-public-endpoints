# Patents & IP APIs

[Back to the open index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [EPO Linked Data (SPARQL)](https://data.epo.org/linked-data/) | EP patent data as linked data | docs only |  | EU | none | 200 |
| [EPO Publication Server REST](https://data.epo.org/publication-server/) | European Patent Office publication server: browse published EP patents by publication date and download full-text XML/PDF without key | docs only | fair use | EU | none | 200 |
| [Google Patents XHR Query](https://patents.google.com/) | Unofficial JSON search behind patents.google.com (global patent full text search) | `https://patents.google.com/xhr/query?url=q%3Dtesla` | Undocumented; may be rate-blocked | global | none | 200 |
| [IPOS Patents/Designs/Trademarks (data.gov.sg)](https://data.gov.sg/dataset/ipos-apis) | Intellectual Property Office of Singapore applications (patents, designs, trademarks) by lodgement date, JSON; Singapore Open Data Licence; data Aug 2018 to Aug 2025 | `https://api.data.gov.sg/v1/technology/ipos/trademarks?lodgement_date=2019-01-02` | fair use | SG | none | 200 |
| [NASA TechTransfer Patents](https://technology.nasa.gov/api) | NASA licensable patents, software and spinoff technologies search (JSON). | `https://technology.nasa.gov/api/query/patent/laser` | fair use | US | none | 200 |
| [Open Definition Licenses API](https://opendefinition.org/licenses/api/) | JSON metadata for 100+ open data/content/software licenses (OD/OSD conformance, domain flags), individually or in groups (e.g. CKAN group) | `https://licenses.opendefinition.org/licenses/groups/ckan.json` | fair use | global | none | 200 |
| [OSI Approved Licenses API (opensource.org/api)](https://opensource.org/blog/introducing-the-new-api-for-osi-approved-licenses) | New official Open Source Initiative API (replaces api.opensource.org) with canonical OSI Approved Licenses: SPDX id, approval dates, categories; public and free | `https://opensource.org/api/license/gpl-3-0` | fair use | global | none | 200 |
| [PatentsView](https://patentsview.org/apis/purpose) | API is intended to explore and visualize trends/patterns across the US innovation landscape | docs only |  | global | none | 200 |
| [Ukraine NIPO SIS Open Data API](https://sis.nipo.gov.ua/en/services/api-description) | Ukrainian State Registers of IP rights (inventions, utility models, trademarks, GIs, industrial designs, copyright) as JSON, filter by obj\_type; open data free reuse | `https://sis.nipo.gov.ua/api/v1/open-data/?obj_type=1` | fair use | UA | none | 200 |
| [USPTO](https://www.uspto.gov/learning-and-resources/open-data-and-mobility) | USA patent api services | docs only |  | global | none | 200 |
| [USPTO bulk data (ODP)](https://data.uspto.gov/bulkdata) | Bulk patent and trademark data products | docs only |  | US | none | 200 |
