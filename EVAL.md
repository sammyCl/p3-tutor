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

I had 8 quick rounds:
- Round 1: Created the quiz reviewer
  - Quiz questions use shorter sentences, possible answers should not share the same start and end, misconceptions in the answer key should be explained instead of just being "M8", questions must directly tie to the lesson objectives and not overlap with the lesson's practice. The reviewer performs 2 passes.
- Round 2: Edited the tutor skill
  - Directed the tutor on how to handle out of scope questions, give a brief explanation of the topic at the user's level, what options the user has at their current level, and makes sure that the user is not instructed to redo their entire plan.
- Round 3: Created the lesson fact reviewer
  - Reviews the facts within the lesson to make sure that absolutes are correct for every scenerio, that there are no self-contradictions within the lesson, and that there are no missing words that leave ambiguous or different meanings to sentences. The reviewer performs 2 passes.
- Round 4: Created the lesson pedagogy reviewer
  - Reviews the lesson to make sure there are real-world examples in each section, especially sections that are in terminology-heavy sections. Also makes sure that the `PREFERENCES.md` is followed by using plain language and short stepwise paragraphs. The reviewer performs 2 passes.
- Round 5: Created the lesson alignment reviewer
  - Makes sure that all parts of the lesson's objectives are addressed, if the user requests a specific scenerio to apply the conceptual knowledge to, makes sure that that scenerio is found throughout the lesson so the user knows how the knowledge can be applied to it. Also verifies that the lesson is at the user's level. The reviewer performs 2 passes.
- Round 6: Created the lesson quality reviewer
  - Verifies that the length of the lesson is close to what is requested, flags areas where further explanation is required, reviews figures to check their accuracy, makes sure references are logical, and makes sure the lesson reads as one piece. The reviewer performs 2 passes.
- Round 7: Created the feedback reviewer
  - Makes sure that explanations match the `PREFERENCES.md`, being warm without filler or flattery, and direct. Also verifies that explanations contain descriptions of why an answer is incorrect and where to look to better understand the correct answer. The reviwer performs 2 passes.
- Round 8: Edits to the tutor skill
  - Makes sure that for questions outside of the user's scope, complicated math is not used. 

Design of Each Reviwer:
- lesson reviewers:
  - lesson-fact-reviewer: Checks a lesson draft for technical correctness and facts.
    - Checklist:
      - Checks that every factual claim is correct, as stated, verified by a high-trust source.
      - Makes sure every absolute is true as stated.
        - Taken from `c1-skills`
      - Does the lesson agree with itself?
      - Are all statements worded precisely enough to be correct?
        - Taken from `c1-skills`
      - Is anything out of date?
      - Does each citation exist and say what the lesson attributes to it?
      - Does the lesson state or imply a common misconception as if it were true?
  - lesson-alignment-reviewer: Checks that the lesson covers the user's description of what they want to learn and why they want to learn it.
    - Checklist:
      - Is every part of the request met?
        - Taken from `c1-skills`
      - Does every main section tie its idea to the learner's own situation from the `MISSION.md`?
        - Taken from `c1-skills`
      - Does the lesson teach every part of the objective's text?
        - Taken from `c1-skills`
      - Is the lesson pitches at this learner's level?
      - Is the win the opening promises delivered?
      - Do the practice tasks and the worked example ask about the objective set in the learner's own situation?
        - Taken from `c1-skills`
  - lesson-pedagogy-reviewer: Reviews how the lesson is teaching, makes sure that it matches the `PREFERENCES.md`, such as making sure that real-world examples are provided throughout the lesson.
    - Checklist:
      - Why, not only what: does every tool, technique, etc, that the lesson discusses say when and why would use it?
        - Taken from `c1-skills`
      - A real example in every section
        - Taken from `c1-skills`
      - Big picture, then specifics 
        - Taken from `c1-skills`
      - Terms in plain language
        - Taken from `c1-skills`
      - Order and pacing
      - Short and stepwise
        - Taken from `c1-skills`
      - Recall and practice the learner can really do
  - lesson-quality-reviewer: An overall review of, does the lesson match what the learner wants? Is the lesson easy to follow, is it the length they ask for?
    - Checklist:
      - Does the lesson fill the time asked for?
        - Taken from `c1-skills`
      - Does any section claim minutes for practice that its words do not fill?
        - Taken from `c1-skills`
      - Where should the missing minutes go?
      - Does each figure earn its place?
      - Are the references worth following?
      - Does the lesson read as one piece?
      - Taken as a whole, would a user want to learn from the lesson?
  - How the Reviewers Run:
    - There are at most 2 passes of each reviwer, and the reviewers may stop early if no Findings are registered in the first pass.
    - On each pass the skill will:
      - Launch the 4 reviewers using the Agent tool.
      - Collect the reviewer's reports.
      - Make changes to the lesson based on the reports.
      - Repeat the loop as needed
      - Each loop will record every finding in a new draft, and record what changes were made to the lesson.
        - `review-records/NNNN-lesson.md`
    - Each pass will launch 4 new subagents, which is how each reviewer will have a fresh context.

