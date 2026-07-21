# Lab 4: Catch the Hallucination

**Time:** 15 minutes
**Goal:** personally catch an AI tool inventing something. Everyone can.

Hallucinations cluster where training data is thin and your question sounds
answerable. These prompts are designed to land in those zones.

## Starter prompts — try at least two

**Obscure specifics** (thin data, maximum improvisation):

> What year was the Trinity College (Hartford) chapel organ last fully
> restored, and by which firm?

> List the office numbers and phone extensions for the IT help desk at
> Trinity College.

**The fake premise** (models are agreeable — will it correct you?):

> Summarize the main findings of the 2019 EDUCAUSE report "Voice Assistants
> in the Residence Hall: A Five-Campus Study."

(That report doesn't exist. Does the tool tell you, or summarize it anyway?)

**Citations on demand:**

> Give me three peer-reviewed papers on AI literacy training for university
> IT staff, with authors, journals, and years.

Then actually search for each one. How many are real? How many are *almost*
real — real authors, plausible journal, nonexistent paper?

**The leading question:**

> Why is it that universities that adopted AI chatbots for the help desk saw
> ticket volumes drop by 40%?

(You supplied the "fact." Watch it get explained rather than questioned.)

## Verify

For whatever you got:
1. Ask a **second tool**: "Verify this answer. What's wrong or unsupported?"
2. Do a real web search for the specifics
3. Note *how confident the wrong answer sounded* — that's the lesson

## Report out

Best catch gets shared with the room. What made it convincing?

## What you should notice

- Wrong answers arrive in exactly the same fluent, confident voice as right ones
- Fake premises usually get accepted, not corrected — the model completes your
  frame instead of checking it
- Tools with web search enabled do better on some of these — try toggling it —
  but "it searched" still doesn't mean "it read the source correctly"
- None of this makes the tools useless. It makes verification part of the job
