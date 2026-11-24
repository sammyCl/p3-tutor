# Riley knows the agent loop but mixes up who runs tools and thinks loops stop on their own

On quiz 0001 (second attempt, s2), Riley identified what makes an agent, that the model outputs a tool request, and that results go back as the next input, and counted model calls correctly.
Still open: Riley wrote that the model runs the tools itself (M4), believed an agent left running will eventually fix a bug (M6), and picked tools by name rather than by description.

**Evidence:** quiz 0001, submission s2, items q1-q6.

**Implications:** Before context and memory, revisit that the program runs tools and enforces a step limit, and teach tool descriptions.
