# Review of lesson 0001

Passes: 2 (stopped because: the cap of two passes)

## Pass 1
### lesson-fact-checker
- Findings: 7
- F1 retrieval failure rate unit: qualified to "top-20 retrieval failure".
- F2 stateless absolute and "your program runs the tool": qualified to "by default" and "a tool you define yourself".
- F4 clearing done by your program; two inexact quotes: reworded to say you set the rule, quotes made exact.
- F5 beta status: added "currently in beta".
- F6 LangChain thread description: reworded.

### lesson-pedagogy-reviewer
- Findings: 18
- Most fixed in pass 2: example before definitions, plain glosses, when-to-use rule per trimming move, Python list example, faded "Your turn", model answer for the summary, split dense paragraphs.
- Not changed: extra "put steps in order" prompt, because it would exceed the word budget.

### lesson-alignment-reviewer
- Findings: 9
- Fixed: time labels now sum to 30, sub-agent shortened, statelessness example added, history-reload alternative added.
- Not changed: extra borderline practice item beyond one preference case, for length.

### lesson-quality-reviewer
- Findings: 11
- Fixed: honest time labels, Figure 3 redrawn in two lanes, worked example gained a cost decision, repeated misconception box cut.
- Not changed: adding independent sources, because none were found this session (noted under Gaps in RESOURCES.md).

## Pass 2
### lesson-fact-checker
- Findings: 7
- F1 caption "grow fastest": changed to "can grow large".
- F2 absolutes: qualified (training aside; you set the trimming rule).
- F3 chunk size and RAG timing: chunks now about 300 tokens (5,400 total); classic RAG versus a search tool explained.
- F4 memory tool wording and sub-agent quote: reworded, quote removed.
- F7 "by default" added to the Figure 1 caption.

### lesson-pedagogy-reviewer
- Findings: 11
- Fixed: concrete reasons for memory tool versus own database, twenty-questions example for summarizing, BM25 and recall glossed, cost check made an application question, "Your turn" step 1 filled in and the rest faded.
- Not changed: P5 (more minutes for retrieval): retrieval label raised to 5 and others trimmed to keep 30.

### lesson-alignment-reviewer
- Findings: 4
- Fixed: opening tie in the trimming section, sub-agent bullet cut to a pointer, sorting rule added before the worked example, skip-retrieval paragraph resolved with the cost ratio, booking note replaced by a preference note, "Your turn" gained a paste-or-retrieve question.

### lesson-quality-reviewer
- Findings: 7
- Fixed: retrieval label 5 min, Figure 3 now shows two indexes with "chunk" wording, Figure 1 caption claim removed, RAG timing clarified.
- Not changed: independent sources and replacing the forum link, because no better vetted source was found this session.
