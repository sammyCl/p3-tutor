# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261112-045303-agent-architecture-m30-r1 - c1-skills snapshot

**My thoughts:**

Lesson:
- Explain why different functions would be used, not just what they do.
- Make sure to double check wording, there are times where some words were missed that led to ambiguity about what was being said.
- Make sure the lessons use real world examples that makes it easier for the student to understand why information is important, instead of just explaining the technical side. Add 1-2 sentences describing a real world example to each 
- Make sure to meet all of the expectations that a student has for a lesson. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, make sure to connect to that real world example.
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.
- Do not use abolutes without checking that they are still accurate statements.

Quizzes:
- Make sure that questions are not too long. The student shouldn't have to struggle to understand what the quiz question is asking for. If a question does have to be longer, utilize multiple paragraphs or bullet points.
- Make sure that quiz answers do not all start or end the same way. Include variation so it is not obvious which answer is correct.
- Explain what the misconception is along with the misconception numbers in the quiz answer keys, this will confuse the student on what is happening.
- Make sure quiz questions have strong connections to the objective, tangential connections should not count.
- Cross-reference against the lesson to make sure quiz questions do not overlap with the questions in the lesson.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

Tutor:
- If the student asks a question that is out of scope for what they are looking for, explain the topic briefly but suggest other ways to approach the problem that are more at their level.
- Do not suggest the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz thoughts asked for shorter stems, options that do not share an opening, misconceptions explained in words and not just by id, a direct tie to the objective and no overlap with the lesson's practice, so a quiz-reviewer with a check for each (under the five quiz criteria) reads the drafts in drafts/ with a fresh context, and the quiz skill now revises at most twice and writes review-records/NNNN-quiz.md.

### Round 2

**Run:** bench/runs/_live/20261115-231614-agent-architecture-m30-r1, a live run with --only quiz,grade-s1

**My thoughts:**

Lesson:
- Explain why different functions would be used, not just what they do.
- Make sure to double check wording, there are times where some words were missed that led to ambiguity about what was being said.
- Make sure the lessons use real world examples that makes it easier for the student to understand why information is important, instead of just explaining the technical side. Add 1-2 sentences describing a real world example to each 
- Make sure to meet all of the expectations that a student has for a lesson. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, make sure to connect to that real world example.
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.
- Do not use abolutes without checking that they are still accurate statements.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

Tutor:
- If the student asks a question that is out of scope for what they are looking for, explain the topic briefly but suggest other ways to approach the problem that are more at their level.
- Do not suggest the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.

What Remained:
- q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: The tutor thoughts asked for a brief explanation of an out-of-scope question followed by ways in at the learner's level, and for help that works from the learner's current setup instead of a different approach, so the tutor skill's section on questions above their level now covers both and a new section, "Work from their setup", asks for the smallest change to what they have.

### Round 3

**Run:** bench/runs/_live/20261115-233608-agent-architecture-m30-r1, a live run with --only tutor-p04,tutor-p05

**My thoughts:**

Lesson:
- Explain why different functions would be used, not just what they do.
- Make sure to double check wording, there are times where some words were missed that led to ambiguity about what was being said.
- Make sure the lessons use real world examples that makes it easier for the student to understand why information is important, instead of just explaining the technical side. Add 1-2 sentences describing a real world example to each 
- Make sure to meet all of the expectations that a student has for a lesson. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, make sure to connect to that real world example.
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.
- Do not use abolutes without checking that they are still accurate statements.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, explain the topic briefly but suggest other ways to approach the problem that are more at their level.
- Do not suggest the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-fact-checker.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson thoughts ask that absolutes be checked before they are used, and the c1 lesson review found self-contradictions and a sentence made wrong by one word, so a lesson-fact-checker with those checks, plus source-backed checks of every claim, date and citation, reads the draft in drafts/ with a fresh context, and the teach skill now revises at most twice, writes review-records/NNNN-lesson.md and writes the final lesson once.

### Round 4

**Run:** bench/runs/_live/20261115-234947-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

