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

**Run:** bench/runs/c3-split/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
