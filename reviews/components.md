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

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that reviews the created quiz and the key, acting as the student. It will check that the quiz answers are correct, making sure that each question only has 1 correct answer for MCQ, or correct answers for FRQ. It also checks that quiz answers are formatted well (answers don't start/end the same way, are about the same length, etc), explains what the misconceptions are instead of leaving a misconception id, makes sure quiz questions directly relate to the objective, and that there is no overlap with the lesson's practice. This is a subagent as it is an iterative process where the subagent will check the quiz multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Adding a subagent to review the quiz has resulted in quizzes that are formatted much better. The quizzes now say what misconceptions students fell into if they get a question wrong, which helps the student to better understand what went wrong. The quiz answers also are checked to make sure their beginnings and ends are formatted differently, this helps to make sure a student can't use the formatting as a way to find the correct answer, ex q2. The quiz questions are also now broken up into smaller parts if they are too long fo easily follow, which will help students to avoid misreading problems.
- Kept in final: TODO

### lesson-fact-checker

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that verifies all information in the lesson is factual and can be backed by evidence. It performs web searches that verify claims, checks for incorrect absolutes, areas where the lesson contradicts itself, sentences made ambiguous/wrong because of missing words, etc. This is a subagent as it is an iterative process where the subagent will check the lesson multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with); Round 3's run has no lesson, so the lesson without it is bench/runs/c1-skills/20261112-045303-agent-architecture-m30-r1 (teach was unchanged from the c1-skills snapshot until Round 3), and the lesson with it is bench/runs/_live/20261115-234947-agent-architecture-m30-r1
- Review: This subagent helps to improve the lesson by identifying false or misleading information, and correcting wording to make sure statements are factual. Previously there were many instances where statements would be included that were missing words that made statements ambiguous or false. Ex. changed "replies" to "+ model request / + model request / + model request", a more thorough and complete answer.
- Kept in final: TODO

### lesson-pedagogy-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that verifies the lesson is clear and easy to follow. It reads through the lesson and verifies that concepts explain "what" and "why", real-world examples, explains the big picture before details, and simplifies dense paragraphs. It also makes changes to the lesson to better match the requests in the `PREFERENCES.md`, such as including real world examples, explaining using computer science terms, etc. This is a subagent as it is an iterative process where the subagent will check the lesson multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 4 (without) and Round 5 (with)
- Review: Makes sure the lesson matches the way the `PREFERENCES.md` is setup. This includes real world examples, "The tool descriptions, short texts that tell the model what it can ask for, such as "get_training_status takes a student name and returns their training status"". This pass makes it much easier for the student to follow the lesson.
- Kept in final: TODO

### lesson-alignment-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that verifies all information in the lesson aligns with the student's learning objective. It verifies that all of the concepts the students want explained are explained, it verifies that there are sections covering each topic. This is a subagent as it is an iterative process where the subagent will check the lesson multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 5 (without) and Round 6 (with)
- Review: Makes sure to cover all of the topics that a student wants covered. This makes the most significant difference when a student wants to learn about a topic for a specific task, as previously the lesson would emphasize the topic instead of how to use the topic for the task. This pass makes changes like:
    - "Which to choose? Clear old tool results when the bulky part is raw output you already used. Summarize when the conversation itself has grown long."
    - "Which to choose? Clear old tool results when the bulky part is raw output you already used. Summarize when the conversation itself has grown long. For your assistant, a one-off booking rarely needs summarizing, but a long troubleshooting chat about a machine might, so default to filtering at the tool and clearing old results."
- Kept in final: TODO

### lesson-quality-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that reviews the entire lesson to verify that it is appropriate for the student. It verifies that the lesson is the correct length, that figures are useful, and that the lesson still reads well after all of the edits. This is a subagent as it is an iterative process where the subagent will check the lesson multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 6 (without) and Round 7 (with)
- Review: Performs an overall review to make sure the lesson is still correct given all of the edits. It also makes sure that the lesson still reads well. This ensures that the final product that the student receives is ready to be read and is easy to follow. Ex:
    - "Finding the right page in a long manual 5 min" to "Finding the right page in a long manual 6 min"
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: A subagent that reviews the feedback that is given after a quiz is graded. It makes sure that the feedback thoroughly explains why an answer is correct or incorrect, and where to look next without being too verbose. It also verifies that the tone of the feedback is warm, but does not contain filler or flattery. This is a subagent as it is an iterative process where the subagent will check the feedback multiple times to verify no changes have to be made, it will have a new context window that is more likely to identify issues that are present.
- With and without: reviews/c2-review.md, Round 7 (without) and Round 8 (with); Round 7's run has no grading, so the grades without it are grade-s1 in bench/runs/_live/20261115-231614-agent-architecture-m30-r1 (Round 2's run; grade was unchanged from the c1-skills snapshot until Round 7), and the grades with it are grade-s1 in bench/runs/_live/20261116-033625-agent-architecture-m30-r1
- Review: Adding the subagent has really improved the feedback that is given. The feedback is now thorough enough for a student to follow, understand where they went wrong, and what to do next. The subagent also makes sure that its feedback is warm. Ex:
    - "You have the what: the result goes back to the model. Missing is the why: the model has not seen the result yet, so the program adds it to the next input and calls the model again, letting it choose its next step or write the answer."
    - "You have what happens: the result goes back to the model. The why is missing: the model has not seen the result yet, so the program adds it to the model's next input, the text it receives on its next call, and calls it again. That lets the model choose its next step or write the final answer. Write out the next input the model gets after the calendar result."
- Kept in final: TODO
