# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261111-225106-agent-architecture-m30-r1, a quick run

**My thoughts:**
Lesson:
- We should add a brief summary of what the lesson will cover at the beginning of the lesson. This will help students have a better idea of what to expect during the lesson. This is briefly covered in other places, but having a more explicit outline would be helpful.
- References a random name, Riley, without having a story or any references to why the name is important, remove that.
- The worked example section is too dense, split it up into multiple questions so it is easier for the student to parse. 
- There is "What is kept in between sessions" and "What is kept in between sessions: notes", they have very similar names but cover different things. Have sections named more appropriately.

Quizzes:
- Quizzes should focus more on addressing the student's questions and showing them how to apply it to real world scenerios. Questions like q5, where they are asked to do math, does not apply to a real world scenerio where they would need to know the information. This type of question is appropriate for a lesson, not a quiz.
- Quizzes questions should be distributed questions to have 4 based on knowledge, and 2 applying that knowledge.

Tutor Grading:
- The tutor's feedback is a bit cold. The tutor should not embellish its language or flatter the student, but should be warmer. We want the student to feel encouraged by the tutor. Do not use terms like "Right", "Wrong", or "The answer is 4".
- Some feedback is unnecessarily verbose, try to keep it more exact.

Tutor Conversation:
- The tutor has to be more careful in its explanations. Make sure that if the student is asking a question from the quiz that the explanation does not answer the question. It is preferred that the agent keeps its response short than for it to tell the student the answer to the problem.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md, tutor/CLAUDE.md
- Why: The thoughts ask that a tutor reply about a quiz item never give the answer away and stay short rather than risk it, so the new tutor skill caps those replies at about 120 words, gives them a fixed shape of help that applies to every option, and has the tutor delete any sentence that hints at what the item tests before sending.

### Round 2

**Run:** bench/runs/_live/20261112-025342-agent-architecture-m30-r1, an --only run of tutor-p01 and tutor-p02

**My thoughts:**

Positives:
- Tutor no longer gives answers to quiz questions.
- Tutor is less verbose in its replies.
- Tutor comes across as warmer.
- Expected behavior increased from 0.5 to 1.0, p01 went from NOT MET to MET.

Remaining from Round 1's Run:

Lesson:
- We should add a brief summary of what the lesson will cover at the beginning of the lesson. This will help students have a better idea of what to expect during the lesson. This is briefly covered in other places, but having a more explicit outline would be helpful.
- References a random name, Riley, without having a story or any references to why the name is important, remove that.
- The worked example section is too dense, split it up into multiple questions so it is easier for the student to parse. 
- There is "What is kept in between sessions" and "What is kept in between sessions: notes", they have very similar names but cover different things. Have sections named more appropriately.

Quizzes:
- Quizzes should focus more on addressing the student's questions and showing them how to apply it to real world scenerios. Questions like q5, where they are asked to do math, does not apply to a real world scenerio where they would need to know the information. This type of question is appropriate for a lesson, not a quiz.
- Quizzes questions should be distributed questions to have 4 based on knowledge, and 2 applying that knowledge.

Tutor Grading:
- The tutor's feedback is a bit cold. The tutor should not embellish its language or flatter the student, but should be warmer. We want the student to feel encouraged by the tutor. Do not use terms like "Right", "Wrong", or "The answer is 4".
- Some feedback is unnecessarily verbose, try to keep it more exact.

New Issues:

Tutor:
- Make sure the tutor does not share its internal thoughts. It should only output information for the student, not its thoughts. Ex: "Ungraded quiz, so I'll decline to settle it. I'll keep the reply short."

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md, tutor/CLAUDE.md
- Why: The thoughts ask for quizzes split four knowing items to two applying items, with real-world situations instead of calculations like q5, so the new quiz skill plans each quiz in that split, ties the applying items to the learner's mission and questions, and allows a numeric item only when the objective itself is about a quantity.

### Round 3

