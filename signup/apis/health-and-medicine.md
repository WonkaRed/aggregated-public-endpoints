# Health & Medicine APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [API Professionnels de santé (Annuaire Santé FHIR)](https://ansforge.github.io/annuaire-sante-fhir-documentation/) | Health professionals directory (FHIR, free key) | `https://gateway.api.esante.gouv.fr/fhir/v2/Practitioner` |  | FR | free key | 403 |
| [CMS Marketplace API](https://developer.cms.gov/marketplace-api/) | ACA plans, providers, drug coverage | `https://marketplace.api.healthcare.gov/api/v1/states?apikey=YOUR_KEY` | free key | US | free key | 401 |
| [CMS.gov](https://data.cms.gov/provider-data/) | Access to the data from the CMS - medicare.gov | docs only |  | global | free key | 200 |
| [Cure Cancer With AI](https://www.curecancerwithai.com/developers) | Oncology research, clinical trials, FDA approvals, news, and MAMMAL predictions | docs only |  | global | free key | 200 |
| [DisGeNET API](https://www.disgenet.com/Tools/API) | Gene-disease associations | `https://api.disgenet.com/api/v1/gda/summary?gene_ncbi_id=351` | free academic tier key | global | free key | 401 |
| [ERstat](https://erstat.ca/developers) | Live Canadian emergency room closures and service disruptions, by province | docs only |  | global | free key | 200 |
| [FDA Recalls](https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-fda-product-food-recalls) | Latest FDA food, drug and product recall notices as JSON with keyword search | docs only |  | global | free key | 200 |
| [FoodData Central](https://fdc.nal.usda.gov/) | National Nutrient Database for Standard Reference | docs only |  | global | free key | 200 |
| [Google Pollen](https://developers.google.com/maps/documentation/pollen) | Pollen forecast | `https://pollen.googleapis.com/v1/forecast:lookup?key=KEY&location.longitude=-122&location.latitude=37&days=1` | GCP key, free credit | global | free key | 200 |
| [Healthsites.io API](https://healthsites.io/api/docs/) | Global open health facility registry (OSM-based) | `https://healthsites.io/api/v3/facilities/?api-key=YOUR_KEY&page=1` | free key | global | free key | 403 |
| [Infermedica](https://developer.infermedica.com/docs/) | NLP based symptom checker and patient triage API for health diagnosis from text | docs only |  | global | free key | 200 |
| [Lexigram](https://docs.lexigram.io/) | NLP that extracts mentions of clinical concepts from text, gives access to clinical ontology | docs only |  | global | free key | 200 |
| [LOINC FHIR](https://loinc.org/fhir/) | LOINC terminology (free account) | `https://fhir.loinc.org/CodeSystem?url=http://loinc.org` | Free account | global | free key | 200 |
| [LOINC FHIR Terminology Server](https://loinc.org/fhir/) | LOINC codes via FHIR | docs only | free LOINC account (basic auth) | global | free key | 200 |
| [NCI Clinical Trials Search API](https://clinicaltrialsapi.cancer.gov/) | Cancer clinical trials | `https://clinicaltrialsapi.cancer.gov/api/v2/trials?size=1` | free key | US | free key | 401 |
| [NHS Health A-Z](https://digital.nhs.uk/developer/api-catalogue/health-a-to-z) | NHS conditions, medicines and guidance | docs only |  | global | free key | 403 |
| [NHS Website Content API](https://developer.api.nhs.uk/nhs-api) | NHS conditions, medicines, live-well content | `https://api.service.nhs.uk/nhs-website-content/conditions/` | free key | UK | free key | 401 |
| [NIH SEER\*Stat API](https://api.seer.cancer.gov/) | Cancer statistics (SEER API) | `https://api.seer.cancer.gov/rest/disease/latest?q=lung` | free key via NCI login | US | free key | 401 |
| [OncoKB](https://api.oncokb.org/oncokb-website/api) | Precision oncology knowledge base | `https://www.oncokb.org/api/v1/info` | free academic registration | global | free key | 200 |
| [PBS Public API v3](https://data.pbs.gov.au/api/pbs-api.html) | Australian Pharmaceutical Benefits Scheme schedule API: subsidised medicines, items, restrictions, prescribers, fees and schedules for the current and past-12-month schedules; freely available, subscription key from the… | `https://data-api.health.gov.au/pbs/api/v3/schedules` | 1 request per 20 s | AU | free key | 401 |
| [Stanza DSCSA Verifier](https://stanzaapi.com/tools/pharma-dscsa) | Verify FDA DSCSA and EU FMD pharmaceutical serialization barcodes | docs only |  | global | free key | 200 |
| [Stanza UDI Decoder](https://stanzaapi.com/tools/udi-decoder) | Decode and validate FDA GUDID and EU MDR medical device UDI barcodes | docs only |  | global | free key | 200 |
| [Swissmedic Open Government Data](https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html) | — Machine-readable Swissmedic lists of authorized medicines and registered medical-device operators | `https://www.swissmedic.ch/swissmedic/en/home/services/listen_neu.html` |  | CH | free key | 200 |
| [THC Open Mindfulness Resources](https://api.theholisticcare.com/docs) | Free mindfulness resources and research metadata \| No | docs only |  | global | free key | 200 |
| [UMLS Terminology Services](https://documentation.uts.nlm.nih.gov/rest/home.html) | UMLS Metathesaurus, SNOMED CT, ICD, CPT crosswalks | `https://uts-ws.nlm.nih.gov/rest/search/current?string=fracture&apiKey=YOUR_KEY` | free UTS license | US | free key | 401 |
| [VA Lighthouse Facilities API](https://developer.va.gov/explore/api/va-facilities) | VA health facilities locations and services | `https://api.va.gov/services/va_facilities/v1/facilities?state=CA` | free key | US | free key | 401 |
| [VSAC FHIR](https://www.nlm.nih.gov/vsac/support/usingvsac/vsacfhirapi.html) | Value Set Authority Center value sets (FHIR) | `https://cts.nlm.nih.gov/fhir/ValueSet` | UMLS API key | US | free key | 401 |
| [WHO ICD-11 API](https://icd.who.int/icdapi) | ICD-11 and ICD-10 classification lookup | `https://id.who.int/icd/entity/1435254666` | free client id/secret (OAuth client credentials) | global | free key | 401 |
