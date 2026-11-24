# Sources for lesson 0001: O3 Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

## Primary source
- [Documentation: Context windows, Anthropic (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Why it is the primary: it defines the context window as the model's "working memory", shows turn by turn how every message and tool result accumulates and is re-sent, and names context rot and compaction in one short page.
  Supports: context window definition; everything in the request counts (system prompt, messages, tool results, tool definitions, output); history is kept within a session by being re-sent each turn; limits and overflow; compaction and clearing old tool results; more context is not automatically better; state artifacts for multi-session agents.

## Other sources
- [Article: Effective context engineering for AI agents, Anthropic Engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Format: engineering guide, about 12 min read.
  What the learner gets from it: the design view, treating context as a finite budget and choosing what goes in, which maps directly onto a small model budget.
  Supports: smallest set of high-signal tokens; context rot; compaction; structured note-taking (a NOTES.md the agent writes and re-reads); just-in-time retrieval vs loading everything up front.

- [Documentation: What are tokens and how to count them, OpenAI Help Center](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
  Format: short documentation page.
  What the learner gets from it: plain rules of thumb (about 4 characters or 0.75 word per token) and the input/output/cached split that makes cost per request concrete; the learner has not met tokens yet.
  Supports: what a token is; tokens set both the context limit and the bill; input vs output pricing; counting before sending (tiktoken, counting API); shorten, split or summarize when input is too large.

- [Documentation: Memory (short-term and long-term), LangChain docs](https://docs.langchain.com/oss/python/concepts/memory)
  Format: documentation (concepts page).
  What the learner gets from it: a vocabulary and a code-level picture of thread-scoped memory vs memory saved across threads, with a per-user store; this is the closest fit to remembering a student's training status.
  Supports: short-term (within one conversation, trimmed when long) vs long-term (across sessions, stored by user namespace); semantic facts / episodic / procedural memory; profile vs collection of memories; writing memory during the interaction vs in the background.

- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  Format: video course, 1 h 32 min total in 8 short lessons (about 8 to 14 min each) with code; the relevant lessons are Editable Memory, Understanding MemGPT, and Agentic RAG and External Memory (about 35 min, more than this lesson needs, so pick lessons).
  What the learner gets from it: instructors talk through the idea of two memory tiers, one inside the context window and one outside, and moving old history into a searchable store.
  Supports: limited window, longer inputs cost more and run slower; in-context vs external memory; saving facts such as names, dates, preferences; searching a database to restore relevant parts.

- [Interactive notebook: Advanced RAG on Hugging Face documentation using LangChain, Hugging Face Cookbook](https://huggingface.co/learn/cookbook/en/advanced_rag)
  Format: runnable Jupyter notebook tutorial in Python.
  What the learner gets from it: a worked example of finding the right passage in long documentation, which is the manual-search problem; Python-first, with printed outputs.
  Supports: chunking (size in tokens, overlap); embeddings and similarity search; top_k tradeoff (more chunks, more noise); reranking; putting labeled retrieved chunks and the question into the prompt; saying "not in the context" when unsupported; long contexts lose information in the middle.

## Community
- [LangChain Forum](https://forum.langchain.com/)
  Use for: questions on short-term vs long-term memory stores, thread state, and retrieval set-up for an agent. Moderation is not stated on the front page (it links Guidelines and Terms), so confirm the guidelines before the learner relies on it.

## Coverage
- Context window and tokens: Anthropic context windows doc, OpenAI tokens article, Anthropic context engineering, DeepLearning.AI course.
- Why more context costs more and can hurt (cost, context rot): OpenAI tokens, Anthropic context windows, Anthropic context engineering, Hugging Face notebook (middle-of-context loss).
- What is kept between steps (history re-sent each turn, tool results accumulate, trimming and compaction): Anthropic context windows doc, Anthropic context engineering, LangChain memory (short-term).
- What is kept between sessions (stores, notes files, per-user memory): LangChain memory, Anthropic context engineering (notes), DeepLearning.AI course, Anthropic context windows doc (multi-session tip).
- Retrieval as memory for long manuals: Hugging Face notebook, DeepLearning.AI course (Agentic RAG lesson), Anthropic context engineering (just-in-time retrieval).
- Notes as memory: Anthropic context engineering, DeepLearning.AI course, LangChain memory.
- Publishers: 5 (Anthropic x2, OpenAI, LangChain x2 including the forum, DeepLearning.AI with Letta, Hugging Face); formats: reference documentation, engineering guide, video course, runnable notebook, community forum.