- quiz-reviewer: Reviews the draft for a quiz, and suggests changes to make sure the quiz covers all requested topics, 
  - Checklist:
    - Is every item answerable by this learner after the lesson?
    - Do one or two items stretch the learner?
    - Does each wrong option tempt someone who holds a real misconception?
    - Do the items together cover the core ideas of the objective?
    - Does any item test a side detail instead of the core?
      - Taken from `c1-skills`
    - When a lesson exists, does any item repeat or closely copy one of the lesson's practice questions?
      - Taken from `c1-skills`
    - Is every stem short enough to take in at one reading?
      - Taken from `c1-skills`
    - Within each mcq item, do the options start and end in varied ways?
      - Taken from `c1-skills`
    - Does every item that asks for "best", "better" or "most" choice say best for what?
    - Does each item have exactly one defensible answer?
    - Does any item give away the answer to another item?
    - Are stems and options clear, concise and correct, in plain language with no double negatives?
      - Taken from `c1-skills`
    - Does rationale say why the answer is right and why the typical wrong answers are wrong, in a way a learner can learn from?
      - Taken from `c1-skills`
    - Whenever the key maps a wrong option to a misconception id, does the rationale also say in words what that misconception is?
      - Taken from `c1-skills`
    - Do the quiz and keys follow `FORMATS.md`?
    - Does every item test the objective it is tagged with directly, not through a loose or tangential link?
      - Taken from `c1-skills`
    - Does each applying item put the learner in a situation for thier mission?
      - Taken from `c1-skills`
  - How the Reviewer Runs:
    - There are at most 2 passes of each reviewer, and the reviewers may stop early if no Findings are registered in the first pass.
    - On each pass the skill will:
      - Launch the reviewer using the Agent tool.
      - Collect the reviewer's report.
      - Make changes to the quiz based on the report.
      - Repeat the loop as needed
      - Each loop will record every finding in a new draft, and record what changes were made to the quiz.
        - `review-records/NNNN-quiz.md`
    - Each pass will launch a new subagent, which is how each reviewer will have a fresh context.

- grade-reviewer: Reviews the draft of the feedback given to the user, makes sure the explanations and summary meet expectations and the `PREFERENCES.md`.
  - Checklist:
    - Explains why, not only what for every partial and wrong item.
      - Taken from `c1-skills`
    - A next step on every item that needs one.
      - Taken from `c1-skills`
    - Right answers are explained
      - Taken from `c1-skills`
    - Explanations are long enough, but not verbose
      - Taken from `c1-skills`
    - Explanations are warm without filler or flattery
      - Taken from `c1-skills`
    - Explanations fit `PREFERENCES.md`
    - Explanations are consistend and correct
    - The summary names what the user has correct, what to work on and why it matters, and gives a concrete next step.
