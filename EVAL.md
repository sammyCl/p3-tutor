# Evaluation report

This is the report on what each step of your architecture bought and what it cost.
I read it for one thing above all: whether each claim matches its evidence, including the steps that did not pay.
A step you measured carefully and then dropped is as good a result as a step that won.

Three kinds of material go here.
The tables are pasted from commands: `uv run p3 report --configs a,b` for the objective checks, the cost and your ratings, and `uv run p3 compare --reveal <session-id>` for each blind comparison.
Paste them as they are, and name the session id or the run ids next to each one, so I can find them in `bench/compare/` and `bench/runs/`.
The evidence from your reviews stays in `reviews/`, and here you point at it: name the round, such as `c2-review` Round 3, or the criterion, such as the `c1-skills` review's Wording and possible misreadings, so I can follow the trail.
The prose is yours.

Each section ends with a marker line.
Replace that line with your own writing; `uv run p3 check --final` fails while one is left.

Words used below.
**Your ratings** is the table `p3 report` prints from your major reviews, one row per criterion and one column per step, from 1 to 5.
A **round** is a quick round in one of your step files in `reviews/`, and its **What changed** is the change Claude Code made from your thoughts in it.
A **pass** is one revise-and-review iteration inside one of your tutor's review loops, so a loop capped at two passes reviews a draft at most twice.
A **tally** is the wins for each config and the ties in one blind comparison, and the **p-value** is the reveal's two-sided sign test on the picks that were not ties: with 10 such picks, 8 for one config is suggestive and 9 is strong.
**Could tell** is the share of pairs where you said you could tell which config made which.
The objective checks use the names `p3 report` prints, such as `teach_facts_correct`, `quiz_key_agreement`, `grade_false_wrong` and `tutor_leaks`, the README's section "The scenarios and the objective checks" lists them, and `guide/06-the-bench.html` ("The headline numbers") says what each one measures.
**Cost** is tokens, output tokens, minutes and subagents per scenario, and the list-price equivalent, which is not what you pay on a subscription.

---

## 1. The baseline, `c0-baseline`

Paste the `p3 report` table for `c0-baseline` (three full runs on the shared topic).

Runs: `bench/runs/c0-baseline/20261111-222758-agent-architecture-m30-r1`, `20261111-223425-agent-architecture-m30-r2` and `20261111-224024-agent-architecture-m30-r3` (the quick run `20261111-222137` is left out). Table from `uv run p3 report --configs c0-baseline`.

### Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

#### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.69 (0.65-0.77) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 (0.33-0.67) |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

#### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 556.7k (506.8k-615.3k) | 27.8k (25.7k-28.8k) | 2.8 (2.5-3.1) | 0 | 0.58 (0.54-0.61) |

#### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 146.5k (127.5k-174.7k) | 5.5k (4.4k-6.2k) | 0.8 (0.6-0.8) | 0 | 0.18 (0.16-0.19) |

#### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 267.8k (265.0k-271.0k) | 7.6k (7.4k-7.8k) | 0.9 (0.9-1.0) | 0 | 0.33 (0.32-0.34) |

#### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 520.2k (455.3k-613.9k) | 10.6k (9.7k-12.1k) | 1.6 (1.5-1.8) | 0 | 0.66 (0.63-0.70) |

#### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.49M (1.41M-1.63M) | 51.5k (49.2k-54.7k) | 6.2 (5.8-6.6) | 0 | 1.75 (1.70-1.83) |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

What did the baseline do well, and where did it fall short, for each of the four jobs?
Read its outputs as you will read your own steps', because your `c1-skills` review compares against it.
Which of the gaps in `KNOWN-GAPS.md` did you see in your own runs, and did you find one that is not listed?
Which number moved the most from one run to the next, and what does that spread mean for a step measured on a single run?

Lesson: The baseline had a relatively strong lesson that scored highly for teaching facts (1.00), and not as well for the length of the lesson (0.69). When reading the lessons they cover all of the steps that the student was looking for, what the context window is, how notes work between sessions, and how to retrieve information from manuals. The figures it creates are relatively strong and explain concepts well. I think the worked example sections should be less dense, because right now they are blocks of text, which is hard for the student to understand. 

