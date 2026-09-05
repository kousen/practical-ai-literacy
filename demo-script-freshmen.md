# Demo Script — First-Year Orientation (September 6)

Instructor-only. **On stage the screen is mirrored (tech check 9/1), so
speaker notes are NOT visible while presenting** — the notes and this file
are for prep and rehearsal; the brief cue document to read on the phone is
`run-card-freshmen.md`. Companion to `slides-freshmen.md` — restructured 2026-08-27
after the planning meeting: **Ken delivers outline sections 1–4 and 6** (what
AI is → how it works → does well → does poorly → verification), with demos as
evidence inside each section. Ewa MCs, then follows Ken with **how to use AI
effectively**, AI-in-college, and the academic integrity policy; Andrew
closes with the year's events. **Stay off effective-use tips, integrity,
policy, and where-AI-is-headed — those are hers.** (Since 9/2 the deck
numbers its sections 1–5 sequentially; the shared planning outline's 4 → 6
jump is gone — students don't care about the planning outline. "§5" below
means OUR verification section.)

**Current plan, Sept 5:** desktop for Slidev and all demos except scheduling.
Use the Claude app on the phone for the actual semester schedule, verify the
dates, then request an Outlook-compatible calendar file. The school has not
authorized a direct AI connector. Ken reports adding his actual class meetings
to Google Calendar successfully. After the phone demo, return to the desktop
and show the existing Google Calendar with only Trinity visible. Identify it
as an earlier import. The .ics file demonstrates the method students can use
without an authorized AI connector; an Outlook import is not part of the live flow.
**The "doing" beat (restored 9/5):** the app emails the .ics to Ken's Trinity
address — a real action with a real permission prompt (tested 9/5 from Claude
Desktop; approved once, never "always"). The say/do slide returns in §3 to set
it up; the ⚿ chip is back on the semester slide.
Both persuasion exercises are dropped. Sycophancy is one spoken sentence.
The shortened opening reaches tokens at 0:45 and the music/Pet around 2:00.
Historical plans for direct calendar writes, the quiz, and poster are superseded.

## Session facts

- **Washington Room, Mather (2nd floor)** — theater stage, large projector,
  audio confirmed. Two sessions, ~200–250 students each.
- Order: James (welcome) → Ewa (intro, MC) → **Ken, ~30 min** → Ewa (~15 min)
  → Andrew.
- Ken presents everyone's slides from his machine and owns the screens.
  Common format: PowerPoint / PDF. Export ours:
  the PDF is auto-published by the release action (`ai-tools-for-academic-success.pdf`); no PPTX needed (dropped 9/2). Local export if ever wanted: `npm run export:freshmen`.
- **Tone guardrail:** this must not read as marketing or advocacy. Mechanism
  and evidence. "This is what's possible; what you'll have access to varies
  and will change" — never "you must use this."

## Deadlines

- **Tue Sept 1, 5:00 pm — TECH CHECK in the Washington Room: DONE, all
  checks passed** (HDMI audio through the house system, Pet round-trip,
  phone over USB-C, QR scan from the projector, back-row readability).
  Original checklist kept for the Sunday morning re-run:
  - [ ] HDMI audio broadcasts; identify the volume knob and who controls it
  - [ ] Bach/Gounod-style audio and the voice-clone mp3 at room volume
  - [ ] **Pet round-trip**: its output goes out over HDMI, but its INPUT is
        the laptop mic — speak to it from where you'll actually stand, and
        confirm it doesn't hear itself through the house speakers (echo)
  - [ ] Interrupting the Pet mid-answer works in the room
  - [ ] Font sizes / Ollama app text from the back rows
  - [ ] **Phone over USB-C to the room's input** (adapter, folded vs.
        unfolded, DND on) — phone is now selected for the §3 workflow
- **Wed Sept 2, 10:00** — sync call with Ewa (calendar invite received);
  Sonia wants structure/slides visibility early that week. Send the deck
  before this call if possible.
- **Thu Sept 3** — on campus; nothing owed to the room after the clean
  check — no assets left to build; rehearsal only.
- **Fri Sept 4** — fallback day. James's and Andrew's slides likely arrive
  this late; combine into the master deck as they land.
- **Sun Sept 6** — the session (not the first slot of the day).