- How the Reviewer Runs:
  - There are at most 2 passes of each reviewer, and the reviewers may stop early if no Findings are registered in the first pass.
  - On each pass the skill will:
    - Launch the reviewer using the Agent tool.
    - Collect the reviewer's report.
    - Make changes to the feedback based on the report.
    - Repeat the loop as needed
    - Each loop will record every finding in a new draft, and record what changes were made to the feedback.
      - `review-records/NNNN-sN-grade.md`
  - Each pass will launch a new subagent, which is how each reviewer will have a fresh context.

One decision that was made:

I chose to split the lesson-reviewer into 4 different reviewers. This is because the lesson is the longest output generated by the tutor. I was worried that if I gave all of the review jobs to one reviewer, the reviewer would not be as effective at identifying all of the issues. Additionally, it allows for each reviewer to specialize in one area, making its feedback more effective. 

This decision does come at a cost, because each subagent requires tokens to launch. As a result, I am using more tokens with 4 subagents than I would be by only implementing 1 reviewer.

### The loops as they ran

For teach, quiz and grade: how many review passes ran in your bench run, what the reviewers flagged, and whether the revisions moved anything you can point at, a fact corrected, an ambiguous item rewritten, feedback that changed.
The loop records in the run's outputs are the evidence; name the files.

For the bench run, `bench/runs/c2-review/20261116-191049-agent-architecture-m30-r1.`, each loop ran 2 passes and stopped at the cap.

The reviewers flagged the following:
- lesson reviewer
  - Records stored in: `teach/outputs/review-records/0001-lesson.md`
  - lesson-fact-checker : 7 findings in pass 1, 7 findings in pass 2, 
    - Examples of findings:
      - "F1 retrieval failure rate unit: qualified to "top-20 retrieval failure"."
      - "F2 stateless absolute and "your program runs the tool": qualified to "by default" and "a tool you define yourself"."
    - Examples of changes: Added, "When a student asks about acrylic settings, the assistant should pull up the one relevant manual page, not paste all 60 pages. "
  - lesson-pedagogy-reviewer : 18 findings in pass 1, 11 findings in pass 2
    - Example of findings: "P1: section "What the model sees on every call": "The context window is the most text the model can look at in one call" is explained, but the section never says what to do when the window is too small or too large for a given job. Fix: add one sentence, such as "Pick what goes in, because the window is a limit and you pay for every token in it.""
    - Example of changes: Added, "Recall, then check Why is the manual chunked before it is searched, instead of searching whole manuals? Check your answer The point is to bring only a few hundred tokens of the right passage into the context. A whole manual would be too big, would cost on every call, and could bury the answer."
  - lesson-alignment-reviewer : 9 findings in pass 1, 4 findings in pass 2
    - Example of findings: 
    "A1: The topic and the learner-fit are met. I found two gaps.
      Length: the section times are 2, 5, 5, 5, 6, 5, 6, 4 and 2 minutes, which adds up to 40 minutes before the checks and reading. This is more than the requested 30. Fix: cut the trim section and the "When you can skip it" subsection down, or drop the stated section times.
      Fit to the learner: the lesson is anchored in the makerspace assistant almost throughout, so I count this as met. The one exception is the sub-agent point, covered under A3."
    - Example of changes: Changed, "One short note, such as "booked laser Friday 2 pm". The retrieved chunks and the calendar listing are dropped, since they can be fetched again." to "A short note, "prefers afternoon slots". The calendar already holds the booking itself, so copying it into notes adds nothing. The preference is a durable fact that no other store holds. Keep it minimal."
  - lesson-quality-reviewer : 11 findings in pass 1, 7 findings in pass 2
    - Example of findings:
      "Q3: The lesson is slightly short (about 420 words). Put the words where the practice is thinnest, and add no padding.
      Worked example: add a sixth decision. For instance, the student's manual is about 24,000 tokens, so should it be pasted or retrieved? Work through the cost arithmetic from the cost section. This ties the cost section to the example, and the example currently never uses it.
      Your turn: it gives only one line of "Given" and four prompts. Add a worked partial answer, or a second contrast, such as a request where the notes are missing or wrong. About 150 words would do.
      "Three ways to keep a long run": the section has no example of what summarizing or a sub-agent returns. Add a short before-and-after of one clearing or compaction on the booking request, about 100 words."
    - Example of changes: Adding "(how reliably the model finds a fact you put in)" to "As the token count grows, accuracy and recall (how reliably the model finds a fact you put in) degrade, an effect called context rot (Claude docs)."

