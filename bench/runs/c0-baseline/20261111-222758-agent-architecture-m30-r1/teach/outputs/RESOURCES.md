# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, attention budget, compaction, note-taking memory, just-in-time retrieval, sub-agents. Use for: anything about what goes in context and what is kept outside it.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, window sizes by model, overflow behaviour. Use for: exact limits and token accounting.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Ready-made file-based memory across sessions. Use for: building the notes store.
- [Claude docs: Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)
  Server-side summarising of long conversations. Use for: very long runs.
- [Anthropic Engineering: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  Carrying state across many sessions. Use for: multi-session design.

## Wisdom (Communities)

- Local: the team's design review and the makerspace staff
  Use for: finding out what students expect the assistant to remember.

## Gaps

- A high-trust, moderated community for agent builders has not yet been found and verified.
