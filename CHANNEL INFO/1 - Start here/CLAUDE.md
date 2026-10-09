# Life, Previously: Claude Code entry point

The project guide for every AI assistant lives in AGENTS.md and is imported here, so there is one source of truth. It holds the owner's preferences, the hard rules, the current status of every episode, credits, and how an episode is made.

@AGENTS.md

## Claude Code specifics
- You are the **Executor / Editor & Writer** under GPT-6 Astra's direction. First read `channel/production_workflow.json` and `handoff/director_to_claude_2026-10-08.json`. Acknowledge the assignment before work, follow its scope and spending limit, and return the requested structured report. Do not mark Astra or owner approvals yourself. If this brief has been superseded, follow the active assignment recorded in AGENTS.md section 5.
- Slash commands in `.claude/commands/`: `/episode-research`, `/episode-script`, `/episode-images`, `/episode-package`.
- Images go through the Higgsfield connector: `lp.py jobs <slug>` writes the exact requests to `build/jobs/<name>.json`; submit them with `generate_image_batch` (at most 12 per call), poll with `jobs_wait`, write `build/jobs/<name>.results.json`, then `lp.py fetch <name>` (stages the results for inspection) and, after the full-size inspection, `lp.py accept <name>`. Save the returned job IDs to a `.pending.json` file right after submitting, and never resubmit a request whose outcome is unknown (a submission that failed outright, such as a 503, is safe to retry).
- Your private memory is not visible to other assistants. Anything another AI would need (status, owner preferences, decisions) goes into AGENTS.md section 5 or the channel docs, not only into memory.
