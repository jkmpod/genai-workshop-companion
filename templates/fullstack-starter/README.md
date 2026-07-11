# Full-stack Starter — FastAPI proxy + minimal chat page

`[level: builder] [effort: weekend] [license: GPLv3, original]`

The security-critical pattern from the companion app itself: **your API key lives on the server, never in the browser.** A FastAPI backend proxies chat requests; a single HTML page talks to it.

## Why this template exists
The #1 beginner mistake in GenAI apps is shipping the API key in frontend code. This template is the antidote — the same server-proxy pattern shown in [app/ARCHITECTURE.md](../../app/ARCHITECTURE.md).

## Run it
```bash
pip install fastapi uvicorn openai
export OPENROUTER_API_KEY=sk-or-...
uvicorn main:app --reload      # then open http://localhost:8000
```

## Where it deliberately stops (your exercises)
1. No auth — add the magic-link pattern from the companion app spec
2. No rate limit — add a per-IP counter (the quota-teaching pattern)
3. No retrieval — merge with `rag-starter` for a full RAG web app
