# Cost Heuristics — back-of-envelope numbers

**Verified: 2026-07-11.** All numbers rough by design; the *method* is the takeaway.

## The only formula you need
```
cost = (input_tokens × in_price + output_tokens × out_price) / 1,000,000
```
1 token ≈ ¾ of an English word. A dense page ≈ 500 tokens.

## Worked examples (July 2026 prices)

**One RAG answer** (system prompt 500 + retrieved chunks 2,000 + question 100 ≈ 2,600 in; ~400 out):
- DeepSeek V4 Flash: ≈ **$0.0005** (≈ ₹0.04)
- Gemini 2.5 Flash: ≈ **$0.0006**
- GPT-5.5: ≈ **$0.025** (≈ ₹2) — roughly 50× the Flash-class cost, per answer

**Embedding a 100-page corpus** (~50K tokens) at typical embedding prices (~$0.02–0.13/M): **under $0.01**. Embeddings are almost never your cost problem.

**This workshop's chat feature** (150 participants × 3 queries × ~$0.001/query on a Flash-class model): ≈ **$0.50 total**. The quota exists to teach deliberate querying, not to save money — scarcity by design.

## Heuristics
1. **Output tokens cost 3–6× input tokens.** Verbose answers are the silent budget killer — cap `max_tokens`.
2. **Input dominates RAG cost** (big context in, small answer out). Trim retrieved chunks before anything else.
3. **Prompt caching cuts repeated-context cost 50–90%** where supported (DeepSeek cache hits ≈ $0.004/M; Groq halves cached input). Long constant system prompt → caching is your biggest lever.
4. **Batch APIs ≈ 50% off** when you don't need real-time (bulk classification, backfills). Stacked with caching on Groq ≈ 25% of list price.
5. **Frontier ≈ 20–100× Flash-class.** Route the routine 90% cheap; spend on the 10% that measurably needs it.
6. **Set the provider spend cap the day you create the key** — never after the first surprise bill.
