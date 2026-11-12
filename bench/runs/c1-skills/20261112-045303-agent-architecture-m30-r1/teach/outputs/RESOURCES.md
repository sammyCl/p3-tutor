# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, just-in-time retrieval, compaction, note-taking, sub-agents. Use for: anything about what to keep in context and how to manage it.
- [Docs: "Context windows" (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How the window fills turn by turn, what counts toward it, overflow behaviour, model sizes. Use for: exact facts about limits and token accounting.
- [Docs: "Memory tool" (Claude docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based, client-side memory across sessions, commands, multisession pattern, security notes. Use for: designing what the assistant saves between visits.
- [Article: "Effective harnesses for long-running agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  Case study of progress files across sessions. Use for: a worked pattern for session handoff.

## Wisdom (Communities)

None chosen yet. Learner has not said whether they want to join communities.

## Gaps

- A high-trust source on retrieval ranking (keyword vs. meaning-based search) for the manuals; needed before the learner designs `search_manuals`.