- quiz-reviewer
  - Records stored in: `quiz/outputs/review-records/0002-quiz.md`
  - 11 findings in pass 1 and 11 findings in pass 2
  - Examples of findings:
    - "1b, 2a q1-q6: all recognition items, ideas overlapped -> replaced the cost-pair q3 with "what an agent buys in return"; q6 kept as the open-case stretch"
    - "1c q1-q3: weak distractors -> rewrote q1 and q3 options as named misconceptions"
  - Example of changes: Rewrote q2 to have numberes steps.

- grade-reviewer
  - Records stored in: `grade-s1/outputs/review-records/0001-s1-grade.md` and `grade-s2/outputs/review-records/0001-s2-grade.md`
  - 15 findings in pass 1 and 11 findings in pass 2 for s1
  - 8 findings in pass 1 and 7 findings in pass 2 for s2
  - Examples of findings:
    - "G2 q2, q4, q6: added next steps -> a question for q2, "label each step", "sketch in Python""
    - "G7 q6: said the first half matches the key"
    - "G4 q1, q2, q5: cut cross-references and extra clauses to fit the limit for correct items."
    - "G8: softened the first sentence to "the loop's shape" and added that the program runs every tool and that descriptions guide the model."
  - Example of changes: "Why" steps were added to wrong items.


### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c1-skills,c2-review`.

Runs: `c1-skills` full run `bench/runs/c1-skills/20261112-045303-agent-architecture-m30-r1`; `c2-review` full run `bench/runs/c2-review/20261116-191049-agent-architecture-m30-r1`. Table from `uv run p3 report --configs c1-skills,c2-review`.

#### Results on agent-architecture

Scored full runs (quick runs and --only runs left out); each cell is the mean over the runs, with the range in brackets.

##### Quality

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 1.00 | 0 | 0.73 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `c2-review` | 1 | 1.00 | 0 | 0.84 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |

Teach facts, key agreement, verdict agreement, false wrong, misconception hit and behavior met are shares (0 to 1); misconceptions, dead links, wrong keys, ambiguous items and leaks are counts per run.
A dash means no run could be scored on that check, and n= says how many of the runs could.
A job that failed counts against the config: no lesson scores 0 teach facts, no quiz and key 0 key agreement, a missing grades file disagrees on every item, and a tutor scenario with no reply is not met; leaks need a reply to check, so such a scenario is left out of them.
The length ratio is a rough reading-time estimate (visible words / 150) over the minutes requested; 0.6 to 1.5 counts as on length.

##### Cost: teach

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 511.6k | 24.6k | 2.5 | 0 | 0.59 |
| `c2-review` | 1 | 3.01M | 113.0k | 8.1 | 8 | 2.59 |

##### Cost: quiz

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 128.4k | 6.7k | 1.0 | 0 | 0.19 |
| `c2-review` | 1 | 764.6k | 28.8k | 3.8 | 2 | 0.63 |

##### Cost: grade

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 249.3k | 6.7k | 0.8 | 0 | 0.30 |
| `c2-review` | 1 | 810.7k | 30.3k | 3.9 | 4 | 0.75 |

##### Cost: tutor

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 412.9k | 6.8k | 1.2 | 0 | 0.51 |
| `c2-review` | 1 | 490.8k | 7.3k | 1.6 | 0 | 0.57 |

##### Cost: all jobs

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 1.30M | 44.7k | 5.5 | 0 | 1.59 |
| `c2-review` | 1 | 5.08M | 179.3k | 17.3 | 14 | 4.53 |

Costs are per run, summed over the job's scenarios; list-price $ is the list-price equivalent, not what you pay on a subscription.

#### Your ratings