## Pre-flight (morning of)

- [ ] Slidev and current PDF fallback loaded; combined presenter order checked.
- [ ] Desktop tabs in order: tokenizer, YouTube Music recording, local Ollama,
      voice-clone workflow, and the BnF record used for source verification.
- [ ] Phone: Claude conversation ready, actual course-schedule screenshot
      available, current Trinity College Hartford academic calendar findable.
- [ ] Phone USB-C video, Do Not Disturb, power, and desktop reconnection tested.
- [ ] Rehearse the downloadable .ics file path in the phone app. Have a saved
      file and preview available if generation or download stalls.
- [ ] Review one included meeting, one excluded break/holiday, first/last dates,
      time zone and an occurrence after the daylight-saving transition.
- [ ] Cue document open on the phone. Switch to Claude before connecting it
      to the projector; reopen cues after disconnecting.
- [ ] Desktop Google Calendar: hide non-Trinity calendars and select a teaching
      week. Show the existing meetings without re-importing them.
- [ ] Gmail (send) permission set to ASK in the Claude app — approve once on
      stage, never "always"; one test send from the phone the night before
- [ ] For optional email: copy the verified date list into Copilot/Outlook;
      it does not inherit the phone conversation. Draft only.
- [ ] YouTube Music clip queued, room volume checked; offline phone copy ready.
- [ ] Pet voice input/output and interruption tested from the stage position.
- [ ] **Moonside Halo lamp on the podium, visible to the room** — it's the
      "is it thinking?" indicator for the Pet conversation (Codex hook) and
      flashes for the voice clone (Claude Code hook). Moonside phone app
      fully CLOSED (it steals the BLE connection); lamp in the same room;
      daemon running (`/tmp/moonside_daemon.log`). One sentence the first
      time it changes color — "blue means it's working, green means it's
      done" — then never mention it again. Nothing depends on it.