Quiz: The quiz scored relatively strong, but the questions do not match the student's objectives as closely as I would like. For example, q3 of quiz 2 asks the user to determine, "Over 100 requests, how many more model calls does the agent make than the workflow?" This question is not really relevant for the user if they are just trying to understand the basics of the differences between the agent and the workflows.

Tutor: The tutor is missing a lot of the benchmarks. It is currently struggling with some of the guardrails, such as making sure to not reveal quiz answers to students for p01 in quiz 1, 2, and 3. The tutor begins by saying it cannot give out answers, but then gives an explanation that lets the student figure out the answer. However, the tutor did also answer most other questions thorougly with solid explanations.

Grading: The tutor's answers are a bit too blunt and cold. Starting grading off with "Right." or "Wrong." can make it difficult for the student to accept the criticism that the tutor has. I want to work on making the tutor warmer. Additionally, some of the explanations are a bit long, I would like to make the tutor be less verbose. However, the grading was always correct, as seen in 1.00 for verdict agreement and 1.00 for misconception hit. 

Known Gaps:
- The tutor narrows a quiz item down while refusing to answer it -> Present p01, p02
- The tutor answers above the learner's level -> Present p05
- Tutor replies run long -> Present
- Lessons come in short -> Present 0.65-0.77

New Known Gaps:
- The grading feedback feels cold.
- The worked examples in the lesson are dense.
- Some quiz items stray from the learner's goal.

Spread:
- Tutor behavior met -> 0.5, 0.67, 0.33
- Length ratio -> 0.77, 0.65, 0.67
- Tutor tokens -> 455k to 614k
- Teach tokens -> 507k to 615k

The number that moved the most was the tutor behavior met, it had significant variation in which probes were met versus unmet. I will have to be careful about mentioning specific changes to keep behavior more consistent. This means that a step measured from a single run may not be accurate, as some sections include significant variation.

---

## 2. Step 1: `c1-skills` against `c0-baseline`

### What changed

Name the rounds that built this step, such as `c1-skills` Rounds 1 to 4, and the inventory entries of the skills they added; the trail from thoughts to change to outcome is already in `reviews/` and `reviews/components.md`, so do not retell it here.
Then what you put in `PREFERENCES.md`, and anything about how the four skills work together that no single inventory entry says.

I had 5 rounds:
- Round 1 : Made the tutor skill -> tutor
  - Make sure the tutor does not give answers away.
- Round 2 : Made the quiz skill -> quiz
  - Remove questions that do not directly connect to the student's learning goals, breakdown quiz questions into knowledge-based and real world applications.
- Round 3 : Made the grade skill -> grade
  - Make grading feedback warmer and less verbose.
- Round 4 : Modified the teach skill -> teach
  - Make sure the lesosn doesn't use names, split worked examples into different sections, don't have overlapping ehadings for sections.
- Round 5 : Modified the tutor skill -> tutor
  - Make sure the tutor doesn't share internal thoughts.

Preferences: 
- Feedback: Tell plainly what was right and wrong.
- How to talk: Friendly and direct, ask questions.
- How long and dense: Short paragraphs, plain language, worked examples, bullets for explaning new processes
- Examples: Relate to CS, use plain english
- How to explain: Start with a general idea, then get more specific. Use real world examples, explain each new term as it appears, speak in plain language.

How the skills fit together:

The `tutor/CLAUDE.md` decides which skill will handle a request, it will then invoke the skill. Each skill uses its own `SKILL.md`, but they share information for the student's mission, preferences, etc. The skills build off of the artifacts of each other, with the quiz relying on the lesson, the grade relying on the quiz, etc.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,c1-skills`: the objective checks, the cost per job, and your ratings.

Runs: `c0-baseline` full runs `bench/runs/c0-baseline/20261111-222758-agent-architecture-m30-r1`, `20261111-223425-agent-architecture-m30-r2` and `20261111-224024-agent-architecture-m30-r3` (the quick run `20261111-222137` is left out); `c1-skills` full run `bench/runs/c1-skills/20261112-045303-agent-architecture-m30-r1`.

#### Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

##### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.69 (0.65-0.77) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.50 (0.33-0.67) |
| `c1-skills` | 1 | 1.00 | 0 | 0.73 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

##### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 556.7k (506.8k-615.3k) | 27.8k (25.7k-28.8k) | 2.8 (2.5-3.1) | 0 | 0.58 (0.54-0.61) |
| `c1-skills` | 1 | 511.6k | 24.6k | 2.5 | 0 | 0.59 |

##### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 146.5k (127.5k-174.7k) | 5.5k (4.4k-6.2k) | 0.8 (0.6-0.8) | 0 | 0.18 (0.16-0.19) |
| `c1-skills` | 1 | 128.4k | 6.7k | 1.0 | 0 | 0.19 |

##### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 267.8k (265.0k-271.0k) | 7.6k (7.4k-7.8k) | 0.9 (0.9-1.0) | 0 | 0.33 (0.32-0.34) |
| `c1-skills` | 1 | 249.3k | 6.7k | 0.8 | 0 | 0.30 |

##### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 520.2k (455.3k-613.9k) | 10.6k (9.7k-12.1k) | 1.6 (1.5-1.8) | 0 | 0.66 (0.63-0.70) |
| `c1-skills` | 1 | 412.9k | 6.8k | 1.2 | 0 | 0.51 |

##### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.49M (1.41M-1.63M) | 51.5k (49.2k-54.7k) | 6.2 (5.8-6.6) | 0 | 1.75 (1.70-1.83) |
| `c1-skills` | 1 | 1.30M | 44.7k | 5.5 | 0 | 1.59 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

#### Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | - | - | - |
| Lesson | Pedagogy | 3 | - | - | - |
| Lesson | Alignment with the learning goal | 4 | - | - | - |
| Lesson | Overall quality | 4 | - | - | - |
| Quiz | Difficulty | 5 | - | - | - |
| Quiz | Coverage of the lesson's core | 4 | - | - | - |
| Quiz | Wording and possible misreadings | 4 | - | - | - |
| Quiz | Writing quality | 4 | - | - | - |
| Quiz | Alignment with the learning goal | 4 | - | - | - |
| Feedback | Useful | 3 | - | - | - |
| Feedback | Explains enough | 3 | - | - | - |
| Feedback | Personalized to how I like things explained | 4 | - | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 5 | - | - | - |

### What the step bought and what it cost

For each job: what did your major review find against `c0-baseline`, and did the objective checks agree?
Where they disagree, which do you believe, and why?
`c1-skills` is also the first config with your `PREFERENCES.md`, while `c0-baseline` keeps the neutral one: which of the differences could come from your preferences rather than the skills?
What did the step cost per scenario, and was the gain worth it?
Say what one run of `c1-skills` against three of `c0-baseline` lets you claim, and what it does not.

Lesson: Overall my rating for the lessons was a low 4. My lessons improved in some ways but still contained a Known Gap. For example, the length of my lessons is still low (0.73). My lessons are more closely aligned with how I like to learn now, with how they use plain english and they organize sections. I also did not have any regression in how well my lessons covered the student's topics and the length ratio for the single run was better than 2 of the c0 runs. I also felt that the lessons needed more real world examples for me to follow them better, this is a change I plan to make in the next round. My rating agrees with the benchmark in that I think the length of the lesson should be improved, and that the lesson matches the student's objectives well. My rating disagrees with the benchmark in that I want the lesson to use more plain english and include real world examples, which is why my rating of the lesson is lower than the benchmark would imply.

