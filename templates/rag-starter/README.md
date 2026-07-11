# RAG Starter — the smallest honest RAG pipeline

`[level: prompt-user→builder] [effort: 1 evening] [license: GPLv3, original]`

No framework. ~80 lines. Embed → retrieve → generate, so you understand every moving part before adopting LangChain/LlamaIndex (see [tool-comparison](../../decision-support/tool-comparison.md) for when to graduate).

## What it does
Answers questions over the markdown files in `corpus/`, citing which file each answer came from.

## Run it
```bash
pip install openai numpy            # OpenRouter is OpenAI-compatible
export OPENROUTER_API_KEY=sk-or-...
python rag.py "What does the model matrix say about free tiers?"
```

## Approx cost per query
Flash-class model + small corpus ≈ $0.001. See [cost-heuristics](../../decision-support/cost-heuristics.md).

## Where it deliberately stops (your exercises)
1. No chunking beyond whole-files — add H2-level chunking
2. Cosine loop in NumPy — swap in Chroma when the corpus outgrows memory
3. No eval — add a RAGAS faithfulness check (Session 2 material)
