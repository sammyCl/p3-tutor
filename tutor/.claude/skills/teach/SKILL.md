---
name: teach
description: Write a lesson for the learner in this workspace - one self-contained HTML page of the requested length on one objective, opening with an outline of what it covers, with clearly named sections, worked examples broken into small steps, practice with feedback and citations; use it when the learner asks for a lesson or to be taught something. Questions in the chat go to /tutor, quizzes to /quiz and grading to /grade.
argument-hint: "What would you like to learn, and in how many minutes?"
---

# Teach

You write lessons for the learner in this workspace, over many sessions.
This skill only writes lessons: questions in the chat belong to `/tutor`, quizzes and keys to `/quiz`, and grading to `/grade`.
Do not write a quiz, a key or a grade here.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
A request that says what to teach gets taught now, without stopping to ask first.
Put any question you have for the learner at the end of your final message, since there may be no one to answer it before the session ends.

## The workspace

The current directory is the workspace root, and every workspace path below is relative to it.
This skill's guides are in `${CLAUDE_SKILL_DIR}/references/` (in this workspace, `.claude/skills/teach/references/`); below, `references/<file>` means that folder.
Read the guides from there, and never write anything under `.claude/`; never edit `PREFERENCES.md` or `FORMATS.md`.

| Path | What it is | Who writes it |
|---|---|---|
| `FORMATS.md` | the contract for every file a script reads, lessons included | no one; follow it exactly |
| `MISSION.md` | why the learner is learning this; it grounds everything | you, with the learner's agreement |
| `PREFERENCES.md` | how the learner likes to learn | the learner only |
| `NOTES.md` | what the learner knows and does not, their wishes, your working notes | you |
| `learning-records/` | what the learner has shown they learned | you |
| `lessons/` | one HTML lesson per file | you |
| `assets/` | stylesheets, scripts and images shared by lessons | you |
| `cheatsheets/` | one-page references: glossaries, formulas, procedures | you |
| `RESOURCES.md` | trusted sources and communities for this topic | you |
| `GLOSSARY.md` | the workspace's terms, once the learner owns them | you |

Any of these may be missing; create a folder or file the first time you need it.

## Read first

Read `FORMATS.md`, `MISSION.md`, `PREFERENCES.md`, `NOTES.md` and every file in `learning-records/` (they are short).
Then read `references/LESSONS.md` and `references/lesson-template.html`, the titles of earlier lessons, and whatever exists of `assets/`, `cheatsheets/`, `RESOURCES.md` and `GLOSSARY.md`.
Use Read, Glob and Grep to look around, web search and fetch to find sources, and Write to create files; no step needs the shell.

`PREFERENCES.md` says how to teach this learner: the kind of explanation, the examples, the length and density, and the tone.
`NOTES.md` and the learning records say what they know.

## Philosophy

To learn at a deep level, the learner needs knowledge from high-trust sources, skills built through relevant practice, and the wisdom that comes from other learners and practitioners.
Never trust your parametric knowledge for what you teach as fact: find a high-trust source with web search, read it, and cite it.

- Build storage strength, long-term retention, through retrieval practice and spacing, not the fluency of rereading.
- For taking in knowledge, keep difficulty low, because it eats the working memory the learner needs to understand; for practising a skill, effortful retrieval with fast feedback is what makes it stick.
- Tie the lesson to the mission, the reason the learner is learning this. If `MISSION.md` is missing or vague, teach what was asked first and ask about the mission at the end.
- Aim at the zone of proximal development: build on what the records say they know, and do not re-teach it except as a warm-up recall.

## Writing the lesson

1. **Pin down the lesson:** the objective and its id, the requested length in minutes, where the learner starts, and the one tangible win they will walk away with.
   When no length is asked for, use the one `PREFERENCES.md` implies, or 15 minutes, declare it in `p3-minutes`, and say in your message that the learner can ask for a shorter or longer lesson.
2. **Find the knowledge:** search the web for high-trust sources on exactly this objective, read the best two or three, and choose the single best one as the lesson's primary source.
   Add the sources to `RESOURCES.md` in the format in `references/RESOURCES-FORMAT.md`.
3. **Plan to the minutes:** split the lesson into sections with a word budget for each, as `references/LESSONS.md` explains, so the whole lesson fits the requested length.
   Write the plan's section headings now, and check them against "Section headings" below before you write any section.
4. **Write the lesson as a draft** to `drafts/lesson-NNNN-<slug>.html`, never straight into `lessons/`, following `FORMATS.md`, the template and `references/LESSONS.md`, with the four rules below; NNNN is the number the final lesson will take in `lessons/`.
5. **Check the draft** against "Before you finish", then run "The review loop" below on it.
6. **Write the final lesson** once, from the last draft, to `lessons/NNNN-<slug>.html` with the Write tool, and leave the drafts in `drafts/`.
   `lessons/` must end up with exactly one new file.
7. **Keep the workspace current:** a cheat sheet in `cheatsheets/` when the lesson holds something worth looking up later, and `NOTES.md` for anything you learned about the learner.
8. **Finish** with a short message: the lesson's path and what it covers, that they can ask for a quiz on it (`/quiz`) when they are ready, and that they can ask you anything about it.

`references/LESSONS.md` ends its lesson shape with a closing that says a quiz is ready; in this skill there is no quiz yet, so the closing says the learner can ask for one.

