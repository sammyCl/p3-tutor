# Agent architecture Resources

## Knowledge

- [Docs: Context windows (Anthropic)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, context rot, compaction. Use for: context and cost questions.
- [Docs: Memory tool (Anthropic)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Notes files as memory between sessions, client-side storage, multisession pattern. Use for: designing saved student notes.
- [Video course: LLMs as Operating Systems: Agent Memory (DeepLearning.AI)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  About 1.5 hours on memory inside and outside the window, in Python; free during beta, check access. Use for: a spoken walkthrough of agent memory.
- [Guide: Retrieval-Augmented Generation (Pinecone)](https://www.pinecone.io/learn/retrieval-augmented-generation/)
  Plain four-stage account of RAG. Use for: how the assistant finds the right manual page.
- [Tutorial: Simple RAG (Hugging Face Cookbook)](https://huggingface.co/learn/cookbook/en/rag_zephyr_langchain)
  Runnable Python notebook: chunk, embed, retrieve. Use for: a first retrieval prototype.

## Wisdom (Communities)

- [DeepLearning.AI Community](https://community.deeplearning.ai/)
  Course Q&A on context engineering and RAG, threads on agent memory; moderation not confirmed. Use for: asking about your assistant's memory design.

## Gaps

- An independent source on context rot beyond Anthropic's docs.