Lesson:
- Explain why different functions would be used, not just what they do.
- Make sure the lessons use real world examples that makes it easier for the student to understand why information is important, instead of just explaining the technical side. Add 1-2 sentences describing a real world example to each 
- Make sure to meet all of the expectations that a student has for a lesson. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, make sure to connect to that real world example.
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Do not use abolutes without checking that they are still accurate statements.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-pedagogy-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson thoughts ask for the why behind each function and a real-world example in every section, and the c1 pedagogy review (rated 3) found terminology-heavy sections with no real-world link, so a lesson-pedagogy-reviewer with those checks, plus plain-language terms, order, short stepwise paragraphs and doable practice from PREFERENCES.md, now reviews the draft beside the fact-checker in the teach skill's loop.

### Round 5

**Run:** bench/runs/_live/20261116-001705-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

Lesson:
- Make sure the lessons use real world examples that makes it easier for the student to understand why information is important, instead of just explaining the technical side. Add 1-2 sentences describing a real world example to each 
- Make sure to meet all of the expectations that a student has for a lesson. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, make sure to connect to that real world example.
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Does not use abolutes without checking that they are still accurate statements.
- Explains why different functions would be used, not just what they do.
- Utilizes more plain english, easier to follow.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-alignment-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson thoughts ask for real-world ties that show why the information matters and for the lesson to connect to the real-world situation whenever the learner asks for it, which the c1 alignment review also found missing, so a lesson-alignment-reviewer that gets the learner's request word for word checks every part of the request, a mission tie in every section, the objective's coverage, the learner's level and the promised win, beside the other two lesson reviewers.

### Round 6

**Run:** bench/runs/_live/20261116-010009-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

Lesson:
- Make sure the length of the lesson matches what the student wants, don't include the time for practice questions in this calculation.

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Does not use abolutes without checking that they are still accurate statements.
- Explains why different functions would be used, not just what they do.
- Utilizes more plain english, easier to follow.
- All of the expectations that a student has for a lesson are met. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, it connects to that real world example.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-quality-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson thoughts ask for a length that matches the request without counting practice time, which the c1 overall-quality review traced to practice being assumed to take longer than it does, so a lesson-quality-reviewer estimates each section's words against the requested minutes, flags practice minutes the words do not fill and says where to add teaching, with short checks on figures, references and whether the lesson reads as one piece; the teach skill now hands it the minutes and lets a length finding add content up to the budget.

### Round 7

**Run:** bench/runs/_live/20261116-012535-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

Feedback:
- The feedback is currently too short. The explanations are not long enough for the student to understand what is wrong. Find a balance between thoroughly explaining the answer without being verbose.
- Make the feedback warmer, make sure not to include filler or flattery, but make sure the student does not feel turned away by talking to you.

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Does not use abolutes without checking that they are still accurate statements.
- Explains why different functions would be used, not just what they do.
- Utilizes more plain english, easier to follow.
- All of the expectations that a student has for a lesson are met. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, it connects to that real world example.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: The feedback thoughts ask for feedback that explains enough without being verbose and is warmer without filler or flattery, and the c1 feedback review found a wrong item that never said why it was wrong and no item that said where to look, so a grade-reviewer with those checks, plus PREFERENCES.md fit and the summary, reads the draft grades in drafts/ with a fresh context, and the grade skill now revises at most twice, lets a too-short partial or wrong item run to about 90 words, writes review-records/NNNN-sN-grade.md and writes grades/ once.

### Round 8

**Run:** bench/runs/_live/20261116-033625-agent-architecture-m30-r1, a live run with --only grade-s1

**My thoughts:**

What Improved:
- Quiz keys now say what the misconceptions are.
- Answers beginnings and ends are now formatted differently.
- Questions are shorter or broken up into multiple bullet points so they are easier to follow.
- If the student asks a question that is out of scope for what they are looking for, the topic is explained briefly but suggests other ways to approach the problem that are more at their level.
- Does not suggest that the student approaches a problem in a completely different way, try to come up with a solution that matches their current setup.
- Double checks wording, there are times where some words were missed that led to ambiguity about what was being said.
- Does not use abolutes without checking that they are still accurate statements.
- Explains why different functions would be used, not just what they do.
- Utilizes more plain english, easier to follow.
- All of the expectations that a student has for a lesson are met. If they only want to understand the technical side that's fine, but if they specifically ask for how the technical side relates to a real world example, it connects to that real world example.
- The feedback is a more appropriate length, the explanations are long enough for the student to understand what is wrong without being too verbose.
- The feedback is warmer, and does not include filler or flattery.

