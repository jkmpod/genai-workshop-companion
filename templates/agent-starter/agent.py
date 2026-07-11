"""
Minimal tool-using agent loop. GPLv3. Teaching code.
WHY hand-rolled: see the raw pattern (choose tool -> observe -> iterate)
before frameworks hide it. Session 2 (LangGraph) formalizes exactly this.
"""
import os, json
from openai import OpenAI

client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key=os.environ["OPENROUTER_API_KEY"])
MODEL = "meta-llama/llama-3.3-70b-instruct"  # fast + tool-capable; see matrix

def calculator(expression: str) -> str:
    # WHY eval is guarded: never eval raw model output without a whitelist
    allowed = set("0123456789+-*/(). %")
    if not set(expression) <= allowed:
        return "rejected: non-arithmetic characters"
    return str(eval(expression))  # safe only because of the whitelist above

def corpus_search(query: str) -> str:
    return ("[stub] Session 2 (Nyaya) covers agent workflows with LangGraph; "
            "Session 3 (CareerAtlas) covers multi-agent role separation.")

TOOLS = [
    {"type": "function", "function": {
        "name": "calculator", "description": "Evaluate arithmetic.",
        "parameters": {"type": "object", "properties": {
            "expression": {"type": "string"}}, "required": ["expression"]}}},
    {"type": "function", "function": {
        "name": "corpus_search", "description": "Search workshop corpus.",
        "parameters": {"type": "object", "properties": {
            "query": {"type": "string"}}, "required": ["query"]}}},
]
IMPL = {"calculator": calculator, "corpus_search": corpus_search}

def run(question, max_steps=5):   # WHY max_steps: agents need a leash
    messages = [{"role": "user", "content": question}]
    for _ in range(max_steps):
        r = client.chat.completions.create(
            model=MODEL, messages=messages, tools=TOOLS, max_tokens=400)
        msg = r.choices[0].message
        if not msg.tool_calls:                    # model chose to answer
            return msg.content
        messages.append(msg)
        for call in msg.tool_calls:               # execute each requested tool
            args = json.loads(call.function.arguments)
            result = IMPL[call.function.name](**args)
            print(f"  [tool] {call.function.name}({args}) -> {result}")
            messages.append({"role": "tool",
                             "tool_call_id": call.id, "content": result})
    return "step limit reached -- raise max_steps or simplify the task"

if __name__ == "__main__":
    import sys
    print(run(" ".join(sys.argv[1:]) or "What is (3+4)*12?"))
