# Security & Threat Intel APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [Abuse IPDB blacklist](https://docs.abuseipdb.com/#blacklist-endpoint) | Top reported IPs (blacklist endpoint) | `https://api.abuseipdb.com/api/v2/blacklist` | 5 req/day free | global | free key | 401 |
| [abuse.ch Hunting API](https://hunting.abuse.ch/api/) | Unified cross-platform IOC search across abuse.ch projects | `https://hunting-api.abuse.ch/api/v1/` | Free Auth-Key | global | free key | 405 |
| [AbuseIPDB](https://docs.abuseipdb.com/) | IP/domain/URL reputation | docs only |  | global | free key | 200 |
| [AbuseIPDB API](https://docs.abuseipdb.com/) | IP abuse reports and confidence score (key) | `https://api.abuseipdb.com/api/v2/check` | 1000 checks/day free | global | free key | 200 |
| [AlienVault Open Threat Exchange (OTX)](https://otx.alienvault.com/api) | IP/domain/URL reputation | docs only |  | global | free key | 200 |
| [Application Environment Verification](https://github.com/fingerprintjs/aev) | Android library and API to verify the safety of user devices, detect rooted devices and other risks | docs only |  | global | free key | 200 |
| [ArkForge Trust Layer](https://arkforge.fr/trust) | Cryptographic proof API for HTTP exchanges — Ed25519, RFC 3161, and Sigstore Rekor attestation | docs only |  | global | free key | 200 |
| [Botd](https://github.com/fingerprintjs/botd) | Botd is a browser library for JavaScript bot detection | docs only |  | global | free key | 200 |
| [Bugcrowd](https://docs.bugcrowd.com/api/getting-started/) | Bugcrowd API for interacting and tracking the reported issues programmatically | docs only |  | global | free key | 200 |
| [CAPEsandbox](https://capev2.readthedocs.io/en/latest/usage/api.html) | Malware execution and analysis | docs only |  | global | free key | 200 |
| [Censys](https://search.censys.io/api) | Search engine for Internet connected host and devices | docs only |  | global | free key | 403 |
| [Censys Platform API](https://docs.censys.com/) | Host, certificate and web property search | `https://api.platform.censys.io/v3/global/asset/host/8.8.8.8` | Free tier with limited monthly credits | global | free key | 401 |
| [Censys Search](https://search.censys.io/api) | Internet host search (key/OAuth) | `https://search.censys.io/api/v2/metadata` | free tier limited | global | free key | 403 |
| [Chainabuse API](https://docs.chainabuse.com/) | Reported crypto scam addresses | `https://api.chainabuse.com/v0/reports?address=0x0` | Free key | global | free key | 401 |
| [CISA Known Exploited Vulnerabilities](https://rapidapi.com/crisp-point-studio-crisp-point-studio-default/api/live-cisa-cybersecurity-vulnerabilities-kev) | CISA KEV catalog of actively exploited CVEs as JSON, filterable by vendor, with CWE and due dates | docs only |  | global | free key | 200 |
| [ClassiFinder](https://classifinder.ai) | Detect leaked secrets and prompt-injection in text and return redacted output | docs only |  | global | free key | 200 |
| [Cloudflare Radar API](https://developers.cloudflare.com/radar/) | Internet traffic, attacks, BGP hijacks, URL scanner | `https://api.cloudflare.com/client/v4/radar/attacks/layer7/summary` | Free Cloudflare API token | global | free key | 400 |
| [Complete Criminal Checks](https://completecriminalchecks.com/Developers) | Provides data of offenders from all U.S. States and Pureto Rico | docs only |  | global | free key | 200 |
| [CompliAPI](https://docs.compliapi.com) | Screen crypto addresses, emails, websites, IDs and countries against OFAC, EU, UK sanctions lists | docs only |  | global | free key | 200 |
| [Criminal IP API](https://www.criminalip.io/developer/api) | IP/domain risk, asset search | `https://api.criminalip.io/v1/asset/ip/report?ip=8.8.8.8` | Free plan credits | global | free key | 200 |
| [CVEdetails API](https://www.cvedetails.com/documentation/apis) | CVE and product vulnerability stats | `https://www.cvedetails.com/api/v1/vulnerability/info?cveId=CVE-2021-44228` | Free account token | global | free key | 401 |
| [Cyber Cure free intelligence feeds](https://www.cybercure.ai/) | Cyber Cure offers free cyber threat intelligence feeds with lists of IP addresses that are currently infected and attacking on the internet. There are list of urls used by malware and list of hash fil | `https://www.cybercure.ai/` |  | global | free key | 200 |
| [DNSDumpster API](https://dnsdumpster.com/developer/) | DNS recon: A, MX, NS, TXT and subdomains | `https://api.dnsdumpster.com/domain/example.com` | Free key, 1 req/2s | global | free key | 401 |
| [Dymo API](https://dymo.tpeoficial.com/products/dymo-api) | Fraud \& reputation detection | docs only |  | global | free key | 200 |
| [Ecosyste.ms Advisories](https://advisories.ecosyste.ms/docs) | Security advisories aggregated across package ecosystems (GHSA etc.) with package mapping (ecosyste.ms, CC BY-SA data, AGPL code) | `https://advisories.ecosyste.ms/api/v1/advisories?per_page=2` | 5000 req/h | global | payment required | 402 |
| [Ecosyste.ms Dependabot](https://dependabot.ecosyste.ms/docs) | Dependabot pull requests across open source, by package/advisory (ecosyste.ms, CC BY-SA data, AGPL code) | `https://dependabot.ecosyste.ms/api/v1/packages?per_page=2` | 5000 req/h | global | payment required | 402 |
| [Events API](https://events.1password.com) | 1Password Events API Specification. | `https://events.1password.com/api/auth/introspect` |  | global | free key | 401 |
| [FastIntercept](https://intercept.sh/threatlists/) | Intercept Security hosts a number of free IP Reputation lists from their global honeypot network | `https://intercept.sh/threatlists/` |  | global | free key | 200 |
| [Fidro](https://fidro.io) | Fraud detection API returning a weighted risk score from VPN, proxy, Tor and datacenter IP detection, email validation and Stripe payment signals | docs only |  | global | free key | 200 |
| [Filescan.io / OPSWAT](https://www.filescan.io/api/docs) | File scanning and reputation | `https://www.filescan.io/api/reports/search` | Free key | global | free key | 200 |
| [FingerprintJS Pro](https://dev.fingerprintjs.com/docs) | Fraud detection API offering highly accurate browser fingerprinting | docs only |  | global | free key | 200 |
| [FOFA](https://en.fofa.info/api) | Search engine for Internet connected assets and devices | docs only |  | global | free key | 200 |
| [FullHunt](https://api-docs.fullhunt.io/#introduction) | Searchable attack surface database of the entire internet | docs only |  | global | free key | 403 |
| [Google reCAPTCHA](https://developers.google.com/recaptcha/intro?hl=en) | ReCAPTCHA lets you embed a CAPTCHA in your web pages in order to protect them against spam and other types of automated abuse. | docs only |  | global | free key | 200 |
| [Google Safe Browsing](https://developers.google.com/safe-browsing/v4) | URL threat lookups (key) | `https://safebrowsing.googleapis.com/v4/threatMatches:find` | free key non-commercial | global | free key | 200 |
| [GreyNoise](https://docs.greynoise.io/reference/getcommunityip) | Query IPs in the GreyNoise dataset and retrieve a subset of the full IP context data | docs only |  | global | free key | 200 |
| [HackerOne](https://api.hackerone.com/) | The industry’s first hacker API that helps increase productivity towards creative bug bounty hunting | docs only |  | global | free key | 200 |
| [HaveIBeenPwned](https://haveibeenpwned.com/API/v3) | Passwords which have previously been exposed in data breaches | docs only |  | global | free key | 200 |
| [Hybrid Analysis](https://www.hybrid-analysis.com/docs/api/v2) | Malware sandbox reports (key) | `https://www.hybrid-analysis.com/api/v2/key/current` | free key | global | free key | 200 |
| [Hybrid Analysis API](https://www.hybrid-analysis.com/docs/api/v2) | Falcon Sandbox malware analysis reports and search | `https://www.hybrid-analysis.com/api/v2/search/hash` | Free key (vetting for full access) | global | free key | 403 |
| [IBM X-Force Exchange](https://api.xforce.ibmcloud.com/doc/) | IP/URL/malware reputation, collections | `https://api.xforce.ibmcloud.com/api/ipr/8.8.8.8` | Free tier 5000/month | global | free key | 401 |
| [Intelligence X](https://github.com/IntelligenceX/SDK/blob/master/Intelligence%20X%20API.pdf) | Perform OSINT via Intelligence X | docs only |  | global | free key | 200 |
| [IPASIS](https://ipasis.com) | Bot detection and fraud prevention API with IP reputation and email validation | docs only |  | global | free key | 200 |
| [IPHub](https://iphub.info/api) | Residential vs non-residential IP classification | `https://v2.api.iphub.info/ip/8.8.8.8` | 1,000/day free | global | free key | 403 |
| [IPinfo](https://ipinfo.io/) | Fast, accurate, and free (up to 50k/month) IP address data API. Offers APIs with details on geolocation, companies, carriers, IP ranges, domains, abuse contacts, and more. All paid APIs can be trialed | `https://ipinfo.io/` |  | global | free key | 200 |
| [IPQualityScore](https://www.ipqualityscore.com/documentation/overview) | Fraud, proxy, email validation (key) | `https://www.ipqualityscore.com/api/json/ip/KEY/8.8.8.8` | 1000 lookups/month | global | free key | 200 |
| [IPQualityScore Proxy/VPN API](https://www.ipqualityscore.com/documentation/overview) | Fraud score, proxy/VPN/Tor detection for IPs; email \& URL checks | `https://www.ipqualityscore.com/api/json/ip/YOUR_KEY/8.8.8.8` | \~1,000 lookups/month free | global | free key | 200 |
| [IPScanner](https://ipscanner.io/api-documentation) | IP network class (residential, mobile, hosting, VPN, residential proxy, Tor) with a confidence score | docs only |  | global | free key | 200 |
| [isMalicious](https://ismalicious.com/api-docs) | Reputation of IPs, domains, URLs and file hashes from aggregated threat feeds, plus CVE lookups | docs only |  | global | free key | 200 |
| [Jumio](https://www.jumio.com/developer/) | Provides identity verification, KYC (Know Your Customer), and AML (Anti-Money Laundering) solutions, including document verification and biometric authentication | docs only |  | global | free key | 200 |
| [Kaspersky OpenTIP](https://opentip.kaspersky.com/Help/Doc_data/en-US/OpenTIPAPI.htm) | Threat Intelligence Portal hash/IP/domain/URL lookup | `https://opentip.kaspersky.com/api/v1/search/hash?request=44d88612fea8a8f36de82e1278abb02f` | Free key, 2000/day | global | free key | 401 |
| [Kiprio SSL Inspector](https://kiprio.com/ssl-api) | TLS certificate analysis with protocol matrix, cipher suite and HSTS grading | docs only |  | global | free key | 200 |
| [LeakInsight](https://rapidapi.com/codigo6-codigo6-default/api/leakinsight-api/) | Find leaked or exposed credentials by email, username, phone, domain, hash, or breach origin | docs only |  | global | free key | 308 |
| [LeakIX API](https://docs.leakix.net/) | Exposed services and leaks search | docs only | Free key; JSON with Accept header | global | free key | 200 |
| [LoginRadius](https://www.loginradius.com/docs/) | Managed User Authentication Service | docs only |  | global | free key | 200 |
| [MalDatabase](https://maldatabase.com/api-doc.html) | Provide malware datasets and threat intelligence feeds | docs only |  | global | free key | 200 |
| [Malshare](https://malshare.com/doc.php) | Malware repository (key) | `https://malshare.com/api.php?action=getlimit` | free key | global | free key | 200 |
| [MalShare API](https://malshare.com/doc.php) | Malware sample repository: daily hash lists, search, download | docs only | Free key, \~2000 calls/day | global | free key | 400 |
| [MalShare.com](http://www.malshare.com/) | The MalShare Project is a public malware repository that provides researchers free access to samples | `http://www.malshare.com/` |  | global | free key | 200 |
| [Malwagon](https://malwagon.com/docs/api) | Detonates files and URLs in instrumented VMs and returns behaviour, IOCs and ATT\&CK | docs only |  | global | free key | 200 |
| [MalwareBazaar](https://bazaar.abuse.ch/api/) | Collect and share malware samples | docs only |  | global | free key | 200 |
| [MalwareBazaar API](https://bazaar.abuse.ch/api/) | Malware samples hash database (free Auth-Key) | `https://mb-api.abuse.ch/api/v1/` | free auth key | global | free key | 200 |
| [Maskbreak](https://maskbreak.com/api) | Detect VPNs, proxies, Tor, bots and antidetect browsers at signup, login and checkout | docs only |  | global | free key | 200 |
| [MetaDefender Cloud](https://docs.opswat.com/mdcloud) | Multi-AV hash/IP/URL lookup | `https://api.metadefender.com/v4/hash/6A5C19D9FFE8804586E8F4C0DFCC66DE` | Free key, daily limits | global | free key | 401 |
| [MXToolbox API](https://mxtoolbox.com/restapi.aspx) | Blacklist and DNS checks | `https://mxtoolbox.com/api/v1/Lookup/blacklist/?argument=8.8.8.8` | Free tier | global | free key | 401 |
| [Neetix Liveliness](https://liveliness.neetix.in/api-reference) | Face liveness, presentation-attack detection and 1:1 face match for identity verification | docs only |  | global | free key | 200 |
| [Netlas API](https://docs.netlas.io/) | Internet scan data search | `https://app.netlas.io/api/responses/?q=host:example.com` | Free community plan | global | free key | 200 |
| [NoPhishy](https://rapidapi.com/Amiichu/api/exerra-phishing-check/) | Check links to see if they're known phishing attempts | docs only |  | global | free key | 200 |
| [Offendersearch](https://offendersearch.app) | Search sex-offender records across all 58 US state, territory and tribal registries in one query; REST API plus open data | docs only |  | global | free key | 200 |
| [ONYPHE API](https://www.onyphe.io/documentation/api) | Cyber defense search engine | `https://www.onyphe.io/api/v2/summary/ip/8.8.8.8` | Free tier | global | free key | 400 |
| [OpenPhish Feeds](https://openphish.com/phishing_feeds.html) | OpenPhish receives URLs from multiple streams and analyzes them using its proprietary phishing detection algorithms. There are free and commercial offerings available | `https://openphish.com/phishing_feeds.html` |  | global | free key | 200 |
| [OpenSanctions API](https://api.opensanctions.org/) | Sanctions, PEPs and entities of interest, match/search | `https://api.opensanctions.org/search/default?q=putin` | free for non-commercial; key required | global | free key | 401 |
| [Patronus Protect](https://api.patronus.studio/) | Detect prompt injection in text, public webpages and documents for AI agents and RAG pipelines | docs only |  | global | free key | 200 |
| [Privacy.com](https://privacy.com/developer/docs) | Generate merchant-specific and one-time use credit card numbers that link back to your bank | docs only |  | global | free key | 301 |
| [Project Honey Pot http:BL](https://www.projecthoneypot.org/httpbl_api.php) | DNS-based harvester/spammer IP lookup | docs only | Free access key; DNS query | global | free key | 200 |
| [ProjectDiscovery CVEDB API](https://docs.projectdiscovery.io/) | CVE intel with PoCs, KEV, EPSS, template coverage | `https://api.projectdiscovery.io/v2/vulnerability/search?q=log4j` | Free PDCP key | global | free key | 200 |
| [Pulsedive](https://pulsedive.com/api/) | Scan, search and collect threat intelligence data in real-time | docs only |  | global | free key | 302 |
| [Pulsedive API](https://pulsedive.com/api/) | Threat intel IOC enrichment, risk scoring, threats and feeds | `https://pulsedive.com/api/info.php?indicator=pulsedive.com` | Free key; \~30 req/min, 1000/day | global | free key | 200 |
| [Rutgers Blacklisted IPs](https://report.cs.rutgers.edu/mrtg/drop/dropstat.cgi?start=-86400) | IP List of SSH Brute force attackers is created from a merged of locally observed IPs and 2 hours old IPs registered at badip.com and blocklist.de | `https://report.cs.rutgers.edu/mrtg/drop/dropstat.cgi?start=-86400` |  | global | free key | 200 |
| [Scanii](https://docs.scanii.com/) | Simple REST API that can scan submitted documents/files for the presence of threats | docs only |  | global | free key | 200 |
| [Sealed Rose](https://sealedrose.com/verify-video) | AI media forensics and synthetic content verification for video, audio, image, and text | docs only |  | global | free key | 200 |
| [SecurityHeaders.com](https://securityheaders.com/api/) | Security header grade (key) | `https://securityheaders.com/` | free key | global | free key | 200 |
| [SecurityTrails API](https://docs.securitytrails.com/) | DNS history and domain data (key) | `https://api.securitytrails.com/v1/ping` | 50 req/month free | global | free key | 200 |
| [Shodan](https://developer.shodan.io/) | Search engine for Internet connected devices | docs only |  | global | free key | 200 |
| [Shodan API](https://developer.shodan.io/api) | Internet-wide scan search and host lookups | `https://api.shodan.io/shodan/host/8.8.8.8?key=YOUR_KEY` | Free account: limited host lookups, no search filters | global | free key | 200 |
| [Shodan Exploits API](https://developer.shodan.io/api/exploits/rest) | Search exploits across ExploitDB, Metasploit, CVE | docs only |  | global | free key | 200 |
| [Shodan Honeyscore](https://developer.shodan.io/api) | Probability an IP is a honeypot | docs only |  | global | free key | 401 |
| [SniffCat](https://sniffcat.com/) | IP abuse lookup, reporting and threat intelligence | docs only |  | global | free key | 200 |
| [Sonatype OSS Index](https://ossindex.sonatype.org/rest) | Component vulnerability lookup by PURL | `https://ossindex.sonatype.org/api/v3/component-report` | Free token now required | global | free key | 401 |
| [Spamhaus Intelligence API](https://docs.spamhaus.com/) | IP/domain listing info from Spamhaus | docs only | Free tier for non-commercial (DQS free account) | global | free key | 200 |
| [Spyse](https://spyse-dev.readme.io/reference/quick-start) | Access data on all Internet assets and build powerful attack surface management applications | docs only |  | global | free key | 200 |
| [Strongarm, by Percipient Networks](https://strongarm.io) | Strongarm is a DNS blackhole that takes action on indicators of compromise by blocking malware command and control. Strongarm aggregates free indicator feeds, integrates with commercial feeds, utilize | `https://strongarm.io` |  | global | free key | 200 |
| [ThreatBook](https://x.threatbook.com/api) | Threat intel IP/domain reputation (CN) | `https://api.threatbook.io/v1/community/ip?apikey=KEY&resource=8.8.8.8` | Free community | global | free key | 401 |
| [ThreatCluster](https://threatcluster.io/api/public/v1/docs) | Threat intelligence: incident clusters, validated IOCs, CVEs, ransomware leak-site victims | docs only |  | global | free key | 200 |
| [threatfeeds.io](https://threatfeeds.io) | threatfeeds.io lists free and open-source threat intelligence feeds and sources and provides direct download links and live summaries | `https://threatfeeds.io` |  | global | free key | 200 |
| [ThreatFox API](https://threatfox.abuse.ch/api/) | IOC sharing platform from abuse.ch (free Auth-Key) | `https://threatfox-api.abuse.ch/api/v1/` | free auth key | global | free key | 200 |
| [Trade.gov Consolidated Screening List](https://developer.trade.gov/) | Export-restricted party screening | `https://data.trade.gov/consolidated_screening_list/v1/search?name=acme` | Free key | US | free key | 200 |
| [Triage (tria.ge) API](https://tria.ge/docs/) | Recorded Future sandbox reports and search | `https://tria.ge/api/v0/search?query=family:emotet` | Free researcher account | global | free key | 401 |
| [URLhaus API](https://urlhaus.abuse.ch/api/) | Malware distribution URLs database, abuse.ch Auth-Key (free) | `https://urlhaus-api.abuse.ch/v1/urls/recent/` | free auth key | global | free key | 200 |
| [URLScan.io](https://urlscan.io/about-api/) | Scan and Analyse URLs | docs only |  | global | free key | 200 |
| [Validin API](https://app.validin.com/docs) | Passive DNS and host response history | `https://app.validin.com/api/axon/domain/dns/history/example.com` | Free community key | global | free key | 403 |
| [Verisys Antivirus API](https://www.ionxsolutions.com/products/antivirus-api) | Antivirus as a service - REST API that scans provided files for malware and NSFW content | docs only |  | global | free key | 200 |
| [Virus and Malware Scan API by attachmentAV](https://attachmentav.com/solution/virus-malware-scan-api/) | Scan files for viruses, worms, trojans, ransomware, and other kinds of malware by sending them to the attachmentAV API powered by Sophos | docs only |  | global | free key | 200 |
| [VirusTotal](https://docs.virustotal.com/reference/overview) | VirusTotal File/URL Analysis | docs only |  | global | free key | 200 |
| [VirusTotal API v3](https://docs.virustotal.com/reference/overview) | File, URL, domain, IP reputation (key) | `https://www.virustotal.com/api/v3/domains/google.com` | 4 req/min 500/day free | global | free key | 200 |
| [vpnapi.io](https://vpnapi.io/api-documentation) | VPN/proxy/Tor detection | `https://vpnapi.io/api/8.8.8.8?key=YOUR_KEY` | 1,000/day free | global | free key | 403 |
| [VulDB](https://vuldb.com/?doc.api) | VulDB API allows to initiate queries for one or more items along with transactional bots | docs only |  | global | free key | 403 |
| [VulnCheck KEV](https://docs.vulncheck.com/) | Extended KEV and NVD++ community data | `https://api.vulncheck.com/v3/index/vulncheck-kev` | Free community tier | global | free key | 401 |
| [Vulners API](https://vulners.com/docs/) | Vulnerability DB search, exploits, bulletins | docs only | Free community key | global | free key | 403 |
| [Web of Trust](https://support.mywot.com/hc/en-us/sections/360004477734-API-) | IP/domain/URL reputation | docs only |  | global | free key | 403 |
| [Web Of Trust (WOT)](https://www.mywot.com/developers/) | Website reputation | docs only |  | global | free key | 200 |
| [WPScan API](https://wpscan.com/api/) | WordPress core/plugin/theme vulnerabilities | `https://wpscan.com/api/v3/plugins/contact-form-7` | 25 req/day free | global | free key | 403 |
| [YARAify API](https://yaraify.abuse.ch/api/) | abuse.ch YARA scanning and rule hub: lookup hashes, query rules | `https://yaraify-api.abuse.ch/api/v1/` | POST; free Auth-Key | global | free key | 405 |
