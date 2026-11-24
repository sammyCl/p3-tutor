# Sources for lesson 0001: O3 Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

## Primary source
- [Guide: Effective context engineering for AI agents, Anthropic Engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Why it is the primary: it covers the whole objective in one plain-language piece: the limited context window, what to keep, notes outside the window, and just-in-time retrieval.
  Supports: context is a limited "attention budget"; recall degrades as context grows (context rot); compaction (summarize and continue in a fresh window); structured note-taking to persistent memory such as NOTES.md; just-in-time retrieval with lightweight references instead of preloading.

## Other sources
- [Documentation: Memory (concepts), LangChain / LangGraph docs](https://docs.langchain.com/oss/python/concepts/memory)
  Format: documentation.
  What the learner gets from it: the clearest split between short-term memory (thread state, kept between steps, saved by a checkpointer) and long-term memory (a store, kept between sessions, organized by namespace and key), in Python terms.
  Supports: what is kept between steps vs between sessions; long conversations overflow the window and add cost and latency; stale information should be trimmed or forgotten.

- [Tutorial: Build a RAG agent (retrieval as a tool), LangChain docs](https://docs.langchain.com/oss/python/langchain/rag)
  Format: tutorial with Python code.
  What the learner gets from it: a worked example of finding the right passage in a corpus too big for the window: split into chunks (1000 characters, 200 overlap), embed, store, and expose search as a tool that returns the top 4 chunks.
  Supports: chunking, embeddings and vector store, retrieval as a tool the agent calls, why not load the full text into context.

- [Guide: Introducing Contextual Retrieval, Anthropic Engineering](https://www.anthropic.com/engineering/contextual-retrieval?utm_source=tldrai)
  Format: guide with measured results.
  What the learner gets from it: the cost-based rule (a knowledge base under about 200,000 tokens, roughly 500 pages, can go straight in the prompt with caching; larger needs retrieval) and why exact-term search (BM25) beats embeddings for codes such as "TS-999", which matches machine manuals and error codes.
  Supports: when to retrieve vs stuff the prompt; keyword plus embedding hybrid search; chunks losing context; prompt caching to cut cost; retrieval failure rates (5.7% down to 2.9% hybrid, 1.9% with reranking).

- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta (Packer and Wooders)](https://learn.deeplearning.ai/courses/llms-as-operating-systems-agent-memory)
  Format: video course, about 80 minutes total; for this lesson use "Editable memory" (12 min), "Understanding MemGPT" (14 min) and "Agentic RAG and External Memory" (8 min). Free access needs a trial or audit option; price of audit not stated on the page.
  What the learner gets from it: a spoken, step-by-step picture of memory as the agent's own editable context plus external storage, with code, from the MemGPT authors.
  Supports: in-context vs external memory; the agent editing its own memory; retrieval as external memory.

- [Paper: Lost in the Middle: How Language Models Use Long Contexts, Liu et al., TACL 2024](https://arxiv.org/abs/2307.03172v3)
  Format: peer-reviewed paper (read abstract and the figures on the U-shaped curve).
  What the learner gets from it: the evidence behind "don't just fill the window": accuracy drops when the relevant text sits in the middle, and adding more retrieved documents helps little.
  Supports: longer context is not free or reliably used; case for retrieving few, relevant pieces (also lowers cost per request).

## Community
- [DeepLearning.AI Community forum](https://community.deeplearning.ai/)
  Use for: course Q&A threads on Agent Memory, Context Engineering, RAG and agentic RAG; asking how others size chunks or decide what to save. Page links community guidelines but I could not confirm the moderation details from the page.

## Coverage
- Context window as a limited, costly resource: Anthropic context-engineering guide; Lost in the Middle; LangChain memory concepts.
- Kept between steps (state, history, trimming, compaction): LangChain memory concepts; Anthropic context-engineering guide; Letta course.
- Kept between sessions (notes files, stores): Anthropic context-engineering guide; LangChain memory concepts; Letta course.
- Retrieval to find the right manual page (chunking, embeddings, BM25, retrieval as a tool): Anthropic Contextual Retrieval; LangChain RAG tutorial; Letta course (agentic RAG lesson).
- Cost per request (what to keep in context vs retrieve): Anthropic Contextual Retrieval (caching, 200k threshold); LangChain memory concepts; Lost in the Middle.
- Publishers: 4 (Anthropic x2, LangChain x2, DeepLearning.AI with Letta, ACL/TACL via arXiv); formats: guide/article, reference documentation, tutorial with code, video course, paper.