Quiz: Overall my rating for the quiz was a solid 4. The benchmarks demonstrate the same scores for the key agreement (1.00) and the ambiguous items (0), as most of my changes were with how the quiz was organized and the types of questions that it asked. Based on the baseline quiz, I wanted the quizzes to be more closely aligned with the student's objectives. I feel like this was covered well as my score for Coverage was a 4 and my score for Alignment was a 4. Overall, I would say my quiz is well organized, is an appropriate difficulty, and creates questions that closely align with the student's objective. The main changes I would like to see are making sure all quiz questions are directly related to the objective, as I had 1 question that was difficult to follow and only tangentially related. My benchmark and scores agree that the quiz has key agreement and no ambiguous items. The scores disagree in that the benchmark implies the quiz is perfect, while I would like to see improvements to how closely the questions align with the students goal.

Grading: My overall rating for the grading is a 3. I believe that it regressed from the c0 baseline, because the explanations are now hard to follow. My goal was to make the explanations less verbose, but that has made it so the explanations are not descriptive enough regarding what the student did wrong. I want to find a balanace between not being too verbose, but still effectively telling the student what was right/wrong. Another change I made was having the grading be warmer, which I do think succeeded. My score and the benchmark agree that the verdicts were correct (1.00), that misconceptions were mentioned (1.00), and that there were no false wrong answers (0.00). However, the benchmark implies that the grading is complete, while I feel the need to do significant work to make sure the explanations the grader provides are thorough and tell the student what to work to improve.

Tutor: My overall score for the tutor was a high 4. I felt like the tutor performed quite well, I thought its explanations were thorough and warm, which is an improvement from the baseline where I felt the explanations were cold. The tutor's guardrails also improved, because for probes like p01 and p02, the tutor no longer gives the student the answer. I still have to improve probes liek p05, which is how the tutor handles questions that are outside the user's current scope. My scores and the benchmark agree that there are no leaks, and that the tutor's behavior improved (0.5->0.83, Guardrails: 4), and also agree that the tutor still has to improve in how it answers some questions (such as probe 5).

Preferences:
- Warmer grading -> A mix of the skill and `PREFERENCES.md`. In the `PREFERENCES.md`, I ask for feedback to be friendly and direct, and be given plainly. I think some of the improvement I saw was from this request, while the improvements I made to the individual skills helped to match more closely to what I was looking for.
- Plain english -> This is mainly from the `PREFERENCES.md`, I did not really touch this in any of the skills.

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.49M (1.41M-1.63M) | 51.5k (49.2k-54.7k) | 6.2 (5.8-6.6) | 0 | 1.75 (1.70-1.83) |
| `c1-skills` | 1 | 1.30M | 44.7k | 5.5 | 0 | 1.59 |

Overall, the number of tokens, output tokens, and minutes went down. I believe that this is mainly because I asked for answers to be less verbose. However, these improvements came at the cost of the tutor's feedback being more difficult to follow, so I do not think the gain is worth it.

As we are comparing one run of c1-skills against 3 runs of c0-baseline, and saw variation in the c0-baseline, there are some assumptions we can make and some we cannot. The main places where we saw spread were in the lesson length and the guardrails on the probes. For the lesson length, we cannot say that the lesson length improved, as c1-skills had a lesson length of 0.73, which is in the range that the 3 lessons for c0-baseline provided. However, we can say that the guardrails for the tutor improved, as the tutor's behavior improved from 0.33-0.67 to 0.83. As this is a significant improvement, and an explicit change that was made during the rounds, I can say that this improvement lets us claim that c1-skills performs better in this area.

---

## 3. Step 2: `c2-review` against `c1-skills`

### What changed

Name the rounds that built this step and the inventory entries of the reviewers they added, as in step 1.
Then the loops' design, for each of teach, quiz and grade: who reviews, what is on each reviewer's checklist and which items came from your `c1-skills` major review, how each reviewer gets a fresh context, how many passes a loop may run and what ends it early, and what each loop records.
Then one design choice you could have made the other way, such as one reviewer against several, a cap of one pass against three, or a reviewer that edits against one that only reports, and why you chose as you did.

TODO: the rounds and entries, and the design of your review loops.

### The loops as they ran

For teach, quiz and grade: how many review passes ran in your bench run, what the reviewers flagged, and whether the revisions moved anything you can point at, a fact corrected, an ambiguous item rewritten, feedback that changed.
The loop records in the run's outputs are the evidence; name the files.

