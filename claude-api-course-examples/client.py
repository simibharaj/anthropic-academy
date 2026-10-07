import os, json, urllib.request
KEY = os.environ["ANTHROPIC_API_KEY"]
MODEL = os.environ.get("CLAUDE_MODEL", "claude-sonnet-5-5")
URL = "https://api.anthropic.com/v1/messages"
HEADERS = {"x-api-key": KEY, "anthropic-version": "2023-06-01", "content-type": "application/json"}

def call(**body):
    body.setdefault("model", MODEL)
    body.setdefault("max_tokens", 500)
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=HEADERS)
    try:
        return json.load(urllib.request.urlopen(req, timeout=60))
    except urllib.error.HTTPError as e:
        return {"error": e.read().decode()}

def text(r):
    if "error" in r: return "ERROR: " + r["error"]
    return "".join(b.get("text", "") for b in r["content"])

def stream(**body):
    body.update(model=body.get("model", MODEL), max_tokens=body.get("max_tokens", 500), stream=True)
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as resp:
        for line in resp:
            line = line.decode().strip()
            if line.startswith("data:"):
                ev = json.loads(line[5:])
                if ev.get("type") == "content_block_delta" and ev["delta"].get("type") == "text_delta":
                    yield ev["delta"]["text"]
