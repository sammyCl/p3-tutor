# Pre-registration: the length study

This file is for 598E students, for whom the length study is the required rider, and for 498E students who chose it as their stretch.
Everyone else can ignore it or delete it.

A pre-registration is a claim you write down, with the analysis that will judge it, before you can see the answer.
Its value is that the claim can be wrong in a way anyone can check, and that you cannot bend it afterwards to fit the numbers.
A clear "no difference as large as the one I cared about" scores as well as a confirmation, so you have no reason to hedge.

**Git history is how I will know the order.**
Fill in sections 1 to 4 and commit this file before the first of the eighteen length-study runs.
`uv run p3 check --final` reads `git log` and confirms that the commit came first.
After that commit, do not edit sections 1 to 4.
If something must change, add a dated entry in section 6 and leave the original as it was.
Section 5 you write at the end, after the runs and the comparisons.

Each section that needs your words ends with a marker line.
Replace that line with your answer; `uv run p3 check --final` fails while one is left.

The design is fixed: two configs, three lengths, three teach-only runs in each cell, on the shared topic.

| | 10 minutes | 30 minutes | 60 minutes |
|---|---|---|---|
| `c1-skills` | 3 runs | 3 runs | 3 runs |
| `final` | 3 runs | 3 runs | 3 runs |

```
uv run p3 bench --config c1-skills --only teach --minutes 10 --repeats 3
uv run p3 bench --config c1-skills --only teach --minutes 30 --repeats 3
uv run p3 bench --config c1-skills --only teach --minutes 60 --repeats 3
uv run p3 bench --config final --only teach --minutes 10 --repeats 3
uv run p3 bench --config final --only teach --minutes 30 --repeats 3
uv run p3 bench --config final --only teach --minutes 60 --repeats 3
```

After the runs, one blind comparison per length, each pairing only the study's teach-only runs at that length, three pairs each:

```
uv run p3 compare c1-skills final --job teach --teach-only --minutes 10
uv run p3 compare c1-skills final --job teach --teach-only --minutes 30
uv run p3 compare c1-skills final --job teach --teach-only --minutes 60
```

`--teach-only` matters at 30 minutes, where the ladder's full runs of `c1-skills` and `final` hold a 30-minute lesson too; it keeps them out, so every length is paired the same way.
These three sessions are your second blind comparison of the project, beside `c0-baseline` against `final`, and you make no other on top.
The numbers for every cell come from one command:

```
uv run p3 report --configs c1-skills,final --teach-only
```

---

## 1. Hypothesis

One or two sentences: as the requested length grows from 10 to 60 minutes, which config loses more quality, in which measure, and why you expect it.
For example: "The single-agent `c1-skills` loses more than `final` as lessons get longer, because one context writing a 60-minute lesson drifts from the plan, so its `teach_facts_correct` falls further from 10 to 60 minutes, and `final` wins more of the blind pairs at 60 minutes than at 10."
It should be something you could be wrong about.

I predict that as the lessons get longer, 10 minutes to 60 minutes, `c1-skills` will lose more, than `final`. I believe that `c1-skills` will struggle to develop a longer lesson, and drift from the plan, and that since it has no reviewers to keep it in check this drift will not be detected. This drift may result in the lesson being an inappropriate level. Since the `final` config has reviewers to keep the lesson in check, resulting in a higher judge's level fit, I think it will stay more aligned to the goal and will not suffer as much of the drift.

We will be able to measure the drift from the plan based on the judge's level fit. A higher judge level fit (5) will indicate that the lesson is an appropriate fit, lesson is the correct level for the student, has appropriate pacing, and accounts for prior knowledge the student has. A lower score (1) will indicate that the lesson is not an appropriate fit, too advanced/not advanced enough for the user, does not have appropriate pacing, or does not account for the prior knowledge the student has.

---

## 2. The smallest difference that matters

Choose one primary measure now, so you cannot pick the better one afterwards, and say how large a difference in it would matter to a learner, and why that size.
Call it Δ (delta).

Know what three runs per cell can show before you choose.
There are three blind teach pairs at each length, and even 3 of 3 for one config has a two-sided sign-test p-value of 0.25, so no single length can settle a preference on its own.
Across all three lengths there are nine pairs: 8 of 9 gives a p-value of about 0.04, and 7 of 9 about 0.18.
An objective measure, such as `teach_facts_correct` or the judge's level fit, gives three numbers per cell, and you can see a difference only when it is larger than the spread between the three runs.
So choose a Δ that is large enough to matter and large enough for three runs to see.

I am using the judge's level of fit to determine if `c1-skills` is weaker than `final` when comparing a 10 minute lesson to a 60 minute lesson. In order to calculate this, we will subtract the average judge's level of fit for the 60 minute lesson from the average judge's level of fit for the 10 minute lesson for `c1-skills` and `final`. We will calculate the drops for each, and compare the drops to see if the drop in `c1-skill` is 1.33 more than the drop for `final`.

In my runs thus far I have seen variations of 1 point for the same snapshot (such as a 4 vs a 5). As a result, I want to account for these small variations. As a result, I believe a Δ of 1.33 would be enough to classify a difference between the `final` and `c1-skills`. A difference of 1.33 is enough to show a lesson going from meeting most expectations (4), to having significant issues (3).

Ex: 
- 10 minute lesson for `c1-skills` is: 4, 5, 5
- 10 minute lesson for `final` is: 5, 5, 4
- 60 minute lesson for `c1-skills` is: 3, 3, 3
- 60 minute lesson for `final` is: 4, 4, 5

