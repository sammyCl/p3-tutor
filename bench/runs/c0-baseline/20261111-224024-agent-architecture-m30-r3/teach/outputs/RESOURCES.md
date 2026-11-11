# Agent architecture Resources

## Knowledge

- [Effective context engineering for AI agents (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on context rot, compaction, structured note-taking, just-in-time retrieval and sub-agents. Use for: anything about what goes in an agent's context and how to keep it small.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official documentation: what counts toward the window, how turns accumulate, compaction and context editing. Use for: precise facts about windows and tokens.
- [Building effective agents (Anthropic)](https://www.anthropic.com/engineering/building-effective-agents)
  The augmented LLM (retrieval, tools, memory) and advice to start simple. The page notes some tooling has changed since December 2024. Use for: workflows versus agents and the building blocks.
- [Claude docs: Memory tool, multisession pattern](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool#multisession-software-development-pattern)
  Concrete way for a model to save notes across sessions (seen as a link in the context-windows page, not read in full). Use for: designing saved student records.

## Wisdom (Communities)

- Local: the senior design team and course instructor.
  Use for: design-review feedback on where each fact lives. No outside community has been vetted yet.

## Gaps

- A high-trust, beginner-friendly source on how retrieval search ranks passages (embeddings, chunking) for the manuals.
