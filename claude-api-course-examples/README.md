# Claude API: course examples

Eight small scripts covering the basics of the Anthropic Messages API. No dependencies beyond Python 3.

| File | Topic |
|---|---|
| 01_basic_request.py | Send a message, read reply and token usage |
| 02_multi_turn.py | Conversation history (API is stateless) |
| 03_system_prompt.py | Role and style via system prompt |
| 04_temperature.py | Predictable vs varied output |
| 05_streaming.py | Print text as it is generated |
| 06_structured_output.py | JSON-only output, parsed |
| 07_tool_use.py | Claude requests a tool, we return the result |
| 08_simple_eval.py | Score a prompt against a small test set |

Run: `export ANTHROPIC_API_KEY=your_key` then `./run_all.sh` (or run any file alone).
Sample results are in `outputs/`. The key is never stored in the code.
