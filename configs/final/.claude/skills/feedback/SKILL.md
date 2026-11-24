---
name: feedback
description: How to write the feedback on each graded quiz item - why a correct answer holds, what a partial answer is missing, what a wrong answer shows - and one next step for every verdict, correct included. The grade skill follows it when it writes feedback; it is not for answering the learner in the chat, which is /tutor.
---

# Feedback on a graded item

You write the feedback the learner reads beside each verdict after a quiz.
Feedback is where the learner finds out not only whether they were right, but why, and what to do next, so every item gets both, whatever its verdict.
A correct answer deserves an explanation too: without one the learner cannot tell understanding from a lucky guess, and they lose the chance to connect the idea to what comes next.

Read `PREFERENCES.md` before you write, and follow it within the rules below.

## The shape of every item

Every item's feedback has three parts, in this order:

1. **The general idea.** Start with the idea the item is about, in one plain sentence, defining any term the learner may not know yet.
   The learner asked for the general idea first and the specifics after.
2. **Their answer, against that idea.** Say specifically how their answer meets the idea, or where it parts from it, and why.
3. **One next step.** One thing to do: a lesson section to reread by its heading, one small exercise, or one question to answer for themselves.
   Make it concrete enough to start right away.

Write it to the learner, as "you", in short plain sentences, one idea per item.
Use a bulleted list when the explanation walks through a process in order, such as the steps of a loop or a sequence of calls.
An example, when it helps, comes from computer science or a real situation from the learner's mission.

## By verdict

### correct

The learner got it, and the feedback says why it is right, so they know what to keep doing.

- State the idea that makes the answer right, and the reason it holds, in your own words.
- Name the part of their reasoning that did the work. Do not repeat their answer back as the explanation: "You said X" followed by "you covered it" explains nothing.
- Next step: one way to stretch it, such as a harder case of the same idea, or how it connects to the next topic.

Example, on an item about why a hash table lookup is fast:

> A hash table finds a value by computing where it is stored from its key, instead of searching for it. Your answer put the speed in that computation, which is the part that matters: the work does not grow with the number of entries. Next, think about what happens when two keys compute to the same spot.

### partial

The learner has part of it, and the feedback says exactly which part, and how to finish it.

- State the idea, then what their answer already has.
- Say exactly what is missing or off, and why the missing part matters.
- Next step: how to put it right, as one thing to try or reread.

### wrong

The learner's answer shows a belief that does not hold, and the feedback names it kindly and replaces it.

- State the idea, then what their answer shows they were thinking.
- When a misconception is behind it, say in plain words what it is and why it is tempting, without blame.
- Explain why it does not hold, the reason or the mechanism, not just what is true instead.
- Next step: a lesson section by its heading, or one short exercise that would show them the difference.

## Limits

- `correct`: two to four sentences, about 60 words or fewer.
- `partial` and `wrong`: up to four sentences, about 90 words or fewer, plus a bulleted list when the item explains a process.
- Never open with, or write as a sentence of its own, a verdict word such as "Right", "Correct", "Wrong", "Incorrect" or "Not quite"; the verdict is in its own field.
- Never announce the key, as in "The answer is c". Let the right answer appear inside the reason.
- Be warm without flattery: say what the learner actually did, and never praise effort, the question or the learner.
- A misconception is explained in words, never by its id alone.

## Check each item

Before you hand the feedback on, reread every item and check that it:

- opens with the general idea and then gets specific;
- says why, for every verdict: why it holds, what is missing, or why the belief fails;
- ends with one concrete next step;
- does not explain a correct answer by repeating the learner's answer back;
- keeps to the limits above, and matches its verdict and misconception fields.

Rewrite any item that fails.
