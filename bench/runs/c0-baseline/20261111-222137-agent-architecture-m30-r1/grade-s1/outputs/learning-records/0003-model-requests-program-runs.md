# Misconception to work on: the model runs the tools and remembers on its own (M4, M3)

In quiz 0001, submission s1, Riley believed that the model opens the booking system and runs the tools itself, in a single call (M4). Riley also said that the model remembers on its own which tool it picked in earlier sessions (M3). Riley does know that the loop needs a stopping condition and that the model chooses tools from the descriptions it is sent.

**Evidence:** quiz 0001, submission s1: q2 (chose "opens the booking system on its own"), q4 (answered 1 model call, "runs the 3 tools itself"), q5 (said the result goes back to the model, with no reason) and q6 (added automatic memory across sessions). q1 and q3 were correct.

**Implications:** Before building on context and memory, make clear that each model call starts fresh with only the text it is given, and that the program runs the tools and feeds the results back. Submission s2, taken four days later, will show whether this has changed. Until then, this record stands.