What Remained:
- Quiz: q03 is now drifting a bit, it does not directly cover how to tell apart workflows and agents, or when to use a workflow over an agent.
- Tutor: don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: The tutor thoughts ask for no complicated math beyond the learner's scope, a simple explanation at their level, the reason it is out of reach, and other steps to take, so the tutor skill's section on questions above their level now forbids any formula, derivation or code there, asks it to name what the learner has not learned yet and whether the mission needs it, and to recommend concrete next steps at their level.

## Major review

**Run:** bench/runs/c2-review/20261116-191049-agent-architecture-m30-r1

**Live tries:**

Lesson:
- I found it interesting that my warm-up question focused on pandas instead of something history related, as that was what the lesson was about. 
- Does a good job of breaking timelines down into bullet points, making it easier for the user to follow.
- Uses sources other than Anthropic sources, which is good given that previous quizzes have heavily relied on Anthropic sources.
- Figures are well laid out, and add something to the lesson. They make it easier for the user to follow ideas. The explanations of what the figures are are also well done and help to understand what the figure represents.
- Lesson is easy to follow and uses plain english, this makes it so the lesson is friendly to students just learning what the lesson is about.
- Knowledge checks are strongly connected to the sections they are attached to.
- Overall, lesson is at an appropriate level and length for the student, explains the topic well, and does a good job making sure the student is following through knowledge checks.

Tutor:
- Did a good job of following the `PREFERENCES.md`. The output was warm but direct, and organized a timeline in bullet points so it was easier to follow. The tutor also explained the topic in computer science terms, and asked a question to check my understanding, which were also listed as my preferences.
- The tutor keeps explanations to an appropriate length. It explains main ideas without overloading the student with information.
- Corrects the student's understanding well, still comes off as warm.

Quiz:
- Quiz questions are directly related to the lesson without having questions that overlap with Knowledge Checks within the lesson.
- Listed quiz answers are logical, there are not obviously wrong answers.
- Has interesting connections to real-world scenerios. q5 describes a theoretical social media post where a someone compares a scenerio to a topic described in the lesson. It is a creative comparison.

Feedback:
- Feedback is direct, but still warm. It is relatively thorough, and does a good job of explaining the user's misconceptions.
- Has a thorough summary of the results of the quiz, and what was done well, and what should be reviewed.

Concern: The lesson, feeback, and quiz took longer to generate. This makes sense as they go through subagent reviews, however it makes me worry that in the future it may take too long to generate the lesson and quiz.

### Lesson

#### Technical correctness and facts

Rating: 5

I am much happier with the technical correctness and facts following the addition of the `lesson-fact-reviewer`. The benchmark still reports that the `teach_facts_correct` is 1.00, indicating that the technical facts that the benchmark is looking for are correct. This has not changed from c1-skills. In c1-skills, I experienced issues where information was ambiguous because it was missing words, or slightly incorrect. When reviewing the lesson, I was able to see the changes that the `lesson-fact-reviewer` made, and I got to see first hand the improvements that were made to clarify ambiguous wording, and keep information consistent throughout the lesson. For example, in this statement where () represent what was removed and [] represent what was added, "Nothing is (remembered) [available to the model] unless it is in the text sent this time. This is why [each step of] the [agent] loop (you learned earlier) is a (series of) separate model (calls,) [call,] and it is the key to everything else in this lesson.", producing a more thorough and complete answer. During my review of the Major Review lesson, nothing stood out to me as incorrect, contradictory, etc.

#### Pedagogy

Rating: 4

The `lesson-pedagogy-reviewer` did a good job of suggesting edits that made the lesson easier to read. Since it reworded elements to have more explanation, be in plain english, took out unnecessary information, and added some real world examples, the lesson was a lot easier to follow. The lesson also contains strong practice questions that directly relate to the sections they are in. This showed significant improvement over c1-skills. However, I still feel that there are some areas where the pedagogy could be improved. For example, the transitions between sections could be smoother. There are some transitions, like "What the model sees on every call" and "Why a long context costs money and accuracy" that are clear, but others, like "Why a long context costs money and accuracy" to "Notes that outlive the session" have harsher transitions. Improving these transitions will make the flow even smoother.

Examples:
- "you, like an HTTP request with no cookie, which must carry everything the server needs." to "you."
- Adding sentences like, "It suits notes the model should decide to write itself."

#### Alignment with the learning goal

Rating: 5

