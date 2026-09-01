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
(step 5 of the spine; cut again 9/1 — the ram-cover slide now carries image
generation), and the ElevenLabs voice clone + family safe word (in
§4, as the looking-real demo). The Ollama fake-citations live demo is dropped
to pay for it — it survives as a rehearsal screenshot on the §4 slide.
Mention on the Wed call that the safe-word tip is back in Ken's §4, so Ewa
isn't surprised.

**Revised 2026-09-01:** Bach/Gounod is now a **live Pet-in-Codex voice
conversation** — free-association follow-ups about the piece, ending with a
meta beat that tees up Ewa's §5 (tell her Wednesday). It demonstrates
conversation-as-the-unit-of-use, not a generation analogy. **All demos stay
in the menu (~33 full); Ken trims to fit the night before** — nothing is
pre-cut. Tech check moved up to Tue 9/1, 5 pm; laptop-audio-over-HDMI is the
headline item. **The §3 spine is now Ken's real semester** (academic
calendar lookup → portal schedule screenshot → no-class dates → one reminder
event → quiz → email) instead of a fictional printed syllabus — no
props, no phone transfer, no seeded calendar. Gemini Notebook demoted to a
night-before option (old notebooks underwhelmed in rehearsal).

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

- **Tue Sept 1, 5:00 pm — TECH CHECK in the Washington Room (moved up from
  Thu).** HDMI video and the mics are expected to be fine. **The real
  question is laptop audio through the house system** — it should ride the
  HDMI connection, but someone may need to find the volume knob, and
  multiple demos depend on it (Bach/Gounod playback, voice-clone mp3, Pet
  voice out). Checklist:
  - [ ] HDMI audio broadcasts; identify the volume knob and who controls it
  - [ ] Bach/Gounod-style audio and the voice-clone mp3 at room volume
  - [ ] **Pet round-trip**: its output goes out over HDMI, but its INPUT is
        the laptop mic — speak to it from where you'll actually stand, and
        confirm it doesn't hear itself through the house speakers (echo)
  - [ ] Interrupting the Pet mid-answer works in the room
  - [ ] Font sizes / Ollama app text from the back rows
- **Wed Sept 2, 10:00** — sync call with Ewa (calendar invite received);
  Sonia wants structure/slides visibility early that week. Send the deck
  before this call if possible.
- **Thu Sept 3** — on campus; now free for follow-ups if the 5 pm check
  surfaces anything.
- **Fri Sept 4** — fallback day. James's and Andrew's slides likely arrive
  this late; combine into the master deck as they land.
- **Sun Sept 6** — the session (not the first slot of the day).

## Pre-flight (morning of)

- [ ] Combined deck (James + Ewa + Ken + Andrew) loaded and page-through
      tested; ours exported to PPTX/PDF as the fallback for the live Slidev
- [ ] Browser tabs, in run order: Tokenizer Playground (loaded once — it
      fetches on first use), claude.ai (calendar connector connected),
      Trinity portal on "My Course Schedule" (signed in; only the schedule
      page ever goes on screen), Google Calendar, Outlook web (Trinity);
      Gemini Notebook only if it made the cut — signed into the personal
      Gmail account
- [ ] Portal schedule screenshot pre-shot on the desktop as the fallback
- [ ] Demo/scrubbed inbox only — never project real student mail
- [ ] Bach/Gounod audio in `demo-assets/`, cued, plays through room speakers
- [ ] **Codex Pet ready**: voice in/out through the house system, mic pickup
      tested from stage position, interruption rehearsed, the Bach/Gounod
      follow-up chain run once that morning
- [ ] ElevenLabs key working; `demo-assets/voice-clone-demo.mp3` plays
      through the room's speakers as the clone fallback
- [ ] Sycophancy pushback prompt and the car wash question rehearsed **that
      morning** — models change weekly. Ollama app open, `gemma4:12b-mlx`
      selected, thinking display hidden, text size checked
- [ ] Rehearsal screenshot of gemma4 fabricating five citations (for the §4
      slide beat)
- [ ] Phone charged (no longer load-bearing — the spine runs from the
      laptop)
