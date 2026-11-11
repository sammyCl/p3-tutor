# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Lesson 0001 (O3) now explains tokens, the context window, and why cost grows per step; not yet checked by quiz 0002.
- Has not met workflows versus agents or multi-agent systems; retrieval is only introduced (no embeddings or chunking yet).
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Lesson `lessons/0001-context-and-memory.html` (O3, 30 min) written, with quiz 0002 and `cheatsheets/context-and-memory.html`. Misconception ids: M3 (model remembers past chats on its own), M7 (bigger window means paste everything in), M8 (retrieval or notes mean the model memorises the content).
- Next: grade quiz 0001 and quiz 0002 when taken; then workflows versus agents. Retrieval ranking (chunking, embeddings) is a gap for the manuals.
