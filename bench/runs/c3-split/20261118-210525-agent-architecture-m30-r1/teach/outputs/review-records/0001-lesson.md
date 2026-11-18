# Review of lesson 0001

Passes: 1 (stopped because: I applied the pass-1 fixes and did not run a second review pass; the final lesson has not been re-reviewed)

## Pass 1
### lesson-fact-checker
- Findings: 10
- F1 "A call with ten tool steps sends the early material ten times" (section "What the loop carries from step to step"): changed to "A request with ten tool steps makes eleven calls, so the early material is sent eleven times."
- F1 "512-character chunks" (section "Retrieval"): removed the figure and the paragraph; the notebook is now only linked.
- F2 "remembers nothing... All it has is the text you send" (section "The context window as the model's whole desk"): reworded to "keeps no conversation state... plus whatever it learned in training".
- F2 "It is the model's only memory" (section "Summary"): changed to "the only place the model reads this conversation from".
- F2 "the window is wiped when the conversation ends" (section "Notes that outlive the session"): reworded to say the window holds only what the program sends each call.
- F3 booking saved in notes vs booking system (section "Worked example and your turn"): one rule now: bookings stay in the booking system, only status changes go to notes.
- F4 thinking text billing: sentence removed (also an alignment finding).
- F4 "Just-in-time loading": changed to "Just-in-time retrieval".
- F6 DeepLearning.AI "calls this agentic RAG": softened to "sometimes called agentic RAG, and the course has a lesson on it".
- F6 community categories: reworded to Course Q&A subcategories and threads on agent memory.
- F7 desk analogy and training knowledge: covered by the F2 rewording.

### lesson-pedagogy-reviewer
- Findings: 20
- P1 clear vs compact: added a rule of thumb and a "Try it" check.
- P1 prompt caching: reduced to a short aside.
- P1 agentic RAG alternative: added the search-every-question alternative.
- P1 just-in-time: added when loading everything up front is fine.
- P3 retrieval opening and window opening: both now lead with a concrete picture.
- P4 system prompt, tool definitions, tokens, embedding, index, stateless: each now defined with an example.
- P4 context rot example: not changed, because the 40-manuals check already gives one.
- P5 time budgets: relabelled (window 3, retrieval 7, practice 5); Step 4 forward reference reworded.
- P6 paragraph splits: window, cost rule and retrieval flow split; memory-tool paragraph not changed, because it is already short.
- P7 faded task after token tally: not added, to hold the word budget; "Your turn" items 2 and 3 now ask why.

### lesson-alignment-reviewer
- Findings: 5
- A2 window section tie to the mission: added a budget sentence.
- A3 trim Hugging Face and chunk size: done.
- A4 thinking, caching, tool definitions: removed or defined.
- A5 reasons and the fourth source: "and why" added; the live tool call is named as a fourth source.
- A6 embedding mechanics in the worked example: steps 1 and 2 merged, and a token cost added.

### lesson-quality-reviewer
- Findings: 11
- Q2 practice label: relabelled to 5 min.
- Q4 Figure 2 two-way notes arrow, tools source, forward reference to the index: added and flagged in the caption; the figure was not moved.
- Q4 Figure 1 "pay on every call": reworded to the input part.
- Q4 growth figure for the token tally: not added, to hold the budget.
- Q5 single source for context rot: not changed, because only the Anthropic docs were opened for it.
- Q6 "memory" wording and the booking inconsistency: fixed.
- Q6 repetition of the resend point: Step 4 shortened.

### lesson-figure-reviewer
- Findings: 3
- G1 Figure 2 text overrun: split into two lines.
- G2 arrow gap: arrows now end at x 291.
- G3 "page" vs "chunks": changed to "a few chunks".
