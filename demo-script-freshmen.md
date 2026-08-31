# Demo Script — First-Year Orientation (September 6)

Instructor-only. Companion to `slides-freshmen.md` — restructured 2026-08-27
after the planning meeting: **Ken delivers outline sections 1–4 and 6** (what
AI is → how it works → does well → does poorly → verification), with demos as
evidence inside each section. Ewa MCs, then follows Ken with **§5 (how to use
AI effectively)**, AI-in-college, and the academic integrity policy; Andrew
closes with the year's events. **Stay off §5, integrity, policy, and
where-AI-is-headed — those are hers.** Slide numbering keeps the shared
outline's numbers, so our deck jumps 4 → 6 deliberately.

**Revised 2026-08-31 (per Ken, via the Desktop planning session):** restored
Bach/Gounod (in §2, replacing raspberry/9.11), the Nano Banana study poster
(step 5 of the spine), and the ElevenLabs voice clone + family safe word (in
§4, as the looking-real demo). The Ollama fake-citations live demo is dropped
to pay for it — it survives as a rehearsal screenshot on the §4 slide.
Mention on the Wed call that the safe-word tip is back in Ken's §4, so Ewa
isn't surprised.

## Session facts

- **Washington Room, Mather (2nd floor)** — theater stage, large projector,
  audio confirmed. Two sessions, ~200–250 students each.
- Order: James (welcome) → Ewa (intro, MC) → **Ken, ~30 min** → Ewa (~15 min)
  → Andrew.
- Ken presents everyone's slides from his machine and owns the screens.
  Common format: PowerPoint / PDF. Export ours:
  `npx slidev export slides-freshmen.md --format pptx` (or `--format pdf`).
- **Tone guardrail:** this must not read as marketing or advocacy. Mechanism
  and evidence. "This is what's possible; what you'll have access to varies
  and will change" — never "you must use this."

## Deadlines

- **Wed Sept 2, 10:00** — sync call with Ewa (calendar invite received);
  Sonia wants structure/slides visibility early that week. Send the deck
  before this call if possible.
- **Thu Sept 3** — on campus: tech check in the Washington Room. **Email the
  AV/setup person now for an appointment** (new person; name is in the email
  thread). Test: HDMI, audio, both demo laptop setups, font sizes from the
  back rows.
- **Fri Sept 4** — fallback day. James's and Andrew's slides likely arrive
  this late; combine into the master deck as they land.
- **Sun Sept 6** — the session (not the first slot of the day).

## Pre-flight (morning of)

- [ ] Combined deck (James + Ewa + Ken + Andrew) loaded and page-through
      tested; ours exported to PPTX/PDF as the fallback for the live Slidev
- [ ] Browser tabs: Tokenizer Playground (loaded once — it fetches on first
      use), a frontier chat with search (claude.ai or ChatGPT), Gemini
      Notebook, Gemini (image generation), Outlook web (Trinity), calendar
- [ ] Bach/Gounod audio in `demo-assets/`, cued, plays through room speakers
- [ ] ElevenLabs key working; `demo-assets/voice-clone-demo.mp3` plays
      through the room's speakers as the clone fallback
- [ ] Sycophancy pushback prompt and the car wash question rehearsed **that
      morning** — models change weekly (if either uses a local model, Ollama
      running)
- [ ] Rehearsal screenshot of gemma4 fabricating five citations (for the §4
      slide beat) and a pre-generated study poster, both in the folder
- [ ] Phone charged, camera ready, mirroring tested; pre-shot syllabus photo
      on the desktop as fallback
- [ ] Printed syllabus (the prop) in the bag
- [ ] Demo/scrubbed inbox only — never project real student mail
- [ ] Screen mirroring, terminal ≥ 18pt, browser zoom 125%
- [ ] Rehearsal screenshots for every demo in one folder, in run order

---

## Run order (~30 min)

| Clock | Segment | Min |
| ----- | ------- | --- |
| 0:00 | §1 What AI actually is (slide) | 2 |
| 0:02 | §2 How it works (slide) → **Demo: tokenizer** → **Demo: Bach/Gounod** | 6 |
| 0:08 | §3 What it does well (slide) → **Demo: syllabus spine + poster** | 12 |
| 0:20 | §4 What it does poorly (slide + citations screenshot; pending asset) → **Demo: sycophancy** → **Demo: voice clone** | 7 |
| 0:27 | §6 Verification (slide) → **Demo: click the sources** | 3 |
| 0:30 | Closing slide, hand back to Ewa (she opens with §5) | 1 |