- [ ] Screen mirroring, terminal ≥ 18pt, browser zoom 125%
- [ ] Rehearsal screenshots for every demo in one folder, in run order
## Between sessions (reset — session one leaves state behind)

- [ ] **Delete the no-class reminder event** session one added to the
      calendar
- [ ] Discard the Copilot email draft (if the email demo made the cut)
- [ ] Start a fresh Claude conversation (memory still knows you — the
      Hartford beat re-fires); close the Pet conversation and any notebook
      chat so session two starts from the same blank state
- [ ] Re-cue the Bach/Gounod audio and the voice-clone fallback mp3
- [ ] Battery/power check; re-silence notifications

---

## Run order (~30 min)

| Clock | Segment | Min |
| ----- | ------- | --- |
| 0:00 | §1 What AI actually is (slide) | 2 |
| 0:02 | §2 How it works (slide) → **Demo: tokenizer** → **Demo: Bach/Gounod Pet conversation** | 8 |
| 0:10 | §3 What it does well (slides + ram cover) → **Demo: my real semester** (find calendar → read schedule → one reminder → quiz → email) | 10 |
| 0:20 | §4 What it does poorly (slide + citations screenshot; pending asset) → **Demo: sycophancy** → **Demo: voice clone** | 7 |
| 0:27 | §6 Verification (slide) → **Demo: click the sources** | 3 |
| 0:30 | Closing slide, hand back to Ewa (she opens with §5) | 1 |

(§5, effective use, is Ewa's — per her 8/27 email.) **This is the full menu,
~31 with everything — deliberately.** Every demo stays available; **Ken
trims to fit the night before (Sat)** by choosing among: the email step,
the Pet follow-up count, sycophancy live vs. screenshot. Nothing is pre-cut. Live overrun ladder (for slippage on the
day, after night-before choices): compress §1 to one breath → cap the Pet
conversation at two follow-ups (skip the meta beat, keep the Ewa tee-up) →
drop the sycophancy demo (keep the slide bullet — say it in a sentence).
The spine, the Pet conversation, and the voice clone are the fixed points.

---

## §1 — What AI actually is (slide only, 2 min)

A bullet or two on history, no more: in progress since the 1950s; what changed
is massive data + massive computation + algorithmic breakthroughs landing
together. Familiar examples do the defining: they've used recommendation
systems (Spotify, TikTok, Netflix) for years — that's AI; ChatGPT and image
generators are the *generative* kind. Model vs. system in one sentence:
the model is the engine, ChatGPT/Copilot/BoodleBox are cars built around one.

---

## §2 — How it works → tokenizer + the Pet conversation (8 min)

Slide first (how autoregressive language models generate text, tokens,
next-token prediction, context, and tools), then evidence:

1. Tokenizer playground: type "Trinity College", paste a sentence from the
   academic calendar page, switch the vendor dropdown — common words one token, rare words
   shatter. (Optional aside if there's a breath to spare — the car wash
   problem: *"I need to wash my car. There's a carwash 50m away. Should I
   walk or drive?"* Many models, even reasonably good ones, advise walking —
   the car has to be there. Rehearse which model that morning; a correct
   answer kills the joke. Bach/Gounod carries the mechanism beat now.)
2. **Bach/Gounod, in conversation (~5 min) — the §2 centerpiece.** This is
   NOT a generation analogy; it's a live demonstration of *conversation as
   the way to use these tools*. Play Bach's Prelude in C major alone, then
   Gounod's melody over it. **TODO(Ken): audio files + cue points — drop in
   `demo-assets/`, note them here.** Then the **Pet in Codex, by voice**
   (interruptible — interrupt it at least once, naturally): *"Was this a
   common practice?"* → *"Did Gounod do this with other pieces?"* → *"Was
   Bach a common source for this sort of thing?"* → *"What are some other
   examples?"* Follow the thread wherever it actually goes — the
   free-association is the demo. **Push back once on purpose** ("really? I
   thought…") — plants the seed the §4 sycophancy demo pays off.

**Beats:** "You don't ask an AI what you'd ask a search engine. It's not
about retrieving a fact — it's a conversation that builds understanding, and
you're free — encouraged — to push back." Mechanism callback in one
sentence: every follow-up worked because the whole conversation is the
context — that's the context bullet, live. **Then go meta:** "Everything you
just watched was live. Is this a good way to use these tools? What would you
watch out for?" — one beat of silence — "Hold that thought: that's exactly
what Ewa's section is about." (Tell Ewa on the Wed call so she can catch
the pass.)

**Fallback ladder:** pet misbehaves → same conversation typed in a chat
window (loses charm, keeps content); AV fails → rehearsal screenshots,
narrate one exchange. Tokenizer fallback: OpenAI tokenizer page.

**Tech check (Tue 5 pm):** laptop mic pickup for the pet from stage
position, pet audio through the house speakers, echo/self-hearing,
interruption behavior in a big room.

---

## §3 — What it does well → my real semester (up to 10 min, full menu)

Slide first (common capabilities and their limits: explanation, option
generation, repetitive transformations, multiple mediums, and practice), then
the centerpiece — **my actual fall semester, all real, no props.** One
Claude conversation carries steps 1–4 (revised 9/1; replaces the fictional
printed-syllabus version — steps in git history):

1. **Find it** — *"Find the current Trinity approved academic calendar."*
   It picks Trinity College Hartford — not Dublin, not Oxford — because the
   system knows you. **Say so out loud:** that's the context slide and
   model-vs-system, live. (If it asks "which Trinity?" instead, that's also
   a fine beat — it asks when context is missing.)
2. **Read it** — paste the portal **"My Course Schedule"** screenshot (Fall
   2026: Mon 1:30–4:10 lecture, Tue seminars, senior project TBA).
   *"Which dates won't my classes meet this fall?"* Vision plus reasoning
   against the calendar it just found — Labor Day, fall break, Thanksgiving,
   and any Trinity day-swap quirks. **Date arithmetic is where models slip:
   verify one no-class date against the calendar page on screen before
   going further** — verification inside the successful workflow. A live
   mistake here is §6 arriving early, not a failure.
3. **Remind me** — *"Add a reminder to my calendar for the first week we
   don't meet."* **Pause on the permission prompt:** "It's asking before it
   acts. Read exactly what it wants to do — and afterwards, check what it
   changed." (Permission is not the same as privacy or correctness — don't
   overclaim what the prompt guarantees.) Point at the ⚿ chip on the slide;
   say yes; show the event land in the calendar tab. "And it could add all
   of them." **Delete the event between sessions.**
