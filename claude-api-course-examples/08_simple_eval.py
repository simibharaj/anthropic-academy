# Prompt evaluation: run a prompt on a small test set and score the results.
from client import call, text
tests = [("The clinic loved the demo and wants pricing.", "positive"),
         ("They said no budget this year.", "negative"),
         ("Please send the brochure.", "neutral")]
passed = 0
for msg, expected in tests:
    got = text(call(max_tokens=10, system="Classify the sentiment as exactly one word: positive, negative, or neutral.",
                    messages=[{"role": "user", "content": msg}])).strip().lower().strip(".")
    ok = got == expected; passed += ok
    print(f"{'PASS' if ok else 'FAIL'} | expected={expected} got={got}")
print(f"score: {passed}/{len(tests)}")
