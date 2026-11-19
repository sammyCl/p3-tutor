# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261118-023157-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**
- Match the requested length of the lesson better, if a student requests a 30 minute lesson, make sure the lesson is actually 30 minutes.
    - Lets create a subagent who's whole job is to go through the lesson like a learner, and gauge a more accurate breakdown of how long the lesson actually is.
- Make sure to use sources from more than one source. Students may want to have explanations provided in different formats, so having a variety of sources will help the student follow better.
    - Lets create a subagent that specializes in collecting multiple resources, instead of limiting to just one source.
- Make an agent who's whole job is to review figures. Make sure the information is accurate, and that the figures are well designed. Figure 3 in the lesson has text that goes outside of the bounding boxes it defines.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-timer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The thoughts ask first for a lesson that fills the 30 minutes requested, and this run's lesson came to about 3,600 words, 24 of 30 minutes, so a timer subagent now walks the first draft section by section like a learner and the teach skill adds teaching where it says before the review loop.

### Round 2

**Run:** bench/runs/_live/20261118-035626-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

- Make sure to use sources from more than one source. Students may want to have explanations provided in different formats, so having a variety of sources will help the student follow better.
    - Lets create a subagent that specializes in collecting multiple resources, instead of limiting to just one source.
- Make an agent who's whole job is to review figures. Make sure the information is accurate, and that the figures are well designed. Figure 3 in the lesson has text that goes outside of the bounding boxes it defines.

What Improved:
- Matched the requested length of the lesson better.
    - Created a subagent who's whole job is to go through the lesson like a learner, and gauge a more accurate breakdown of how long the lesson actually is.
    - Increased length ratio from 0.77 to 0.86.

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-sources-finder.md, tutor/.claude/skills/teach/SKILL.md
- Why: The thoughts ask first for sources from more than one place, in different formats, and all four of this run's links were from Anthropic, so a sources subagent now finds, opens and checks five to eight sources from at least four publishers in at least three formats before the lesson is written, and the teach skill cites them across the lesson.

### Round 3

**Run:** bench/runs/_live/20261118-043114-agent-architecture-m30-r1, a live run with --only teach

**My thoughts:**

- Make an agent who's whole job is to review figures. Make sure the information is accurate, and that the figures are well designed. Figure 3 in the lesson has text that goes outside of the bounding boxes it defines.

What Improved:
- Matched the requested length of the lesson better.
    - Created a subagent who's whole job is to go through the lesson like a learner, and gauge a more accurate breakdown of how long the lesson actually is.
    - Increased length ratio from 0.77 to 0.86 to 0.93.
- Makes sure to use sources from more than one source. Students may want to have explanations provided in different formats, so having a variety of sources will help the student follow better.
    - Created a subagent that specializes in collecting multiple resources, instead of limiting to just one source.
    - Increased the links in the lesson from 4 (all from Anthropic) to 8 (from 5 different publishers)

**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-figure-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The thoughts ask for an agent whose whole job is the figures, their accuracy and design, after a figure's text ran outside its boxes, so a figure reviewer now joins the review loop and measures every label against its box from the SVG's coordinates, and checks each figure's layout, accuracy against the text and sources, and design.


## Major review

**Run:** bench/runs/c3-split/20261118-210525-agent-architecture-m30-r1

**Live tries:**

- I liked how the lesson said where information was coming from. This is helpful so I can reference those sources later if I want further information.
- The lesson did a good job of still having computer science based explanations even though the topic of the lesson was how to plan a vacation.
- The worked examples were relevant to the different sections and added to the learner's experience. I actually felt a bit challenged by some of them, in a good way.
- I liked how the `PREFERENCES.md` was followed, especially since most times this topic is covered they tend to be more wordy and flattery. The lesson continued to be warm but direct.

### Lesson

#### Technical correctness and facts

Rating: 5

