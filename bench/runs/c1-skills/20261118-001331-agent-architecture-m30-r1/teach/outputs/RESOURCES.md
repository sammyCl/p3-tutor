# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, context rot, just-in-time retrieval, compaction, structured note-taking, sub-agents. Use for: what to keep in context, what to save outside it, and when to split work.
- [Docs: "Context windows" (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window (system prompt, messages, tool results, tool definitions, output), how turns accumulate, compaction and context editing. Use for: exact definitions and what is re-sent each call.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Why chunks lose meaning, embeddings plus BM25, reranking, measured failure rates, and when a whole knowledge base can just go in the prompt. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- None added yet. Ask the learner whether they want community suggestions (for example, a makerspace or university AI group).

## Gaps

- A high-trust source on per-request cost budgeting for agents (token pricing, caching) that is not tied to one vendor.
