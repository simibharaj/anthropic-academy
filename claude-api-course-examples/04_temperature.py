# Temperature: low = predictable, high = more varied.
# Note: newest models deprecate this setting, so this example uses claude-haiku-4-5, which still supports it.
from client import call, text
for t in (0.0, 1.0):
    r = call(model="claude-haiku-4-5-20251001", temperature=t, max_tokens=60,
             messages=[{"role": "user", "content": "Give me a name for a coffee shop. Just the name."}])
    print(f"temperature={t}:", text(r))
