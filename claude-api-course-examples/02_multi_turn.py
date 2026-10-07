# Multi-turn: the API is stateless, so you resend the full history each time.
from client import call, text
history = [{"role": "user", "content": "My name is Alex. Remember it."}]
a = text(call(messages=history)); print("Claude:", a)
history += [{"role": "assistant", "content": a}, {"role": "user", "content": "What is my name?"}]
print("Claude:", text(call(messages=history)))
