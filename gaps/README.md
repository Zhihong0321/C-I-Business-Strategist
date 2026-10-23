# Knowledge gaps

Questions the repo cannot answer yet. AIs log them here so the next research round targets what people actually ask.

## How a gap gets in
| Who | How |
|---|---|
| Coding agents with git (Claude Code, Codex, Gemini CLI, Cursor) | Copy `TEMPLATE.md` to `open/YYYY-MM-DD-short-slug.md`, fill it in, commit `gap: <question>` |
| Chat apps (ChatGPT, Gemini, Claude.ai) | The AI ends its answer with a GAP block; you file it with the "Knowledge gap" issue form. A GitHub Action turns issues from the repo owner or collaborators into a file in `open/` automatically. |
| People | Use the issue form, or add a file directly |

## Lifecycle
1. `open` — logged.
2. `researching` — a research prompt has been written (add it to `research/`).
3. `answered` — knowledge added to `kb/` with a source; move the file to `answered/` and note where the answer lives.
4. `wont-fix` — out of scope.

Run `python tools/build.py` to refresh `INDEX.md` after changes. Always check `INDEX.md` before logging, to avoid duplicates.