The `lesson-alignment-reviewer` did a good job of recommending changes so the lesson covered both the technical topics that the student was interested in, and the applications of these topics. The main alignment problem I had with `c1-skills` was that when the student wanted to learn about context, memory between sessions, and how to access information about manuals, in relation to how these can be used in a makerspace assistant, the lesson did not address which sections were relevant to a makerspace assistant. With the `lesson-alignment-reviewer`, applications that are relevant to the makerspace assistant have been added, such as the addition of "The booking itself, so copying it into notes adds nothing. The preference is a durable fact that no other store holds. Keep it minimal.". Additionally, the judge said that the lesson was at an appropriate level for the student, and mentions the makerspace project throughout it. The judge did mention that the lesson may be dense, but I disagree with this assessment as I felt like the definitions that were provided still made it easy to follow.

#### Overall quality

Rating: 4

Overall this was a large improvement from `c1-skills`. The `lesson-quality-reviewer` did a good job of suggesting edits to the document that kept it simple to read. The figures of the lesson were still easy to follow, and had good explanations of what each figure represented. The references made contextual sense, and none of the links were broken. The website is also easy to navigate, and has appropriate interactions for the questions. From `c1-skills`, I have seen improvements in how the lesson now incorporates real world examples and making sure to utilize plain english throughout the document. The length of the lesson also appears to have improved from 0.728, as this one had a length ratio of 0.844. The main changes I would like to see in the future are improving the length ratio further, and making sure that the lesson recommends resources other than Anthropic pages, that way the student has a chance to learn from a variety of resources. 

Examples:
- "code" to "code in several languages"
- Adding the clarifying statement, "(how reliably the model finds a fact you put in)"

### Quiz

#### Difficulty

Rating: 5

The quiz is an appropriate level for the student. It has a good mix of conceptual questions that the user may be told in the lesson, q1, q3, q4, and real-world questions which require the user to apply their knowledge, q2, q5, q6. The incorrect answers also help to reveal key misconceptions that the student may have if they choose those answers. For example, in the q1 answer key, "Option a is the misconception that a workflow cannot contain a model call (it can, at fixed steps)". These are very believable misconceptions that the student may have, so including them makes the quiz difficult, without being impossible for someone just learning to understand.

#### Coverage of the lesson's core

Rating: 5

The main objectives for the lesson were to determine the differences between agents and workflows. The core points of the lesson for 04 are to know the differences between a workflow and an agent, the benefits and costs of using an agent, and when a workflow is the better choice. 

- Differences between a workflow and agent: q1, q2, 
- Benefits of an agent: q3, q6
- Costs of an agent: q4, q5 
- When a workflow is a better choice: q4, q5

As all of the objectives are covered by at least one question from the quiz, with multiple being covered by 2, we can conclude that there are no coverage gaps of the lesson's core.

#### Wording and possible misreadings

Rating: 4

Overall the wording of the quiz has improved from `c1-skills`. The questions were clear, especially with how questions with multiple steps, like q2, are now separated into bullet points. This makes it much easier for the student to follow and understand the process. I also appreciate how the answers for the questions no longer have multiple possible answers starting the same way. This is a significant improvement over what happened in `c1-skills`, where a question had 3 answers starting with "An agent...", making it clear what the correct answer was. I think a good next step would be to prevent run-on sentences, as some questions, such as q6, have run-on sentences that are a bit difficult to follow. 

#### Writing quality

Rating: 4

Overall I saw significant improvement in the writing quality compared to `c1-skills`. One of the points I had brought up was that processes should be split up into bullet points, and this is present in q2. I also think the key's rationale improved, as they directly define what each misconception means and how it occurs, such as "Option d is the misconception that workflows never call tools (M8)". However, there are still some questions, like q5, that define a process that is not properly put into bullet points. I think making this a more explicit requirement would make it easier for the user to follow in the future.

#### Alignment with the learning goal

Rating: 5

I feel that all of the quiz questions directly connect to the objective. This quiz aims to test that a student can determine the difference between agents and workflows, and when to use one over the other. All of the quiz questions fall into one of these categories, q1 and q2 determine differences between agents and workflows, while q3, q4, q5, and q6 have the user determine if an agent or a workflow is better for a problem. I feel that all of the quiz questions directly address these topics, which is an improvement over `c1-skills`, where there were some quiz questions that were only tangentially related to the lesson.

### Feedback

#### Useful

Rating: 4

