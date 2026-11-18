# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, compaction, structured note-taking, just-in-time retrieval, sub-agents. Use for: what to keep in context, what to save outside it, and why. Primary source for lesson 0001 (objective O3).
- [Article: "Managing context on the Claude Developer Platform" (Anthropic)](https://claude.com/blog/context-management)
  Context editing (clearing stale tool results) and the file-based memory tool that stores notes in your own infrastructure. Use for: how notes between sessions work in practice.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25, hybrid search, reranking, and the "under 200,000 tokens, skip retrieval" remark. Use for: finding the right page in a long manual.

## Wisdom (Communities)

None added yet; the learner has not been asked about communities.

## Gaps

- A source on measuring cost per request in tokens (needed when the budget lesson comes up).
- A source on workflows versus agents and multi-agent trade-offs (objectives not yet taught).