- [ ] Ollama car-wash prompt rehearsed; recorded answer already on the slide.
- [ ] Voice-clone fallback: demo-assets/voice-clone-demo.mp3, room audio checked.
- [ ] BnF record preloaded and saved locally for an offline source check.
- [ ] Browser zoom and projected light/dark mode checked; notifications silenced.
- [ ] Claude usage meter (Settings → Usage & billing): weekly limit was 42%
      left on 9/5. Stage usage is small (phone chat, one email send, seconds
      of Claude Code — the Pet is Codex's budget). Spend a usage-limit reset
      ONLY if the weekly bar is under ~15% in the morning; also check the
      weekly reset date — if it rolls over Sunday, ignore all this.

## Between sessions

- [ ] Reconnect desktop and reopen Slidev at the start.
- [ ] Start fresh phone/Pet conversations; re-cue music and clone fallback.
- [ ] Keep the checked .ics fallback; reset the Google Calendar view to the
      selected teaching week with only Trinity visible. Existing events stay put.
- [ ] Discard any optional email draft. Check power and Do Not Disturb.

---

## Run order (25-minute rehearsal target in a 30-minute slot)

| Clock | Segment | Min |
| ----- | ------- | --- |
| 0:00 | Title + §1 Familiar AI and generative AI (one content slide) | 0.75 |
| 0:45 | §2 **Demo: tokenizer** → prediction example → **Demo: Bach/Gounod Pet conversation** → context debrief | 6.75 |
| 7:30 | §3 Capabilities + ram cover → model/system → say/do → file/import distinction → **Demo: my real semester** (incl. the send + ⚿ prompt) → calendar slide | 8 |
| 15:00 | §4 **Demo: car wash** → brief limitations → **Demo: voice clone** | 5 |
| 20:00 | §5 Verification → **Demo: one claim and its source** | 4 |
| 24:00 | Closing slide, hand back to Ewa (she opens with effective use) | 1 |

(Effective use is Ewa's.) **Target 25 minutes in rehearsal, leaving five
minutes for reactions, transitions, and delays.** These are budgets, not
measured durations. Tokenizer at 0:45; music/Pet around 2:00.
Email is optional and uses buffer only if time permits. No live Outlook import.
Live cut ladder: cap Pet at two follow-ups (skip meta); end scheduling at the
downloaded file; use the recorded car-wash answer without a live rerun.
Protect the source check. Fixed: Pet conversation, schedule-file demo, voice clone.

---

## §1 — What AI actually is (title + one content slide, 45 sec)

0:00–0:20, over the title: "These tools can help with difficult things and
make surprising mistakes on easy ones. I want to show you how both happen."
0:20–0:45, one concrete comparison: Spotify can recommend an existing song;
a generator produces text, images, or audio in response to a request.
One sentence of background: "AI research goes back decades, and you've used
it in recommendations and spam filters. Today we're looking at generative AI."
Then show the tokenizer. Model/system and agents move to §3 beside the demo
that gives those distinctions a purpose.

---

## §2 — How it works → tokenizer + the Pet conversation (6 min 45 sec)

Show text fragments first, explain prediction second, and explain the
conversation's context after the audience has watched it in use:

1. **0:45–1:30: tokenizer.** Use either the live playground ("Trinity
   College" and one short sentence) or the prepared screenshot. Show the
   colored fragments, then name them "tokens": whole words, parts of words,
   or punctuation, represented by numbers. On the screenshot, "Collge" and
   "Let's" split; the period is separate. Counts are specific to that text
   and tokenizer. If live works, advance past the screenshot without a
   second explanation. No vendor tour or pricing aside.
2. **1:30–2:00: prediction.** "If I say 'Please pass the…', several
   continuations fit. If we were just talking about dinner, that changes
   which continuations fit." Explain that training learns patterns and an
   autoregressive language model generates one token at a time using the
   preceding context. The tokenizer showed representation; this analogy
   illustrates generation. "Fluent is not the same as verified."
3. **2:00–7:00: Bach/Gounod, in conversation (~5 min).** Give students an
   observation task: "Watch what changes when I ask a follow-up." This is
   NOT a generation analogy; it's a live demonstration of *conversation as
   the way to use these tools*. **Play ~30 seconds of the Ave Maria from
   YouTube Music** (subscription — no ads; tab queued to the chosen
   recording, at the start). The opening bars are Bach's prelude on its own
   — "that's Bach, 1722" — then the melody enters — "and that's Gounod,
   1852, on top." One clip does both halves. Then the **Pet in Codex, by voice**
   (interruptible — interrupt it at least once, naturally): *"Was this a
   common practice?"* → *"Did Gounod do this with other pieces?"* → *"Was
   Bach a common source for this sort of thing?"* → *"What are some other
   examples?"* Follow the thread wherever it actually goes — the
   free-association is the demo. **Challenge one claim:** "What evidence
   supports that?" Let students see questioning as well as fluent answers.

**Beat:** "The follow-up changes what we're asking, and we can ask for
evidence when a claim needs checking." Save the context explanation for the
debrief slide. **Then go meta — ask the Pet
itself, live:** "Everything we just did was live. Is this a good way to use
a tool like you? What should I watch out for?" Let it answer — interrupt if
it rambles; an AI listing its own failure modes *is* the demo. Then, simply:
"Ewa will have more to say about that." (No coordination needed; mention it
to her in passing.)

4. **7:00–7:30: context debrief.** Refer to an actual follow-up: "I didn't
   need to repeat who we were discussing. The earlier exchange gave the
   follow-up its meaning." The slide's "Did he do that elsewhere?" is an
   example. Training and tools also shape answers; remembering the exchange
   doesn't establish that its claims are true.

**Fallback ladder:** pet misbehaves → same conversation typed in a chat
window (loses charm, keeps content); AV fails → rehearsal screenshots,
narrate one exchange. Tokenizer fallback: the prepared screenshot on slide 3.

**Tech check (Tue 5 pm):** laptop mic pickup for the pet from stage
position, pet audio through the house speakers, echo/self-hearing,
interruption behavior in a big room.

---

## §3 — What it does well → my real semester (7 min 30 sec)

One capabilities slide (~20 sec), the ram-cover reveal (~15 sec), then
model/system and file/import distinction (~30 sec). The ram and its caption
reveal together. Connect the phone only for the scheduling demo.

### Phone: find, read, check, export

1. **Find it:** "Find the current Trinity College Hartford approved academic
   calendar." Check the institution and year on the source page. Finding the
   correct college does not establish whether the app used personal memory.
2. **Read it:** provide the actual portal course-schedule screenshot.
   "List my class meetings this fall, with dates, local start/end times,
   locations, and the dates they will not meet. Use the approved academic
   calendar. Ask me about missing details; do not assign times to TBA items."
3. **Check it:** compare one included meeting and one excluded holiday/break
   with the actual schedule and academic calendar. Confirm the term limits.
   The output needs checking even if a previous Google import succeeded.
4. **Export it:** ask for the file below and a readable preview. Show the
   download and one previewed event.
5. **Send it:** *"Email that .ics file to my Trinity address."* **Pause on
   the permission prompt** — point at the ⚿ chip: "Steps 1–4 were saying.
   This is doing — and it's asking before it acts. Read what it wants to do;
   approve once, never 'always.'" Approve → the file lands in the Outlook
   inbox, exactly where it gets imported from. (Tested 9/5 from Claude
   Desktop: real prompt, file arrived. **Confirm once from the phone tonight**
   — permissions are per account, so it should ask there too.) Fallback:
   download/share the file from the phone — no prompt; say so plainly.
   Then: "The file is ready. It hasn't changed Outlook. I review it, then
   choose whether to import it."

**Copy-ready file prompt:**

> Using the class meetings and exceptions we just checked, create a
> downloadable iCalendar (.ics) file I can import into Outlook. Include only
> confirmed class meetings for this term, excluding confirmed holidays and
> breaks. Preserve start/end times in America/New_York across daylight-saving
> changes. Include locations only where provided. Do not invent TBA meetings,
> add attendees, or send invitations. Also show a readable preview with the
> total number of meetings, first and last dates, excluded dates, and one
> meeting after the daylight-saving transition. Ask me about unresolved
> details before creating the final file.

Rehearse the download in the exact phone app. File creation does not verify
the schedule; the source comparison is the verification. On stage, inspecting
one included and one excluded date illustrates that habit without reading the
whole semester. Before using it for real, review the full file/preview.

**Ken's existing result:** actual class meetings were added to Google Calendar
without problems (reported Sept 5). You can mention or show that as a prior
result, clearly labeled. It does not prove the new file imports correctly into
the school's Outlook account, and it is not a reason to duplicate those events.

### Return to desktop

Disconnect the phone, reopen the cue document, and show desktop Google Calendar
with only the Trinity calendar visible. Select a representative teaching week;
collapse the sidebar after filtering if that improves readability.
The next slide is a cropped screenshot of that calendar (Sept 5) — no tab
switch needed. Say: "I imported these meetings earlier. Here's how they look."
The existing events illustrate the result; do not imply they came from the file
just generated. Explain that students can open/import an .ics file today. If
the college authorizes a connector later, the tool could add events directly.
Return to Slidev for the car-wash sequence.

**Outlook reference for preparation, not a live step:** transfer the file from
phone to desktop. In Outlook on the web, Calendar → Add calendar → Upload
from file → choose the .ics → select a separate demo calendar → Import and Save.
Inspect a resulting event. School configuration may affect availability; if
the account does not offer import, finish at the checked file and say so.
An import is a snapshot, not a subscription or ongoing synchronization.
Do not assume re-importing will update or deduplicate existing events.

Optional email, time permitting: paste the checked date list into desktop
Copilot/Outlook and ask for a draft. It has no access to the phone conversation
unless you supply it. Read and edit one sentence; do not send to real students.

**Fallback:** pre-shot course schedule, checked .ics file with readable preview,
and an image of the previously imported Google events. No account changes are
needed to demonstrate the output.

[Sources]
Microsoft, work/school account import instructions and snapshot limitation:
https://support.microsoft.com/en-us/outlook/import-or-subscribe-to-a-calendar-in-outlook-com-or-outlook-on-the-web
Ken's reported Google Calendar result and school connector restriction, Sept 5.
[/Sources]

---

## §4 — What it does poorly → car wash and voice clone (5 min)

Keep the transition brief. Use the car wash for an obvious error and the voice
clone for convincing imitation. Sycophancy gets one spoken sentence only.
Newer systems reduce fabrication, but none eliminate it; price and model size
are not guarantees.

### Demo: the car wash (confidently wrong on a simple thing)

Right after the §4 opener slide — **two slides with the live run between
them.** Slide 1 typesets the exact question at room-readable size and labels
the model (`gemma4:12b-mlx` in Ollama; the app collapses the model's thinking,
so no flag is needed): *"I need to wash my car. The carwash is 50m away.
Should I walk or drive?"* Switch to the app and run it live, then advance.
Slide 2 typesets Wednesday's answer (9/2) as the large headline — "**You
should walk**" — and enlarges the key Verdict: *"Grab your keys (just in
case) and enjoy the 1-minute stroll!"* The full screenshot remains on the
slide only as a receipt; do not ask the audience to read it. It has the keys
and still leaves the car. Tuesday's run gave a different reason ("no need to
put unnecessary mileage on it just to get to the starting line") — same wrong
verdict, different reasons → segue straight into the next slide, "Same
question, different answers." **If the live run gets it right, slide 2 IS the
demo** ("here's what it told me Wednesday") — no separate fallback needed.

**Beat:** "It gives sensible-sounding reasons for walking, but misses the
condition that makes the answer useful: the car has to get there."
The output demonstrates the error, not its internal reasoning process.
Pause on the question so students can choose walk or drive before the reveal.
**Disclosure (say it):** "This is one small model on my laptop, with one
prompt. This recorded response shows a failure, not its frequency across models."

On the variance slide: different wording does not necessarily mean an error.
One sentence on sycophancy: "These tools can also agree with you when you're
wrong." No founding-year pushback and no retries to provoke a failure.

The citation slide is spoken only: a plausible reference still needs checking.
Avoid dividing trustworthy and untrustworthy output by price or model size.
The next voice clone demonstrates the same issue in another medium.

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

## §5 — Verification → one claim and its source (4 min)

Keep the opener short. Use a claim from the earlier Gounod conversation,
then compare it with a source. The prepared example checks the distinction
between composition in 1852 and publication in 1853.

1. Ask for the source and the relevant passage for that claim. If it wasn't
   discussed earlier, introduce it as a check of the date Ken supplied with
   the music; do not pretend the model said it.
2. Open the source. Preload the BnF record below; its notes distinguish the
   composition date from the first-edition date.
3. Point to the two dates and explain the French labels aloud. Ask whether the
   passage supports the precise claim, not merely whether a link exists.
4. Finish with the essential check: can you explain how the evidence supports it?

Allow 60–90 seconds for the source demonstration, with space for a correction.
Do not request five sources or require a scholarly search to finish in 30 seconds.
If the live citation is inaccessible, say so and use the prepared record.
Save it locally during rehearsal for offline use, labeled as a saved page.
A second chatbot's agreement is not independent confirmation. Both persuasion
exercises are removed; do not ask the model to argue the opposite.

[Sources]
BnF catalog, Méditation sur le 1er prélude de piano de S. Bach, CG 89a:
https://catalogue.bnf.fr/ark:/12148/cb140152042
Work notes: composition 1852, first edition Paris: Heugel, 1853 (checked Sept 5).
[/Sources]

---

## Closing (1 min)

"They're like eager toddlers: they want to please you, and they have a
toddler's grasp on reality. Verify anything that matters. Ask for help
thinking, not for a way out of thinking." A metaphor for the demonstrated failures,
not a literal claim about intentions or a description of all capabilities.

Then: "That's my part — Ewa takes it from here. Ewa?"

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
  search doesn't) — dropped 8/31 to pay for the restored demos; the
  screenshot version was parked too on 9/2 (Ken won't bet a beat on a
  hallucination happening on cue). The §5 click-the-sources habit remains;
  the 9/1 rehearsal prompt is in §4 if evidence is ever wanted.
- **Pangram detection** — detection adjacency reads as "we'll catch you";
  that conversation belongs to Ewa's integrity segment if anywhere.
- **Browser agent (Claude in Chrome / Astro's equivalent)** — e.g. filling in
  a Moodle course page, which Ken did 9/4 and found genuinely useful. Parked
  9/5: untested live the night before, slow and fiddly on stage, and a
  faculty task a first-year can't judge. Excellent for the faculty version
  and the AI Lab. In this talk it's at most one spoken clause on the say/do
  slide ("agents can also drive a browser").

(Voice clone + family safe word: restored to §4 on 8/31 — no longer parked.
Tell Ewa on the Wed call so the safety-tip conversation doesn't double up.)