(§5, effective use, is Ewa's — per her 8/27 email.) On paper this is ~31
against a 30-minute slot — the cut order is live, not theoretical. Overrun
order: compress §1 to one breath → drop the email step of the spine → drop
the Nano Banana poster → drop the sycophancy demo (keep the slide bullet —
say it in a sentence). The spine and the voice clone are the fixed points.

---

## §1 — What AI actually is (slide only, 2 min)

A bullet or two on history, no more: in progress since the 1950s; what changed
is massive data + massive computation + algorithmic breakthroughs landing
together. Familiar examples do the defining: they've used recommendation
systems (Spotify, TikTok, Netflix) for years — that's AI; ChatGPT and image
generators are the *generative* kind. Model vs. system in one sentence:
the model is the engine, ChatGPT/Copilot/BoodleBox are cars built around one.

---

## §2 — How it works → tokenizer + Bach/Gounod (6 min)

Slide first (how autoregressive language models generate text, tokens,
next-token prediction, context, and tools), then evidence:

1. Tokenizer playground: type "Trinity College", paste a sentence from the
   syllabus, switch the vendor dropdown — common words one token, rare words
   shatter. (Optional aside if there's a breath to spare — the car wash
   problem: *"I need to wash my car. There's a carwash 50m away. Should I
   walk or drive?"* Many models, even reasonably good ones, advise walking —
   the car has to be there. Rehearse which model that morning; a correct
   answer kills the joke. Bach/Gounod carries the mechanism beat now.)
2. **Bach/Gounod (~3 min):** play Bach's Prelude in C major alone, then
   Gounod's Ave Maria over it — a new melody composed over an existing
   structure, every note shaped by the pattern underneath.
   **TODO(Ken): audio files + cue points — drop in `demo-assets/`, note
   them here.**

**Beat:** "For this language model, text is represented as tokens, not words,
and generation happens one token at a time. Gounod gives us an analogy for new
material fitting an existing structure — with an important limit: he composed
deliberately; the model generates statistically. Fluent is not the same as
verified, and that's the frame for everything else today."

**Fallback:** OpenAI tokenizer page; describe Bach/Gounod in one sentence and
move on — the tokenizer already made the mechanism point.

---

## §3 — What it does well → the syllabus spine + poster (12 min)

Slide first (common capabilities and their limits: explanation, option
generation, repetitive transformations, multiple mediums, and practice), then
the one-document-five-tools centerpiece:

1. **Photograph it** — hold up the printed syllabus, shoot it with the phone,
   *"Extract every date, deadline, and reading into a table."*
2. **Schedule it** — calendar connector: *"Build a study schedule for the
   first six weeks, check conflicts, add the blocks."* **Pause on the
   permission prompt:** "It's asking. It can't touch what I haven't allowed."
   Point at the ⚿ chip on the slide; repeat the pause on any later
   permission prompt — same beat, same chip.
3. **Quiz me on it** — in **Gemini Notebook** — say "(formerly NotebookLM)"
   once, then just Gemini Notebook: *"Quiz me on week 1. One question at a
   time. Don't give me the answer until I've tried twice."* Answer one wrong
   on purpose; let it coach. **This is the beat that decides whether they
   hear 'cheating machine' or 'study partner' — do not rush it.**
4. **Email about it** — Copilot/Outlook: draft the professor email about the
   week-6 conflict. Read it aloud, edit one sentence live: it proposes, you
   decide. (First thing to drop on overrun.)
5. **Poster it (~2 min)** — Nano Banana (Gemini image generation): *"Turn
   this syllabus into a one-page study poster / six-week timeline diagram."*
   The repo's `image-prompt` skill can pre-write the prompt during rehearsal.
   (Second thing to drop.)

**Fallback:** pre-shot photo, pre-built calendar, quiz screenshot, saved
draft, pre-generated poster. Any one can go static; not all five.

---

## §4 — What it does poorly → two demos (7 min)

Slide first (variable outputs, sycophancy, looking-real-vs-being-real, and the
limits introduced by training data, prompts, system instructions, and tools).
Newer systems reduce fabrication, but none eliminate it; price and model size
are not guarantees. **Pending asset:** during rehearsal, capture gemma4
inventing five perfect-looking scholarly sources (`ollama run gemma4`, *"Give
me five scholarly sources on [niche topic from the syllabus], with authors,
years, and journals."*) and add the screenshot as rendered content on the §4
slide before the final export. Until then, describe it in one breath. Then:

### Demo: watch it fold (sycophancy)

Rehearsed pushback: ask a question with a checkable right answer, get the
right answer, then insist confidently that it's wrong. See whether it
apologizes and agrees. Behavior varies — rehearse the exact model and question
that morning, and keep a rehearsal screenshot as backup.

**Beat:** "This is sycophancy: the response followed my pressure instead of
the evidence. Confidence is not evidence. The behavior varies by model and
prompt, which is why I rehearsed this exact example."

### Demo: looking real vs. being real (the voice clone)

Adapted from the workshop's Demo 5 (full steps in `demo-script.md`). ~3 min.

1. Say a topical sentence about **this morning** out loud — specific to
   today, so the room knows it wasn't pre-recorded.
2. Have the clone speak the identical words (run from this repo's folder so
   Claude Code knows the voice id from `CLAUDE.md` — no pasting IDs on
   stage). The side-by-side — your voice, then the clone, same sentence —
   is the demo. Narrate the few seconds of delay; it's suspense, not lag.
3. Let the room sit in the uncanny valley for a beat.

**Beats:** "I consented to this — I created that voice clone on purpose."
Voice is no longer proof of identity. **The take-home: for an urgent call,
hang up and call the person back on a number you already know.** A private
family phrase can be a second check, but it is not a guarantee. Say it slowly;
it's the most repeatable tip of the day. It's also the citation lesson in a
different medium: looking real — sounding real — is not being real.

**Fallback:** `demo-assets/voice-clone-demo.mp3` through the room speakers.

---

## §6 — Verification → click the sources (3 min)

Slide first (wrong on simple things, right on hard ones; confidence ≠ truth),
then the undramatic habit — self-contained now that the Ollama contrast is
gone: in the frontier chat with search on, ask for scholarly sources on the
niche syllabus topic (the old §4 prompt), click one, find the quoted passage
in the actual source. Thirty seconds. Calibration beat lands here too:
"Newer systems reduce fabrication, but no model, product tier, or polished
interface removes the need to check."

**Beat:** "Fluent prediction is not verified evidence. Open the source, check
the passage, and ask whether the evidence actually supports the claim."

---

## Closing (1 min)

"Prediction produces possibilities. Verification tests them." Tools change
every year they're here; keep the durable framework: distinguish the model
from the system, recognize pattern generation, and check claims against
evidence. Hand back to Ewa.

---

## Cut demos — parked, not deleted

Kept here with their old prep notes in git history (`git log` on this file);
usable for the faculty/adult version or future sessions:

- **Deep Research bookend** (start at minute zero, open at the end) — the
  best "what agents are" demo; doesn't fit the six-section brief.
- **Wispr dictation opener** — lovely accessibility beat; could still sneak
  in as a 20-second aside while typing a prompt in §3, if rehearsal shows it
  doesn't cost time.
- **Lyrics trainer** ("nobody typed any code") — reads as marketing under
  the new tone guardrail; keep for the AI Lab sessions.
- **Codex pet + Halo lamp** — agents/ambient status; AI Lab material now.
- **Ollama fake-citations pair** (gemma4 invents sources / frontier-with-
  search doesn't) — dropped 8/31 to pay for the restored demos; survives as
  the rehearsal screenshot on the §4 slide and the §6 click-the-sources
  habit. Full live steps in git history on this file.
- **Pangram detection** — detection adjacency reads as "we'll catch you";
  that conversation belongs to Ewa's integrity segment if anywhere.

(Voice clone + family safe word: restored to §4 on 8/31 — no longer parked.
Tell Ewa on the Wed call so the safety-tip conversation doesn't double up.)
