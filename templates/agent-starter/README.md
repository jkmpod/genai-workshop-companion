# Agent Starter — one loop, two tools

`[level: builder] [effort: 1 evening] [license: GPLv3, original]`

The essential agent pattern in ~70 lines: an LLM that chooses tools, observes results, and iterates until done. What LangGraph formalizes — visible here in raw form first.

## What it does
Answers questions using two tools: a calculator and a (stub) corpus search. The model decides which tool to call, or answers directly.

## Run it
```bash
pip install openai
export OPENROUTER_API_KEY=sk-or-...
python agent.py "What is 12.5% of 480, and which session covers agents?"
```

## Where it deliberately stops (your exercises)
1. Two tools, hand-rolled loop — port it to LangGraph and compare the code you deleted
2. No memory across runs — add SQLite conversation storage (Nyaya-style, Session 2)
3. No quality evaluation — add a second "critic" model pass (CareerAtlas-style, Session 3)
