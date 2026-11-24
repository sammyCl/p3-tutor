# Review of lesson 0001

Passes: 2 (stopped because: the cap of two passes)

Timer (before pass 1): 8 findings. The draft was 66% of the target length; I added a cost step, a sorting worked example, a chunking worked example, two checks and a second practice task, and relabelled five sections.

## Pass 1 (on `drafts/lesson-0001-context-and-memory-timed.html`)
### lesson-fact-checker
- Findings: 10
- F1 "5.7% to 2.9% with hybrid search": corrected to say 2.9% came from keyword matching plus chunk context.
- F1 "main design job": changed to "essential for building capable agents".
- F1 "adding more retrieved documents helped little": removed.
- F3 Step 2 vs Step 5 contradiction (training lookup counted as a call): Step 5 now lists four calls and says the training status was loaded by the program.
- F3 "following August": changed to November.
- F3 45,000 tokens for 90 pages: changed to 36,000.
- F4 overlap keeps a sentence whole: softened. F4 "beyond that, you need retrieval": softened to "the usual route".
- F2 stateless wording and "biggest saver": qualified ("through a plain model API", "often").
- F5 200,000 figure dates from 2024: said so in the text.
- F6 utm tracking tag: removed.
### lesson-pedagogy-reviewer
- Findings: 21
- Most were fixed: terms defined (token, latency dropped, output tokens, namespace, vector store), big idea first in "The window", when to trim or summarize, caching explained, a bandsaw example for the attention effect, process steps as a numbered list, a decision sentence for key-value store versus notes file.
- P5 time budget and P7 missing checks: two retrieval and one sessions checks were added in the timing step; relabelled times and added a heading and time for the second practice section.
- Not changed: splitting the attention paragraph and a collapsed model answer for the summary prompt (kept to the word budget).
### lesson-alignment-reviewer
- Findings: 8
- A1 length and untitled practice section: gave it a heading, time and outline entry.
- A2 mission ties: added sentences on the design review and the sponsor budget.
- A4 jargon and placeholder helpers: glossed, and noted the helper functions are placeholders.
- A5 decision rule: added the sorting rule after Figure 2 and in the summary.
- A6 manual-size inconsistency: Step 3 notes the assumption and says to count real manuals.
- A3 tangents: kept hybrid search and caching, shortened.
### lesson-quality-reviewer
- Findings: 7
- Q2 labels, Q4 Figure 2 placement and Q6 Step 2 vs Step 5: fixed (labels, figure moved after the retrieval section, Step 5).
- Q5 utm tag: removed. Not changed: a link to provider caching documentation, because I opened none this session.
### lesson-figure-reviewer
- Findings: 6
- Fig 2 text overruns: relabelled; Fig 1 "Tool request + result"; Fig 2 moved after retrieval and "pages" changed to chunks.

## Pass 2 (on `drafts/lesson-0001-context-and-memory-pass2.html`)
### lesson-fact-checker
- Findings: 5
- Tutorial returns file paths in its current version: text updated.
- Step 6 note "lens cleaning; prefers afternoons": changed to "lens change; booked Friday 2 pm".
- Universal statelessness wording: qualified in the Figure 1 caption and summary.
- "three later calls": changed. Step 2 expiry re-check: added. Warm-up "for tools you define": added.
### lesson-pedagogy-reviewer
- Findings: 8
- Fixed: embedding example and vector store definition. Not changed, for length: checkpointer sentence, extra checks, summary model answer, paragraph splits.
### lesson-alignment-reviewer
- Findings: 7
- Fixed: caching assumption in the manual-size check. Not changed: shortening hybrid search and dropping the E-417 check (it teaches the exact-code point the mission needs); warm-up tie.
### lesson-quality-reviewer
- Findings: 9
- Q1 length of about 125% of target (within the bench's 0.6 to 1.5 band): not cut; I judged the extra practice worth the length, and relabelled "The window" (4 min) and retrieval (8 min).
- Not changed: link to provider caching docs; generic community link (kept as the community entry).
### lesson-figure-reviewer
- Findings: 4
- Fixed: Fig 1 arrow ends; Fig 2 context box widened to fit its label; arrow tips at y 112; lead-in no longer claims the figure holds the rule.
- Not changed: labels on the Fig 2 arrows.
