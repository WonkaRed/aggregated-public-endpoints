# Test & Mock Data APIs

[Back to the open index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [AddressMock](https://addressmock.com/api) | Random US, Hong Kong and Cape Verde addresses with matched city, state and ZIP | docs only |  | global | none | 200 |
| [Agify.io](https://agify.io/) | Predict age from first name | `https://api.agify.io/?name=michael` | 100 names/day free | global | none | 200 |
| [Arabic Personal Names](https://github.com/forabi/arabic-personal-names) | JSON lists of real Arabic male, female and last names, built for generating realistic test profiles. | `https://raw.githubusercontent.com/forabi/arabic-personal-names/master/male.json` | fair use | MENA | none | 200 |
| [Automation Exercise API](https://automationexercise.com/api_list) | Practice e-commerce API for test automation: products list, brands, search, user create/login/delete with documented positive and negative cases | docs only | fair use | global | none | 200 |
| [Beeceptor Echo](https://beeceptor.com/) | Echo / mock endpoint | `https://echo.free.beeceptor.com` | fair use | global | none | 200 |
| [Beeceptor's CRUD APIs](https://beeceptor.com/crud-api/?ref=public-api-lists) | Free stateful CRUD APIs | docs only |  | global | none | 200 |
| [Big List of Naughty Strings (JSON)](https://github.com/minimaxir/big-list-of-naughty-strings) | Array of strings known to break input handling (SQLi/XSS/unicode/format) for fuzz and QA | `https://raw.githubusercontent.com/minimaxir/big-list-of-naughty-strings/master/blns.json` | MIT per https://github.com/minimaxir/big-list-of-naughty-strings/blob/master/LICENSE | global | none | 200 |
| [Country Info SOAP Service (oorsprong)](https://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso) | Long-running public SOAP/WSDL sample service (capital, ISO codes, flags, currencies, phone codes) widely used to test SOAP clients | `http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL` | fair use | global | none | 200 |
| [Dicebear Avatars](https://avatars.dicebear.com/) | Generate random pixel-art avatars | docs only |  | global | none | 200 |
| [Dummy REST API Example employees](https://dummy.restapiexample.com) | Employee list fixture (name, salary, age). | `https://dummy.restapiexample.com/api/v1/employees` | Aggressive rate limiting (429) at times. | global | none | 200 |
| [DummyJSON](https://dummyjson.com/docs) | Fake products, users, carts, recipes, quotes | `https://dummyjson.com/products/1` | fair use | global | none | 200 |
| [DummyJSON carts](https://dummyjson.com/docs/carts) | Carts with line items; nested-array fixture for tool schemas. | `https://dummyjson.com/carts?limit=5` |  | global | none | 200 |
| [DummyJSON HTTP status mock](https://dummyjson.com/docs) | /http/{code} returns a JSON status/message pair, for error-handling tests. | `https://dummyjson.com/http/200` |  | global | none | 200 |
| [DummyJSON product categories](https://dummyjson.com/docs/products) | JSON list of product categories with slug/name/url. | `https://dummyjson.com/products/categories` |  | global | none | 200 |
| [DummyJSON products search](https://dummyjson.com/docs/products) | Search endpoint on DummyJSON products (title, price, category, tags, reviews); realistic tool-calling fixture. | `https://dummyjson.com/products/search?q=phone&limit=5` |  | global | none | 200 |
| [DummyJSON recipes](https://dummyjson.com/docs/recipes) | Recipes with ingredients, instructions, tags, rating; text-rich fixture. | `https://dummyjson.com/recipes?limit=5` |  | global | none | 200 |
| [echo.websocket.org SSE](https://websocket.org/tools/websocket-echo-server/) | /.sse emits server-sent events (server.data, request headers) for SSE client tests; sibling /.ws is WebSocket echo. | `https://echo.websocket.org/.sse` | Stream stays open. | global | none | 200 |
| [English Random Words](https://random-words-api.vercel.app/word) | Generate English Random Words with Pronunciation | docs only |  | global | none | 200 |
| [Fake REST API](https://fake-rest-api-mobile-apps.vercel.app) | This API provides a simple and free platform to generate realistic JSON data for testing mobile apps and web applications. No authentication or signup is required, making it ideal for developers needing quick access to … | docs only |  | global | none | 200 |
| [FakeNamely](https://fakenamely.com/api) | Fictional identities, addresses and names for tests | docs only |  | global | none | 200 |
| [Faker](https://fakerjs.dev/) | Generate massive amounts of fake (but realistic) data for testing and development. | docs only |  | global | none | 200 |
| [FakeRESTApi (Azure)](https://fakerestapi.azurewebsites.net/index.html) | Swagger-documented fake REST API (Activities, Authors, Books, CoverPhotos, Users) supporting full CRUD for client and test automation practice | `https://fakerestapi.azurewebsites.net/api/v1/Books` | fair use | global | none | 200 |
| [FakeStoreAPI](https://fakestoreapi.com/docs) | Fake e-commerce products, carts, users | `https://fakestoreapi.com/products/1` | fair use | global | none | 200 |
| [FakeStoreAPI carts](https://fakestoreapi.com/docs) | Shopping-cart fixture with product ids and quantities. | `https://fakestoreapi.com/carts/1` |  | global | none | 200 |
| [FakeStoreAPI users](https://fakestoreapi.com/docs) | Users with nested address/geolocation; nested-object fixture. | `https://fakestoreapi.com/users/1` |  | global | none | 200 |
| [Fish Text](https://fish-text.ru/api) | Russian lorem ipsum | `https://fish-text.ru/get?type=sentence&number=2` | none | global | none | 200 |
| [flaky](https://flakyapi.dev) | Fake REST API with chaos controls: force any status code, add latency, or a failure rate | docs only |  | global | none | 200 |
| [Free Store API](https://www.iamtiksha.com/blog/free-store-api-web-dev-practice/) | The Store API is a dynamic REST API designed to simulate a real-world e-commerce backend. It allows developers to practice full-stack integration by handling features like JWT authentication, product filtering, persiste… | docs only |  | global | unconfirmed, check docs | 200 |
| [FreeAPI.app Random Users](https://freeapi.app/apis) | 500 paginated fake user profiles, randomuser-style | `https://api.freeapi.app/api/v1/public/randomusers` | none stated | global | none | 200 |
| [Genderize localized](https://genderize.io/) | Gender prediction with country\_id | `https://api.genderize.io/?name=andrea&country_id=IT` | 100/day | global | none | 200 |
| [GoREST](https://gorest.co.in/) | Online fake REST/GraphQL API for testing: users, posts, comments, todos; anonymous reads, free bearer token for writes | `https://gorest.co.in/public/v2/users` | fair use | global | none | 200 |
| [GraphQLZero](https://graphqlzero.almansi.me/) | JSONPlaceholder-style fake data over GraphQL | `https://graphqlzero.almansi.me/api?query=%7Buser%28id%3A1%29%7Bname%7D%7D` |  | global | none | 400 |
| [grpcbin](https://github.com/moul/grpcbin) | httpbin for gRPC: public gRPC request/response test server (unary, streaming, errors, headers) on grpcb.in:9000 plaintext and :9001 TLS; Docker image moul/grpcbin | docs only | fair use | global | none | 200 |
| [Hipster Ipsum](https://hipsum.co/the-api/) | Hipster lorem ipsum | `https://hipsum.co/api/?type=hipster-centric&paras=1` | none | global | none | 200 |
| [httpbin](https://httpbin.org/) | HTTP request/response testing service | `https://httpbin.org/get` | fair use | global | none | 200 |
| [httpbingo (go-httpbin)](https://github.com/mccutchen/go-httpbin) | Hosted go-httpbin, a maintained MIT-licensed Go reimplementation of httpbin for HTTP client testing (status codes, redirects, delays, auth, echo); alternative to httpbin.org | `https://httpbingo.org/get` | fair use | global | none | 200 |
| [httpbingo.org anything echo](https://httpbingo.org) | Go httpbin clone: echoes method, headers, args and body as JSON. | `https://httpbingo.org/anything` |  | global | none | 200 |
| [httpbingo.org NDJSON stream](https://httpbingo.org) | N lines of JSON request echo, streamed. NDJSON fixture. | `https://httpbingo.org/stream/3` |  | global | none | 200 |
| [httpbingo.org SSE stream](https://httpbingo.org) | text/event-stream with count param, ping events with JSON data. Mock SSE for streaming-client tests. | `https://httpbingo.org/sse?count=3&delay=100ms` |  | global | none | 200 |
| [httpbun](https://httpbun.com/) | Open-source HTTP client testing server inspired by httpbin, with extras (/mix, /payload, bodies on /get, any-method endpoints); self-hostable via Docker | `https://httpbun.com/get` | fair use | global | none | 200 |
| [ItsThisForThat](https://itsthisforthat.com/api.php) | Generate Random startup ideas | docs only |  | global | none | 200 |
| [JSONBlob](https://jsonblob.com/api) | Keyless JSON blob store: POST JSON to get a URL you can GET/PUT/DELETE; quick mock backend without signup | `POST https://jsonblob.com/api/jsonBlob {"people":["bill","steve"]}` | fair use | global | none | 200 |
| [JSONing](https://jsoning.com/api/) | Fake REST API for prototyping | docs only |  | global | none | 200 |
| [JSONPlaceholder](https://jsonplaceholder.typicode.com/) | Fake posts, users, todos REST API | `https://jsonplaceholder.typicode.com/posts/1` | fair use | global | none | 200 |
| [Korean JSON API](https://koreanjson.com/) | Super simple JSON API in Korean for GET, POST, PUT, DELETE actions providing JSON data in Korean for prototyping projects. | docs only |  | global | unconfirmed, check docs | 200 |
| [loremfile](https://loremfile.dev/docs/manifest) | Hotlinkable CC0 sample files in 78 formats, each with a SHA-256 in a JSON manifest | docs only |  | global | none | 200 |
| [Metaphorpsum](https://github.com/kylestetz/metaphorpsum) | Open-source (MIT) placeholder-text generator producing random metaphorical English sentences and paragraphs (/sentences/n, /paragraphs/n/m); adds readable lorem-ipsum alternative. | `http://metaphorpsum.com/sentences/3` | fair use | global | none | 200 |
| [Micro-Jaymock](https://micro-jaymock.now.sh/) | Tiny API mocking microservice for generating fake JSON data | docs only |  | global | none | 200 |
| [mock.shop (Shopify Storefront demo)](https://mock.shop/) | Shopify Storefront API mock store, no token | `https://mock.shop/api?query=%7Bproducts%28first%3A2%29%7Bedges%7Bnode%7Btitle%7D%7D%7D%7D` |  | global | none | 405 |
| [Mockae](https://mockae.com/) | Fake REST API powered by Lua | docs only |  | global | none | 200 |
| [MyFakeAPI Users](https://myfakeapi.com/) | Free fake REST API of users, products, cars, blog posts for prototyping | `https://myfakeapi.com/api/users/` | none stated | global | none | 200 |
| [NovaFortix Dev](https://public-dev-apis.surge.sh) | Zero-auth REST endpoints for mock user profiles, UUIDs and HTTP status codes | docs only |  | global | none | 200 |
| [Platzi Fake Store API](https://fakeapi.platzi.com/en/about/introduction/) | Fake store REST and GraphQL with auth | `https://api.escuelajs.co/api/v1/products?offset=0&limit=3` | fair use | global | none | 200 |
| [Postman Echo](https://www.postman-echo.com/) | Echo service for GET/POST/auth tests | `https://postman-echo.com/get?foo=bar` | fair use | global | none | 200 |
| [Postman Echo streamed JSON](https://www.postman-echo.com) | /stream/{n} returns n JSON chunks; chunked-response fixture. | `https://postman-echo.com/stream/3` |  | global | none | 200 |
| [Random User](https://randomuser.me/documentation) | Random user with localized names by nationality | `https://randomuser.me/api/?nat=fr,de` |  | global | none | 200 |
| [ReqRes resources list](https://reqres.in) | Paginated color-resources list (page, per\_page, total\_pages) pagination fixture. | `https://reqres.in/api/unknown` |  | global | none | 200 |
| [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) | Public practice CRUD API for learning API testing (bookings, basic+token auth, JSON/XML, deliberate bugs); data resets every 10 minutes | `https://restful-booker.herokuapp.com/booking` | rate-limited; resets every 10 min | global | none | 200 |
| [restful-api](https://restful-api.dev) | Fake REST API for testing and prototyping with CRUD endpoints | docs only |  | global | none | 200 |
| [Restful-API.dev](https://restful-api.dev/) | Free object store test API | `https://api.restful-api.dev/objects` | 100 req/day | global | none | 200 |
| [SampleAPIs Fake Bank](https://sampleapis.com/api-list/fakebank) | Fake bank accounts | `https://api.sampleapis.com/fakebank/accounts` | unknown | global | none | 200 |
| [Sampuli](https://sampuli.site/api) | Format-true synthetic test data for 90 countries: IDs, IBANs, cards, addresses | docs only |  | global | none | 200 |
| [seaborn-data: Anscombe Quartet](https://github.com/mwaskom/seaborn-data) | Anscombe's quartet CSV | `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/anscombe.csv` |  | global | none | 200 |
| [Short Id](https://github.com/aguedo/idgen) | Generate unique short Ids | docs only |  | global | none | 200 |
| [Sling Academy Sample Data](https://www.slingacademy.com/article/sample-users-free-fake-api-for-practicing-prototyping/) | Free mock API with 1000 fictitious users, photos, blog posts and products, with offset/limit/search params | `https://api.slingacademy.com/v1/sample-data/users` | fair use | global | none | 200 |
| [SMART Health IT Sandbox FHIR](https://docs.smarthealthit.org/) | Open FHIR R4 sandbox with synthetic patients | `https://r4.smarthealthit.org/Patient?_count=1` |  | global | none | 200 |
| [Supercrontab Mock Endpoints](https://supercrontab.com/mock) | Mock endpoints in 8 formats, each returning any of 14 HTTP status codes | docs only |  | global | none | 200 |
| [Swagger Petstore (v2)](https://petstore.swagger.io/) | Canonical OpenAPI sample server (pets, store orders, users) used to exercise API tooling and codegen; api\_key 'special-key' for auth tests | `https://petstore.swagger.io/v2/pet/findByStatus?status=available` | shared demo, data changes | global | none | 200 |
| [TestingAPIs](https://testingapis.com/docs/) | Free fake REST API with products, posts, todos, any HTTP status code and request echo | docs only |  | global | none | 200 |
| [This Person Does not Exist](https://thispersondoesnotexist.com) | Generates real-life faces of people who do not exist | docs only |  | global | none | 200 |
| [TotalShiftLeft Sandbox](https://demo.totalshiftleft.ai/) | Free multi-protocol sandbox: REST, GraphQL \& SOAP with OAuth2/JWT auth and OpenAPI 3.0 spec | docs only |  | global | none | 200 |
| [UI Names](https://github.com/thm/uinames) | Generate random fake names | docs only |  | global | none | 200 |
| [UUID Generator](https://www.uuidtools.com/docs) | Generate UUIDs | docs only |  | global | none | 200 |
| [UUID Tools API](https://www.uuidtools.com/docs) | Generate UUIDs | `https://www.uuidtools.com/api/generate/v4` |  | global | none | 200 |
| [Vendure Demo Shop API](https://docs.vendure.io/) | Vendure e-commerce read-only demo shop API | `https://readonlydemo.vendure.io/shop-api?query=%7Bproducts%28options%3A%7Btake%3A2%7D%29%7Bitems%7Bname%7D%7D%7D` |  | global | none | 200 |
| [Vietnamese Name DB](https://github.com/duyet/vietnamese-namedb) | Vietnamese given names (boy/girl, with and without accents) as text lists plus \~JSON records of full names split into family/middle/given names (MIT) | `https://raw.githubusercontent.com/duyet/vietnamese-namedb/master/uit_member.json` | fair use | VN | none | 200 |
| [Waldrand Avatar](https://avatar.waldrand.dev) | Deterministic SVG/PNG/WebP avatars from any string, four styles | docs only |  | global | none | 200 |
| [Webhook.site](https://docs.webhook.site/api/tokens.html) | Create disposable webhook/HTTP request-catcher URLs via API without an account; inspect captured requests (free tier 10 token creations/min) | `POST https://webhook.site/token {}` | 10 req/min free | global | none | 200 |
| [WebSocket.org Echo Server](https://websocket.org/tools/websocket-echo-server/) | Public echo endpoint for WebSocket (wss), Server-Sent Events (/.sse) and plain HTTP, with browser test UI at /.ws; for testing real-time clients | `wss://echo.websocket.org` | fair use | global | none | 200 |
| [What The Commit](https://whatthecommit.com/index.txt) | Random commit message generator | docs only |  | global | none | 200 |
| [Yes No](https://yesno.wtf/api) | Generate yes or no randomly | docs only |  | global | none | 200 |
