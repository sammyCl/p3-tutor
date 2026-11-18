# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

- Quiz 0001, s1: knows what makes a system an agent (the loop) and that a step limit is the safeguard against a stuck loop; knows the model chooses tools from their names and descriptions.

## Misconceptions still open
- M4: thinks the model opens systems and runs the tools itself, so it counted 1 model call for 3 tool runs (quiz 0001 s1, q2 and q4).
- M3: thinks the model remembers its earlier tool choices across sessions on its own (s1, q6).
- Gives the "what" but not the "why" when asked what happens to a tool result (s1, q5).

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  s1 is graded (`grades/0001-s1.json`); s2 has not been graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
