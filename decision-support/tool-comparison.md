# Tool Comparison — the GenAI app stack

**Verified: 2026-07-11.** One honest line per tool beats a feature table. Organized by the pipeline layer you're choosing for. The workshop's three apps (Saathi, Nyaya, CareerAtlas) deliberately use *different* stacks — compare their repos.

## Orchestration / framework

| Tool | Reach for it when | Skip it when | License/cost |
|---|---|---|---|
| **LangChain** | agents, tools, memory, complex multi-step pipelines; biggest ecosystem (~85K GitHub stars) | a pure document Q&A bot — heavier than needed | open (MIT), free |
| **LangGraph** | agent workflows needing state, branching, retries (used in Nyaya, S2) | single-shot RAG | open, free |
| **LlamaIndex** | retrieval-heavy apps; 300+ data connectors; better pure-RAG ergonomics | agent-heavy systems where RAG is one feature among many | open (MIT), free |
| **No framework** (direct API, ~100 lines) | learning; small well-understood pipelines — embed → retrieve → prompt is genuinely simple | you need connectors/agents/evals fast | — |

## Vector store

| Tool | Reach for it when | Skip it when | Cost |
|---|---|---|---|
| **Chroma** | prototyping; <~5M vectors; the tutorial default for a reason (used in Nyaya) | production scale, heavy concurrency | open, free |
| **pgvector** | you already run Postgres — Supabase gives it managed (used in Saathi) | >~10–30M vectors, or no Postgres in your stack | open, free |
| **SQLite + manual cosine** | tiny corpora — this repo's companion app does exactly this; zero infra | anything beyond toy scale | free |
| **Pinecone** | zero-ops managed production (used in CareerAtlas) | budget PoCs — ~$50/mo minimum; total vendor lock-in | paid |
| **Qdrant** | best free self-host that scales (Apache 2.0); 1GB free cloud | you want zero ops and have budget (→ Pinecone) | open/paid |

## Model access

| Tool | Reach for it when | Catch |
|---|---|---|
| **OpenRouter** | one key, 300+ models, swap by changing a string (Saathi, Nyaya, this app) | small markup; free models fragile at peak |
| **Groq** | speed-critical UX on open models (300–1,000 tok/s on LPU hardware) | open models only — no GPT/Claude/Gemini |
| **Direct provider APIs** | production commitment to one vendor; best caching discounts | one key + one bill per vendor |

## Evaluation & observability

| Tool | Reach for it when | Cost |
|---|---|---|
| **RAGAS** | scoring RAG pipelines: faithfulness, answer relevance, context precision (used in Nyaya, S2) | open, free |
| **LangSmith** | tracing LangChain apps in production (used in Saathi) | free tier, then ~$39/seat/mo |
| **Langfuse** | open-source LangSmith alternative; OpenTelemetry-friendly | open, free self-host |

## UI layer

| Tool | Reach for it when | Skip it when |
|---|---|---|
| **Streamlit** | data-app UIs in pure Python; fastest demo path (used in Nyaya) | polished consumer products |
| **Next.js / React + Vite** | real products: auth, routing, polish (Saathi; CareerAtlas; this app) | you don't know JS and just need a demo |
| **FastAPI** | Python backend serving models/RAG behind a clean API (this app; CareerAtlas) | — it's the safe default |

## The meta-lesson

Every layer has a **prototyping default** (Chroma, Streamlit, OpenRouter free) and a **production default** (Pinecone/Qdrant, Next.js, paid APIs). Knowing *which phase you're in* matters more than knowing every tool. Start disposable; upgrade the layer that breaks first.