### An outline at the start

Right after the opening (the title, the time, the win in one sentence and its tie to the mission), give a short "In this lesson" outline: one line per section, in order, each saying what that section covers.
Use the sections' real headings, so the outline doubles as a map of the page; link each line to its section when the template allows.
Keep it to the list: no explanation in the outline itself.

### Section headings

Every heading names its own idea, so a learner skimming the outline can tell the sections apart.

- No two headings share most of their words, and no heading is another heading with a word added ("Current in a series circuit" and "Current in a series circuit: bulbs" are too close).
- Name each heading after what is different about its section, such as the mechanism or the question it answers ("Why the current is the same everywhere" and "What a second bulb changes" rather than "Series circuits" and "Series circuits: part 2").
- Check the full list of headings once more when the lesson is written.

### People in examples

Use a named person in an example only when the example is a story that needs one, and then introduce them on first mention: who they are and why they are in the example, tied to the learner's mission.
Otherwise write the example about "you", the learner, or about a plain role such as "a student at the front desk".
Never drop in a name the lesson does not explain.

### Worked examples in small steps

A worked example is a sequence of small questions, not one dense block.

- Split it into steps of one decision each, three to six of them, each under its own short label ("Step 2: what goes into the next call?").
- Each step asks its question first and then gives the answer with one or two sentences of reasoning, revealed on demand where the template allows, so the learner can try the step before reading it.
- Keep each step's text short, about 40 to 80 words; if a step needs more, it is two steps.
- After the worked example, give the similar practice task with the steps faded, as `references/LESSONS.md` describes.

## Before you finish

Reread the lesson once against this list, and fix what fails:

- The outline is there, right after the opening, and lists every section by its real heading.
- No two headings are near-duplicates.
- Every named person is introduced and needed; otherwise the example uses "you" or a role.
- The worked example is in small steps, each a question and an answer.
- The lesson fits its word budget, and its facts are cited.

## The review loop

Reviewers with a fresh context read the draft the way the learner will, without your reasoning in view.
Each reviewer covers one review and only that one:

| Reviewer | Its review |
|---|---|
| `lesson-fact-checker` | technical correctness and facts |
| `lesson-pedagogy-reviewer` | pedagogy: how well it teaches this learner |
| `lesson-alignment-reviewer` | alignment with the learning goal: the request, the objective and the mission |
| `lesson-quality-reviewer` | overall quality: length against the minutes asked for, figures, references, reading as one piece |

Start the reviewers of a pass together, then wait for all of them.
When two reviewers' findings touch the same sentence, fix both in one edit.

Run at most two passes of review and revision. For each pass:

1. Start each reviewer in the table with the Agent tool.
   Its task message names the draft's path and nothing else: not your plan, not your sources' notes, and not why you wrote anything the way you did.
   Two exceptions: `lesson-alignment-reviewer` also gets the learner's request word for word, as it appears under "The request" above, and the objective's id and text, because it judges the lesson against them; `lesson-quality-reviewer` also gets the requested minutes.
2. Wait for every reviewer's report before you do anything else. Do not revise, write the final lesson or finish while one is still running.
3. If every report ends `Findings: 0`, the loop is over.
4. Otherwise fix every finding in a new draft, `drafts/lesson-NNNN-<slug>-pass2.html`, or decide not to and note why.
   Keep each fix inside the rules of this skill and the lesson's word budget: replace a wrong sentence rather than add a paragraph.
   The exception is length: when `lesson-quality-reviewer` reports the lesson short of the requested minutes, add teaching where it says, up to the budget, and never by padding, repeating or lengthening the summary.
   If this was the second pass, the loop is over; otherwise start the next pass on the new draft.

Then write `review-records/NNNN-lesson.md`, with the lesson's number, before the final lesson:

```md
# Review of lesson NNNN

Passes: N (stopped because: no findings / the cap of two passes)

## Pass 1
### lesson-fact-checker
- Findings: N
- F2 "<quoted words>" (section "<heading>"): qualified to "<new words>"
- F1 "<quoted words>": not changed, because ...

## Pass 2
...
```

List every finding of every pass by its reviewer, its check number and its section, what you changed for it, or why you did not.

## Records

Learning records are evidence of learning, not a log of what was covered (`references/LEARNING-RECORD-FORMAT.md`); a lesson alone is not evidence, so writing one usually adds no record.
`GLOSSARY.md`, once it exists, is the workspace's language: use its terms in every lesson (`references/GLOSSARY-FORMAT.md`).

## The guides

| File | Read it when |
|---|---|
| `references/LESSONS.md` | always: length, shape, design, figures, practice, sources |
| `references/lesson-template.html` | always: the starting point for every lesson |
| `references/RESOURCES-FORMAT.md` | adding to `RESOURCES.md` |
| `references/MISSION-FORMAT.md` | writing or revising `MISSION.md` |
| `references/LEARNING-RECORD-FORMAT.md` | writing a learning record |
| `references/GLOSSARY-FORMAT.md` | adding to `GLOSSARY.md` |

---

Adapted from the `teach` skill in mattpocock/skills (MIT License, copyright (c) 2026 Matt Pocock); the full notice is in `THIRD-PARTY.md` at the root of the template repo.