Average for 10 minute lesson:
- `c1-skills`: 4.67
- `final`: 4.67

Average for 60 minute lesson:
- `c1-skills`: 3.00
- `final`: 4.33

`c1-skills` drop = 4.67 - 3.00 = 1.67

`final` drop = 4.67 - 4.33 = 0.33

Difference between drops = 1.67 - 0.33 = 1.33

According to the Δ, this example would support that `final` is stronger than `c1-skills` when lesson length is increased from 10 minutes to 60 minutes.

---

## 3. The measures

Name each measure you will report, and how you will compute it.
At least these:

- **Your primary measure** from section 2, per cell, as the mean and the range of the three runs.
- **The blind comparison** of `c1-skill` against `final` at each length, one session per length, never across lengths, and `final`'s share of the non-tie picks at each.
- **Length accuracy:** `teach_length_ratio` per cell, the lesson's estimated reading time against the minutes requested.
  It is a rough estimate at 150 words a minute, and a "60-minute" lesson that is really 35 confounds every other measure, so say now what you will do with a cell whose lessons miss their length.
- **Cost against length:** tokens per minute of lesson for each config, and whether `final`'s overhead grows in step with length or faster.
  Say whether you divide by the minutes requested or by the estimated minutes.

My four methods of measure will be:
- level fit
  - In order to calculate this, we will subtract the average judge's level of fit for the 60 minute lesson from the average judge's level of fit for the 10 minute lesson for `c1-skills` and `final`. We will calculate the drops for each, and compare the drops to see if the drop in `c1-skill` is 1.33 more than the drop for `final`.
  - I will also report the mean and range for each cell.
- blind comparison
  - I will do a blind comparison for each of the 3 pairs of lessons for 10 minutes, 30 minutes, and 60 minutes. I will keep track of the ratio of `final` wins compared to non-tie picks. My prediction is that at longer lengths, the `final` runs will perform better, so I would expect the ratio of `final` wins compared to non-tie picks to be higher for 60 minute lessons than 10 minute lessons.
- length accuracy
  - I will take the average `teach_length_ratio` for each set of lessons, and compare how the lessons length ratio changes as the length of the lessons gets longer. I predict that as the length of the lessons gets longer, the `c1-skills` will be farther from 1.00 than `final` will be, as `final` has a subagent that checks the length.
  - I will report the mean and range of the three runs.
  - I will also report large misses, any mean ratio below 0.6 or above 1.5. Big misses indicate that the lesson is not meeting some of the user's key requirements, so it should be tracked. Big misses will be considered as an indication that the method that produced them is weaker.
- cost against length
  - I will calculate based on requested minutes, as that is the value the user is asking for.
  - For each run of each lesson length, I will take the average of the number of tokens divided by the length the user asked for. I expect that the `final` runs will have a larger cost against length, as `final` utilizes subagents that use up tokens.
  - I will also keep track of how much cost against length increases for `final` as the length of the lesson increases. We want to see if there is a proportional difference for the increase in tokens compared to the increase in length.

---

## 4. The analysis, and what each result will mean

The comparison is the change from 10 to 60 minutes in your primary measure, for each config, read against the spread of the three runs.
Write the rule now.
This is the default rule, and you can tighten it, but do not loosen it after you see your numbers.

| The result | I will say |
|---|---|
| the two configs' changes differ by Δ or more in the direction I predicted, and the three runs' ranges at 60 minutes do not overlap | supported |
| they differ by Δ or more in the other direction, and the ranges at 60 minutes do not overlap | contradicted: the opposite holds on these runs |
| they differ by less than Δ | no difference as large as Δ on these runs, with the ranges reported |
| anything else | inconclusive with three runs per cell, and I say so |

Then name the threats to validity you will report (lecture 22): blinding failures (your could-tell share at each length), judge bias toward longer outputs (lecture 24), the rough length estimate, and three runs per cell.
Say which one worries you most for your hypothesis.

I will keep the same rule, as it matches my hypothesis.

Threats to Validity:
- blinding failures: I may be able to recognize which lessons were created by `final` purely based off of the structure. This could result in the blind comparison being inaccurate if I subconsciously choose the lessons created by `final` every time. 
- judge bias toward longer outputs: Both humans and models tend to choose longer outputs as the "better" output. As a result, if `final` or `c1-skills` tends to have longer outputs, I may tend to choose these lessons during the blind picks, and the model may rate those lessons higher during its judge of level fit.
- Rough length estimate: Lesson length calculations may not properly predict the amount of time a user would spend reading, looking through the figures, or answering Knowledge Checks. This could mean a lesson is actually longer or shorter than the lesson predicted, resulting in an incorrect length accuracy. 
- three runs per cell: There can be variation between runs, which we have seen so far. This could mean 2/3 runs score lower than expected, and skew the data in an inaccurate direction.

I am most concerned about only having 3 runs. Averaging 3 runs can still contain a significant amount of noise, as having only 2 runs having skewed data can greatly affect the results.

---

## 5. Outcome (write this after the fact)

What did each measure show, cell by cell?
Which row of the table in section 4 is it?
Did the lessons meet their lengths, and what did the cost per minute of lesson do?
What would you do next, and what would you want a reader to take from this?

TODO: your outcome.

---

## 6. Amendments

Dated entries only, one per change, each saying what changed and why.
Leave this section as it is if nothing changed.
