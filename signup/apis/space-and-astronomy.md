# Space & Astronomy APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [Astronomy API (AstronomyAPI.com)](https://docs.astronomyapi.com/) | Star charts, positions, moon phases | `https://api.astronomyapi.com/api/v2/bodies` | free tier | global | free key | 200 |
| [Bhoonidhi STAC API (ISRO/NRSC)](https://bhoonidhi.nrsc.gov.in/bhoonidhi-api/) | NRSC Bhoonidhi earth-observation data hub API: STAC-compliant collections/items/search over ISRO (Resourcesat, Cartosat, EOS-04 SAR, Oceansat) and regional Sentinel/Landsat archives since 1986, plus download; JWT token … | `https://bhoonidhi-api.nrsc.gov.in/data/collections` | 20 token requests/hour/IP | IN | free key | 401 |
| [BoM Space Weather API](https://sws-data.sws.bom.gov.au/api-docs) | Bureau of Meteorology Australian Space Forecast Centre API: POST JSON methods for K-index, A-index, Dst, aurora alerts/outlooks, magnetic and radio-blackout alerts for Australian observing sites; free registration key i… | `https://sws-data.sws.bom.gov.au/api/v1/get-k-index` | free; subject to change | AU | free key | 405 |
| [N2YO](https://www.n2yo.com/api/) | Satellite passes, positions, TLE | `https://api.n2yo.com/rest/v1/satellite/tle/25544` | 1000 req/hr | global | free key | 200 |
| [NASA ADS](https://ui.adsabs.harvard.edu/help/api/) | Astrophysics Data System literature search | `https://api.adsabs.harvard.edu/v1/search/query?q=black+hole` | 5000/day with free token | global | free key | 202 |
| [NASA APOD (api.nasa.gov)](https://api.nasa.gov/) | Astronomy Picture of the Day; DEMO\_KEY works for light use | `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY` | DEMO\_KEY 30/hr 50/day per IP; free key 1000/hr | US | free key | 200 |
| [NASA DONKI (space weather)](https://ccmc.gsfc.nasa.gov/tools/DONKI/) | CME, flare, geomagnetic storm database (DEMO\_KEY rate-limited; free key via api.nasa.gov) | `https://api.nasa.gov/DONKI/FLR` | DEMO\_KEY 30/hr; free key 1000/hr | global | free key | 200 |
| [NASA Mars Rover Photos](https://api.nasa.gov/) | Photos from Curiosity, Perseverance, Opportunity, Spirit | `https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY` | DEMO\_KEY limits | US | free key | 200 |
| [NASA NeoWs (Near Earth Objects)](https://api.nasa.gov/) | Near-earth asteroid feed and lookup | `https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-01-01&end_date=2024-01-02&api_key=DEMO_KEY` | DEMO\_KEY limits; free key 1000/hr | US | free key | 200 |
| [NASA Open APIs](https://api.nasa.gov/) | Space imagery, Mars Rover, and more (✅ Free, 🔑 API Key) | `https://api.nasa.gov/` |  | global | free key | 200 |
| [Open Ephemeris](https://openephemeris.com/docs) | Sub-arcsecond planetary positions, natal charts, transits, and Human Design from NASA JPL DE440 | docs only |  | global | free key | 200 |
| [OrbitalWiki](https://orbitalwiki.com/developers) | Catalog of 16,000+ satellites merging CelesTrak, GCAT, Wikidata; free tier included | docs only |  | global | free key | 308 |
| [Rainbow Weather](https://developer.rainbow.ai/) | Global real-time nowcasting API powered by radar + satellite fusion | docs only |  | global | free key | 200 |
| [Solar System OpenData](https://api.le-systeme-solaire.net/en/) | Planets and moons data (French) | `https://api.le-systeme-solaire.net/rest/bodies/terre` | free key by email | global | free key | 401 |
| [Space-Track](https://www.space-track.org/documentation) | Satellite catalog (free account) | `https://www.space-track.org/documentation` | Free account | global | free key | 200 |
| [Space-Track.org](https://www.space-track.org/documentation) | US Space Force satellite catalog, TLE, conjunctions | `https://www.space-track.org/ajaxauth/login` | free account | global | free key | 200 |
