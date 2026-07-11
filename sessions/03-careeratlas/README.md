# Session 3 — CareerAtlas: AI Career Planning (18 Jul 2026)

**One line:** resume analysis → skill-gap identification → personalized learning roadmaps → job matching, via multi-agent workflows with web-grounded research.

## Recap
- Multi-agent split: resume parsing / gap analysis / roadmap research / quality evaluation / job matching
- Web-grounded insights (Tavily) keep recommendations current
- Retrieval (Pinecone) + fast inference (Groq) + Gemini embeddings — a deliberately different stack from S1/S2
- Key lesson: agent role-separation mirrors how you'd delegate to a human team

## Stack
React · Vite · FastAPI · Supabase · Pinecone · Tavily · Groq · Gemini embeddings

Why these? CareerAtlas is the "managed vector DB + speed-critical inference" case study in [tool-comparison.md](../../decision-support/tool-comparison.md).

## Materials
- Slides / Recording / Project repo: *(links added post-session)*

## Check yourself (ungraded)
CareerAtlas uses five specialized agents instead of one big prompt. Name one benefit and one cost of that choice.
