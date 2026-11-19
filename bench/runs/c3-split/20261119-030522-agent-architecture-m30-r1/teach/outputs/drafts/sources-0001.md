# Sources for lesson 0001: O3 Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

## Primary source
- [Article: Effective context engineering for AI agents, Anthropic](https://anthropic.com/research/effective-context-engineering-for-ai-agents)
  Why it is the primary: it explains in plain language the whole objective in one piece (a limited context window, context rot, compaction, note-taking memory outside the window, just-in-time retrieval) and every idea maps to the makerspace assistant.
  Supports: context window as a finite "attention budget"; context rot (recall weakens as tokens grow); compaction (summarize and continue in a fresh window); structured note-taking (NOTES.md-style files read back later); just-in-time retrieval (keep lightweight references, load content with tools only when needed); smallest set of high-signal tokens as the goal.

## Other sources
- [Documentation: Memory tool, Anthropic Claude Platform docs](https://platform.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
  Format: documentation (with Python code and a worked tool-call exchange).
  What the learner gets from it: a concrete, code-level picture of memory between sessions: the model asks for file operations, the app runs them against storage the app controls (for example a per-user directory or database keys), and a later session reads the same store. This is the shape of "remember each student's training status".
  Supports: memory that persists between sessions; client-side storage you control; the view/create/str_replace/insert/delete/rename commands; the tool_use / tool_result loop applied to memory; pairing memory with compaction and context editing; multisession progress-log pattern; security (path validation, size caps, expiry).

- [Paper: Lost in the Middle: How Language Models Use Long Contexts, Liu et al. (Stanford and collaborators), TACL 2024, arXiv 2307.03172](https://arxiv.org/abs/2307.03172)
  Format: peer-reviewed paper (abstract and figures are enough for the lesson).
  What the learner gets from it: independent evidence, not vendor advice, that stuffing a long manual into the window does not guarantee the model uses it: accuracy is best when the relevant text is at the start or end and worse in the middle.
  Supports: why a bigger window is not a substitute for retrieval; position and length effects on long inputs; why to send only the relevant manual pages.

- [Tutorial: Build a RAG agent with LangChain, LangChain docs](https://docs.langchain.com/oss/python/langchain/rag)
  Format: tutorial with Python code.
  What the learner gets from it: the step-by-step retrieval pipeline for a document collection: load, split into chunks (about 1,000 characters, 200 overlap), embed and store, then per question retrieve similar chunks and generate. It also contrasts a fixed retrieve-then-generate flow with an agent that decides when and what to search.
  Supports: retrieval as memory for long manuals; chunking and overlap; embeddings and vector store; retrieval at question time; fixed pipeline versus agentic search.

- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta (Charles Packer, Sarah Wooders)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  Format: video course, about 1h32m in total (8 short video lessons of 1 to 14 min, 5 with code). For a 30-minute lesson, point the learner at "Editable memory" (12 min), "Understanding MemGPT" (14 min) and "Agentic RAG and External Memory" (8 min).
  What the learner gets from it: a second, visual explanation using an operating-system analogy (in-context memory like RAM, out-of-context archival memory like disk) that a computer science student will recognize, with the agent editing its own saved facts.
  Supports: the context window is limited and longer contexts cost more and run slower; moving old details to a searchable store and keeping key facts in context; persisting and editing facts such as names, dates and preferences; in-context versus out-of-context memory; agentic RAG.

## Community
- [DeepLearning.AI Community forum (Short Course Q&A category)](https://community.deeplearning.ai/t/about-the-short-course-q-a-category/311436)
  Use for: questions about building agent memory and retrieval in Python, plus questions about the Letta course above. The forum has moderators who enforce a published Code of Conduct and community rules (per its moderators page and rules pages found in search; I did not open the rules text itself).

## Coverage
- Context window as a limited working space, and what it costs: primary (attention budget, context rot); Letta course (longer contexts cost more and run slower); Lost in the Middle. I opened the Anthropic Context windows page (https://platform.claude.com/docs/en/build-with-claude/context-windows) which shows that every turn re-sends the whole history, system prompt, tools and tool results, but it would be a third Anthropic source, so only that one fact (token accumulation across steps) has a single backing source if the lesson needs it, and the lesson writer may swap it in for the memory-tool page if the budget-cost point matters more.
- What is kept between steps: primary (compaction, clearing old results); memory tool docs (context editing, compaction); Letta course (summarize key facts, swap in relevant items).
- What is kept between sessions: memory tool docs; primary (note-taking); Letta course (persistent editable memory).
- Retrieval as memory for long manuals: LangChain tutorial; primary (just-in-time retrieval); Letta course (agentic RAG); Lost in the Middle (why retrieve rather than stuff).
- Notes as memory: primary; memory tool docs; Letta course.
- Publishers: 4 (Anthropic x2, arXiv/TACL paper authors, LangChain, DeepLearning.AI with Letta); formats: article, documentation, peer-reviewed paper, tutorial with code, video course.
