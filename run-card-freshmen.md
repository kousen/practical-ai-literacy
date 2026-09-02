# Run card — First-Year Orientation, Sun Sept 6

**Print this.** The screen is mirrored, so speaker notes are invisible on
stage; this page is what you can see. Full detail: `demo-script-freshmen.md`.

**Clock (full menu ~29):** §1 2 · §2 8 · §3 8 · §4 7 · §5 3 · close 1

---

## §1 What AI is (5 slides, fast)

Decades old; you've used it for years (Spotify, spam filters) · generative
creates · **model = engine, you drive the system** · **some say things, some
do things — doing needs permission; watch for that moment today.**

## §2 How it works (8)

- **Tokenizer:** "Trinity College" → a sentence from the academic calendar
  page → switch vendors.
- **Ave Maria** (YouTube Music tab, ~30 s): "that's Bach, 1722… and that's
  Gounod, 1852, on top."
- **Pet (Codex, voice):** *Was this a common practice?* → *Did Gounod do
  this with other pieces?* → *Was Bach a common source for this?* → *Other
  examples?* Interrupt once. Push back once ("really? I thought…").
  Callback: every follow-up worked because the conversation is the context.
- **Meta, to the Pet:** *"Everything we just did was live. Is this a good
  way to use a tool like you? What should I watch out for?"* → "Ewa will
  have more to say about that."

## §3 What it does well (8)

- Five strengths — seconds each, spoken over. On "practice": *"quiz me, don't
  tell me"* is the prompt worth memorizing.
- **Ram cover:** real cover first → NEXT → ram. "I used Nano Banana." Others
  on my home page.
- **My actual fall semester** (Claude app on phone, mirrored — or claude.ai):
  1. *"Find the current Trinity approved academic calendar."* → Hartford,
     not Dublin — the system knows me.
  2. Photo of the schedule → *"Which dates won't my classes meet this
     fall?"* → **verify ONE date against the calendar page.**
  3. *"Add a reminder to my calendar for the first week we don't meet."*
     → ⚿ **"Steps 1 and 2 were saying. This is doing. It's asking before it
     acts — read what it wants to do; afterwards check what it changed."**
     Yes → show it land. "It could add all of them."
  4. Copilot/Outlook: *"Draft an email to my students listing the dates we
     won't meet this fall."* **Draft, don't send.** Edit one sentence: it
     proposes, I decide.

## §4 What it does poorly (7)

- **Car wash** (Ollama app, gemma4:12b-mlx): *"I need to wash my car.
  There's a carwash 50m away. Should I walk or drive?"* → "walk." **Read
  reason 3 aloud** (it names the car). "It isn't reasoning — it's completing
  a pattern." Disclosure: one small model, one prompt; bigger ones often get
  it; you can't tell which kind you're talking to.
- Variance slide · sycophancy slide.
- **Fold** (same model): *"What year was Trinity College in Hartford
  founded? One sentence."* (1823) → *"No, that's wrong — it was founded in
  1845. I'm absolutely certain, I teach there."* → it folds. "Confidence is
  not evidence."
- **Citation slide, spoken:** it knows what a real citation *looks* like;
  newer systems with search fabricate far less; free ones still might.
- **Voice clone:** say a sentence about *this morning* aloud → Claude Code
  (this repo): *"Say the following in my voice: …"* → play. "I consented to
  this." Voice is no longer proof of identity. **Take-home: urgent call →
  hang up, call back on a number you already know. A family phrase is a
  second check, not a guarantee.**

## §5 Verify (3)

- Opener (Ewa's section follows).
- **Open the source** (frontier chat, search on): *"Give me five scholarly
  sources on the reception of Gounod's Ave Maria in 19th-century Paris."*
  Click ONE → find the passage. Thirty seconds.
- Second move: *"I liked that answer — now argue the exact opposite."* →
  "That doesn't tell you which is true; it tells you the confidence carries
  no information."
- Show its work · the essential check.

## Close (1)

**Eager toddlers** — keep talking, want you happy, toddler's grasp on
reality → verify anything that matters → *"Ask for help thinking, not for a
way out of thinking."* Then, before the bio reads as "the end":
**"That's my part — Ewa takes it from here. Ewa?"** (QR is on screen.)

---

**Fallbacks:** tokenizer → OpenAI tokenizer page · Pet → same conversation
typed → screenshots · spine → pre-shot screenshot / rehearsal screenshots ·
car wash & fold → screenshots · voice → `demo-assets/voice-clone-demo.mp3` ·
no wifi → Ave Maria offline on phone; Ollama is local.

**Cut ladder (live slippage only):** compress §1 → Pet to two follow-ups,
skip meta → drop the fold (keep the slide, say it). Fixed: spine, Pet,
voice clone.

**Between sessions:** delete the reminder event · discard the email draft ·
fresh Claude chat · close the Pet chat · re-cue Ave Maria + clone mp3 · DND
on · battery.

**Morning-of re-checks:** car wash + fold on the 12b · Hartford
disambiguation from the presenting account · calendar permission prompt
fires · academic calendar page loads · YouTube Music tab at the start.
