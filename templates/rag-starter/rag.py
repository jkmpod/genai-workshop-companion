"""
Minimal RAG: embed corpus -> retrieve top-k by cosine -> answer with citations.
GPLv3. Teaching code: clarity over robustness (see repo LICENSE-EXPLAINED.md).
WHY no framework? So every step is visible. Graduate to LangChain/LlamaIndex
when you need connectors, memory, or agents -- not before.
"""
import os, sys, glob
import numpy as np
from openai import OpenAI

# OpenRouter is OpenAI-compatible: one base_url change, any model. (WHY: model
# portability is the meta-skill; see decision-support/model-matrix.md)
client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.environ["OPENROUTER_API_KEY"])

EMBED_MODEL = "openai/text-embedding-3-small"   # embeddings are cheap; see cost-heuristics
CHAT_MODEL = "google/gemini-2.5-flash"          # escalation ladder: start Flash-class

def embed(texts):
    r = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return np.array([d.embedding for d in r.data])

def load_corpus(folder="corpus"):
    docs = []
    for path in glob.glob(f"{folder}/*.md"):
        docs.append((path, open(path, encoding="utf-8").read()))
    if not docs:
        sys.exit("corpus/ is empty -- add some .md files first")
    return docs

def main(question):
    docs = load_corpus()
    doc_vecs = embed([text for _, text in docs])       # WHY whole-file: smallest
    q_vec = embed([question])[0]                        # honest version; chunking
    sims = doc_vecs @ q_vec / (                         # is exercise #1
        np.linalg.norm(doc_vecs, axis=1) * np.linalg.norm(q_vec))
    top = np.argsort(sims)[-3:][::-1]                   # top-3 files
    context = "\n\n".join(f"[source: {docs[i][0]}]\n{docs[i][1]}" for i in top)

    msg = client.chat.completions.create(
        model=CHAT_MODEL,
        max_tokens=400,   # WHY cap: output tokens are the silent budget killer
        messages=[
            {"role": "system", "content":
             "Answer ONLY from the provided sources. Cite the [source: path] "
             "you used. If the sources are insufficient, say so plainly."},
            {"role": "user", "content": f"{context}\n\nQuestion: {question}"}])
    print(msg.choices[0].message.content)

if __name__ == "__main__":
    main(" ".join(sys.argv[1:]) or "What is this corpus about?")
