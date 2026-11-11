# Riley knows what makes an agent and what the model outputs; stopping conditions and tool descriptions are still open

On quiz 0001 (spaced retake, submission s2), Riley identified the agent loop, knew that the model outputs a tool request and the program runs the tool, and explained that results go back as the next input.
Still open: M6 (believing a stuck agent will eventually succeed without a stopping condition), M4 showing in the reasoning on q4 (the model runs the tools itself), and choosing tools by name only instead of by full description.

**Evidence:** quiz 0001, submission s2, items q1, q2, q5 correct; q3 wrong (M6); q4 right count with M4 reasoning; q6 partial.

**Implications:** Before building on context and memory, revisit stopping conditions (cost and budget angle) and tool descriptions, with an exercise that writes a description for check_calendar. Check again later that Riley says the program, not the model, runs tools.
