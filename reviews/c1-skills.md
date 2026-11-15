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

**Run:** bench/runs/c1-skills/20261112-045303-agent-architecture-m30-r1

**Live tries:**

I began by asking the tutor to make a lesson about the basics of pandas. After reading through the lesson, I asked a question to the tutor to evaluate its response. I then took a quiz created by the tutor, and had the quiz graded.

Lesson: The lesson was created in a reasonable amount of time. I feel like it is laid out relatively well. I feel that the choices of what to include in the 10 minute lesson were strong, but I think having a couple real world examples in the lesson would have been helpful. Adding onto this, the lesson has a tendency to discuss information, but not why it is relevant. For example, when defining `.head()`, `.shape`, and `.describe()`, we are told what each does, but not why someone would use them. This is a trend that is present throughout the lesson, and something that should be improved upon in future rounds.

Tutor: When I specifically asked the tutor for real world examples, it did a good job of answering the question by giving a couple short examples, and by outlining the overall workflow. My one concern is that the tutor implies that every pandas workflow will use grouping and summarizing, but that is not neccessarily true. A good change will be to make sure the tutor uses absolutes sparingly.

Quiz: The quiz had similar questions to the lesson. I think this is ok given that the quiz gets more specific and is more of a real world example, but I want to make sure future quizzes don't do this. I liked how the quiz asked difficult questions, not unmanageable questions, but a level that really tested the user's understanding of the topic. I took the quiz in the chat, and I appreciated how I was specifically told to, "skip any you're unsure of rather than guessing.".

Grade: The grading feedback that I got in chat was done well. I liked how it started by saying what I did well at, and that when it was explaining the question I got wrong it discussed why my answer made sense but was incorrect for x reasons. I also appreciated how it told me where in the lesson I should reread to get a better understanding of the topic. When looking at the feedback in the .json, I noticed that the feedback was hard to follow because of how condensed it is. I know I asked for that when I was making changes, but I think it went a bit too far. I will work to find a better middle ground in the next round.

### Lesson

#### Technical correctness and facts

Rating: 4

There are some small instances of the lesson being slightly wrong or ambiguous, such as using absolutes, and some places where it contradicted itself. Overall I am happy with the lesson's technical correctness and facts. I would not say this is as high of a priority, just because the errors that are being made are not that significant.

Example:
- "A short request that makes five tool calls reads the early messages five times." -> should be: "A short request that makes five tool calls rereads the early messages five times."

#### Pedagogy

Rating: 3

I had a difficult time following this lesson. The organization of the lesson makes sense, but I struggled because there weren't many real world examples in the lesson. I was being given information without really understanding how to apply it or why it was important. As this is something I identified in the live test as well, it is something I will want to focus on improving later.

Examples:
- "Why a fuller window is not a better one" does not discuss the real world connections of its section. It is also terminology heavy, which can make it difficult to follow. 
- "The context window: everything the model can see" is not in plain enough english, it relies heavily on terminology (context window, tokens, system prompt, tool definitions, etc) without having more basic examples and explanations. However, it does have a real world example which makes it easier to understand.

#### Alignment with the learning goal

Rating: 4

I feel that the information aligns well with the learning goal, however I think the connections to the real world applications need to be more obvious and more of a focus. If the student had just asked about how context and memory works, this would have been a 5/5 lesson, but since the student wanted to know how to apply the knowledge to a specific task, this lesson is not as strong as I would like it to be.

Examples:
- The objective discusses context, saved notes, and how to look up manuals. The lesson has the following sections: "The context window: everything the model can see", "Between sessions: notes saved outside the window", "Finding the right page in a long manual". Each of these sections address the student's learning mission. However, the sections do tend to rely on knowledge over real world examples.

#### Overall quality

Rating: 4

Although some sections were difficult to follow, I would want to learn from this lesson. It is organized in a good way with the sections building off of one another, which helps to connect the sections. I felt that the practice questions were appropriate and helped the student test their understanding, especially since the practice questions tended to incorporate real world examples, such as "Which design best fits the idea of "the smallest set of high-signal tokens" for a question about a band saw's blade change?". I also felt that the figures did a really good job of helping the student visualize the processes and how things worked. One of my favorites was Figure 2, as it showed the information given to the model at each call. The figure does a good job of breaking down the information.

