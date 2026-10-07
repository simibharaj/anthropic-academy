# Basic request: send one user message, read the reply and token usage.
from client import call, text
r = call(messages=[{"role": "user", "content": "Explain what an API is in two sentences."}])
print(text(r))
print("usage:", r.get("usage"))
