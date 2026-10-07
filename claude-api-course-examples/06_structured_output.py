# Structured output: ask for JSON only, then parse it.
import json
from client import call, text
r = call(system="Respond with valid JSON only. No prose, no code fences.",
         messages=[{"role": "user", "content": "Extract: 'Dr. Lee runs Sunrise Clinic in Tampa and wants a demo on Oct 10.' Keys: doctor, clinic, city, demo_date."}])
raw = text(r).strip()
print(raw)
print("parsed:", json.loads(raw))