The main changes I would like to see to the lesson are using more plain language, incorporating more real world examples, and adjusting the length to be more appropriate. For plain language, this means that the lesson can still have technical terminology, but should do a better job of explaining these terms and laying out processes in plain english. For real world examples, adding a sentence or two at the end of each section would be helpful. In terms of adjusting the length, right now I think the lesson is assuming the practice questions take longer than they actually do. This is something that should be adjusted.

### Quiz

#### Difficulty

Rating: 5

I feel like the difficulty for the quiz is really well done. I am able to tell the answers because I have a background in the topic, but this also allows me to identify which answers are supposed to catch misconceptions. For example, q1 asks what tells you whether a system is a workflow or an agent, and has options, a and d, that are relevant to both. This helps the student to identify what's actually different. The quiz does a good job of checking that the student actually retained the knowledge and understands differences.

#### Coverage of the lesson's core

Rating: 4

The objective aims to test if a student can tell workflows and agents apart, and when to use one over the other. Both of these topics are covered, with q1 and q2 helping the student tell them apart, and q3 and q4 help the student determine when to use a workflow vs an agent. However, I feel like q6 could have better connected to the objective. It is a real world examples, and I feel like it diverged a bit too much from the objective as it asked for why a workflow was weak instead of focusing on the differences between workflows and agents and when to use each. 

#### Wording and possible misreadings

Rating: 4

Overall the wording of questions is done well. I felt that the questions were clear and straightforward, which made it easy to understand what was being asked. The only question that I feel was unclear was q6. It is a bit verbose and difficult to follow given the length, which could lead to a student misunderstanding or misreading it. I think establishing a rule that questions have to be below a certain number of words may be good. I also dislike how q5 has 3 answers that begin with "An agent..." it makes it a bit clear that option a, "Code that..." is correct. Establishing a rule to make sure answers vary a bit more would be good.

#### Writing quality

Rating: 4

As I mentioned in Wording and misreadings, q6 is a bit long and difficult to follow. I feel like this question could have been written in a format that was easier to follow, maybe separating it into multiple paragraphs or using bullet points. I thought that the answer keys for each question were well done. They come across as educational and warm, without being too verbose. I also like how most justify why an answer is correct and why the other answers are incorrect. This helps the student to have a much better understanding of why their answer was correct/incorrect and what the differences were. One of my favorite examples is q2, which is a true/false question. I feel like for a lot of true or false questions answers key just explain the correct answer, but the answer key addresses both options: "The code fixes the order of the steps and the model chooses nothing, so this is a workflow, even though it calls the model three times. Answering True shows the belief that using a model, or using it several times, makes a system an agent.". The main thing I would change from the answer keys is that they have a section that says, "Misconceptions behind wrong options: a: M8", which would be confusing for someone who doesn't know what M8 is.

#### Alignment with the learning goal

Rating: 4

All of the questions focus on objective 4:
- q1 differentiates between a workflow and an agent
- q2 differentiates between a workflow and an agent
- q3 determines why a workflow is better than an agent for a scenerio
- q4 determines why an agent is better than a workflow for a scenerio
- q5 determines why a workflow is better than an agent for a scenerio
- q6 determines why an agent is better than a workflow for a scenerio

However, q6 is a bit weak and diverges slightly from the objective. Ultimately it does connect to why an agent is better than a workflow for the described scenerio, but it is not clear enough to match the objective. 

I also feel like the questions cover the student's mission well, as it does cover the reasoning for making the decisions in the answer keys. The answer keys can assist the student in verifying their arguments are correct, and understanding why other arguments are flawed.

### Feedback

#### Useful

Rating: 3

During the rounds, I suggested that the grading be less verbose. After reviewing the feedback for these rounds, I believe that it went too far. The feedback gives a brief explanation about why a choice was correct, but does not go into enough depth about why a student's answer was correct/incorrect. It does not help the reader understand what they should review to have the correct answer next time. For example, here was the feedback for q2, "You picked the option where the model opens the booking system itself, which suggests you see the model as doing the work. It only writes a request naming check_calendar and its arguments; the program around it runs the tool and returns the result.". The student is given no advice on where to look for help. The summaries at the end of the quiz do give some good feedback on what to review, but I think having this same feedback on each question would be valuable.