4. **Quiz me** — same conversation: *"Quiz me on [week-1 reading / what we
   just worked out]. One question at a time. Don't give me the answer until
   I've tried twice."* Answer one wrong on purpose; let it coach. **This is
   the beat that decides whether they hear 'cheating machine' or 'study
   partner' — do not rush it.** *Night-before option:* run it in Gemini
   Notebook on a **fresh** notebook if it impresses in rehearsal (the old
   ones didn't) — say "(formerly NotebookLM)" once if used; personal Gmail
   account, and be signed into it before walking on. **TODO(Ken): pick the
   quiz content.**
5. **Email it** — Copilot/Outlook: *"Draft an email to my students listing
   the dates we won't meet this fall."* (The portal page literally has an
   "Email all my classes" link.) Read it aloud, edit one sentence live: it
   proposes, you decide. (Night-before candidate for trimming.)
(Poster step cut 9/1 — the ram slide covers image generation, and a
schedule visual is text-heavy, which image models still garble.)

**Fallback:** pre-shot portal screenshot on the desktop, rehearsal
screenshots of the no-class-dates answer and the quiz exchange, saved email
draft. Any one can go static; not all of them.

**Rehearsal checks:** (a) Claude actually disambiguates to Hartford from the
account you present from; (b) the 2026–27 approved academic calendar page
is findable and current; (c) the calendar connector is connected and the
permission prompt fires on the write.

---

## §4 — What it does poorly → two demos (7 min)

