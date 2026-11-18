# Sources for lesson 0003: O3 Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

## Primary source
- [Reference documentation: Context windows, Anthropic Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Why it is the primary: it defines the context window as the model's working memory and shows turn by turn how everything (system prompt, history, tool results, tool definitions, output) accumulates and counts.
  Supports: context window as working memory; history is resent and grows each turn (what is kept between steps); everything in the request counts, including tool results; context rot (more is not better); compaction and clearing old tool results; token counting before sending (cost control); overflow behavior.

## Other sources
- [Reference documentation: Memory tool, Anthropic Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Format: documentation (with Python example).
  What the learner gets from it: a concrete picture of memory between sessions as a folder of files the app stores and the model reads and writes through tool calls, including the multisession progress-log pattern.
  Supports: notes files as memory; what persists between sessions vs what is lost when the context resets; just-in-time loading instead of loading everything; client-side storage the developer controls; size caps and expiry.

- [Video course: LLMs as Operating Systems: Agent Memory, DeepLearning.AI with Letta (Charles Packer, Sarah Wooders)](https://www.deeplearning.ai/short-courses/llms-as-operating-systems-agent-memory)
  Format: video course, about 1.5 hours total in 8 short video lessons (5 to 14 min each) with code; free during platform beta, so check access. Lessons "Editable Memory" (12 min) and "Agentic RAG and External Memory" (8 min) are the most relevant.
  What the learner gets from it: a spoken, step-by-step view of memory tiers inside and outside the context window, in Python.
  Supports: limited context window and its cost and speed; in-context vs external memory (core vs archival); agent editing its own memory with tools; retrieval as external memory.

- [Guide: Retrieval-Augmented Generation (RAG), Pinecone Learn](https://www.pinecone.io/learn/retrieval-augmented-generation/)
  Format: explanatory guide.
  What the learner gets from it: a plain four-stage explanation (ingest, retrieve, augment, generate) that matches finding the right page in a long manual, and why RAG beats stuffing everything into the context window.
  Supports: RAG as retrieval memory; chunking and embeddings; retrieved text placed in the prompt; agentic RAG; cost/accuracy reasons to retrieve instead of pasting.

- [Tutorial notebook: Simple RAG for GitHub issues using Hugging Face Zephyr and LangChain, Hugging Face Cookbook](https://huggingface.co/learn/cookbook/en/rag_zephyr_langchain)
  Format: tutorial / runnable notebook (Python).
  What the learner gets from it: a worked example in code: split text into 512-character chunks, embed them, store in a vector index, retrieve the top 4 for a question, and pass them to the model.
  Supports: chunking, embeddings, similarity search, retrieved chunks as context (a manual-Q&A analogue).

## Community
- [DeepLearning.AI Community forum](https://community.deeplearning.ai/)
  Use for: questions on agent memory, context engineering and RAG, with dedicated categories for "Agent Memory: Building Memory-Aware Agents", "Context Engineering" and "Retrieval Augmented Generation". The page lists guidelines, but I could not confirm moderation or recent activity.

## Coverage
- Context window as working memory, and what counts toward it: Anthropic context windows (primary); DeepLearning.AI course.
- What is kept between steps (history resent each turn, tool results, trimming/compaction): Anthropic context windows; Anthropic memory tool (compaction section); DeepLearning.AI course.
- What is kept between sessions (notes files, progress log): Anthropic memory tool; DeepLearning.AI course.
- Retrieval as memory (RAG, chunking, embeddings): Pinecone guide; Hugging Face notebook; DeepLearning.AI course (agentic RAG lesson).
- Token cost: Anthropic context windows (token counting, usage, accumulation); Pinecone (retrieving vs packing context). Prompt-caching pricing page was read (https://platform.claude.com/docs/en/build-with-claude/prompt-caching) but left out to keep to two Anthropic sources.
- Publishers: 4 (Anthropic, DeepLearning.AI, Pinecone, Hugging Face); formats: reference documentation, video course, guide, runnable tutorial notebook.
