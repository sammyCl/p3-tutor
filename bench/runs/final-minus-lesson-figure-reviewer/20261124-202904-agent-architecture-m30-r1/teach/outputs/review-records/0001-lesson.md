# Review of lesson 0001

Passes: 2 (stopped because: the cap of two passes)

## Pass 1 (draft `drafts/lesson-0001-context-and-memory-timed.html`)
Findings by reviewer: lesson-fact-checker 9, lesson-pedagogy-reviewer 15, lesson-alignment-reviewer 6, lesson-quality-reviewer 8. All were handled in `drafts/lesson-0001-context-and-memory-pass2.html`, except as noted.

### lesson-fact-checker
- F1 "four chunks ... by the Lost in the Middle result they are easier for the model to use" (section "Finding the right page in a long manual"): reworded to a hedged claim.
- F2 "so a sentence cut at a boundary still appears whole" (same section): changed to "text near a boundary usually appears in both neighboring chunks".
- F2 "The model keeps nothing" (section "Why every step re-sends the history"): qualified to "When you call a model from code".
- F2 "a safety fact should never depend on a model's recall": reworded as the lesson's own advice.
- F3 clearing called compaction by Anthropic but kept apart in the lesson: reconciled in the bullet text.
- F4 "it" in "And on Friday?": changed to "Friday".
- F4 "as text" (warm-up): changed to "a structured request".
- F5 window sizes 200k to 1M: updated; server-side compaction mentioned and "clear first" labelled as the lesson's own rule.
- F1 TACL 2024 date: changed to "published in TACL".

### lesson-pedagogy-reviewer
- P1 to P7 (15 findings): fixed the ones on undefined terms (system prompt, tool definitions, tokenizer, thread), the makerspace token example, the rule for when to write a note, when embeddings are overkill, the check option wording, the summary answer and the first-use order of "compaction". Not changed, to hold the length: moving the saved-note example before the vendor terms, extra recall checks in the tokens, window and notes sections.

### lesson-alignment-reviewer
- A1 section times summed to 34: relabelled to 30.
- A2 weak mission ties: added design consequences in the window and cost sections.
- A3 retrieval not framed as memory: added a sentence in the retrieval section.
- A4 "your last lesson" and undefined system prompt: replaced and defined.
- A5, A6 no cost or defence practice: added a cost item in the second case.

### lesson-quality-reviewer
- Q2 time labels: relabelled. Q4 figures: added a figure for the cost growth, clarified figure 1. Q5 and Q6: clarified the Go further claim; mixed terms reconciled in later pass.

## Pass 2 (draft `drafts/lesson-0001-context-and-memory-pass2.html`)
Findings by reviewer: lesson-fact-checker 7, lesson-pedagogy-reviewer 17, lesson-alignment-reviewer 1, lesson-quality-reviewer 9. The loop ended at the cap, and the fixes below were made while writing `lessons/0001-context-and-memory.html`.

### lesson-fact-checker
- F2 "the call fails or something must be cut" (figure 1): changed to "the call fails, or the reply is cut short".
- F2 "Call 1: 2,000 tokens": the setup now counts the student's question.
- F2 warm-up tool wording: "For the tools you define, your program runs them."
- F3 figure order: renumbered 1, 2, 3.
- F5 Lost in the Middle: hedged as a 2023 study that varies by model.
- F7 retrieval as long-term memory: reworded to "how the assistant looks up reference material that lives outside the window".
- F2 "the model keeps nothing between calls" (quiz-style check): the "itself" wording was added in the warm-up; the section text was qualified in pass 1.

### lesson-pedagogy-reviewer
- P1 tool versus search on every question: added a sentence. P4 forward pointer to "context window": fixed. P4 "compaction" before its definition: bullet reworded. P5 figure order: fixed. P5 section times: rebalanced to 30.
- Not changed, to hold the length: P1 just-in-time and JSON-versus-database sentences, P3 reordering of the notes section, P6 paragraph splits, P7 extra recall checks, worked-example rejected-alternative clauses.

### lesson-alignment-reviewer
- A5 decision rule in one place: added a "Placement rule" bullet to the summary.

### lesson-quality-reviewer
- Q1 length 113% of target: removed the duplicate check in "When the window fills up" and the bullet list that repeated figure 2.
- Q2 labels: rebalanced to 30 minutes.
- Q4 figure 3 numbering: fixed. Q4 figure 1 versus text: caption explains why tool results are drawn separately.
- Not changed: Q3 cutting the second case (kept, it fades the support and tests the cost reasoning), Q5 adding another vendor-neutral source (none found beyond the paper and the tokenizer page), Q6 repeated points.
