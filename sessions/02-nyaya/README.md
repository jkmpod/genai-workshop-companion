# Session 2 — Nyaya Agent: Legal Research Assistant (11 Jul 2026)

**One line:** a domain-specific RAG system that answers legal queries from a curated corpus with citation-backed memos — multi-agent, evaluated with RAGAS.

## Recap
- Legal corpus + case law = sense-making input; **citation is the trust anchor**
- Pipeline: corpus (ChromaDB) → multi-agent research (LangGraph) → synthesis → citation-backed memo → RAGAS evaluation
- Conversation memory management for long-form interactions
- Indian Kanoon API as the grounded data source
- Key lesson: retrieval + synthesis accelerate; the final legal opinion stays human

## Stack
LangChain · LangGraph · Streamlit · ChromaDB · SQLite · OpenRouter · Indian Kanoon API · RAGAS

Why these? Nyaya is the "Chroma + Streamlit for fast domain prototyping" case study in [tool-comparison.md](../../decision-support/tool-comparison.md).

## Materials
- Slides / Recording / Project repo: *(links added post-session)*

## Check yourself (ungraded)
Why does a *citation-backed* answer change the trust equation compared to a fluent answer without sources? One sentence.
