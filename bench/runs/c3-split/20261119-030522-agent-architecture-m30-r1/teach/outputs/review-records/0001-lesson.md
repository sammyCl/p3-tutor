# Review of lesson 0001

Passes: 2 (stopped because: the cap of two passes; pass 2 was revised but not re-reviewed, so its fixes are unchecked by a fresh reviewer)

## Pass 1
### lesson-fact-checker
- Findings: 7
- F1/F3 "The window gets B and A plus the question" vs "best 3 chunks" (section "Finding the right manual page"): figure and Step 3 now say "best few chunks"; the example says the program takes the top two in this tiny manual.
- F2 "Your manuals are not in the model's training" (retrieval check): reworded to "unlikely to be in the model's training data" and "cannot reliably quote".
- F3 "one manual page per item" (section "Keeping a long task alive"): example rewritten as ten questions, each using one page.
- F4a embeddings: rewritten as separate chunk, embedding and vector store steps.
- F4b "light-touch first move": changed to "one of the safest, lightest-touch forms of compaction".
- F4c "structure lets a later session pick up": claim removed.
- F5 Lost in the Middle dating: now "from 2023", "often highest", and a warning that it tested models of that time.
- F6 LangChain "two designs": reworded to what the page shows; the fixed-vs-agent choice is deferred to a later lesson.
- F7 RAM analogy: replaced with a desk picture and "nothing on it carries over by itself".

### lesson-pedagogy-reviewer
- Findings: 18
- P1 caching, meaning search, just-in-time, memory tool vs lookup: each given a one-line "when to use".
- P3 notes example moved to the opening of the section.
- P4 tool definitions, attention budget, lossy, key, embedding, vector store: glossed; table row relabelled "next section".
- P4 "Only output tokens are billed higher": claim dropped from the answer.
- P5 section minutes: window raised to 4, retrieval to 7, long-task to 5; not all of the suggested raises, to hold 30 minutes.
- P6 dense paragraphs: contents of the window, the two read-back options, chunk ranking and size failures, and the stale-status answer turned into lists.
- P7 stale fact bridge added in the notes section; "Your turn" step 2 given a hint; a clearing-versus-compaction check replaced the old compaction check; a sample answer added to the summary prompt.
- P7 "chunk holds the warning but not the table" practice question: not added, because it would push the length over; the size trade-off is in the worked example only.
- P1 "Cost grows" arithmetic as a table: not changed, because the paragraph is short and the figure of 12,500 is easy to follow.

### lesson-alignment-reviewer
- Findings: 7
- A2 ties for the window and long-task sections: added a sentence on what it means for the assistant, and rewrote the long-task example as many manual questions.
- A3 fixed-vs-agentic paragraph: cut to two sentences.
- A4 RAM and embeddings terms: fixed as above.
- A5/A6 cost and clearing-versus-compaction in "Your turn": added.
- A3 minor extras (FIFO aside): removed the aside.

### lesson-quality-reviewer
- Findings: 4
- Q3/Q6 repeated "bigger window" box: removed and folded into one sentence.
- Q4 figure number mismatch: fixed as in F1.
- Q5 community link is a weak destination: kept (the only community link opened in this session), with a clearer description and a pointer to a teammate or instructor.
- Q6 "memory" term seam: the table's first row renamed "Working window (not lasting memory)".

### lesson-figure-reviewer
- Findings: 3
- G2 Figure 2 arrows stopped short of the boxes: y2 set to 98, 196, 284.
- G3 "best 3 chunks" label and "Four steps" title: label changed to "best few chunks"; the title still says four steps, and the load and answer steps are left out on purpose.
- Optional bar chart of tokens per call: not added.

## Pass 2
Not run: the cap of two passes was reached after the pass-1 revision was written as the pass-2 draft, so the pass-2 draft was not re-reviewed.
