# Glossary — plain words first

**LLM (Large Language Model)** — software trained on huge amounts of text that predicts likely next words. The engine behind ChatGPT, Gemini, Claude.

**Token** — a chunk of text, roughly ¾ of an English word. Models charge per million tokens, separately for input (your prompt) and output (the answer).

**Context window** — how much text a model can consider at once. 128K tokens ≈ a 300-page book.

**Embedding** — a list of numbers representing the *meaning* of text, so similar meanings sit near each other mathematically. What makes semantic search possible.

**Vector database** — a database that stores embeddings and finds "nearest neighbours" fast. Examples: Chroma, pgvector, Pinecone.

**RAG (Retrieval-Augmented Generation)** — instead of asking the model from memory, you first *retrieve* relevant documents, then ask the model to answer *from those documents*. Reduces hallucination, enables citing sources. (Sessions 1 & 2 are RAG apps.)

**Agent** — an LLM given tools (search, code, APIs) and permission to take multiple steps toward a goal, deciding its own next action. (Sessions 2 & 3 use multi-agent designs.)

**Guardrails** — checks around a model that block unsafe inputs/outputs — e.g. Saathi refusing to give medical decisions.

**Hallucination** — a fluent but wrong answer. The failure mode RAG, citations, and evaluation exist to catch.

**Fine-tuning** — further training a model on your own data. Rarely the first tool to reach for; RAG usually wins for facts.

**Open-weights model** — a model whose weights you can download and run yourself (Llama, DeepSeek, Qwen, GLM). Contrast: proprietary API-only models (GPT, Claude, Gemini).

**Inference** — running the model to get an answer (as opposed to training it).

**System prompt** — standing instructions given to a model before user input; where an app's behaviour and guardrails are declared.

**Evaluation (evals)** — systematic testing of LLM outputs. RAGAS (used in Session 2) scores RAG pipelines on faithfulness and relevance.
