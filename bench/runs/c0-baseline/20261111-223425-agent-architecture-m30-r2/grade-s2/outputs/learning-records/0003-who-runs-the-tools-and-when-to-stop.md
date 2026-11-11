# Riley knows how results flow back, but still says the model runs tools and that agents need no stop rule

On the spaced retry of quiz 0001, Riley correctly said the model outputs a tool request (q2) and that the result goes back in as the next input (q5). Two misconceptions remain: the model runs the tools itself (M4, in the q4 reasoning) and a stuck agent will eventually succeed without a stopping condition (M6, q3). Future lessons on context and memory should first restate that the program runs tools and that every step is a separate model call.

**Evidence:** quiz 0001, submission s2, items q2, q3, q4, q5 (compare s1, where q2 was wrong and q5 was a bare "sends it back").

**Implications:** Riley's q6 answer relied on the tool's name alone; the point that the model chooses from the full description matters for the tool-description skill in the mission.
