# Sources for lesson 0001: O3 Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

## Primary source
- [Guide: Effective context engineering for AI agents, Anthropic Engineering (Applied AI team, 29 Sep 2025)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Why it is the primary: it covers the whole objective in one plain-language piece: the context window as a limited budget, context rot, just-in-time retrieval, compaction and note-taking memory.
  Supports: the context window as a finite resource; recall degrades as tokens grow (context rot); keep the smallest set of high-signal tokens; just-in-time retrieval via lightweight references and tools; compaction (summarize and restart); structured note-taking to storage outside the window (a NOTES.md or to-do list) that is read back later.

## Other sources
- [Documentation: Context windows, Claude API docs, Anthropic](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Format: documentation (with diagrams).
  What the learner gets from it: a concrete picture of what is kept between steps, since every turn re-sends all earlier turns, tool results and tool definitions, so the window fills and the bill grows.
  Supports: the context window as "working memory", distinct from training data; history accumulating turn by turn; system prompt, tool results and tool definitions all count; output counts too; token counting before sending; overflow error; compaction and clearing old tool results.

- [Documentation: Memory overview, LangChain docs (LangGraph)](https://docs.langchain.com/oss/python/concepts/memory)
  Format: documentation.
  What the learner gets from it: a clean split of short-term memory (one conversation thread) and long-term memory (across sessions), with a storage model a Python student can map onto a dict or database (namespace like a folder, key like a file name, JSON documents).
  Supports: what is kept between steps versus between sessions; semantic (facts, such as a student's training status), episodic and procedural memory; where each is stored.

- [Tutorial: Build a RAG agent with LangChain, LangChain docs](https://docs.langchain.com/oss/python/langchain/rag)
  Format: tutorial with Python code.
  What the learner gets from it: a worked example of finding the right page in long documents: split into chunks (1,000 characters, 200 overlap), embed, store in a vector store, search for the top 4 matches. Caveat: the page shows an agent variant where the model decides when to search, and a fixed retrieve-then-answer RAG is described only in passing. Use it for the indexing and retrieval steps.
  Supports: retrieval; chunking; embeddings; vector store; retrieving only a few chunks to keep context small.

- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta (Charles Packer, Sarah Wooders)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  Format: video course, about 1 h 32 min in total, 8 video lessons of 1 to 14 min with 5 code notebooks (suggested: "Editable memory", 12 min, and "Agentic RAG and External Memory", 8 min).
  What the learner gets from it: someone talking through and coding the idea that the window is limited, so the agent moves things in and out of it, with notebooks to run. The multi-agent lesson is out of scope for this objective.
  Supports: limited context space and its cost; memory inside versus outside the window; editable facts such as names and preferences; moving overflow history to a searchable store; agentic RAG.

- [Paper: Lost in the Middle: How Language Models Use Long Contexts, Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni, Liang; TACL 2024 (arXiv 2307.03172)](https://arxiv.org/abs/2307.03172v3)
  Format: peer-reviewed paper (abstract read; the full PDF would not load as text, so rely on the abstract's claims only).
  What the learner gets from it: evidence, not just advice, that stuffing a whole manual into the window does not work reliably: models do best when the relevant text is at the start or end of the input and worse in the middle.
  Supports: why retrieving a few relevant pages beats loading a whole manual; long context is not used evenly.

- [Course notes: Tokenizers, Hugging Face LLM Course](https://huggingface.co/learn/llm-course/en/chapter2/4?fw=pt)
  Format: course documentation with code.
  What the learner gets from it: what a token is (word, character and subword splits, with "annoyingly" as "annoying" + "ly"), the unit that the window and the bill are counted in. The page says nothing about context length, so link tokens to the window using the Anthropic docs above.
  Supports: tokens as the unit of text a model reads; subword tokenization.

## Community
- [LangChain Forum](https://forum.langchain.com)
  Use for: questions on agent memory, checkpointers and stores, and retrieval set-up (category "OSS Product Help"), and sharing a design for feedback ("Talking Shop"). I could not confirm from the page that it is moderated; it links Guidelines and Terms.

## Coverage
- Context window and tokens (central): Anthropic context engineering post, Claude context windows docs, Hugging Face tokenizers, DeepLearning.AI course, Lost in the Middle.
- What is kept between steps (the growing message history): Claude context windows docs, LangChain memory overview (short-term, thread-scoped), DeepLearning.AI course.
- What is kept between sessions (long-term memory, notes): LangChain memory overview, Anthropic context engineering post (structured note-taking), DeepLearning.AI course.
- Retrieval from long manuals: LangChain RAG tutorial, Anthropic post (just-in-time retrieval), Lost in the Middle, DeepLearning.AI course (agentic RAG).
- Cost and budget: Claude context windows docs (everything counts toward the window, token counting) and the Anthropic post (smallest high-signal set). No source gives pricing arithmetic for the learner's budget; the lesson should build that example itself.
- Publishers: 6 (Anthropic x2, LangChain x2 plus its forum, DeepLearning.AI, arXiv/TACL, Hugging Face); formats: guide, documentation, tutorial, video course, paper, course notes, community forum.
