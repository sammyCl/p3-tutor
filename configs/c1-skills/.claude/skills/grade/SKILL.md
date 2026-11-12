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
Then read the quiz in `quizzes/`, its key in `keys/`, the submission in `submissions/`, and the lesson on the quiz's objective in `lessons/` if there is one.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.
Never write anything under `.claude/`, and never edit `PREFERENCES.md` or `FORMATS.md`.

`FORMATS.md` gives the exact shape of the grades file: follow it down to the file name, the verdict words and the JSON keys.

## 1. Verdicts

- Judge what the response means, not how it is worded: it is `correct` when it means what the key's answer means, even if it is oddly worded, misspelled, or reached by a valid route the key did not expect.
- The key's `accepted` list gives examples of correct wordings, not the only ones.
- It is `partial` when part of it is right: the right method with a slip or the wrong unit, one half of a two-part idea, or the right answer with a stated reason or an added claim that is wrong.
- It is `wrong` when it misses the idea, contradicts it, or is blank.
- For `mcq`, compare the option chosen with the key; if the learner wrote out an option's text instead of its id, match it to its option.
- For `numeric`, the number is right when it is within the key's tolerance (1% of the answer when the key gives none), after converting any unit the learner stated; a reason given with it is still judged by the rules above.
- If you are sure the key itself is wrong, grade against what is actually correct, and say so in the summary.

## 2. Misconceptions

- Name a misconception id when the response shows that misconception: for `mcq`, the key's `distractors` entry for the chosen option; for other items, the misconception the answer or its reasoning shows, from the ids the workspace already uses (the keys' distractors and rationales, `NOTES.md`, the learning records).
- Use `null` for a correct response, a slip, a blank, or a wrong answer that shows no known misconception, and never invent an id.

## 3. Feedback

Feedback is written to the learner, and it should leave them encouraged and knowing exactly what to keep and what to fix.
Be warm without flattery: name what they actually did well, and do not praise effort, the question, or the learner.

The verdict is already in its own field, so the feedback does not repeat it:

- Never open with, or use as a sentence of its own, a verdict word such as "Right", "Correct", "Wrong", "Incorrect" or "Not quite".
- Never announce the key, as in "The answer is 4" or "The correct option is c". Explain the idea, and let the right answer appear inside the reason ("each tool result needs one more call to the model, so three tools make four calls").
- Open with what the learner did: the idea they used, the part they got, or the belief their answer shows.

Keep each item's feedback exact: one to three sentences, at most about 50 words, with one idea per item.
Cut anything that restates the question, repeats the learner's answer back at length, or explains a second idea; an analogy only when it does more than the plain sentence would.

By verdict:

- **correct:** name the idea they used, then add at most one short insight that links it to what comes next.
- **partial:** say what they have, then exactly what is missing or off, and how to put it right.
- **wrong:** say what their answer shows they were thinking, then the idea that holds and why, in plain words; when a misconception is behind it, say why it is tempting, without blame.

Follow `PREFERENCES.md` for the tone and the kind of example, within these limits.

## 4. The summary

A few sentences to the learner on the whole submission, in the same warm and exact voice:

1. What they have down, named by idea, not by item number alone.
2. The one thing to work on next, and why it matters for their mission.
3. One concrete next step: a section of a lesson to revisit, or a short practice to try.

No verdict words, no list of scores, and no more than about 80 words.

## 5. Check before you write

For every item, reread the feedback and check that it:

- has no verdict word as its first word or as a sentence of its own, and no "the answer is";
- is three sentences or fewer, and about 50 words or fewer;
- says what was right or what the learner was thinking, and what to keep or fix;
- matches its verdict and misconception fields.

Rewrite any item that fails.

## 6. Write the files

1. Write `grades/NNNN-sN.json`, named after the quiz and the submission, exactly as `FORMATS.md` shows, with one entry per quiz item in order, including unanswered ones.
2. Write a learning record when the grades are evidence: real understanding of something non-trivial, or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`.
3. Update `NOTES.md` with what the learner knows and does not know yet.

## 7. Finish

Finish in the chat with the summary and the one next step, after the files are written.
