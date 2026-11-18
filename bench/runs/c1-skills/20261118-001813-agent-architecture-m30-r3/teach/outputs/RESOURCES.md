# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: anything on what an agent keeps in context and how to manage it.
- [Docs: "Context windows" (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, compaction, overflow. Use for: exact mechanics and current window sizes.
- [Article: "Contextual Retrieval" (Anthropic)](https://anthropic.com/news/contextual-retrieval)
  Chunks, embeddings, BM25 and reranking, with Anthropic's own measurements. Use for: designing retrieval over the machine manuals.
- [Docs: "Memory tool" (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A concrete design for model-managed notes across sessions (listed from a link on the context-windows page; not yet read in full). Use for: the between-sessions memory design.

## Wisdom (Communities)

No community recorded yet; none verified. Ask the learner which one their team trusts.

## Gaps

- A high-trust, moderated community for agent builders.
