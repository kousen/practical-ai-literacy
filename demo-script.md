# Demo Script

Instructor-only. Four live demos, in slide order, each with prep, exact steps,
narration beats, and a fallback if it dies on stage.

**Universal pre-flight (morning of):**

- [ ] Wispr Flow running and mic tested *in the actual room*
- [ ] Claude Desktop open, signed in, MCP servers connected (check the tools icon)
- [ ] Terminal with Claude Code, `cd` into the prepared demo folder
- [ ] Copies of `labs/data/` files on the desktop for quick access
- [ ] Browser tabs: copilot.microsoft.com (Trinity account), claude.ai, chatgpt.com,
      the Tokenizer Playground (loaded and tested — it fetches the tokenizer on first use),
      openrouter.ai
- [ ] Ollama running, model already pulled (`ollama run gemma4` answers a test question)
- [ ] ElevenLabs key working; `demo-assets/voice-clone-demo.mp3` plays through the room's speakers
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

## Micro-demo: The Tokenizer Playground

**When:** the "Tokens: The Unit of Everything" slide — 2 minutes, in the browser.

**URL:** <https://huggingface.co/spaces/Xenova/the-tokenizer-playground>
(runs in the browser via Transformers.js; needs network to load the page, then
tokenizes locally — keep the tab open from the morning pre-flight)

**Steps:**

1. Type "Trinity College" — watch it split, note the token count
2. Paste a sentence from a real email — point out common words are one token,
   rare words shatter into fragments
3. Try something odd: "supercalifragilistic" or a long URL — fragments everywhere
4. Switch the tokenizer dropdown between models to show different vendors
   slice text differently

**Narration beats:**

- "This is what the model actually sees — not words, not letters"
- Connects forward to pricing (metered per million of *these*) and context
  windows (the memory is measured in *these*)
- Why models are historically bad at "how many R's in strawberry": they don't
  see letters at all

**Fallback:** OpenAI's tokenizer at <https://platform.openai.com/tokenizer>
shows the same idea. If both are unreachable, the slide's ¾-of-a-word rule of
thumb carries the point.

---

## Micro-demo: An Open-Weights Model on This Laptop

**When:** the "Open-Weights Models" slide — 3–4 minutes.

**Prep (night before):** `ollama pull gemma4` (multi-GB download — never on
room wifi, morning of). Test the exact question you'll ask. Have OpenRouter.ai
loaded in a tab.

**Steps:**

1. Terminal, big font: `ollama run gemma4` — point out what just happened:
   a capable model, running entirely on this laptop
2. **Optional flourish:** turn off wifi first, visibly. "No cloud. No account.
   No data leaving this machine."
3. Ask it the car wash problem — your standard trick question. Let the room
   watch a local model reason (or stumble — either is the lesson: this is the
   evaluate-it-yourself method from the first section, applied live)
4. Ask the same question in a frontier tool for contrast if time allows

**Then OpenRouter.ai (1 minute):**

5. Switch to the OpenRouter tab: hundreds of models — commercial and
   open-weights — behind one interface, each with its price **per million
   tokens** right there in the list
6. Sort by price or popularity. "This is the menu. Token pricing isn't
   abstract — it's a column on this page."

**Narration beats:**

- Why an institution cares: privacy (nothing leaves the machine), cost
  (no per-use fee), and smaller models are genuinely useful for drafting,
  summarizing, classifying
- Honest trade-off: local models are less capable than the frontier ones —
  which you may have just watched happen
- OpenRouter connects back to the cost-literacy slide: the market is visible

**Fallback:** if Ollama misbehaves, OpenRouter alone carries the segment — many
open-weights models are runnable there in the browser, and the pricing table
makes the cost point regardless.

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

**When:** "Coding Agents (Yes, for You Too)" slide.

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

- Nobody wrote code. "Coding" undersells these agents —
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

## Demo 5: The Voice Clone Moment

**When:** the "Voice" slide in the Multimodal section — 3 minutes. Sequence it
so you've just been talking; the contrast is the demo.

**Prep:** ElevenLabs key set (`ELEVENLABS_API_KEY`). The voice id lives in
this repo's `CLAUDE.md` ("Ken Kousen", `AnMHhwDcnqFSc3sT34OR`), so run Claude
Code **from this repo's folder** and it knows what "my voice" means — no
pasting IDs on stage. A pre-rendered fallback lives at
`demo-assets/voice-clone-demo.mp3` (gitignored — do not commit voice samples
to the public repo).

**Steps:**

1. Mid-sentence, stop and say: "Actually, let me have… me… finish this section"
2. In Claude Code (in this repo's folder), live: *"Say this in my voice:
   [something topical about the morning so far — make it specific to today so
   the room knows it wasn't pre-recorded]"*
   — and if anyone asks how it knew your voice, show them `CLAUDE.md`: project
   memory, a bonus lesson in how agents pick up context
3. Play it. Let the room sit in the uncanny valley for a beat
4. Then the turn: **"I consented to this. I trained that voice on purpose.
   Now — who here does phone-based password resets?"**

**Narration beats:**

- Professional voice cloning is consumer-grade now: minutes of audio, modest cost
- Voice is no longer an authentication factor — connect directly to help-desk
  procedures, vishing, and "grandparent scam" patterns campus users will face
- **The take-home advice:** agree on a safe word or phrase with family and
  close friends. An urgent call that sounds exactly like your kid, your parent,
  or your boss can be a clone — the safe word is the check the caller can't fake.
  This is the single most repeatable tip of the day; say it slowly
- This is also a *tools* callback: a coding agent just called a third-party
  API through a skill — the same plumbing from the Connected AI section
- Ethics note worth saying aloud: cloning requires consent; this one is mine

**Fallback:** play `demo-assets/voice-clone-demo.mp3` — pre-rendered in your
cloned voice, with lines written to make the same point.

---

## Optional Demo (if time): Pangram vs. an Evasive Paragraph

**When:** the "For Instructors in the Room" slide — 5 minutes, near the end.

**Prep:** free account at <https://www.pangram.com> tested that morning; rehearse
the full sequence the night before and screenshot each step.

**Steps:**

1. In any chat tool, live: *"Write a paragraph about campus Wi-Fi upgrades
   that reads as if a human wrote it, specifically designed to pass AI
   detectors."*
2. Let the room admire how human it sounds
3. Paste it into Pangram → in rehearsals, it gets caught anyway. Point at the
   confidence score
4. **The kicker, narrated:** dedicated "humanizer" tools (GPT Humanizer and
   friends) exist precisely to rewrite AI text until it passes — and against
   strong humanizers, detection accuracy degrades. Show a rehearsal screenshot
   if you ran one; don't burn live time on it
5. Land the point: detection is a moving front in an arms race, not a settled
   fact. Policy and assessment design can't be outsourced to a classifier

**Why this demo can't fail:** if Pangram catches the paragraph, you've shown
modern detection is much better than people think. If it doesn't, you've shown
the arms race live. Either way you're right — say so out loud, it gets a laugh.

**Fallback:** rehearsal screenshots of steps 1–3.

---

## Timing discipline

Demos 1 and 4 are fixed points. If the morning runs long, Demo 2 compresses
to Skills-only (2 min) and Demo 3 compresses to the before/after screenshots.
Protect the labs — hands-on time is what they'll remember.