Your ratings from 1 to 5 in the major reviews (reviews/<step>.md), which review full runs on the shared topic; a dash means no rating there yet, one that p3 check does not accept, or a job that step does not review (Tutor in c2-review; Quiz, Feedback and Tutor in c3-split).

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | 5 | - | - |
| Lesson | Pedagogy | 3 | 4 | - | - |
| Lesson | Alignment with the learning goal | 4 | 5 | - | - |
| Lesson | Overall quality | 4 | 4 | - | - |
| Quiz | Difficulty | 5 | 5 | - | - |
| Quiz | Coverage of the lesson's core | 4 | 5 | - | - |
| Quiz | Wording and possible misreadings | 4 | 4 | - | - |
| Quiz | Writing quality | 4 | 4 | - | - |
| Quiz | Alignment with the learning goal | 4 | 5 | - | - |
| Feedback | Useful | 3 | 4 | - | - |
| Feedback | Explains enough | 3 | 3 | - | - |
| Feedback | Personalized to how I like things explained | 4 | 4 | - | - |
| Tutor | Guardrails | 4 | - | - | - |
| Tutor | Personalization | 5 | - | - | - |

### What the step bought and what it cost

Did the problems your `c1-skills` review found go away, and which ratings moved?
Which loop earned its cost and which did not?
If a loop ran several passes and the final output was no better than the first draft, say so, because that is the finding.

There were problems from `c1-skills` that went away:

Quiz:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- Quiz questions are more tighlty tied to the objective.

Tutor:
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.

Lesson:
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Does not use abolutes without checking that they are still accurate statements.
- Explains why different functions would be used, not just what they do.
- Utilizes more plain english, easier to follow.
- All of the expectations that a student has for a lesson are met. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, it connects to that real world example.

Feedback:
- The feedback is a more appropriate length, the explanations for incorrect answers are long enough for the student to understand what is wrong without being too verbose.
- The feedback is warmer, and does not include filler or flattery.

The following scores improved:
- Technical correctness: 4 -> 5
- Pedagogy: 3 -> 4
- Quiz alignment: 4 -> 5
- Quiz coverage: 4 -> 5
- Useful: 3 -> 4

However, the token counts and amount of time to complete each task increased significantly. The number of tokens increased from 1.30M to 5.08M, and the minutes increased from 5.5 to 17.3. The only benchmark score that increased was the length ratio of the lesson, 0.73 to 0.84. This is because most of my benchmark scores were already at the maximum, with the lesson ratio and tutor behavior being the exceptions. These questions bring into question whether the changes from the reviewer were worth it. I would argue that despite the benchmark not increasing significantly, the changes that were experienced in my scoring of the different attributes demonstrates that the addition of the reviewers made a significant difference in the final products of the different skills. The lesson, quiz, and feedback all experienced massive improvements as a result of their reviewers. As a result, despite the significant increase in time and tokens, I would argue that it makes sense to keep the reviewers in the process.  

The teach loop went from 0.51M to 3.01M tokens, with Technical 4->5, Pedagogy 3->4, and Alignment 4->5 improving. 

The quiz loop went from 0.13M to 0.76M tokens, with Coverage 4→5 and Alignment 4→5 improving.

The grade loop went from 0.25M to 0.81M tokens, with Useful 3→4 improving. 

I believe that all of the loops have proven their worth. The teach loop is made of 4 reviewers, one for technical facts, which showed improvment, pedagogy, which showed improvement, alignment, which showed improvement, and quality, which remained the same. With each reviewer resulting in improvements, it is clear that the teach loop is worth the cost, even though the cost is significantly larger then for the other loops. It makes sense that quality remained the same, as it already had a score of 4, and it was a case of more small issues showing up. The quiz reviewer resulted improvement in coverage and alignment. The grade reviewer only showed improvement in one score, however, it was also a massive improvement compared to the previous score. A 3->4 jump is much more significant than a 4->5 jump, as it demonstrates that the category is now only experiencing minor issues instead of containing significant issues. As a result, I consider it to be appropariate to keep the grade reviewer.

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
