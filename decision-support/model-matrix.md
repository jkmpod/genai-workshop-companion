# Model Decision Matrix

**Verified: 2026-07-11.** Prices are USD per **million tokens** (input / output), standard non-batch API rates, from provider pricing pages and independent trackers (pricepertoken.com, llm-stats.com, morphllm.com/llm-api). **Prices change quarterly or faster — always recheck before committing budget.**

How to read this: novices — look at `Use-case fit` and `Free route` only. Builders — cost, context, and `Avoid for` are your columns. All models below are reachable through OpenRouter with one key unless noted.

| Model | $/M in | $/M out | Context | Speed | Free route | Strengths | Avoid for | Use-case fit | Weights | Verified |
|---|---|---|---|---|---|---|---|---|---|---|
| Gemini 2.5 Flash (Google) | 0.15 | 0.60 | 1M | fast | ✅ AI Studio ~1,500 req/day, no card | cheap workhorse, multimodal | frontier reasoning | S1 doc-extraction, general | proprietary | 2026-07-11 |
| Gemini 3.1 Flash-Lite (Google) | 0.10 | 0.40 | 1M | fast | limited | cheapest proprietary API | complex multi-step agents | high-volume simple tasks | proprietary | 2026-07-11 |
| DeepSeek V4 Flash | 0.14 | 0.28 | 1M | medium | ✅ free variant on OpenRouter (rate-limited) | cheapest quality option; native reasoning; cache hits ~$0.004/M | latency-critical UIs | S1/S2 RAG on a budget | open | 2026-07-11 |
| Llama 3.1 8B (Groq) | 0.05 | 0.08 | 128K | fastest (≈800 tok/s) | ✅ Groq free: most generous req/day, no card | speed, prototyping volume | nuanced reasoning, long outputs | classification, extraction at speed | open | 2026-07-11 |
| Llama 3.3 70B (Groq) | 0.59 | 0.79 | 128K | fast (≈390 tok/s) | ✅ Groq free (lower daily caps) | GPT-4o-class quality at speed | very long documents | S3 agent steps, chat UX | open | 2026-07-11 |
| Qwen3 Coder (`:free`, OpenRouter) | 0 | 0 | 1M | medium | ✅ ~20 req/min, ~200 req/day | strongest free coding model | production reliability (free-tier fragility) | learning to build, hackathons | open | 2026-07-11 |
| GLM-5.2 (Z.AI) | 1.40 | 4.40 | 200K | medium | GLM-4.7-Flash is free | best open-weights general intelligence | tightest budgets | self-hostable quality | open | 2026-07-11 |
| MiniMax M3 | 0.60 | 2.40 | 200K | medium | ❌ | cheapest model >80% SWE-bench Verified | multimodal input | budget coding agents | open | 2026-07-11 |
| Gemini 3.1 Pro (Google) | 2.00 | 12.00 | 1M+ | medium | ❌ (rises to 4/18 over 200K ctx) | huge documents, video, multimodal | cost-sensitive high volume | S2-style long legal corpora | proprietary | 2026-07-11 |
| Claude Sonnet 5 (Anthropic) | ~2.00 | ~10 | 200K+ | medium | ❌ | balanced flagship; strong code + writing | budget bulk processing | production assistants | proprietary | 2026-07-11 |
| GPT-5.5 (OpenAI) | 5.00 | 30.00 | 400K | slow-medium | ❌ | frontier reasoning + coding (88.7% SWE-bench V) | high-volume, cost-sensitive | hardest reasoning steps only | proprietary | 2026-07-11 |
| Claude Opus 4.8 (Anthropic) | 5.00 | 25.00 | 200K+ | slow-medium | ❌ | frontier coding (88.6% SWE-bench V), prose | high-volume, cost-sensitive | hardest coding/writing steps | proprietary | 2026-07-11 |

## The pattern to internalize (more durable than any row)

1. **Route by step, not by app.** Extraction step → cheap fast model. Final reasoning step → frontier model. A pipeline mixing $0.14 and $5.00 models beats one model everywhere.
2. **Escalation ladder:** start with the cheapest model that might work (free tier → Flash-class → mid → frontier). Escalate only on measured failure, not vibes.
3. **In June 2026, five models scored within 0.4 points of each other on SWE-bench Verified while spanning a 5× price range.** Benchmarks converge; prices don't. Shop.
4. **Free tiers are for learning, not production.** Rate limits, silent model deletions, and no SLA are the price of ₹0.

## Free routes with no credit card (verified 2026-07)

| Route | What you get | Catch |
|---|---|---|
| Google AI Studio | Gemini 2.5 Flash ~1,500 req/day, 1M tokens/min | prompts may be used for training on free tier |
| Groq | every hosted open model; ~30 req/min; most generous daily caps in class | open models only; limits are org-level |
| OpenRouter `:free` models | ~26 free models incl. Qwen3 Coder, DeepSeek variants | ~20 req/min, ~200 req/day; fragile at peak |
| Cerebras | very high daily token volume | model catalog changes without notice |
