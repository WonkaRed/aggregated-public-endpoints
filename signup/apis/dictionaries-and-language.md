# Dictionaries & Language APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [API Ninjas Dictionary](https://api-ninjas.com/api/dictionary) | English definitions | `https://api.api-ninjas.com/v1/dictionary?word=bright` | free tier | global | free key | 400 |
| [API Ninjas Rhyme](https://api-ninjas.com/api/rhyme) | Rhyming words | `https://api.api-ninjas.com/v1/rhyme?word=bright` | free tier | global | free key | 400 |
| [API Ninjas Text Language](https://api-ninjas.com/api/textlanguage) | Language detection | `https://api.api-ninjas.com/v1/textlanguage?text=hola` | free tier | global | free key | 400 |
| [API Ninjas Thesaurus](https://api-ninjas.com/api/thesaurus) | Synonyms/antonyms | `https://api.api-ninjas.com/v1/thesaurus?word=bright` | free tier | global | free key | 400 |
| [BabelNet API](https://babelnet.org/guide) | Multilingual encyclopedic dictionary (free key, 1000 babelcoins/day) | `https://babelnet.io/v9/getSynsetIds?lemma=apple&searchLang=EN&key=YOUR_KEY` | 1000 req/day | global | free key | 403 |
| [Behind the Name API](https://www.behindthename.com/api/) | Name meanings, usage, related names | `https://www.behindthename.com/api/lookup.json?name=mary&key=YOUR_KEY` | free key | global | free key | 200 |
| [Collins](https://api.collinsdictionary.com/api/v1/documentation/html/) | Bilingual Dictionary and Thesaurus Data | docs only |  | global | free key | 403 |
| [Detect Language API](https://detectlanguage.com/documentation) | Language detection, 1000 req/day free | `https://ws.detectlanguage.com/0.2/detect?q=buenos%20dias` | 1000 req/day | global | free key | 401 |
| [DetectLanguage](https://detectlanguage.com/documentation) | Language detection (key) | `https://ws.detectlanguage.com/0.2/languages` | free key 1000/day | global | free key | 200 |
| [Farasa Arabic NLP API](https://farasa.qcri.org/) | QCRI Farasa Arabic toolkit web API: segmentation, lemmatization, POS, NER, diacritization, spellcheck; free registered key (research use) | `POST https://farasa.qcri.org/webapi/segmentation/ {"text":"يقول إن اللغات الطبيعية","api_key":"YOUR_KEY"}` | fair use | global | free key | 401 |
| [Igbo API](https://docs.igboapi.com) | Igbo-English dictionary API returning words with part of speech, definitions, example sentences, audio pronunciations and Nsibidi; free API key via signup (X-API-Key header) | `https://igboapi.com/api/v2/words?keyword=bia` | fair use | NG | free key | 400 |
| [KanjiAlive (RapidAPI)](https://app.kanjialive.com/api/docs) | Kanji with stroke video, radicals and examples | `https://kanjialive-api.p.rapidapi.com/api/public/kanji/親` | RapidAPI free tier | JP | free key | 401 |
| [Korean Basic Dictionary (krdict) Open API](https://krdict.korean.go.kr/openApi/openApiInfo) | National Institute of Korean Language learner dictionary | `https://krdict.korean.go.kr/api/search?key=YOUR_KEY&q=나무` | 50k/day | KR | free key | 400 |
| [Lexicala API](https://api.lexicala.com/documentation/) | Multilingual dictionary data (50 languages), free tier via RapidAPI | `https://lexicala1.p.rapidapi.com/search?text=hello&language=en` | free tier | global | free key | 401 |
| [Lingua Robot](https://www.linguarobot.io/) | English dictionary with inflections (RapidAPI) | `https://lingua-robot.p.rapidapi.com/language/v1/entries/en/example` | free tier | global | free key | 401 |
| [Merriam-Webster](https://dictionaryapi.com/) | Dictionary and Thesaurus Data | docs only |  | global | free key | 200 |
| [Merriam-Webster Collegiate](https://dictionaryapi.com/) | Collegiate dictionary and thesaurus JSON | `https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key=YOUR_KEY` | 1000 req/day non-commercial | US | free key | 200 |
| [Merriam-Webster Thesaurus](https://dictionaryapi.com/products/api-collegiate-thesaurus) | Collegiate thesaurus JSON | `https://www.dictionaryapi.com/api/v3/references/thesaurus/json/umpire?key=YOUR_KEY` | 1000 req/day non-commercial | US | free key | 200 |
| [Owlbot Dictionary API](https://owlbot.info/) | English dictionary: definitions, pronunciation, example sentences, images and emoji; free token by email | `https://owlbot.info/api/v4/dictionary/owl` | fair use | global | free key | 403 |
| [Oxford](https://developer.oxforddictionaries.com/) | Dictionary Data | docs only |  | global | free key | 200 |
| [Random Word API (vercel)](https://random-word-api.vercel.app/) | Random words by length/type | `https://random-word-api.vercel.app/api?words=10` |  | global | payment required | 402 |
| [SayItVid](https://sayitvid.com) | English video pronunciation search with timestamps, IPA phonetics and subtitle context | docs only |  | global | free key | 200 |
| [Standard Korean Dictionary API](https://stdict.korean.go.kr/openapi/openApiInfo.do) | National Institute of Korean Language standard dictionary search | `https://stdict.korean.go.kr/api/search.do?key=YOUR_KEY&q=%EB%82%98%EB%AC%B4&req_type=json` | 50k req/day | KR | free key | 200 |
| [Synonyms](https://www.synonyms.com/synonyms_api.php) | Synonyms, thesaurus and antonyms information for any given word | docs only |  | global | free key | 200 |
| [TemplateFox](https://pdftemplateapi.com) | PDF generation API with a visual template editor, dynamic data merging, and SDKs for 7 languages. Free plan includes 60 PDFs/month and 3 templates | `https://pdftemplateapi.com` |  | global | free key | 200 |
| [Text Analysis - Sapling grammar](https://sapling.ai/docs/) | Grammar/spell check API (free tier) | `https://api.sapling.ai/api/v1/edits` | free tier | global | free key | 405 |
| [Urimalsaem Open Dictionary API](https://opendict.korean.go.kr/service/openApiInfo) | Korean open crowd dictionary search | `https://opendict.korean.go.kr/api/search?key=YOUR_KEY&q=%EB%82%98%EB%AC%B4&req_type=json` |  | KR | free key | 200 |
| [WaniKani API](https://docs.api.wanikani.com/) | Japanese kanji/vocab subjects (personal token) | `https://api.wanikani.com/v2/subjects?types=kanji` | free account token | JP | free key | 401 |
| [Wordnik](https://developer.wordnik.com/) | Definitions, examples, word of the day, related words | `https://api.wordnik.com/v4/word.json/hello/definitions?api_key=YOUR_KEY` | free key | global | free key | 401 |
| [Wordnik Word of the Day](https://developer.wordnik.com/docs) | Daily word with definitions | `https://api.wordnik.com/v4/words.json/wordOfTheDay?api_key=YOUR_KEY` | free key | global | free key | 401 |
| [Words](https://www.wordsapi.com/docs/) | Definitions and synonyms for more than 150,000 words | docs only |  | global | free key | 200 |
| [WordsAPI (RapidAPI)](https://www.wordsapi.com/docs/) | English words: definitions, synonyms, syllables, frequency | `https://wordsapiv1.p.rapidapi.com/words/hatchback/typeOf` | 2500 req/day free | global | free key | 401 |
| [Yahoo! JAPAN Furigana API](https://developer.yahoo.co.jp/webapi/jlp/furigana/v2/furigana.html) | Adds furigana/romaji readings to Japanese text (JSON-RPC) | `https://jlp.yahooapis.jp/FuriganaService/V2/furigana` | POST JSON-RPC | JP | free key | 401 |
| [Yahoo! JAPAN Morphological Analysis API](https://developer.yahoo.co.jp/webapi/jlp/ma/v2/parse.html) | Yahoo! JAPAN Text Analysis (JLP) morphological analysis V2: JSON-RPC POST that tokenises Japanese text into words with part-of-speech, reading and base form. Free Client ID (AppID) from Yahoo! Developer Network. Distinc… | `https://jlp.yahooapis.jp/MAService/V2/parse` | daily request quota per AppID | JP | free key | 401 |
| [Yandex Dictionary API](https://yandex.com/dev/dictionary/) | Bilingual dictionary lookups (free key, legacy) | `https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=YOUR_KEY&lang=en-ru&text=time` | 10k req/day | global | free key | 403 |
