# Streaming: print text as it is generated.
from client import stream
for chunk in stream(messages=[{"role": "user", "content": "Write a 3 line poem about clinics."}]):
    print(chunk, end="", flush=True)
print()
