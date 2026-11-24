# Agent architecture Resources

## Knowledge

- [Guide: "Effective context engineering for AI agents", Anthropic Engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a limited budget, context rot, just-in-time retrieval, compaction, note-taking. Use for: deciding what to keep in the window.
- [Documentation: Context windows, Claude API docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, compaction and clearing. Use for: cost and size questions.
- [Documentation: Memory overview, LangChain docs](https://docs.langchain.com/oss/python/concepts/memory)
  Short-term versus long-term memory and a storage model. Use for: designing what is saved between sessions.
- [Tutorial: Build a RAG agent, LangChain docs](https://docs.langchain.com/oss/python/langchain/rag)
  Chunking, embedding, vector store and search, in Python. Use for: finding the right page in the manuals.
- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  About 1.5 hours with notebooks. Use for: hands-on practice with memory inside and outside the window.
- [Paper: "Lost in the Middle", Liu et al.](https://arxiv.org/abs/2307.03172v3)
  Evidence that long inputs are not used evenly. Use for: arguing against pasting whole manuals into the prompt.
- [Course notes: Tokenizers, Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter2/4?fw=pt)
  What a token is. Use for: the unit that windows and bills are counted in.

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com)
  Use for: questions on agent memory and retrieval set-up, and design feedback. Moderation not confirmed.

## Gaps

- A vendor-neutral survey of agent memory and a source with pricing arithmetic for budgets.