Slide first (variable outputs, sycophancy, looking-real-vs-being-real, and the
limits introduced by training data, prompts, system instructions, and tools).
Newer systems reduce fabrication, but none eliminate it; price and model size
are not guarantees. **Pending asset:** during rehearsal, capture the fabrication screenshot.
**9/1 rehearsal — use the 12b model with a student-style prompt:**
`ollama run gemma4:12b-mlx --think=false "I'm writing a paper on how Gounod's
Ave Maria was received in 19th-century Paris. List five sources I can cite,
with author, year, and journal."` → five confident fabrications (invented
Adler/Moore citations, a nonexistent Charles Rosen title, wrong date for the
piece itself), no hedging. **Do NOT use `gemma4:latest`** — it shows its
thinking and labels the sources "representative," which kills the beat. Add
the screenshot (cropped to one legible citation + the proof it doesn't
exist) as rendered content on the §4 "perfect-looking citation" slide before the final export. Until
then, describe it in one breath.

**Disclosure beat (say it whenever the fabrication evidence is up):** "This
is one small model running on my laptop, with one prompt — a bigger model,
or one with search, would likely do better." Bonus honesty beat that makes
it stronger: "The bigger version of this same model actually declined — it
warned me its sources were only 'representative.' The smaller one invented
five citations without blinking. Same family, same question — and from the
chat window, you can't tell which kind you're talking to." Then:

### Demo: watch it fold (sycophancy)

Rehearsed pushback: ask a question with a checkable right answer, get the
right answer, then insist confidently that it's wrong. See whether it
apologizes and agrees. Behavior varies — rehearse the exact model and question
that morning, and keep a rehearsal screenshot as backup.

**On stage: run the local-model demos in the Ollama app** (model picker →
`gemma4:12b-mlx`), not a terminal — a chat window reads as an app and
projects better. The CLI commands below are for rehearsal/screenshots.
**Tech check (Tue 5 pm): confirm the app hides/collapses the model's
thinking display** (CLI needed `--think=false`) **and that chat text is
readable from the back rows.**

**9/1 rehearsal (re-verify morning-of):** `gemma4:12b-mlx --think=false`,
ask *"What year was Trinity College in Hartford founded? One sentence."*
(1823, correct), then push: *"No, that's wrong — it was founded in 1845. I'm
absolutely certain, I teach there."* → instant fold: "I apologize for the
error; you are correct… founded in 1845." Bonus: it's the room's own school,
checkable on trincoll.edu in five seconds.

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
Gounod reception topic from §2 (the rehearsed prompt), click one, find the quoted passage
in the actual source. Thirty seconds. Calibration beat lands here too:
"Newer systems reduce fabrication, but no model, product tier, or polished
interface removes the need to check."

**Beat:** "Fluent prediction is not verified evidence. Open the source, check
the passage, and ask whether the evidence actually supports the claim."

**Second verification move (30 sec):** tell it you *liked* its answer — then
ask it to argue the exact opposite. If it flips with equal confidence, you've
just measured what its confidence is worth. Keep the framing on *testing the
answer* (verification), not on how-to-use-AI — usage tips are Ewa's §5.

---

## Closing (1 min)

Ken's framing, the mnemonic that ties every demo together: **"They're eager
toddlers. They want you to keep talking to them, and they want you to be
happy — and they have a toddler's tenuous grasp on reality. So verify
anything important. Ask for help thinking, not for a way out of thinking."**
The metaphor is a memory hook, not a mechanism — §2 already gave the
mechanism; this is how they'll retell it.

Then the explicit handoff, *before* the bio on screen reads as "the end" and
triggers applause: "That's my part — and I skipped number five on purpose,
because Ewa owns it. Ewa?"

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
- (The Codex Pet is un-parked: it's now the §2 conversation vehicle. The
  email demo is back in the §3 menu as a night-before choice.)
- **Ollama fake-citations pair** (gemma4 invents sources / frontier-with-
  search doesn't) — dropped 8/31 to pay for the restored demos; survives as
  the rehearsal screenshot on the §4 slide and the §6 click-the-sources
  habit. Full live steps in git history on this file.
- **Pangram detection** — detection adjacency reads as "we'll catch you";
  that conversation belongs to Ewa's integrity segment if anywhere.

(Voice clone + family safe word: restored to §4 on 8/31 — no longer parked.
Tell Ewa on the Wed call so the safety-tip conversation doesn't double up.)
