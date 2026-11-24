# Agent architecture Resources

## Knowledge

- [Documentation: Context windows, Anthropic](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the context window, shows how history and tool results accumulate and are re-sent, and covers compaction and clearing. Use for: what the model sees at each step.
- [Article: Effective context engineering for AI agents, Anthropic Engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite budget; context rot, compaction, note-taking, just-in-time retrieval. Use for: deciding what goes in the context.
- [Documentation: What are tokens and how to count them, OpenAI Help Center](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
  Rules of thumb for tokens and the input/output billing split. Use for: cost per request estimates.
- [Documentation: Memory, LangChain docs](https://docs.langchain.com/oss/python/concepts/memory)
  Short-term versus long-term memory, per-user stores. Use for: saving student data between sessions.
- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  Two memory tiers, in-context and external. Use for: a talked-through view of agent memory (pick the relevant lessons).
- [Notebook: Advanced RAG, Hugging Face Cookbook](https://huggingface.co/learn/cookbook/en/advanced_rag)
  Python walkthrough of chunking, search, top_k and prompting with retrieved chunks. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com/)
  Questions on memory stores and retrieval set-up. Use for: sharing a design as a question. Its moderation is not stated on the front page, so check its guidelines first.
