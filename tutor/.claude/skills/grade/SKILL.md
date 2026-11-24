---
name: grade
description: Grade a learner's submission to a quiz - a verdict and the misconception it shows for every item, with short, exact, encouraging feedback and a summary with one next step - and record what the grades show; use it whenever the learner asks for a submission to be graded or hands in a complete set of quiz answers.
argument-hint: "Which quiz and submission should I grade?"
---

# Grade

You grade the learner's answers to a quiz in this workspace.
Grading gives the learner a verdict on each answer and feedback that helps them learn, and it is your best evidence of what they know.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When the learner gives a complete set of answers in the chat instead of naming a submission, write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows, and grade that.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short).
Then read the quiz in `quizzes/`, the submission in `submissions/`, and the lesson on the quiz's objective in `lessons/` if there is one.
Never read `keys/` or a draft key in `drafts/`: the keys guard blocks the main conversation from `keys/`, and the `grader` subagent reads the key for you.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.
Never write anything under `.claude/`, and never edit `PREFERENCES.md` or `FORMATS.md`.

`FORMATS.md` gives the exact shape of the grades file: follow it down to the file name, the verdict words and the JSON keys.

## 1. Verdicts and misconceptions, from the grader

1. Start the `grader` subagent with the Agent tool.
   Its task message names the quiz (`quizzes/NNNN.json`), its key (`keys/NNNN.json`) and the submission (`submissions/sN.json`), and nothing else.
2. Wait for its report before you do anything else. Do not write feedback, drafts or grades while it is still running.
3. Take each item's verdict and misconception id exactly as the report gives them; do not change them, because you cannot see the key.
   Write the feedback from the report's Idea and Their answer lines.
4. If the report names a key problem, say so in the summary.
5. If the grader does not return a verdict for every item, start it once more; if it still does not, finish without writing grades and tell the learner the grading could not be completed.

## 2. Misconceptions

The grader names a misconception id for each item, or `null`; explain it to the learner in words, never by its id alone.

## 3. Feedback

Write each item's feedback by the feedback skill: read `.claude/skills/feedback/SKILL.md` and follow it, its shape, its rules by verdict and its limits.
Every item, `correct` included, says why and ends with one next step.

## 4. The summary

A few sentences to the learner on the whole submission, in the same warm and exact voice:

1. What they have down, named by idea, not by item number alone.
2. The one thing to work on next, and why it matters for their mission.
3. One concrete next step: a section of a lesson to revisit, or a short practice to try.

No verdict words, no list of scores, and no more than about 80 words.

## 5. Check before you write

For every item, run the checks in the feedback skill's "Check each item", and rewrite any item that fails.

## 6. The review loop

Write the grades as a draft first, never straight into `grades/`: `drafts/grades-NNNN-sN.json`, in the exact shape `FORMATS.md` gives for the grades file.
A reviewer with a fresh context then reads the feedback the way the learner will, without your reasoning in view.
Run at most two passes of review and revision. For each pass:

1. Start the `grade-reviewer` subagent with the Agent tool.
   Its task message names the draft's path, the quiz, the submission, and the lesson on the quiz's objective in `lessons/` if there is one (or says there is none), but not the key: the reviewer checks the feedback, and the verdicts in the draft are the grader's.
   Hand it nothing else: not your reasoning, and not why you wrote any feedback the way you did.
2. Wait for its report before you do anything else. Do not revise, write the final grades or finish while it is still running.
3. If the report ends `Findings: 0`, the loop is over.
4. Otherwise fix every finding in the draft, or decide not to and note why.
   Keep to the feedback skill's limits while you fix them.
   If this was the second pass, the loop is over; otherwise start the next pass.

Then write `review-records/NNNN-sN-grade.md`, with the quiz's number and the submission's id:

```md
# Review of grades NNNN-sN

Passes: N (stopped because: no findings / the cap of two passes)

## Pass 1
- Findings: N
- G1 q2: added why the learner's picture fails -> "<new words>"
- G5 q4: not changed, because ...

## Pass 2
...
```

List every finding of every pass by its check number and item id, what you changed for it, or why you did not.

## 7. Write the files

1. Write `grades/NNNN-sN.json` once, from the last draft, named after the quiz and the submission, exactly as `FORMATS.md` shows, with one entry per quiz item in order, including unanswered ones; leave the draft in `drafts/`.
2. Write a learning record when the grades are evidence: real understanding of something non-trivial, or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`.
3. Update `NOTES.md` with what the learner knows and does not know yet.

## 8. Finish

Finish in the chat with the summary and the one next step, after the files are written.
