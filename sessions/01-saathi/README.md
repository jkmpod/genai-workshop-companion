# Session 1 — Saathi: Family Health Memory App (4 Jul 2026)

**One line:** manage and question your family's health records in natural language — document understanding + wearables + RAG with guardrails.

## Recap (the sense-making loop on Saathi)
- Scattered records + wearable streams = raw input for sense-making
- GenAI accelerates *portions*: document understanding, retrieval, summarization — never the medical decision
- Pipeline: ingest documents → embed + retrieve (RAG, pgvector) → generate insight → guardrails
- Then vs now: months of custom NLP (2021) → days with LLMs (2026)
- Key guardrail lesson: AI assists, humans (and doctors) decide

## Stack
Next.js · FastAPI · Supabase (Postgres + pgvector) · OpenRouter · OpenAI embeddings · LangSmith

Why these? See [decision-support/tool-comparison.md](../../decision-support/tool-comparison.md) — Saathi is the "pgvector because we already have Postgres" case study.

## Materials
- Slides: *[Docs folder in the repo](https://github.com/bharatm23/saathi-v0/blob/main/docs/Saathi%20-%20SlideDeck.html)*
- Recording: *[Google Drive Link](https://drive.google.com/file/d/1bIiXIIsJPlKE383rEpBH-JF9YRbvN3KE/view?usp=sharing)*
- Project repo: **[Github Repo Link](https://github.com/bharatm23/saathi-v0/)

## Check yourself (ungraded)
In Saathi's pipeline, which step would you hand to the *cheapest* model on the [matrix](../../decision-support/model-matrix.md), and which to the priciest? Why?
