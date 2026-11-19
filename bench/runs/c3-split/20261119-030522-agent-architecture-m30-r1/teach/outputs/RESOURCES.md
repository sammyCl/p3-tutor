# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic)](https://anthropic.com/research/effective-context-engineering-for-ai-agents)
  Context window as an attention budget, context rot, compaction, note-taking, just-in-time retrieval. Use for: deciding what to keep in context.
- [Documentation: Context windows (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, compaction and tool-result clearing. Use for: cost per request and window limits.
- [Documentation: Memory tool (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side memory the model reads and writes through tool calls, with Python code. Use for: saving facts between sessions.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (Liu et al., TACL 2024)](https://arxiv.org/abs/2307.03172)
  Independent evidence that position in a long input affects recall (tested on 2023-era models). Use for: why not to paste whole manuals.
- [Tutorial: "Build a RAG agent with LangChain"](https://docs.langchain.com/oss/python/langchain/rag)
  Chunking, embeddings, vector store and retrieval, in Python. Use for: building the manual search.
- [Video course: "LLMs as Operating Systems: Agent Memory" (DeepLearning.AI with Letta)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  In-context versus out-of-context memory, editable memory, agentic RAG. Use for: a second, visual explanation of memory.

## Wisdom (Communities)

- [DeepLearning.AI community forum, Short Course Q&A](https://community.deeplearning.ai/t/about-the-short-course-q-a-category/311436)
  Moderated forum for learners of the short courses. Use for: questions on agent memory and retrieval in Python.

## Gaps

- No source yet on cost per request across providers, or on measuring retrieval quality; needed for the budget goal.
