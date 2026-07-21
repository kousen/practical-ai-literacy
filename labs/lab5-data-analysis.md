# Lab 5 (Bonus): The Student-Aid Scenario

**Time:** 20 minutes (done as an instructor demo in class; here's the full version)
**Data:** `data/student-aid-scenario.csv` — **entirely invented**. No real
students, no real amounts, no real policies. That's the point: realistic
practice without touching anything FERPA-covered.

## Steps

1. **Attach the CSV** to any capable tool (Copilot with the file in Excel,
   or claude.ai / chatgpt.com / gemini.google.com with the file attached) and ask:

   > Analyze this financial-aid application data. What patterns do you see in
   > aid offered relative to aid requested? Anything notable by residency or
   > EFC band?

2. **Ask for outliers:**

   > Which applications look unusual, and why?

3. **Challenge the analysis** — the most important step:

   > What would make this analysis misleading? What can't we conclude from
   > this data?

   (Sample size, missing variables, correlation vs. causation, how the bands
   were defined... a good tool will name several. Did it?)

4. **Produce the deliverable:**

   > Write a one-page brief for a financial aid committee: key patterns,
   > caveats, and two questions the committee should investigate further.

5. **Verify before you'd ever send it:** hand-check three numbers the brief
   cites against the actual CSV. Open the file. Count. This step is not optional
   in real life.

## Things hiding in the data (spoiler — check after step 2)

- International applicants have noticeably lower offer-to-request ratios and
  the longest decision times
- Nearly every appeal is associated with a long decision time — but which way
  would causation run? (You can't tell from this data. Did the tool admit that?)

## What you should notice

- Grounded analysis of a real file beats "chat about data" — the tool cites
  actual rows and computes actual numbers
- The "what would make this misleading" prompt should be a reflex for any
  analysis you didn't do yourself
- The workflow — ground, converse, challenge, verify — is the same one from
  Lab 1, applied to data