**Run:** bench/runs/_live/20261112-031206-agent-architecture-m30-r1, an --only run of quiz

**My thoughts:**

Positives:
- Quizzes now have questions that are much more relevant to real world scenerios. 
- Quiz questions are a good combination of knowledge-based and real world applications, such as questions 2, 5, and 6.

Remaining from Round 1's Run:

Lesson:
- We should add a brief summary of what the lesson will cover at the beginning of the lesson. This will help students have a better idea of what to expect during the lesson. This is briefly covered in other places, but having a more explicit outline would be helpful.
- References a random name, Riley, without having a story or any references to why the name is important, remove that.
- The worked example section is too dense, split it up into multiple questions so it is easier for the student to parse. 
- There is "What is kept in between sessions" and "What is kept in between sessions: notes", they have very similar names but cover different things. Have sections named more appropriately.

Tutor Grading:
- The tutor's feedback is a bit cold. The tutor should not embellish its language or flatter the student, but should be warmer. We want the student to feel encouraged by the tutor. Do not use terms like "Right", "Wrong", or "The answer is 4".
- Some feedback is unnecessarily verbose, try to keep it more exact.

New Issues:

Tutor:
- Make sure the tutor does not share its internal thoughts. It should only output information for the student, not its thoughts. Ex: "Ungraded quiz, so I'll decline to settle it. I'll keep the reply short."

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md, tutor/CLAUDE.md
- Why: The thoughts ask for grading feedback that is warmer without flattery, never says "Right", "Wrong" or "The answer is 4", and is less verbose, so the new grade skill opens each item on what the learner did instead of a verdict word, caps feedback at three sentences and about 50 words, and checks every item against those rules before writing the grades.

### Round 4

**Run:** bench/runs/_live/20261112-034318-agent-architecture-m30-r1, an --only run of grade-s1

**My thoughts:**

Positives:
- The feedback is less verbose, making it easier for the student to digest. This is present across all 6 questions.
- The feedback is warmer, helping to encourage the student. This is present across all 6 questions.

Remaining from Round 1's Run:

Lesson:
- We should add a brief summary of what the lesson will cover at the beginning of the lesson. This will help students have a better idea of what to expect during the lesson. This is briefly covered in other places, but having a more explicit outline would be helpful.
- References a random name, Riley, without having a story or any references to why the name is important, remove that.
- The worked example section is too dense, split it up into multiple questions so it is easier for the student to parse. 
- There is "What is kept in between sessions" and "What is kept in between sessions: notes", they have very similar names but cover different things. Have sections named more appropriately.

New Issues:

Tutor:
- Make sure the tutor does not share its internal thoughts. It should only output information for the student, not its thoughts. Ex: "Ungraded quiz, so I'll decline to settle it. I'll keep the reply short."

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/SKILL.md, tutor/CLAUDE.md
- Why: The thoughts still ask for a lesson outline at the start, no unexplained names like Riley, worked examples split into smaller questions, and section headings that are not near-duplicates, so teach is rewritten to write only lessons and to follow those four rules, with a check of each before it finishes.

### Round 5

**Run:**  bench/runs/_live/20261112-035712-agent-architecture-m30-r1, an --only run of teach

**My thoughts:**

Positives:
- The new lesson has an outline at the start, making it easier for the student to follow.
- Random name references were removed.
- The worked example section was split into much more manageable chunks by separating things into different sections.
- Sections were renamed appropriately.
- Overall the flow of the lesson and the language was much easier to follow.

Remaining Issues:

Tutor:
- Make sure the tutor does not share its internal thoughts. It should only output information for the student, not its thoughts. Ex: "Ungraded quiz, so I'll decline to settle it. I'll keep the reply short."

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: The thoughts ask that the tutor never share its internal thoughts, such as "Ungraded quiz, so I'll decline to settle it", so the tutor skill now says its reply holds only words to the learner, never narration of its decisions, and has it delete a first sentence that is about itself before sending.


## Major review

**Run:** bench/runs/c1-skills/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
