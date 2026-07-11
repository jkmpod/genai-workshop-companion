# The Companion App — pointer & purpose

The app's **source code lives in its own repository**: *(link added at deploy — `github.com/<jk>/genai-workshop-companion-app`)*. This folder holds only the architecture documentation, because the *design* is workshop content even where the code isn't vendored here.

## Why the app is a worked example
It was built with the same identify → use → iterate loop the workshop teaches, using spec-driven development with four role-separated agents (Architect, Senior Developer, QC Lead, DevOps) in Claude Code. The specs and agent definitions ship inside the app repo — read them; the *process* is the artifact.

## What the app does (until sunset, end of Week 3)
1. **Workshop content** — renders the pages in this repo, cohort-gated
2. **Resources** — the tagged lists in [resources/](../resources/)
3. **Chat** — recommends templates/tools/costs, grounded ONLY in [decision-support/](../decision-support/) + [templates/](../templates/); 3 queries per participant on the workshop key, then bring-your-own OpenRouter key

## After sunset
The app dies; this repo remains. Everything the chat could tell you is browsable in `decision-support/` — by design, the chat was never the only path to any answer.
