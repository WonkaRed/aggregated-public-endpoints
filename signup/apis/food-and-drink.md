# Food & Drink APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [1,000,000+ Recipe and Grocery List API (v2)](http://api2.bigoven.com/web/documentation) | Documentation This is the documentation for the partner endpoint of the BigOven Recipe and Grocery List API. The update brings with it Swagger-based documentati | `https://api2.bigoven.com/collections` |  | global | free key | 301 |
| [Agromonitoring Agro API](https://agromonitoring.com/api/history-ndvi) | OpenWeather Agro API: register field polygons and get Sentinel-2/Landsat NDVI/EVI imagery and statistics, NDVI history, soil temperature/moisture and accumulated weather; free tier up to 1000 ha, 60 calls/min. | `http://api.agromonitoring.com/agro/1.0/ndvi/history?start={start}&end={end}&polyid={polyid}&appid={API_KEY}` | free: 1000 ha, \<10 polygons/month, 60 calls/min | global | free key | 401 |
| [API Ninjas Cocktail](https://api-ninjas.com/api/cocktail) | Cocktail recipes searchable by name or ingredients, returning ingredients and instructions; alternative to TheCocktailDB; free tier | `https://api.api-ninjas.com/v1/cocktail?name=bloody%20mary` | free tier monthly quota | global | free key | 400 |
| [API Ninjas Nutrition](https://api-ninjas.com/api/nutrition) | Natural-language nutrition lookup: parses text like "1lb brisket and fries" into per-item calories, macros, sodium etc.; free tier | `https://api.api-ninjas.com/v1/nutrition?query=1lb%20brisket` | free tier monthly quota | global | free key | 400 |
| [API Ninjas Recipe](https://api-ninjas.com/api/recipe) | Recipe search by keyword returning title, ingredients, servings and instructions; free tier | `https://api.api-ninjas.com/v1/recipe?query=italian%20wedding%20soup` | free tier monthly quota | global | free key | 400 |
| [BoozeAPI](https://boozeapi.com/) | REST API Cocktail Recipes | docs only |  | global | free key | 200 |
| [CalorieNinjas](https://calorieninjas.com/api) | Nutrition from text | `https://api.calorieninjas.com/v1/nutrition?query=1lb%20brisket` | 10k/month | global | free key | 200 |
| [Chomp](https://chompthis.com/api/) | Data about various grocery products and foods | docs only |  | global | free key | 200 |
| [CookbookSocial Nutrition](https://cookbooksocial.app/api) | Nutrition data for 4,631 ingredients with food names in 19 languages | docs only |  | global | free key | 200 |
| [Edamam](https://developer.edamam.com/) | Recipe and nutrition search | `https://api.edamam.com/api/recipes/v2` | 10 calls/min | global | free key | 200 |
| [Edamam nutrition](https://developer.edamam.com/edamam-docs-nutrition-api) | Nutrition Analysis | docs only |  | global | free key | 200 |
| [Edamam recipes](https://developer.edamam.com/edamam-docs-recipe-api) | Recipe Search | docs only |  | global | free key | 200 |
| [FatSecret Platform API](https://platform.fatsecret.com/docs/guides) | Food and nutrition database (generic + branded foods, recipes, barcode on higher tiers) with free Basic tier; OAuth2 client-credentials token from free developer account | `https://platform.fatsecret.com/rest/foods/search/v1?search_expression=apple&format=json` | Basic free tier with daily call limit | global | free key | 200 |
| [Food Info](https://food-info.org/developer) | Nutrition data for millions of foods from six national food composition datasets | docs only |  | global | free key | 200 |
| [FoodSafetyKorea Open API (MFDS)](https://www.foodsafetykorea.go.kr/api/main.do) | Ministry of Food and Drug Safety (Korea) open API: food recalls/hazardous food (I0490), food nutrition, health functional food, HACCP and business licence datasets as JSON/XML via /api/{key}/{serviceId}/{type}/{start}/{… | `https://openapi.foodsafetykorea.go.kr/api/sample/I0490/json/1/5` | 'sample' key returns up to 5 rows; free key on signup | KR | free key | 200 |
| [Hot Pepper Gourmet](https://webservice.recruit.co.jp/doc/hotpepper/reference.html) | Japanese restaurant search (Recruit), free key by email | `https://webservice.recruit.co.jp/hotpepper/gourmet/v1/?key=YOUR_KEY&large_area=Z011&format=json` | 3000 req/day | JP | free key | 200 |
| [Kroger](https://developer.kroger.com/reference) | Supermarket Data | docs only |  | global | free key | 200 |
| [Noms](https://noms.sh/docs) | Nutrition data for 3.7M foods and 298K brands across 230 countries, with barcodes and images | docs only |  | global | free key | 200 |
| [Nutritionix](https://developer.nutritionix.com/) | Nutrition NLP | `https://trackapi.nutritionix.com/v2/search/instant?query=apple` | limited | global | free key | 200 |
| [Open Food Repo](https://www.foodrepo.org/api-docs/swaggers/v3) | Swiss food data | `https://www.foodrepo.org/api/v3/products` | unknown | CH | free key | 301 |
| [Rakuten Recipe Category Ranking](https://webservice.rakuten.co.jp/documentation/recipe-category-ranking) | Top-ranked recipes per category from Rakuten Recipe | `https://app.rakuten.co.jp/services/api/Recipe/CategoryRanking/20170426?format=json&applicationId=YOUR_APP_ID` | 1 req/sec | JP | free key | 400 |
| [ReceptAPI](https://receptapi.se) | Swedish recipes as structured JSON: normalized ingredients, EU-14 allergens, steps with timers and scalable servings | docs only |  | global | free key | 200 |
| [RecipeAPI](https://recipeapi.io) | Recipes, ingredients, nutrition data and cooking instructions | docs only |  | global | free key | 200 |
| [Spoonacular](https://spoonacular.com/food-api/docs) | Recipes and nutrition | `https://api.spoonacular.com/recipes/random` | 150 points/day | global | free key | 200 |
| [Tasty](https://rapidapi.com/apidojo/api/tasty/) | API to query data about recipe, plan, ingredients | docs only |  | global | free key | 200 |
| [Tiny Plates](https://www.tinyplates.dev/docs) | Structured recipes, semantic search, serving adjustments and shopping lists | docs only |  | global | free key | 200 |
| [USDA ERS ARMS API](https://www.ers.usda.gov/developer/) | USDA Economic Research Service data APIs | `https://api.ers.usda.gov/data/arms/state?api_key=YOUR_KEY` |  | US | free key | 403 |
| [USDA FAS Export Sales Reports OpenData API](https://apps.fas.usda.gov/opendataweb/home) | USDA FAS weekly export sales by commodity/country; free api.data.gov key header | `https://apps.fas.usda.gov/OpenData/api/esr/exports/commodityCode/104/allCountries/marketYear/2023` | free key | global | free key | 403 |
| [USDA FoodData Central](https://fdc.nal.usda.gov/api-guide) | Nutrient data for foods, branded products | `https://api.nal.usda.gov/fdc/v1/foods/search?query=cheddar&api_key=DEMO_KEY` | DEMO\_KEY works; 1000 req/hr with free key | US | free key | 200 |
| [USDA Local Food Portal API](https://www.usdalocalfoodportal.com/fe/fregisterpublicapi/) | USDA AMS Local Food Directories: farmers markets, CSAs, on-farm markets, food hubs and agritourism with location search; free API key | docs only | fair use | US | free key | 200 |
| [USDA NASS Quick Stats](https://quickstats.nass.usda.gov/api) | Agricultural survey and census statistics | `https://quickstats.nass.usda.gov/api/api_GET/?commodity_desc=CORN&year=2020&format=JSON` | Free key by email | US | free key | 200 |
| [Vinmonopolet Products API](https://api.vinmonopolet.no/) | Norwegian state liquor monopoly product catalogue (wine, beer, spirits) with free subscription key | `https://apis.vinmonopolet.no/products/v0/details-normal` | Free subscription key | NO | free key | 401 |
| [What's on the menu?](https://nypl.github.io/menus-api/) | NYPL human-transcribed historical menu collection | docs only |  | global | free key | 200 |
| [Your Move - Nutrition API](https://ymove.app/nutrition-api) | A complete nutrition API. Search foods, get nutrition facts and values. Generate meal plans and look up packaged products from 180+ countries worldwide. | docs only |  | global | free key | 200 |
| [Zestful](https://zestfuldata.com/) | Parse recipe ingredients | docs only |  | global | free key | 200 |