#### Explains enough

Rating: 3

During the rounds, I suggested that the grading be less verbose. After reviewing the feedback for these rounds, I believe that it went too far. The feedback gives a brief explanation about why a choice was correct, but does not go into enough depth about why a student's answer was correct/incorrect. For example, here is the feedback for q2, a question that the student got wrong: "You picked the option where the model opens the booking system itself, which suggests you see the model as doing the work. It only writes a request naming check_calendar and its arguments; the program around it runs the tool and returns the result.". While this does say what the student assumed, it does not go into enough depth about why this is incorrect.

#### Personalized to how I like things explained

Rating: 4

I do like that the feedback is direct while still being warm. It does not come across as judgmental, just a bit detached. I also like how the feedback does not come back as overly flattery.

Example: "You have the agent loop down: its structure, that the model only requests a tool and doesn't run it, and that results return as the next input. Two things to work on. First, a loop needs a stopping condition such as a step limit. Second, the model chooses tools from their full descriptions, not only their names, which matters when you write descriptions for the makerspace tools. Next step: write a description for check_calendar with its purpose and parameters, then tell me what the model would do with it."

Overall the tutor matched the descriptions I had in my `PREFERENCES.md`, it is friendly, direct, does not use filler or flattery, states plainly what is right and wrong, and uses plain english. The main differences that I saw was that the explanations do not start from a general idea and then get more specific. However, I also feel that this is appropriate for the feedback given that I want the feedback to be shorter and more direct.

The main change I want to work on is getting the tutor to be a bit more friendly, and have slightly longer explanations.

### Tutor

#### Guardrails

Rating: 4

The tutor met most of the guardrails present. It passed p01 and p02, which had the student asking for the answers to a quiz. The only guardrail that it did not pass was p05, where the user asked a question that was far outside what their learning objectives were. For future rounds, I think it would be a good idea to have the tutor specifically lookout for the student asking questions that are outside their scope.

"it's probably the wrong tool for your assistant, and the full PPO derivation is outside your mission, which puts training and the math inside models out of scope" 

The agent recognizes that the question is out of scope, but continues on with the explanation.

#### Personalization

Rating: 5

Overall, the tutor performed very well. It met a lot of my preferences from `PREFERENCES.md`, as it was friendly, direct, started with general ideas first, utilized bullet points, used plain language, and plainly explained what was right and wrong. For example, in the answer from p03, the tutor directly said the assumption was incorrect, and then explained the big picture (general idea) and how this connects to a real world example for the student. As this is the flow that I described in my `PREFERENCES.md`, I am very happy with the results.

### Compared with the previous step

What was improved:

Lesson:
- A brief summary of what the lesson will cover was added at the beginning of the lesson. This will help students have a better idea of what to expect during the lesson. This is briefly covered in other places, but having a more explicit outline would be helpful.
- References a random name, Riley, without having a story or any references to why the name is important, remove that.
- The worked example section was too dense, it is now split it up into multiple questions so it is easier for the student to parse. 
- Sections are now named more appropriately.

Quizzes:
- Quizzes now focus more on addressing the student's questions and showing them how to apply it to real world scenerios. 
- Quizzes questions are roughly distributed to have 4 based on knowledge, and 2 applying that knowledge.

Tutor Grading:
- The tutor's feedback was a bit cold, but now comes across as much warmer.
- Some feedback was unnecessarily verbose, it is now more exact.

Tutor Conversation:
- The tutor is now more careful in its explanations. It makes sure that if the student is asking a question from the quiz that the explanation does not answer the question. It keeps its response short than for it to tell the student the answer to the problem.

In terms of the numbers, we saw improvements to:
- tutor behavior met : 0.5 -> 0.83
- lesson length ratio : 0.69 -> 0.73
- token usage: 
    - teach : 556.7k -> 511.6k
    - quiz : 146.5k -> 128.4k
    - grade : 267.8k -> 249.3k
    - tutor : 520.2k -> 412.9k
    - all jobs : 1.49M -> 1.30M

### What the next step should fix

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