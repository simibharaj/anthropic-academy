# System prompt: sets role and style for the whole conversation.
from client import call, text
r = call(system="You are a concise healthcare sales coach. Reply in 2 sentences max.",
         messages=[{"role": "user", "content": "How do I open a cold call with a busy clinic manager?"}])
print(text(r))
