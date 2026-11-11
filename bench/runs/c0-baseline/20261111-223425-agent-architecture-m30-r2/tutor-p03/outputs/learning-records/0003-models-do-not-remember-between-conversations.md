# Language models do not remember earlier conversations on their own

The learner assumed a model automatically remembers what students told it in earlier conversations, and expected the makerspace assistant to remember each student's input from last week. This was corrected in the chat: the model only sees what is in its current context, so anything kept between sessions must be saved by the assistant's code and put back into the context.
Whether the correction landed is not yet confirmed; the next lesson on context and memory should check it with a short retrieval question.

**Evidence:** chat message at the start of the session, answered by the tutor.
**Implications:** Build the context and memory lesson on this: what stays in context, what is saved between sessions, and what each costs in tokens.
