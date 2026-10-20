# Education APIs

[Back to the signup index](../README.md)

| Name | Description | Example call | Limits | Region | Auth | Status |
|---|---|---|---|---|---|---|
| [API Ninjas Trivia](https://api-ninjas.com/apis/trivia) | Random trivia question/answer pairs (category, question, answer); free key covers 100-question pool | `https://api.api-ninjas.com/v1/trivia` | free tier: 100 questions, limit param premium | global | free key | 400 |
| [bund.dev Studiensuche API](https://studiensuche.api.bund.dev/) | University study programme search | `https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote` |  | DE | free key | 403 |
| [CareerNet Open API](https://www.career.go.kr/cnet/front/openapi/openApiSchoolCenter.do) | KRIVET CareerNet (Korea Research Institute for Vocational Education \& Training) API: Korean school and university directory (svcCode=SCHOOL), majors, job encyclopedia, career counselling cases; JSON or XML. | `https://www.career.go.kr/cnet/openapi/getOpenApi?apiKey=YOUR_KEY&svcType=api&svcCode=SCHOOL&contentType=json&gubun=univ_list` | free key on registration | KR | free key | 200 |
| [CLIST API v4](https://clist.by/api/v4/doc/) | Aggregated competitive-programming contest calendar, problems and ratings across 200+ judges (Codeforces, AtCoder, LeetCode...); free key after login | `https://clist.by/api/v4/contest/?upcoming=true&format=json` | 10 req/min default | global | free key | 401 |
| [College Scorecard API](https://collegescorecard.ed.gov/data/api-documentation/) | US college costs, admissions, debt, earnings and completion data per institution | `https://api.data.gov/ed/collegescorecard/v1/schools?api_key=DEMO_KEY&school.name=Harvard` | api.data.gov key; DEMO\_KEY 30/hr, 1000/hr with free key | US | free key | 200 |
| [Current Affairs](https://rapidapi.com/malaithiru370/api/current-affairs-of-india) | Current International Affairs, quizzes and more | docs only |  | global | free key | 200 |
| [QuizAPI](https://quizapi.io/docs/1.0/overview) | Tech quiz questions (Linux, DevOps, code, SQL) | `https://quizapi.io/api/v1/questions?limit=5` |  | global | free key | 401 |
| [University of Waterloo Open Data API](https://openapi.data.uwaterloo.ca/api-docs/index.html) | Waterloo courses, class schedules, terms, locations | `https://openapi.data.uwaterloo.ca/v3/Terms` |  | CA | free key | 401 |
| [Wolfram Alpha Short Answers](https://products.wolframalpha.com/short-answers-api/documentation) | Computational answers (AppID) | `https://api.wolframalpha.com/v1/result?i=2%2B2` | 2000 calls/month free AppID | global | free key | 200 |