The explanations have improved quite a bit from `c1-skills`. The explanations are much more thorough now, and actually provide useful feedback when a user selects an incorrect answer. For example, q2's feedback was, "You pictured the model reading the calendar itself, a reasonable guess. But the model only takes in text and writes out text, with no link to your booking system. It writes something like check_calendar("laser cutter", "tomorrow") as a request, and the program, as in your Python classes, does the actual call. Who runs check_calendar after that, the model or the program?" I like how the feedback addresses the misconception that the user had, and then asks them to think from another perspective. This actually makes the feedback actionable, and gives the user a better understanding of how to improve. I think for future runs, I want to add more of an explanation for why a user's answer is correct. For example q1's feedback is only two sentences, where the first sentence just repeats the answer the user selected.

#### Explains enough

Rating: 3

The explanations are now much more thorough. They give the user a much better understanding of why their answer is incorrect. For example, the feedback for q4 says, "You pictured one call where the model runs all three tools, but the program runs them. A model call ends after one request, so the model is called again to see each result:
- Call 1: question in, asks for check_calendar
- Call 2: calendar result in, asks for search_manuals
- Call 3: manual result in, asks for check_training_record
- Call 4: training result in, writes the answer
Next time, label each step 'model call' or 'program runs tool' and count only the first kind." The explanation addresses:

1. What the student assumed
2. How to correctly approach the problem
3. How the student should change their perspective in the future.

By combining these three aspects to the feedback, the student is able to gain a much better understanding of why their approach was incorrect, and what to do differently in the future.

What I would like to see improved is the explanations for when the student gets a correct answer. For example, for q5 the feedback was, "You said the result goes back in as the next input, so the model can decide its next step. You covered both what happens and why.". This explanation says that the student was correct, but does not describe why they are correct. I would like to see this improved in the future.

#### Personalized to how I like things explained

Rating: 4

The feedback is warm and direct, which are two key aspects I described in my `PREFERENCES.md`. I also noticed that the feedback is provided in bullet point form for some questions, like q4, this makes the feedback a lot easier to follow and understand. I think the `grade-reviewer` is doing a good job of helping to match the feedback to my `PREFERENCES.md`, as it makes changes to make the feedback friendlier, as evidenced by: "softened the first sentence to "the loop's shape" and added that the program runs every tool and that descriptions guide the model.". It also works to write explanations in plain english, as requested by my `PREFERENCES.md`, "q3: states the misconception in plain words -> "an agent needs no stopping condition because more tries will eventually work"".

There aren't many more changes that I would like to see with the feedback, but I would like the explanations to follow my `PREFERENCES.md` request of starting with a general idea, and then getting into more specific examples.

### Compared with the previous step

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

In terms of the numbers, we saw changes to:
- all jobs : 1.30M -> 5.08M
- minutes (all jobs) : 5.5 -> 17.3
    - teach : 2.5 -> 8.1
    - quiz : 1.0 -> 3.8
    - grade : 0.8 -> 3.9
    - tutor : 1.2 -> 1.6
- subagents spawned : 0 -> 14 (teach 8, quiz 2, grade 4)
- list-price cost : $1.59 -> $4.53

Scores:
- Technical correctness: 4 -> 5
- Pedagogy: 3 -> 4
- Quiz alignment: 4 -> 5
- Quiz coverage: 4 -> 5
- Useful: 3 -> 4

All other scores remained the same.

### What the next step should fix

Lesson:
- Make transitions between sections smoother, make sure that each section begins by connecting to the previous section. This will help the student understand how sections connect together. 
- Match the requested length of the lesson better, if a student requests a 30 minute lesson, make sure the lesson is actually 30 minutes.
- Make sure to use sources from more than one source. Students may want to have explanations provided in different formats, so having a variety of sources will help the student follow better.

Quiz:
- Avoid long, run-on sentences, such as q6, it makes it difficult for the student to follow.
- Make sure processes are put into lists, like q2 does, put as an explicit requirement.

Feedback:
- Explain why a correct answer is correct, don't just repeat the correct answer. For example, s1 q1's feedback is two sentences where the first sentence just repeats the answer. s2 q5's feedback says "You covered both what happens and why" without giving the why.
- Have explanations start from a general idea, and then get more specific, while still staying direct.

Tutor: 
- don't include complicated math if it is outside the user's scope. Stick to simple explanations that are at the users level, and explain why it is outside of the user's current reach. Instead recommend other steps that the user can take.