TODO: what the review loops did in the run.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c1-skills,c2-review`.

TODO: paste the report tables.

### What the step bought and what it cost

Did the problems your `c1-skills` review found go away, and which ratings moved?
Which loop earned its cost and which did not?
If a loop ran several passes and the final output was no better than the first draft, say so, because that is the finding.

TODO: your judgment of step 2.

---

## 4. Step 3: `c3-split` against `c2-review`

### What changed

Name the rounds that built this step and the inventory entries of the pipeline's subagents.
Then the split: the roles you split the teach job into, what each one receives and returns, what runs in order and what in parallel, and who puts the lesson together at the end.
Why this split and not a smaller one, and what did you try that you took out again?

TODO: the rounds and entries, and the design of your teach split.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c2-review,c3-split`.

TODO: paste the report tables.

### What the step bought and what it cost

What did the split change in the lesson: its structure, its figures, its references, its fit to you, and how did your four Lesson ratings move against `c2-review`'s?
What did it cost in tokens, minutes and subagents against `c2-review`, and how much of that was overhead rather than writing?
Each step has one run, so say how confident you are, and what would change your mind.

TODO: your judgment of step 3.

---

## 5. `final` against `c0-baseline`, with repeats

### What went into `final`

A diagram of `final`: the main conversation, each skill, each subagent and the guard hook, with arrows for who starts whom and which files each one reads and writes.
ASCII art in a code block or a Mermaid block are both fine; for example:

```
/quiz (skill, main conversation)  writes drafts/0002.json
  -> quiz-reviewer (subagent, fresh context)  reads drafts/
  <- revise, at most 2 passes
  => quizzes/NNNN.json, keys/NNNN.json, review-records/NNNN-quiz.md
```

Draw yours, all four jobs, and delete the example.

TODO: your diagram.

What did you keep from each step, what did you drop, and why?
Point at the inventory entries in `reviews/components.md` rather than repeating them.
If `final` had to get cheaper tomorrow, which component would you cut first and which last, and what do you expect the tutor to lose?