The technical correctness is still scoring highly. The benchmark still reports that the `teach_facts_correct` is 1.00, indicating that the technical facts that the benchmark is looking for are correct. This has not changed from `c1-skills`. An improvement I saw over `c2-review` was that the lesson now includes multiple sources. Previously, the lesson would only use Anthropic as a source, this time there are 4 different sources. This helps technical correctness as information comes from a wider variety of resources.

New resources:
    - deeplearning.ai
    - huggingface
    - pinecone
    - claude

Another improvement was that the `leson-figure-reviewer` was able to update some of the figures to be as accurate as possible. For example, it made an arrow for Figure 2 describing how saved notes and the context window interact go both ways, as the notes are read and written.

During my review session, nothing stood out to me as incorrect or contradictory.

#### Pedagogy

Rating: 4

I do not feel that there were any major improvements to the pedagogy of the lesson this round. Overall, the lesson was still well written, in plain english, which made it easier to follow. I also felt that the lesson did a good job of having a lot of real-world examples to help a reader follow along. However, I feel that some of the examples were weak. For example, the section "The context window as the model's whole desk" makes sense at the beginning where it is explained that like the desk, the context window only has what is on/in it. However, this comparison fell apart a bit when the lesson began discussing how the "desk is measured in tokens". I think using stronger examples in the future would be helpful.

#### Alignment with the learning goal

Rating: 5

The lesson continued to be strongly aligned with the learning goal. All 3 topics the lesson was supposed to cover, what the context window is, notes that live outside the session, and how to access manuals, were explained thoroughly and had their own sections:

- The context window as the model's whole desk
- Notes that outlive the session
- Retrieval: fetching one page from a long manual

 These sections also did a good job of connecting to the student's ultimate goal of making a makerspace assistant.

 - "For your assistant, every rule, tool and manual page you add to the desk is a cost paid on every call, so what goes in the window is a budget decision."
 - "For your assistant, a note might be a small file per student, such as /memories/students/s1234.md"
 - "Start with one manual section per chunk and test with real student questions."

#### Overall quality

Rating: 5

I believe that the overall quality of the lesson has increased from `c2-review` to `c3-split`. The lesson now utilizes more sources, which helps to give different perspectives and explanations to the student. The lesson also has more accurate figures, as the `lesson-figure-reviewer` was able to look through each figure and make small changes to increase technical correctness. The lesson is also still easy to navigate, with no dead links or Knowledge Checks that don't work. The lesson is written well in plain english, which makes it easy for the user to follow. The `lesson-timer` did not perform as well for this lesson as it did on previous lessons, but it was helping to get the length ratio to 0.93, which is a significant improvement. 

### Compared with the previous step

- Matched the requested length of the lesson better.
    - Created a subagent who's whole job is to go through the lesson like a learner, and gauge a more accurate breakdown of how long the lesson actually is.
    - Increased length ratio from 0.77 to 0.86 to 0.93.
- Makes sure to use sources from more than one source. Students may want to have explanations provided in different formats, so having a variety of sources will help the student follow better.
    - Created a subagent that specializes in collecting multiple resources, instead of limiting to just one source.
    - Increased the links in the lesson from 4 (all from Anthropic) to 8 (from 5 different publishers)
- Improved the technical correctness of figures by adding the `lesson-figure-reviewer`. 

### What the next step should fix

- Make sure the tutor grading feedback for correct answers is thorough and actionable.
    - Maybe create a skill that tells the user what to do next for if they get the answer partial, correct, or wrong. 
    - Reference the `c2-review` major review s1 q1 and s2 q5 for examples of how the tutor doesn't provide thorough explanations for correct answers.
- Make a skill that tells the tutor how to handle questions that are outside of the user's current scope. This includes outlining a basic explanation of the topic, why it is outside of the students reach, and a relevant topic that is within their skill set to try instead. It should not include complicated math. 
    - Reference `c2-review`'s major review probe 5 for reference, demonstrates how the tutor still explains things out of scope using mathematical equations.
- Select some subagents to get rid of. Right now it takes an unreasonable amount of time to run a lesson (~10 minutes). For a student who is waiting to learn about a topic, this is too long. I will use my findings in the `EVAL.md` to decide which subagents stay.

