# Reviews: final

Your review of `final`: optional quick rounds, its major review, your three learning sessions, and your review of the two test topics.
Quick rounds are optional here; use one for each component that `final` adds, such as a grader subagent, so its inventory entry has its with and without.
`p3 check` ignores an optional round you leave untouched.
The major review covers all four jobs on one of the three runs of `final`, and its previous step is `c3-split`; for the quiz and the feedback, which `c3-split` did not review, compare with `c2-review`, and for the tutor with `c1-skills`.
Its live tries are your three learning sessions, all on one of your two test topics, written up under Learning sessions below, so its Live tries line points at them.
Hold the sessions on `tutor/` as you snapshotted `final`, and note what they make you want to change instead of changing it.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1 (optional)

**Run:** bench/runs/c3-split/20261118-210525-agent-architecture-m30-r1

**My thoughts:**

- Make sure the tutor grading feedback for correct answers is thorough and actionable.
    - Maybe create a skill that tells the user what to do next for if they get the answer partial, correct, or wrong. 
    - Reference the `c2-review` major review s1 q1 and s2 q5 for examples of how the tutor doesn't provide thorough explanations for correct answers.
- Make a skill that tells the tutor how to handle questions that are outside of the user's current scope. This includes outlining a basic explanation of the topic, why it is outside of the students reach, and a relevant topic that is within their skill set to try instead. It should not include complicated math. 
    - Reference `c2-review`'s major review probe 5 for reference, demonstrates how the tutor still explains things out of scope using mathematical equations.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/feedback/SKILL.md, tutor/.claude/skills/grade/SKILL.md
- Why: The new feedback skill makes every graded item, correct ones included, open with the general idea, say why the answer holds or fails rather than repeating it back, and end with one next step by verdict, answering the thoughts about thin feedback on correct answers in c2-review s1 q1 and q5; grade now writes its feedback by it.

### Round 2 (optional)

**Run:** bench/runs/_live/20261123-231313-agent-architecture-m30-r1/grade-s1/outputs/grades/0001-s1.json

**My thoughts:**

- Make a skill that tells the tutor how to handle questions that are outside of the user's current scope. This includes outlining a basic explanation of the topic, why it is outside of the students reach, and a relevant topic that is within their skill set to try instead. It should not include complicated math. 
    - Reference `c2-review`'s major review probe 5 for reference, demonstrates how the tutor still explains things out of scope using mathematical equations.

What improved:
- Make sure the tutor grading feedback for correct answers is thorough and actionable.
    - Maybe create a skill that tells the user what to do next for if they get the answer partial, correct, or wrong. 
    - Reference the `c2-review` major review s1 q1 and s2 q5 for examples of how the tutor doesn't provide thorough explanations for correct answers.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/out-of-scope/SKILL.md, tutor/.claude/skills/tutor/SKILL.md
- Why: The new out-of-scope skill gives a question past the learner's level or mission a short plain-words explanation, the specific reason the rest waits, and one related topic within their reach to try instead, and bans every equation, formula and math symbol, answering the thought about probe 5; the tutor skill now follows it for such questions.

### Round 3 (optional)

**Run:** **Run:** bench/runs/_live/20261123-233131-agent-architecture-m30-r1, a live run with --only tutor-p05

**My thoughts:**

- Add a subagent that allows grading to see the key. It should have the name "grader". It will read the quiz, answer key, and submission. Since the guard was added, the misconception rate is 0.00. 

What improved:
- Make sure the tutor grading feedback for correct answers is thorough and actionable.
    - Maybe create a skill that tells the user what to do next for if they get the answer partial, correct, or wrong. 
    - Reference the `c2-review` major review s1 q1 and s2 q5 for examples of how the tutor doesn't provide thorough explanations for correct answers.
- Make a skill that tells the tutor how to handle questions that are outside of the user's current scope. This includes outlining a basic explanation of the topic, why it is outside of the students reach, and a relevant topic that is within their skill set to try instead. It should not include complicated math. 
    - Reference `c2-review`'s major review probe 5 for reference, demonstrates how the tutor still explains things out of scope using mathematical equations.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grader.md, tutor/.claude/skills/grade/SKILL.md, tutor/.claude/agents/grade-reviewer.md
- Why: Since the guard, grading could not see the key and every misconception field was null, so a grader subagent, the one name the guard allows, now reads the quiz, key and submission and returns each item's verdict and misconception id, and the grade skill starts it, waits for its report and writes the feedback from it without reading keys/; grade-reviewer no longer reads the key.

## Major review

**Run:** bench/runs/final/TODO

**Live tries:**

TODO: one line that points at your three learning sessions under Learning sessions below, and names anything else you tried with `final`.

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

### What I would do next

TODO

## Learning sessions

### Session 1

**Date:** TODO

**Topic:** TODO

TODO

### Session 2

**Date:** TODO

**Topic:** TODO

TODO

### Session 3

**Date:** TODO

**Topic:** TODO

TODO

## Test topics

### TODO: your first test topic's id

TODO

### TODO: your second test topic's id

TODO
