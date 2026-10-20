# Music & Audio APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [AcoustID](https://acoustid.org/webservice) | Audio fingerprint lookup to MusicBrainz ids; free app key | `https://api.acoustid.org/v2/lookup` | 3 req/s | global | free key | 200 |
| [AI Mastering](https://aimastering.com/api_docs/) | Automated Music Mastering | docs only |  | global | free key | 200 |
| [AudD](https://audd.io) | Music recognition from audio files, URLs, and live streams | docs only |  | global | free key | 200 |
| [audiometa.io](https://www.audiometa.io) | Aggregated live web signals and multiple APIs into one catalog. artists, tracks, playcounts, social reach, and more | docs only |  | global | free key | 200 |
| [Bandsintown](https://help.artists.bandsintown.com/en/articles/9186477-api-documentation) | Artist info and events; app\_id from artist registration | `https://rest.bandsintown.com/artists/Coldplay?app_id=x` | fair use | global | free key | 200 |
| [Conversion Tools](https://conversiontools.io/) | Online File Converter for documents, images, video, audio, and eBooks. REST API is available. Libraries for Node.js, PHP, Python. Support files up to 50 GB (for paid plans). The free tier is limited b | `https://conversiontools.io/` |  | global | free key | 200 |
| [Freesound](https://freesound.org/docs/api/) | CC-licensed sound effects and samples; free API key | `https://freesound.org/apiv2/search/text/?query=rain` | 60 req/min, 2000/day | global | free key | 200 |
| [Gemini API](https://ai.google.dev/docs) | The Gemini API provides developers with tools to leverage advanced AI models for content generation, including text, images, audio, and more. It enables seamless integration for creating applications that utilize state-… | docs only |  | global | free key | 302 |
| [Genius](https://docs.genius.com/) | Song and lyric metadata | `https://api.genius.com/search?q=kendrick` | unknown | global | free key | 403 |
| [GetSongBPM API](https://getsongbpm.com/api) | Song tempo (BPM), musical key, time signature, danceability and acousticness search by song/artist as JSON; free key, backlink to getsongbpm.com required | `https://api.getsong.co/search/?api_key=YOUR_API_KEY&type=song&lookup=hello` | free with attribution backlink | global | free key | 401 |
| [Jamendo](https://developer.jamendo.com/v3.0) | Free/CC licensed music catalog and streams; free client id | `https://api.jamendo.com/v3.0/tracks/?format=json&limit=1` | free non-commercial | global | free key | 200 |
| [Last.fm](https://www.last.fm/api) | Scrobbles, artist/album/track info, tags, charts; free key | `https://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&format=json` | fair use (\~5 req/s) | global | free key | 200 |
| [Listen Notes](https://www.listennotes.com/api/docs/) | Podcast search engine; free tier key (mock server keyless) | `https://listen-api-test.listennotes.com/api/v2/search?q=star` | free plan 300 req/month; test server returns mock data | global | free key | 200 |
| [Listen Notes Podcast API](https://www.podcastapi.com/) | Search podcasts and episodes, fetch metadata, get recommendations, and access audience insights. REST API with a free plan and official SDKs | docs only |  | global | free key | 403 |
| [Mubert AI Music API](https://landing.mubert.com) | Integrate AI music into your app, game or service | docs only |  | global | free key | 301 |
| [MusicGPT](https://musicgpt.com/api) | AI Music Generator with text-to-speech, voice changer, remix \& 20+ music features. | docs only |  | global | free key | 200 |
| [Musixmatch](https://developer.musixmatch.com/) | Lyrics snippets | `https://api.musixmatch.com/ws/1.1/chart.tracks.get` | 2000/day | global | free key | 200 |
| [Napster](https://developer.napster.com/api/v2.2) | Music | docs only |  | global | free key | 301 |
| [Napster API](https://developer.napster.com/api/v2.2) | Napster catalog metadata and charts with a free public apikey | `https://api.napster.com/v2.2/tracks/top` | fair use | global | free key | 301 |
| [Particle](https://particle.pro) | Podcast intelligence: podcast \& episode search, transcripts, speakers, entity mentions, sponsor \& advertising data, alerts and embeds | docs only |  | global | free key | 200 |
| [Phish.net API v5](https://docs.phish.net/) | Phish.net fan database API: shows, setlists, songs, venues, jamcharts and reviews for Phish as JSON/XML/HTML; free key from phish.net/api/keys | `https://api.phish.net/v5/shows/showdate/1997-11-22.json?apikey=YOUR_API_KEY` | fair use; filter queries | US | free key | 200 |
| [Phishin](https://phish.in/api-docs) | A web-based archive of legal live audio recordings of the improvisational rock band Phish | docs only |  | global | free key | 200 |
| [Podcast Index](https://podcastindex-org.github.io/docs-api/) | Open podcast directory: feeds, episodes, trending; free key+secret | `https://api.podcastindex.org/api/1.0/search/byterm?q=news` | fair use | global | free key | 200 |
| [Podchaser \| Podcast Data API](https://www.podchaser.com/api) | The podcast API for discovery and insights. Access 6M+ podcasts with audience demographics, transcripts, Apple/Spotify charts. For media monitoring and intel | docs only |  | global | free key | 200 |
| [Setlist.fm](https://api.setlist.fm/docs/1.0/index.html) | Concert setlists by artist/venue; free key for non-commercial | `https://api.setlist.fm/rest/1.0/search/artists?artistName=metallica` | 2 req/s, 1440/day | global | free key | 200 |
| [Songkick](https://www.songkick.com/developer/) | Music Events | docs only |  | global | free key | 406 |
| [Songlink / Odesli](https://www.notion.so/API-d0ebe08a5e304a55928405eb682f6741) | Get all the services on which a song is available | docs only |  | global | free key | 200 |
| [Spotify Web API](https://developer.spotify.com/documentation/web-api) | Catalog data via client credentials | `https://api.spotify.com/v1/search?q=x&type=track` | dynamic | global | free key | 200 |
| [Sunor](https://docs.sunor.cc) | AI music generation API via Suno, with pay-as-you-go credits | docs only |  | global | free key | 200 |
| [Taddy Podcast API](https://taddy.org/developers/podcast-api) | Podcast GraphQL API; free tier key | `https://api.taddy.org/` | free tier 500 req/month | global | free key | 200 |
| [Taddy Podcasts](https://taddy.org/developers/podcast-api) | Get details on podcasts \& episodes, Podcast \& Episode Search, Webhook notifications | docs only |  | global | free key | 200 |
| [VoiceRSS TTS](https://www.voicerss.org/api/) | Text-to-speech, 350 req/day free | `https://api.voicerss.org/?key=YOUR_KEY&hl=en-us&src=Hello` | 350 req/day | global | free key | 200 |
