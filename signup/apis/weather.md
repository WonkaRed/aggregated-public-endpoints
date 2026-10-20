# Weather APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [AccuWeather](https://developer.accuweather.com/apis) | Weather and forecast data | docs only |  | global | free key | 403 |
| [Admiralty UK Tidal API](https://developer.admiralty.co.uk/) | UK tidal predictions (Discovery free tier) | docs only | Free tier key | UK | free key | 200 |
| [Aemet](https://opendata.aemet.es/centrodedescargas/inicio) | Weather and forecast data from Spain | docs only |  | global | free key | 200 |
| [AEMET OpenData](https://opendata.aemet.es/dist/index.html) | Spanish AEMET forecasts, observations, radar (free API key by email) | `https://opendata.aemet.es/opendata/api/prediccion/especifica/municipio/diaria/28079` | none stated | ES | free key | 200 |
| [Ambient Weather](https://ambientweather.docs.apiary.io/) | Personal weather station data | `https://rt.ambientweather.net/v1/devices?apiKey=KEY&applicationKey=KEY` | 1 req/s | global | free key | 200 |
| [aprs.fi API](https://aprs.fi/page/api) | APRS/CWOP station positions and weather reports | `https://api.aprs.fi/api/get?name=OH2TI&what=wx&apikey=KEY&format=json` |  | global | free key | 200 |
| [AQICN](https://aqicn.org/api/) | Air Quality Index Data for over 1000 cities | docs only |  | global | free key | 200 |
| [CIMIS (California Irrigation Mgmt)](https://et.water.ca.gov/Rest/Index) | California ET and weather station data; free app key | docs only | free; see docs | US-CA | free key | 200 |
| [Clima Cell](https://docs.tomorrow.io/reference/realtime-weather) | Real-time weather data in a free or paid API | `https://docs.tomorrow.io/reference/realtime-weather` |  | global | free key | 200 |
| [ColorfulClouds](https://open.caiyunapp.com/ColorfulClouds_Weather_API) | Weather | docs only |  | global | free key | 200 |
| [CWA Open Data Taiwan](https://opendata.cwa.gov.tw/devManual/insrtuction) | Taiwan Central Weather Administration open data API (free key by registration) | `https://opendata.cwa.gov.tw/index` | none stated | TW | free key | 200 |
| [data.go.kr KMA Short-term Forecast](https://www.data.go.kr/data/15084084/openapi.do) | Korea Meteorological Administration village forecast via Public Data Portal | `https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey=YOUR_KEY&dataType=JSON&base_date=20261019&base_time=0500&nx=55&ny=127` | 10k req/day dev | KR | free key | 403 |
| [DMC Chile / Meteochile](https://climatologia.meteochile.gob.cl/) | Chilean weather service data | `https://climatologia.meteochile.gob.cl/` | none stated | CL | free key | 200 |
| [DMC Chile Climatología API](https://climatologia.meteochile.gob.cl/application/servicios/) | Chile Dirección Meteorológica station data; free registration | `https://climatologia.meteochile.gob.cl/application/servicios/getDatosRecientesEma/330020` | free; see docs | CL | free key | 200 |
| [Euskalmet](https://opendata.euskadi.eus/api-euskalmet/-/api-de-euskalmet/) | Meteorological data of the Basque Country | docs only |  | global | free key | 200 |
| [Frost API (MET Norway)](https://frost.met.no/) | Norwegian historical weather observations (free client id) | `https://frost.met.no/sources/v0.jsonld` |  | NO | free key | 401 |
| [GISTDA](https://disaster.gistda.or.th/services/open-api) | Thailand natural disaster information | docs only |  | global | free key | 200 |
| [GribStream](https://gribstream.com/) | Global weather forecast API for any use. Leverage the NBM and GFS models. Great for bulk pulls | docs only |  | global | free key | 200 |
| [HG Weather](https://hgbrasil.com/status/weather) | Provides weather forecast data for cities in Brazil | docs only |  | global | free key | 307 |
| [IMD API Portal (api.imd.gov.in)](https://api.imd.gov.in/public/index.php) | India Meteorological Department's newer registered API gateway: city forecasts, district nowcasts and warnings, cyclone tracks, lightning, coastal bulletins and port warnings (JSON; x-api-key plus token after free regis… | `https://api.imd.gov.in/api/v1/cityforecast` | fair use | IN | free key | 401 |
| [IMD City Weather API](https://mausam.imd.gov.in/imd_latest/contents/api.pdf) | India Meteorological Department city weather API (IP whitelisted) | docs only | IP whitelisting required | IN | free key | 401 |
| [Israel IMS Weather API](https://ims.gov.il/en/ObservationDataAPI) | Israel Meteorological Service data portal (token) | `https://ims.gov.il/en/ObservationDataAPI` | none stated | IL | free key | 200 |
| [Israel Meteorological Service API](https://ims.gov.il/en/ObservationDataAPI) | IMS weather station data API | `https://api.ims.gov.il/v1/envista/stations` | free token by email | IL | free key | 401 |
| [KMA API Hub](https://apihub.kma.go.kr/) | Korea Meteorological Administration weather, forecasts, earthquakes | `https://apihub.kma.go.kr/api/typ01/url/kma_sfctm2.php?tm=202401011200&stn=0&help=1&authKey=KEY` | free authKey | KR | free key | 401 |
| [KMA API Hub (Korea)](https://apihub.kma.go.kr/) | Korea Meteorological Administration API hub (free key) | `https://apihub.kma.go.kr/` | none stated | KR | free key | 200 |
| [KNMI](https://developer.dataplatform.knmi.nl/) | Dutch weather, radar and climate data | docs only |  | global | free key | 200 |
| [KNMI Data Platform](https://developer.dataplatform.knmi.nl/) | Dutch weather datasets (free anonymous key published) | `https://api.dataplatform.knmi.nl/open-data/v1/datasets/Actuele10mindataKNMIstations/versions/2/files` |  | NL | free key | 401 |
| [KNMI EDR API](https://developer.dataplatform.knmi.nl/edr-api) | KNMI Environmental Data Retrieval API (key) | `https://developer.dataplatform.knmi.nl/edr-api` | none stated | NL | free key | 200 |
| [KNMI Open Data API](https://developer.dataplatform.knmi.nl/open-data-api) | Dutch KNMI datasets and files (anonymous public key published in docs) | `https://api.dataplatform.knmi.nl/open-data/v1/datasets` | none stated | NL | free key | 200 |
| [Korea KMA](https://www.data.go.kr/) | Korea weather | `https://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getUltraSrtNcst` | free key | KR | free key | 200 |
| [Korea Meteorological Administration](https://apihub.kma.go.kr/) | Weather and climate data from KMA | docs only |  | global | free key | 200 |
| [MesoWest (via Synoptic)](https://mesowest.utah.edu/) | Univ. of Utah mesonet aggregation | `https://api.synopticdata.com/v2/stations/metadata?state=UT&token=YOUR_TOKEN` | free; see docs | US | free key | 401 |
| [MET Malaysia API](https://api.met.gov.my/) | Malaysian Meteorological Department API v2.1: locations, forecasts and observations by dataset/category/location (free registration token, 'METToken' header) | `https://api.met.gov.my/v2.1/locations?locationcategoryid=TOWN` | fair use | MY | free key | 401 |
| [MET Norway Frost](https://frost.met.no/index.html) | Norwegian historical observations | docs only | Free client id | NO | free key | 200 |
| [Met Norway Frost API](https://frost.met.no/) | Norwegian historical observations (free client id by signup) | `https://frost.met.no/index.html` | none stated | NO | free key | 200 |
| [Met Office DataHub](https://datahub.metoffice.gov.uk/docs) | UK Met Office site-specific forecasts, maps (free tier key) | `https://datahub.metoffice.gov.uk/docs` | free tier \~360 calls/day | UK | free key | 200 |
| [Met Office DataPoint](https://www.metoffice.gov.uk/services/data/datapoint/) | Weather data for the UK | docs only |  | global | free key | 200 |
| [Meteo-France public API (portail-api)](https://portail-api.meteofrance.fr/) | Meteo-France APIs on portail-api.meteofrance.fr (free key / token subscription) | `https://portail-api.meteofrance.fr/` | none stated | FR | free key | 200 |
| [Meteoblue](https://content.meteoblue.com/en/business-solutions/weather-apis) | Global weather data with 100+ weather variables, 14 days ahead and 4 days of history data. | docs only |  | global | free key | 200 |
| [Meteocat XEMA API](https://apidocs.meteocat.gencat.cat/) | Catalan Meteorological Service (Meteocat) XEMA station metadata and observations, forecasts; free self-serve key in x-api-key header | `https://api.meteo.cat/xema/v1/estacions/metadades` | free plan quota per month | ES-CT | free key | 403 |
| [Meteosource](https://www.meteosource.com/) | Global weather forecasts based on machine learning and historical data | docs only |  | global | free key | 200 |
| [mPING API](https://mping.ou.edu/static/mping/api.html) | Crowdsourced precipitation-type reports | `https://mping.ou.edu/mping/api/v2/reports` |  | US | free key | 401 |
| [Météo-France](https://portail-api.meteofrance.fr/) | French weather forecasts and alerts | docs only |  | global | free key | 301 |
| [Météo-France API Portal](https://portail-api.meteofrance.fr/) | French national forecasts, observations, warnings | docs only | Free tier, signup | FR | free key | 302 |
| [Météo-France Public API](https://portail-api.meteofrance.fr/) | Observations, forecasts, vigilance (free key portail-api) | `https://public-api.meteofrance.fr/public/DPObs/v1/liste-stations` |  | FR | free key | 401 |
| [NC State Climate Office CRONOS](https://products.climate.ncsu.edu/api/) | NC ECONet and multi-network obs API (free key) | docs only | free; see docs | US-NC | free key | 400 |
| [NCEI Climate Data Online API](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | GHCN daily station data and metadata | `https://www.ncei.noaa.gov/cdo-web/api/v2/stations?limit=5` | 5 req/s, 10k/day | global | free key | 400 |
| [Netatmo](https://dev.netatmo.com/) | Public weather stations | `https://api.netatmo.com/api/getpublicdata` | OAuth | global | free key | 200 |
| [NIWA Tide API](https://developer.niwa.co.nz/docs/tide-api/1/overview) | NZ tide predictions | docs only | Free key | NZ | free key | 200 |
| [NOAA Climate Data](https://www.ncdc.noaa.gov/cdo-web/) | Weather and climate data | docs only |  | global | free key | 200 |
| [NOAA NCEI CDO Web Services v2](https://www.ncdc.noaa.gov/cdo-web/webservices/v2) | Climate Data Online API (free token by email) | `https://www.ncdc.noaa.gov/cdo-web/webservices/v2` | 10k requests/day; 5/sec | US | free key | 200 |
| [Oikolab](https://docs.oikolab.com) | 70+ years of global, hourly historical and forecast weather data from NOAA and ECMWF | docs only |  | global | free key | 200 |
| [Open Weather API](https://openweathermap.org/api) | Current weather data available free at rate of 1 request per \~90 seconds (only first 1000 API calls per day are free) | `https://openweathermap.org/api` |  | global | free key | 200 |
| [OpenUV](https://www.openuv.io) | Real-time UV Index Forecast | docs only |  | global | free key | 200 |
| [OpenWeatherMap](https://openweathermap.org/api) | Current, forecast, geocoding, air pollution | `https://api.openweathermap.org/data/2.5/weather?q=London&appid=KEY` | 1000 calls/day One Call 3.0, 60/min 2.5 | global | free key | 200 |
| [Pirate Weather](https://pirateweather.net/) | Dark Sky-compatible forecast API (NOAA models); free key | `https://api.pirateweather.net/forecast/KEY/45.42,-75.69` | 10k/month free | global | free key | 401 |
| [QWeather](https://dev.qweather.com/en/) | Chinese/global weather API | `https://devapi.qweather.com/v7/weather/now?location=101010100&key=KEY` | 1000 calls/day free | global | free key | 200 |
| [Seniverse (心知天气)](https://seniverse.yuque.com/hyper_data/api_v3) | Weather now/daily for Chinese cities; free plan | `https://api.seniverse.com/v3/weather/now.json?key=YOUR_KEY&location=beijing&language=en` | free plan limited fields | CN | free key | 403 |
| [Stormglass](https://docs.stormglass.io/) | Marine weather and tides | `https://api.stormglass.io/v2/weather/point?lat=58.7&lng=17.9&params=waveHeight` | 10 req/day free | global | free key | 200 |
| [Synoptic Data (MesoWest) API](https://docs.synopticdata.com/services/weather-data-api) | 170k+ surface stations incl. CWOP, MADIS, mesonets: latest/timeseries | `https://api.synopticdata.com/v2/stations/latest?stid=WBB&token=TOKEN` | open-access tier | global | free key | 401 |
| [Taiwan CWA Open Data](https://opendata.cwa.gov.tw/) | Taiwan Central Weather Administration | `https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=KEY` | free key | TW | free key | 200 |
| [TMD NWP Forecast API](https://data.tmd.go.th/nwpapi/register) | Thai Meteorological Department numerical weather prediction API: hourly/daily point forecasts (temperature, humidity, rain, wind) by lat/lon or province; free registration for a bearer token (separate from the uid/ukey … | `https://data.tmd.go.th/nwpapi/v1/forecast/location/daily/at?lat=13.75&lon=100.50&fields=tc,rh,rain` | fair use | TH | free key | 401 |
| [TMD Thailand Weather API](https://data.tmd.go.th/) | Thai Meteorological Department forecasts | docs only | Free key | TH | free key | 302 |
| [TMD Weather API](https://data.tmd.go.th/api/index1.php) | Thai Meteorological Department forecasts and observations | `https://data.tmd.go.th/api/WeatherToday/V2/?uid=api&ukey=api12345` | demo uid/ukey available | TH | free key | 200 |
| [Tomorrow](https://docs.tomorrow.io) | Weather API Powered by Proprietary Technology | docs only |  | global | free key | 200 |
| [Tomorrow.io](https://docs.tomorrow.io/reference/welcome) | Weather forecast and timelines | `https://api.tomorrow.io/v4/weather/realtime?location=london&apikey=KEY` | 500 calls/day, 25/hr | global | free key | 200 |
| [Tomorrow.io Weather API](https://www.tomorrow.io/weather-api/) | Offers free plan of weather API. Provides accurate and up-to-date weather forecasting with global coverage, historical data and weather monitoring solutions | `https://www.tomorrow.io/weather-api/` |  | global | free key | 403 |
| [UK Met Office DataHub](https://datahub.metoffice.gov.uk/docs/f/category/site-specific/overview) | UK site-specific forecasts, maps (free tier key) | docs only | Free tier limits | UK | free key | 200 |
| [Visual Crossing](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/) | Weather history and forecast | `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/London?key=KEY` | 1000 records/day | global | free key | 200 |
| [Visual Crossing Timeline](https://www.visualcrossing.com/resources/documentation/weather-api/timeline-weather-api/) | Forecast + history; free key | `https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Santiago?key=KEY` | 1000 records/day | global | free key | 401 |
| [Weather Underground](https://weatherflow.github.io/Tempest/api/) | Tempest personal weather stations | `https://swd.weatherflow.com/swd/rest/stations?token=KEY` | personal token | global | free key | 200 |
| [WeatherAPI](https://www.weatherapi.com/) | Weather and astronomy data (✅ Free tier, 🔑 API Key) | `https://www.weatherapi.com/` |  | global | free key | 200 |
| [WeatherAPI.com](https://www.weatherapi.com/docs/) | Weather, astronomy, timezone, search | `https://api.weatherapi.com/v1/current.json?key=KEY&q=London` | 1M calls/month free | global | free key | 200 |
| [Weatherbit](https://www.weatherbit.io/api) | Current, forecast, history | `https://api.weatherbit.io/v2.0/current?city=London&key=KEY` | 50 calls/day, 1/s | global | free key | 200 |
| [WillyWeather API](https://www.willyweather.com.au/info/api.html) | Australia/NZ/US forecasts, tides, swell | docs only | Free key, limits | AU | free key | 200 |
| [Yahoo! JAPAN YOLP Weather](https://developer.yahoo.co.jp/webapi/map/openlocalplatform/v1/weather.html) | Rainfall observation and 60-minute nowcast for coordinates in Japan | `https://map.yahooapis.jp/weather/V1/place?coordinates=139.732293,35.663613&output=json&appid=YOUR_APPID` | 50k req/day | JP | free key | 200 |
| [Yandex.Weather](https://yandex.com/dev/weather/) | Assesses weather condition in specific locations | docs only |  | global | free key | 200 |