TODO: what `final` is made of, and what you would cut first.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,final`, with three scored runs of each.

TODO: paste the report tables.

### What the repeats let you claim

For each headline number: is the difference between the two configs larger than the spread between runs of the same config?
Where the ranges overlap, say "not distinguishable with three runs", and do not rank the two by their means.
Then the overall cost: how many times more tokens and minutes per scenario does `final` take, and for which jobs is it worth it, by your review and by the numbers?

TODO: your reading of `final` against the baseline.

---

## 6. The ablation

Which component did `final-minus-<x>` remove, and what did you expect to happen before you ran it?
Paste `uv run p3 report --configs final,final-minus-<x>`.
What changed, in quality and in cost, and does one run against three let you say the component matters?
If you looked at its outputs, what did you see that the numbers do not show?

TODO: your ablation, its prediction, its table and your reading.

---

## 7. The guard

What does your guard block, and what does it allow, and how does it tell the grader from the main conversation?
Why is it a PreToolUse hook in `tutor/.claude/settings.json`, and not a permission deny rule, a hook in a subagent's frontmatter, a subagent's `tools` list, or an instruction in a skill?
What changed elsewhere in the tutor because of it, such as grading handed to a subagent the guard allows?
Paste the result of running its tests, and list the cases they cover: the main conversation reading `keys/` with each of Read, Grep, Glob, Bash and PowerShell, the grader reading them, and the reads that must still work.
Then the bench evidence that the hook runs in the bench and not only in its tests: the run id and scenario of a trace where it allowed the grader's read of `keys/` or blocked the main conversation's, since a hook that fails to start lets every call through.
Then `tutor_leaks` for `final` against `c0-baseline`, and any denial of the guard you found in a trace.
Last, the gap you know of: one way the main conversation could still reach a key, or a case your tests do not cover, and why you accepted it or how you closed it.

TODO: the guard, its tests and the evidence.

---

## 8. The blind comparison

### `c0-baseline` against `final`

Paste the reveals of the four sessions (teach, quiz, grade, tutor), three run pairs each, with their session ids.

TODO: paste the four reveals with their session ids.

### Your open reviews against your blind picks

This is the check on your own bias, as lecture 24 checks a model judge's.
For each job, what did your open reviews say about `final` against `c0-baseline`: your `final` major review, written before the blind comparison, your `c1-skills` review's comparison with the baseline, and your ratings across the ladder?
Then, for each job, did the blind tally and your reasons agree with them?
Where they disagree, what do you think happened: knowing the labels shaped what you saw in the open, the outputs you judged blind differed from the ones you reviewed, or the difference was too small to see?
Did your picks follow your open reviews more often in the pairs where you could tell than in the pairs where you could not?
Which do you believe now, and what does that say about the ratings in your reviews?

TODO: your open reviews against your blind picks.

### A second blind comparison

For 498E this is optional: if you made one, say which configs and job, why you chose it, paste its reveal, and say whether it agreed with your open reviews.
For 598E, and for the length-study stretch, the length study's three comparisons are your second; say so here and write them up in section 13.
If you made no second comparison, say so in one line.

TODO: your second blind comparison, or why there is none.

---

## 9. The test topics

### The two topics

Name each topic and its id, why you chose it, and the commit in which you committed its items, before its first run.
If you fixed a real mistake in a topic after its runs, as `bench/own/README.md` describes, list the run ids you deleted, what you changed and why.

TODO: your two topics and their commits.

### Results

For each topic, paste `uv run p3 report --topic <id> --configs c0-baseline,final`, and sum up your open review of the topic in `reviews/final.md` in two or three sentences.

TODO: paste the tables for both topics, with your summaries.

### Did the architecture still pay off?

Compare each topic with the shared topic: did `final` win where it won before, and did it fail somewhere new?
Was there anything about the topic, its kind of knowledge or its learner, that explains the difference?
On the life-skill topic, did both configs stay inside general knowledge when your probe asked for personal advice?

TODO: your reading of the test topics.

### Your learning sessions against the bench

Your three learning sessions are in `reviews/final.md`.
Did the bench predict what you saw in them?
Which failure from your sessions would a check or a review of a bench run have caught, and which could no fixed test have caught?
Would you use this tutor again for something you need to learn, and what would it need first?

TODO: the bench against your sessions.

---

## 10. The judge check

Take ten decisions the judge made: for example ten tutor replies it marked met or not met, or ten fact verdicts from your lessons (the judge checks six facts in each lesson on the shared topic, so ten come from two lessons).
Label each one yourself before you look at the judge's verdict, and list your ten labels and its ten verdicts here, with the run id and the scenario of each.
How many of ten did you agree on?
Read the disagreements: is the judge wrong, are you, or is the expected behavior unclear?
What does that agreement mean for the judge numbers you reported above?

TODO: your ten labels, the agreement, and what it means.

---

## 11. A change that did not pay off

At least one change, anywhere in the project, that cost you tokens, time or complexity and did not buy a difference you could see in your reviews or measure in the checks.
What was it, what did you expect, what did the evidence show, and what did you do about it?
Name the round or the inventory entry where it shows.

TODO: the change that did not pay off.

---

## 12. The trade-offs

Paste your ratings across the whole ladder, from `uv run p3 report --reviews`, and the cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

TODO: paste the ratings and cost tables for the whole ladder.

Looking at the whole ladder: which machinery paid for itself, which did not, and how do you know?
If you rebuilt this tutor for P4 with a third of the token budget, what would you keep?
Which number in this report do you trust least, your own ratings included, and why?

TODO: your trade-offs.

---

## 13. The stretch

For 598E this is the rider, and its write-up goes here, with `PREREG.md` beside it.
Cover five things:

1. the option's name;
2. what you did, and the files that hold it;
3. the evidence: the reviews, the blind comparisons, the objective checks and the cost it rests on, pasted or named;
4. what that evidence lets you claim, and what it does not;
5. one thing you would do next, and what result would tell you it worked.

TODO: your stretch.
