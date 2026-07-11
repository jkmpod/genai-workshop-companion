"""
FastAPI chat proxy. GPLv3. Teaching code.
THE point of this file: the key stays server-side. The browser never sees it.
"""
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.environ["OPENROUTER_API_KEY"])  # server env ONLY

class ChatIn(BaseModel):
    message: str

@app.post("/api/chat")
def chat(body: ChatIn):
    r = client.chat.completions.create(
        model="google/gemini-2.5-flash",     # escalation ladder: start cheap
        max_tokens=400,                       # cap output = cap cost
        messages=[{"role": "user", "content": body.message}])
    return {"answer": r.choices[0].message.content}

@app.get("/", response_class=HTMLResponse)
def page():
    # WHY inline HTML: zero build step; swap for React/Vite when the UI grows
    return """<!doctype html><meta charset="utf-8"><title>Chat</title>
<body style="font-family:sans-serif;max-width:40em;margin:2em auto">
<h3>Minimal chat (key stays on the server)</h3>
<input id="q" style="width:75%" placeholder="Ask something">
<button onclick="send()">Send</button><pre id="out"></pre>
<script>
async function send(){
  const q = document.getElementById('q').value;
  document.getElementById('out').textContent = '...';
  const r = await fetch('/api/chat', {method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({message:q})});
  document.getElementById('out').textContent = (await r.json()).answer;
}
</script></body>"""
