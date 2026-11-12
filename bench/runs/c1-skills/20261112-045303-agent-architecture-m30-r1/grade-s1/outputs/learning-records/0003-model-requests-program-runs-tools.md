# Open misconception: the model runs the tools itself (M4)

In quiz 0001 (submission s1), Riley chose that the model opens the booking system itself and said the model runs three tools inside one call. Riley also believes the model remembers tool choices across sessions (M3). Riley does know that agents are loops, that they need a step limit, and that tools are chosen from their descriptions.

**Evidence:** quiz 0001, submission s1, items q2, q4 and q6.

**Implications:** Before moving on to context and memory, teach that the model only outputs a tool request, the program runs the tool, and every step is a separate model call with its own input. This also sets up why a model remembers nothing between calls unless the program passes it back in.
