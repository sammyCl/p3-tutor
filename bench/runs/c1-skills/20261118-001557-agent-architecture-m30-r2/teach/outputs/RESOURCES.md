# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source for what belongs in context, context rot, just-in-time retrieval, compaction, note-taking memory and sub-agents. Use for: any decision about what the assistant keeps in context or saves.
- [Docs: "Context windows" (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of what counts toward the window, how turns accumulate, compaction and context editing. Use for: how many tokens a request really holds and why history is re-sent.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Explains RAG, chunking, embeddings, BM25 and the lost-context problem, with measured failure rates. Use for: designing how the assistant finds the right page in a long manual.

## Wisdom (Communities)

None added yet. Learner has not said whether they want communities; ask in a later session.

## Gaps

- A beginner-friendly source on the memory tool and per-user memory design (for training status between visits).
