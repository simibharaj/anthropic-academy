# Tool use: Claude asks for a tool, we run it, send the result back.
from client import call, text
tools = [{"name": "get_lead_status", "description": "Look up the status of a sales lead by company name.",
          "input_schema": {"type": "object", "properties": {"company": {"type": "string"}}, "required": ["company"]}}]
def get_lead_status(company): return f"{company}: demo scheduled for Oct 10"
msgs = [{"role": "user", "content": "What's the status of Sunrise Clinic?"}]
r = call(tools=tools, messages=msgs)
tu = next(b for b in r["content"] if b["type"] == "tool_use")
print("Claude requested:", tu["name"], tu["input"])
msgs += [{"role": "assistant", "content": r["content"]},
         {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tu["id"], "content": get_lead_status(**tu["input"])}]}]
print("Final answer:", text(call(tools=tools, messages=msgs)))
