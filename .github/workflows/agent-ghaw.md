---
# agentplane — gh-aw dispatch demo. UNVERIFIED: this file has not been
# compiled by `gh aw compile` or run in CI. It exists to prove the shape of
# the dispatch lane (agentplane hands the task off and records
# `status: dispatched`), not to prove the lane works.
#
# Compile with: gh extension install githubnext/gh-aw && gh aw compile
on:
  issues:
    types: [labeled]

if: contains(github.event.issue.labels.*.name, 'agent:tool/ghaw')

permissions:
  contents: read
  issues: write

engine: copilot

tools:
  github:
    allowed: [get_issue, add_issue_comment]

timeout_minutes: 10
---

# agentplane dispatch demo

Read issue #${{ github.event.issue.number }} in ${{ github.repository }}.

It contains a fenced `agentplane` YAML block describing a governed task:
domain, tool, runner, writable paths, and acceptance criteria.

Do not modify the repository. Post one comment on the issue that:

1. Restates the task in two sentences.
2. Lists the writable paths the task declares.
3. States plainly that this is a dispatch-only lane: no diff was produced, no
   verification ran, and agentplane records the outcome as `dispatched` rather
   than `succeeded`.
