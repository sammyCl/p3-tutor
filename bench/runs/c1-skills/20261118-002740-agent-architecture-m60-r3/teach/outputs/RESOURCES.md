# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Context, context rot, compaction, structured note-taking, just-in-time retrieval, sub-agents. Use for: anything about what goes in an agent's context and how to keep it small.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How a client-side file memory works, the six commands, security checks. Use for: memory between sessions.
- [Article: "Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  RAG basics, chunking, embeddings versus BM25, losing context in chunks, when to skip RAG. Use for: finding pages in long manuals.
- [Docs: Compaction (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/compaction)
  Server-side summarizing of long conversations. Use for: keeping long runs inside the window.

## Wisdom (Communities)

None yet.

## Gaps

- A high-trust community for agent builders, and independent (non-vendor) sources on context rot and retrieval cost, have not been found yet.
