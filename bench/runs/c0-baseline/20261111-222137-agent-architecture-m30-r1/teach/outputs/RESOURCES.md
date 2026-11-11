# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, pre-retrieval versus just-in-time retrieval, compaction, structured note-taking, sub-agents. Use for: deciding what goes in context and how to retrieve.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How the window fills turn by turn, what counts toward it, overflow, compaction and context editing. Use for: token accounting and cost.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory between sessions, client-side handler, security notes, multisession pattern. Use for: designing notes between visits.
- [Article: "Effective harnesses for long-running agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
  Linked from the docs as a case study of progress notes across sessions; not yet read. Use for: long tasks across sessions.

## Wisdom (Communities)

- Local: Riley's team design review and course instructor
  Use for: having the memory plan challenged by people who know the makerspace.

## Gaps

- A high-moderation online community for agent builders has not been found yet.
