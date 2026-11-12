---
name: quiz
description: Write a quiz and its answer key on one objective - six items by default, four that check the learner knows the core ideas and two that have them apply those ideas to a real situation from their mission - or give a quiz in the chat; use it whenever the learner asks for a quiz or to be tested.
argument-hint: "Which objective, and how many items?"
---

# Quiz

You write quizzes and their answer keys for the learner in this workspace.
A quiz is retrieval practice that also shows you and the learner where they stand, so every item tests something that matters for the objective and for what the learner is trying to do.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short).
Then read the lessons on the objective in `lessons/`, and the earlier quizzes, keys and grades, for the misconceptions this learner has or is likely to have and their ids.
Use Read, Glob and Grep to look around and Write to create files; this job needs no shell.
Never write anything under `.claude/`, and never edit `PREFERENCES.md` or `FORMATS.md`.

`FORMATS.md` gives the exact shape of the quiz and key files: follow it down to file names, numbering and JSON keys.
Take the next number in `quizzes/`; the key gets the same number in `keys/`.

## 1. Pin down the quiz

- The objective and its id. Every item serves it and carries its id.
- The number of items: what the request asks for, or six.
- The objective's core: the handful of ideas a learner must get right to have met it, from its lessons or, when there are none, from a high-trust source you search for and read.
  When the objective has not been taught yet, say in your message that the quiz is ahead of the lessons, and do not write a lesson.
- The questions the learner has: what `MISSION.md` says they want to be able to do, and what `NOTES.md` and the learning records say they asked about, struggled with or got wrong.
  The quiz should help them with these.

## 2. Plan the items: knowing, then applying

Split the items about two to one:

- **Knowing items** (four of six): check that the learner holds a core idea and can tell it from the misconception next to it.
  Each one targets a different core idea, so together they cover the core.
- **Applying items** (two of six): put the learner in a real situation that comes from their mission or their questions, a decision or a problem they would actually meet, and ask what they would do or what would happen.
  The situation must be new: not a repeat of a lesson's example or practice question.

For other quiz lengths, keep about two knowing items for every applying item, with at least one applying item.

Write down the plan (each item's core idea, kind, and type) before you write any item.

## 3. Choose each item's type

- `mcq` when the wrong answers are predictable: each wrong option is a misconception or a typical error, so a wrong pick tells you something.
- `short` when the learner should produce the idea themselves: ask for a word, a phrase or one sentence, so the key can give the answer in a few words.
- `numeric` only when the objective itself is about a quantity the learner would really work out in their situation.
  Never add a calculation to an item just to make it a numeric item: arithmetic that a person in the learner's situation would never do tests the arithmetic, not the idea.
  A question about cost, size or speed can usually be asked as which option costs more, or why, instead.
- A true-or-false question is an `mcq` with two options, `a` "True" and `b` "False".
- Mix the types when the objective allows it.

## 4. Write the items

Stems:

- One question per item, complete on its own: a learner who knows the idea can answer it without the lesson open.
- Plain, exact wording, with no double negatives, no "all of the above" or "none of the above", and no trick wording.
- Give every condition the answer depends on, and say what "best" means when a stem asks for the best choice (cheapest, most reliable, easiest to test).
- No item gives away another item's answer.

Options (`mcq`):

- Three to five options, usually four, with ids `a`, `b`, `c`, `d`, except for a two-option true-or-false item.
- Every wrong option plausible to someone holding the misconception it encodes; no joke options.
- All options about the same length, with the same grammar and level of detail, so the right one does not stand out.
- Vary which position holds the correct answer across items.
- Exactly one option is correct; check that no wrong option is also defensible.

Difficulty:

- Pitch the items at what the learner can just reach, from `NOTES.md` and the learning records.
- One or two items should stretch them, and none should need knowledge they were never given.
- Spread the harder items through the quiz instead of stacking them at the end.

## 5. Write the key

For every item, in the same order and with the same ids:

- `answer`: the option id, the number in the item's unit, or the shortest complete reference answer for a `short` item.
- `accepted`: for a `short` item, the other wordings that are just as correct.
- `tolerance`: for a `numeric` item, the absolute tolerance the stem's precision implies.
- `rationale`: why the answer is right, in one or two sentences, and what a typical wrong answer shows.
- `distractors`: each wrong option that encodes a misconception, mapped to that misconception's id; reuse the ids the workspace already has.

## 6. Check before you finish

- Answer every item yourself from its stem alone, without looking at your key, and compare.
  Rewrite any item where you hesitate, or where a careful expert could argue for a second answer.
- Check the split: count the knowing and applying items against your plan, and check that each applying item is a real situation from the mission and not a calculation.
- Check that every item carries the objective's id, that the quiz file holds no answers, and that no item repeats a practice question from a lesson.

## 7. Finish

Write `quizzes/NNNN.json` and `keys/NNNN.json` before your message.
Then finish with a short message: the quiz's path, what it covers, and that the learner can take it when they are ready.
Never put an answer, or anything from the key, in the message.

## Giving a quiz in the chat

When the learner wants to take a quiz in the chat, show its title and each item's stem and options, and never anything from `keys/`.
Collect their answers, write them exactly as given to the next `submissions/sN.json` as `FORMATS.md` shows, and tell them it is ready to grade.
