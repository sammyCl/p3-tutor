# Agent architecture Resources

## Knowledge

- [Guide: Effective context engineering for AI agents (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Covers the limited context window, compaction, note-taking and just-in-time retrieval. Use for: deciding what an agent keeps in context.
- [Documentation: Memory concepts (LangChain)](https://docs.langchain.com/oss/python/concepts/memory)
  Short-term versus long-term memory in Python terms. Use for: what is kept between steps and between sessions.
- [Tutorial: Build a RAG agent (LangChain)](https://docs.langchain.com/oss/python/langchain/rag)
  Chunking, embeddings and retrieval as a tool, with code. Use for: finding the right page in a long manual.
- [Guide: Introducing Contextual Retrieval (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  The 200,000-token rule, keyword plus embedding search and measured results (2024). Use for: retrieve-or-paste decisions.
- [Video course: LLMs as Operating Systems: Agent Memory (DeepLearning.AI with Letta)](https://learn.deeplearning.ai/courses/llms-as-operating-systems-agent-memory)
  An agent that edits its own memory. Use for: model-managed memory. Free access needs a trial or audit.
- [Paper: Lost in the Middle (Liu et al., TACL)](https://arxiv.org/abs/2307.03172v3)
  Accuracy drops when the relevant text is in the middle of a long context. Use for: why a full window is not free.

## Wisdom (Communities)

- [DeepLearning.AI Community](https://community.deeplearning.ai/)
  Course Q&A on agent memory and RAG. Use for: asking how others size chunks or decide what to save. Moderation not confirmed.

## Gaps

- Provider documentation on prompt caching, to back the caching claims.
