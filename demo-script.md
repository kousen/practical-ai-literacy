# Demo Script

Instructor-only. Four live demos, in slide order, each with prep, exact steps,
narration beats, and a fallback if it dies on stage.

**Universal pre-flight (morning of):**

- [ ] Wispr Flow running and mic tested *in the actual room*
- [ ] Claude Desktop open, signed in, MCP servers connected (check the tools icon)
- [ ] Terminal with Claude Code, `cd` into the prepared demo folder
- [ ] Copies of `labs/data/` files on the desktop for quick access
- [ ] Browser tabs: copilot.microsoft.com (Trinity account), claude.ai, chatgpt.com
- [ ] Screen mirroring, font sizes bumped (terminal ≥ 18pt, browser zoom 125%)
- [ ] Do a 30-second dry run of each demo — models and tools change weekly;
      last week's demo is not this week's demo

---

## Demo 1: Wispr Flow — before you even introduce yourself

**When:** the moment the title slide is up. Before "hi, I'm Ken."

**Steps:**

1. Open a visible text editor (big font)
2. Dictate your own introduction, deliberately including an "um" and a
   self-correction ("this workshop covers, um, actually let me say it this
   way...")
3. Let them watch clean, punctuated text appear with the disfluencies gone
4. *Then* introduce yourself: "That was an AI tool. That's the whole morning
   in one demo — it did the tedious part, I supplied the content."

**Narration beats:**

- Faster than typing, and it's *edited* text, not a transcript
- Works in every app — email, Word, chat, code editors
- "How much of your day is typing things you could have said?"

**Fallback:** if the mic or room audio fails, show a 30-second pre-recorded
screen capture (record one the night before), or simply narrate it and move
on — this demo is a tone-setter, not load-bearing.

---

## Demo 2: Skills + MCP in Claude Desktop

**When:** Connected AI section — "Skills" and "MCP" slides.

**Prep (do the day before):**

- A simple status-report skill installed in Claude Desktop. Keep the skill
  file in this repo so attendees can see it's just plain-language instructions
- Two MCP servers connected and *tested*: filesystem (pointed at a demo folder
  containing the labs/data files) plus one more visual one (e.g., web search
  or any public MCP service that's currently reliable)

**Part 1 — Skills (2 min):**

1. Paste the messy meeting notes into Claude Desktop, no instructions beyond
   "format these as a status report"
2. The skill kicks in: consistent template, tone, structure
3. **Show the skill file itself** — it's a page of English. "Someone on your
   team writes this once. Now everyone's reports look like this."

**Part 2 — MCP (3–4 min):**

1. Ask: "Look in the demo folder and summarize what's there"
2. **Pause on the permission prompt.** This is the money shot for an IT
   audience: "It's asking. It can't touch anything I haven't allowed. When
   campus asks you 'is this safe?' — this permission model is the answer."
3. Have it read `helpdesk-tickets.csv` via the filesystem server and report
   top categories
4. One query through the second server to show the same protocol reaching a
   completely different system

**Narration beats:**

- MCP is "USB for AI" — one standard plug, many devices
- The library/institutional-systems angle: this is how a catalog or a
  ticketing system becomes something an assistant can query
- Skills are prompting-as-infrastructure; MCP is data-access-as-infrastructure

**Fallback:** if an MCP server won't connect, the filesystem server alone
carries the demo. If Claude Desktop itself is down, describe the permission
prompt over the slide and lean on Demo 3, which shows the same pattern in the
terminal.

---

## Demo 3: Claude Code doing non-code work

**When:** "AI Coding Assistants (Yes, for You Too)" slide.

**Prep:** a `demo-messy-folder/` (NOT in this repo — create it fresh) with
15–20 files: PDFs, CSVs, screenshots, docs with inconsistent names like
`report_final_v2_ACTUAL.docx`, `IMG_4032.png`, `notes (1).txt`. Two minutes
with any file generator or by hand.

**Steps:**

1. Terminal, big font, `claude` already running in that folder
2. Prompt: *"Look at the files in this folder. Propose a sensible folder
   structure and consistent naming scheme, then show me the plan before
   moving anything."*
3. Narrate while it works: it's listing files, reading a few, thinking
4. **Pause on the plan.** "It proposed; I approve. Same permission story as
   the MCP demo."
5. Approve. Let it reorganize. Show the result in Finder
6. Encore if time allows: *"Now write a summary.md describing what's in each
   folder"*

**Narration beats:**

- Nobody wrote code. "Coding assistant" undersells these tools —
  they're do-things-on-a-computer agents
- For IT staff: this is the fastest on-ramp to automation you've ever had —
  it can also *write and explain* the script version for repeat use
- Codex inside ChatGPT occupies the same niche; the concept, not the vendor,
  is the lesson

**Fallback:** keep a before/after screenshot pair from your rehearsal run. If
the live agent stalls, show the screenshots and narrate the permission flow.

---

## Demo 4: The student-aid scenario

**When:** its own slide, end of the Connected AI section.

**Prep:** `labs/data/student-aid-scenario.csv` — open it in Excel briefly
first so the room sees it's ordinary-looking data. Say "entirely invented"
*out loud* — twice.

**Steps (any capable tool; Copilot with the file open in Excel keeps it in
the Microsoft world they know):**

1. "Analyze this financial-aid data. What patterns do you see in aid offered
   vs. requested, by residency and EFC band?"
   - *Planted:* international applicants get lower offer ratios and the
     longest decision times — a decent tool finds this
2. "Which applications look unusual, and why?"
3. **The challenge step:** "What would make this analysis misleading? What
   can't we conclude?"
   - *Planted:* appeals correlate with long decision times, but causation is
     genuinely ambiguous. Does the tool admit it can't tell? Point at it
     either way — "that admission (or its absence) is the whole game"
4. "Write a one-page brief for the committee: patterns, caveats, two
   questions to investigate"
5. **Verify one number by hand, live.** Open the CSV, count, confirm. "Thirty
   seconds. Not optional for anything you'd send."

**Narration beats:**

- The workflow is the lesson: ground → converse → challenge → verify
- This is realistic practice precisely *because* the data is fake — the
  FERPA-safe way to build the skill
- Full version is Lab 5 in the repo for them to redo later

**Fallback:** this demo is nearly failure-proof (attach file, ask questions),
but if the tool gives a shallow analysis, that's not a failure — turn it into
the verification lesson: "Would you have caught how thin that was?"

---

## Timing discipline

Demos 1 and 4 are fixed points. If the morning runs long, Demo 2 compresses
to Skills-only (2 min) and Demo 3 compresses to the before/after screenshots.
Protect the labs — hands-on time is what they'll remember.
