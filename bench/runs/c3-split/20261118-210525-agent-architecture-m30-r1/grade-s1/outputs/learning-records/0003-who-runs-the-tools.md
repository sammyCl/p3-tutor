# Riley still believes the model runs its own tools and remembers on its own

Quiz 0001, first attempt: Riley holds the agent loop and a step limit, and knows the model picks tools from their descriptions. Riley also expects the model to open the booking system (q2), to run all three tools inside one call (q4), and to remember its earlier tool choices across sessions (q6). The two beliefs are M4 (the model runs tools itself) and M3 (memory is automatic).

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6; correct on q1 and q3.

**Implications:** Teach who does what in each step of the loop (the model writes a request, the program runs the tool and calls the model again) before context and memory. Show that a model sees only its current input, which is why memory must be added deliberately. Compare against submission s2, taken four days later, to see whether this held.
