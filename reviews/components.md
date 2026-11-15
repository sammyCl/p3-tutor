# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Describes how an agent should answer a student's questions directly. The student will ask a question, and based on your knowledge of their objectives and background, answer the question appropriately. Make sure not to answer questions regarding quizzes, and keep explanations at an appropriate level for the user. As this is a description of how the agent should handle questions, it is a skill rather than an agent.
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: The skill has improved the agent's ability to answer questions that the student has. The agent approaches guardrails regarding quizzes appropriately and has the correct tone when answering a student's question. Ex. p01 and p02 are now met because the agent no longer gives the students the answers to the quiz.
- Kept in final: TODO

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: Describes how an agent should create a quiz and answer key for the quiz. It makes sure the quiz covers the student's objectives, and that the answer key for the quiz is appropriately explained. As this is a description of how the agent should create the quiz and answer key, it is a skill rather than an agent.
- With and without: reviews/c1-skills.md, Round 2 (without) and Round 3 (with)
- Review: Helps the agent to create quizzes at an appropriate difficulty with a mix of knowledge and real world questions. For example, all quiz questions closely align with the student's learning objectives. 
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: Describes how an agent should grade a student's work and provides feedback on what went wrong and how to improve. Ensures the agent's responses are warm, and that explations are thorough (to be improved). As this is a description of how the agent should grade the student's work, it is a skill rather than an agent.
- With and without: reviews/c1-skills.md, Round 3 (without) and Round 4 (with)
- Review: Helps the agent to have warmer responses to the student's work. For example, responses no longer start with, "Right.".
- Kept in final: TODO

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: Describes how the agent should create a lesson for the student. The lesson should cover the student's learning objectives, and explain the lesson in a way that is easy to follow. This means the lesson should be in plain english, should have real world examples, and should cover the main points of the student's question.A s this is a description of how the agent should create a lesson, it is a skill rather than an agent.
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: Lessons are easy to follow and cover all main talking points. They are also written in plain english so it is easier for the student to understand. The lessons also contain real world examples so the student can connect the information to applications.
- Kept in final: TODO
