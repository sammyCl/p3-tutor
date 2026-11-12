# The model requests tools; whether Riley sees the program runs them is still open

On quiz 0001 (second attempt, s2), Riley correctly said the model outputs a structured tool request, that each tool result goes back as the next input, and that the number of model calls is the number of tool requests plus the final answer.
Two things are still open. Riley's reasoning on the call count said the model "runs" each tool itself (M4). Riley also thinks the loop will eventually succeed without a stopping condition (M6, q3).
Riley says the model picks a tool "by the name" only (q6), so descriptions are not yet understood as the model's whole basis for choosing.

**Evidence:** quiz 0001, submission s2, items q2, q4, q5, q3 and q6.

**Implications:** Before tool descriptions or context, recheck who runs a tool (the program) and why a loop needs a stopping condition. Teach the tool description (name, purpose, parameters) as the model's only view of a tool.
