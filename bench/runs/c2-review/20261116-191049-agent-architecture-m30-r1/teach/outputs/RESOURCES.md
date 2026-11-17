# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context, context rot, compaction, note-taking, just-in-time retrieval, sub-agents. Use for: anything about what an agent keeps in its context.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, context rot, trimming options. Use for: window and token questions.
- [Claude docs: Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)
  Statelessness and resending history. Use for: how conversations are carried between calls.
- [Claude docs: Memory tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side file notes that persist between sessions. Use for: memory between visits.
- [Claude docs: Context editing](https://platform.claude.com/docs/en/build-with-claude/context-editing) and [Compaction](https://platform.claude.com/docs/en/build-with-claude/compaction)
  Trimming old tool results and summarizing (both beta when checked). Use for: keeping long sessions in the window.
- [Anthropic Engineering: Contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
  RAG, chunks, embeddings, BM25, and when to skip retrieval. Use for: finding the right manual page.

## Wisdom (Communities)

- [LangChain forum thread on agent workflows with LangGraph and RAG](https://forum.langchain.com/t/building-reliable-ai-agent-workflows-with-langgraph-and-rag/4945)
  Practitioners discussing memory and retries. Use for: sanity-checking a design.

## Gaps

- Vendor-neutral and independent sources (research on long-context degradation, a neutral retrieval guide) not yet found.
