# Recording Script — AI Tools for Academic Success (makeup video)

Instructor-only. Companion to `slides-freshmen.md` (29 slides; the speaker
notes there are the per-slide script and the source of truth) and the short
cue sheet `run-card-freshmen.md`. Rewritten 2026-10-31 for the **recorded
version** of the Sept 6 first-year orientation talk. The live-session
version of this file (stage logistics, Ewa/Andrew handoffs, phone over
USB-C) is in git history: `git show 5cef429:demo-script-freshmen.md`.

**Why this exists:** Andrew Purrington (AI Academic Fellow) asked on Sept 30
for a makeup option for students who missed the Sept 6 session; it counts as
a required AI Lab component. He pairs Ken's video with Ewa's materials in a
Moodle module and adds quiz questions. Thread: Trinity Outlook, "Orientation
Session Makeup for the AI Lab."

**One recording, two edits** (agreed 2026-10-19):

- **Moodle cut** — Trinity framing, ends on the toddlers slide.
- **YouTube cut** (Tales from the jar side) — same body, with the 5-second
  `Updated_Tftjs_intro.mp4` at the head and the to-camera intro.

**Hard rules on camera:**

- **Never show the Outlook inbox.** The Claude Desktop email-approval prompt
  is fine (the address is public). Cut right after the approval.
- Ken's real course schedule and the real CPSC-415 Moodle page are fine; the
  Moodle screenshot on the slide is already blurred (phone, Zoom link).
- **Cold start every take.** Claude and the Codex Pet both remembered the
  Bach/Gounod conversation across rehearsals and the two live sessions (the
  Pet said "we've discussed this"). Claude: incognito chat or memory off.
  Codex: memory controls still unverified — don't guess; if it shows
  memory, say on camera that it was cleared, or retake.
- **Tone guardrail unchanged:** mechanism and evidence, never advocacy. "This
  is what's possible; what you'll have access to varies and will change."
  Comparative asides (Google, pricing, "better than") stay spoken, off slides.
- The deck now owns §6 (learning + course policy). No handoff to Ewa; the
  talk ends on the toddlers slide.

## Recording setup

- **Descript**, camera + screen as one sequence, **in segments** (see table
  below), two compositions in one project. Template: the "Claude Code with
  Any Model" project (camera + screen, ~40 min raw → 19 min final; expect
  ~2:1). CleanShot X only for screenshots.
- Laptop only. No phone switch; the schedule screenshot is pasted from
  `demo-assets/portal-course-schedule.png`.
- Capture **system audio + mic** for the music clip and the Pet.
- Slidev in presenter-less fullscreen; slides in `?clicks=` order as noted.
- Target **~25–26 minutes final.** Segment boundaries are the cut points;
  retakes replace a segment, not the whole recording.

## Pre-flight (before the first take)

- [ ] Descript project created, two compositions named (Moodle / YouTube).
- [ ] Camera framing, mic level, system-audio capture tested with 10 s of
      the Ave Maria clip and one Pet sentence.
- [ ] Slidev running on the current `main`; PDF/QR unaffected (rolling release).
- [ ] Tabs in order: OpenAI tokenizer, Slidev, Claude Desktop (incognito /
      memory off), Codex (Pet, voice, **Intelligence = Instant**), Ollama app
      with `gemma4:12b-mlx` loaded, Claude Code in this repo, Quote
      Investigator page.
- [ ] `demo-assets/portal-course-schedule.png` on the clipboard path; a
      checked `.ics` from rehearsal saved as a retake fallback.
- [ ] Gmail send permission in Claude set to **ASK** (reset any "always
      allow"); one rehearsal send the day before so the prompt is known to appear.
- [ ] Ave Maria embed plays from the start in Slidev; YouTube link as backup.
- [ ] Pet: rehearse the four-question chain + "What haven't I asked you
      about?" + the meta question on Instant; listen for 1852/1853.
- [ ] Ollama car-wash question rehearsed once; recorded answer is on slide 19
      regardless of the live result.
- [ ] Voice clone: Claude Code open in this folder (voice id comes from
      `CLAUDE.md`); `demo-assets/voice-clone-demo.mp3` as fallback.
- [ ] Quote Investigator and Center for Mark Twain Studies pages loaded.
- [ ] Notifications off; browser zoom and light/dark mode checked on camera.
- [ ] Claude usage meter checked; the recording spends little.
- [ ] Optional: Moonside Halo lamp in frame as the "is it thinking?" light.
      If it's visible, one sentence the first time it changes color, then
      never mention it. Moonside phone app closed (it steals BLE). Nothing
      depends on it.

---

## Segment plan

| Seg | Slides | Content | Target |
| --- | ------ | ------- | ------ |
| 0 | — | To-camera intro | 0:30 |
| 1 | 1–4 | Title → predictive vs generative → **tokenizer** → next-token odds | 2:00 |
| 2 | 5–6 | **Ave Maria clip + Pet conversation** → context debrief | 5:30 |
| 3 | 7–13 | Conversation not search → three asks → ram → start with what you dislike → engine/car → say/do → file for review | 2:30 |
| 4 | 14 | **Demo: my actual fall semester** (five steps, ends on the approval prompt) | 4:00 |
| 5 | 15–16 | Google Calendar receipt → Moodle receipt | 1:30 |
| 6 | 17–21 | Section turn → **car wash** → variance → citation | 3:30 |
| 7 | 22 | **Voice clone** | 2:30 |
| 8 | 23–26 | Verify → **Twain / Grant Allen** → essential check | 2:30 |
| 9 | 27–29 | Learning → rules → toddlers close | 1:30 |

Budgets, not measurements. Running long is an edit problem, not a cut
problem: trim Pet follow-ups and the ram beat first. Protect the semester
demo's approval moment and the Twain source check.

---

## Segment 0 — To-camera intro (~30 s, no slides)

Draft in the title-slide notes; Ken to tune:

> "This is the talk I gave Trinity's incoming class in September 2026: what
> these tools actually are, what they're good and bad at, and how to tell
> the difference. I recorded this version for students who missed it — and
> for everyone who isn't eighteen and has asked me the same questions. The
> schedule you'll see is my real one. I built it the same way."

Record it twice: once Trinity-framed (Moodle cut), once with one extra
sentence of context for the YouTube cut.

---

## Segment 1 — What AI is → tokens → what comes next (slides 1–4, 2 min)

**Slide 1, 0:00–0:20.** "These tools can help with difficult things and make
surprising mistakes on easy ones. I want to show you how both happen."

**Slide 2, 0:20–0:45. Predictive vs. generative.** One sentence of
background: "AI research goes back decades, and you've used it in
recommendations and spam filters. Today we're looking at generative AI."
Predictive AI picks an existing song you'll probably like; generative AI
produces text, images, or audio in response to your request. Two tasks, not
everything either product does. "Let's look at how a language model
represents text."

**Slide 3, 0:45–1:30. Tokenizer.** Live (`platform.openai.com/tokenizer`,
type "Trinity College" and one short sentence) OR the screenshot. Name the
colored fragments "tokens": whole words, parts of words, punctuation,
represented by numbers. On the screenshot: "Collge" splits into "Coll" +
"ge"; the period is its own token; "Let's" is one token in GPT-5.x (the
legacy GPT-4 tab splits it). Counts belong to this text and tokenizer. If
live works, advance without re-explaining. "These chunks are represented by
numbers. Next: how the model generates more of them."

**Slide 4, 1:30–2:00. "Please pass the…" — two clicks.** The numbers are
real: GPT-2 XL, measured locally, top five, bars scaled so 10% = full.

- *Click 1 (no other context):* word 8.6%, following 3.6%, message 2.8%,
  information 2.5%, link 1.8%. The model reads "pass" as pass **along** —
  "pass the word along," "pass the message on" — stock phrases from the
  email and forum text it was trained on. (If asked: after "Please pass the
  word" it predicts " along" at 61%.) It didn't pick a weird word; it picked
  the other meaning of "pass," because nothing said dinner. Even the top
  guess is under one in ten. There is no single right answer.
- *Click 2 (after "We sat down to dinner."):* salt 5.5%, wine 2.9%, bread
  2.3%, salad 2.1%, mashed 1.8%. Nothing was looked up; the context changed
  which patterns fit. "mashed" is a token that's only part of what's coming.
  (Backup line: after a football sentence it puts two-thirds on "ball.")

One token at a time, from the preceding context. "Autoregressive just means
building on the text so far." **"Fluent is not the same as verified."** Cut.

---

## Segment 2 — Bach → Gounod, in conversation (slides 5–6, 5.5 min)

**Slide 5.** Observation task first: "Watch what changes when I ask a
follow-up." This is not a generation analogy; it is conversation as the way
to use these tools.

1. **Click Play** on the embedded Ave Maria (Rusanda Panfili). ~30 s from
   the start: the opening bars are Bach's prelude alone — "that's Bach,
   1722" — then the melody enters — "and that's Gounod, 1852, on top."
   Optional aside while introducing the clip: a coding agent checked the
   YouTube page metadata for a Content ID block before this was recorded
   (none — a home pandemic recording) and pulled "published 1853" from her
   description. **Pause the player before switching to the Pet.**
2. **Pet in Codex, by voice**, interruptible — interrupt at least once,
   naturally: "Was this a common practice?" → "Did Gounod do this with other
   pieces?" → "Was Bach a common source for this sort of thing?" → "What are
   some other examples?" Follow the thread wherever it goes; the
   free-association is the demo.
3. **Challenge one claim:** "What evidence supports that?" — asking for
   support, not pressuring it to agree.
4. **"What haven't I asked you about?"** Let it offer two or three
   directions; pick one. This is the first of the "three asks" (slide 8) —
   the viewer sees it work before it's named.
5. **Meta beat:** "Everything we just did was live. Is this a good way to
   use a tool like you? What should I watch out for?" Interrupt if it
   rambles; an AI listing its own failure modes is the demo. Then: "Hold
   onto that list — in a few minutes we'll test a claim against an actual
   source."

**Slide 6, context debrief (~30 s).** Refer to a real follow-up: "I didn't
need to repeat who we were discussing. The earlier exchange gave the
follow-up its meaning." The on-screen "Did he do that elsewhere?" is an
example, not a transcript. "What haven't I asked?" worked the same way: this
thread, matched against patterns from everything it has read. Remembering
the discussion doesn't make its claims true. Cut.

**Retake ladder:** Pet misbehaves → same conversation typed in a chat
window; embed fails → YouTube link. If the Pet shows memory of a previous
take, say so on camera or retake the segment.

---

## Segment 3 — What it does well, the setup (slides 7–13, 2.5 min)

**Slide 7, "A conversation, not a search box" (~30 s).** Name the principle
the music demo just showed. Spoken only: "Don't ask it what you'd ask Google.
Google is free, and it still gives a decent answer to a question you can
phrase." The point of a language model is the conversation: it reads the
nuance in *your* context — the passage you're stuck on, the problem, the
draft — and applies what it absorbed from everything it has read. You're
asking for an interpretation, not a fact. Examples in one breath: an
explanation of a hard passage, practice questions, another approach to a
problem, a table of dates pulled from a screenshot.

**Slide 8, "Three asks you'd never make of a person" (~40 s, three clicks).**
It doesn't get tired, bored, or offended.

1. "What haven't I asked? What am I forgetting? What do other people do that
   hasn't occurred to me?" — point back to the Pet. Pattern-matching across
   everything it has read: things others already do that weren't in your
   experience yet.
2. "Give me ten titles." None work? "Give me ten more" — and say what was
   wrong with the first ten. You can do that all afternoon.
3. Stuck and not sure how it could even help? "Here's what I'm dealing with
   — what can you do for me here?" More context, better answer.

Habits, not features; no product names.

**Slide 9, ram cover (~15 s, one click).** Real O'Reilly cover first; click
reveals the ram and caption. "I used Nano Banana to make the other one."
Two-step reveal on purpose: the viewer registers the real book before the
joke. Never recite credentials; the gag does it.

**Slide 10, "Start with the part you don't want to do" (~15 s).** The answer
to "what should I even use this for?": the tedious, repetitive parts you
already dislike. Low bar, immediate win. "I didn't want to type my semester
into a calendar. So I didn't." Hold the Moodle "wait, what?" story for slide 16.

**Slide 11, "The model is the engine. The app is the car." (~15 s).** The
model generates the words; the app adds the interface and connects it to
search, files, calendar. You never drive an engine. Same model, different
apps, different abilities. (Don't say "harness.") "Watch the app find a
calendar, read my schedule, and produce a calendar file for me to review."

**Slide 12, "Some say things. Some do things." (~15 s).** Say "agent" once,
plainly: a system that wraps a model with tools and takes actions. A chat
answers you; an agent acts for you. Saying needs no permission; doing does —
"watch for the moment it asks." Mechanism, not hype. Optional clause: "agents
can also drive a browser — I used one to fill in a course page."

**Slide 13, "A calendar file is ready for review" (~15 s).** Trinity hasn't
authorized an AI connector to Outlook, so the demo produces a file a student
can review and import themselves. Two moments of human control: the one
action it takes (emailing me the file) asks first; the calendar write stays
mine, after review. Cut.

---

## Segment 4 — Demo: my actual fall semester (slide 14, 4 min)

**The point, said out loud before step 5:** not the vision model reading a
screenshot, and not finding a PDF — the combination. Two sources (the public
academic-calendar PDF of breaks and holidays, plus my schedule screenshot)
cross-checked so the invites skip the days classes don't meet. A search
engine returns pages; it doesn't combine them into a job.

Setup: Claude Desktop, **cold start**, email permission at ASK. One
conversation, five steps; the slide's chips name each one.

1. **Find it** — *"Find the current Trinity College Hartford approved
   academic calendar."* Check institution and academic year on the source
   page. (Finding Hartford doesn't prove memory was used; a cold start is
   why we can say that.)
2. **Read it** — paste `demo-assets/portal-course-schedule.png`. *"List my
   class meetings this fall, with dates, local start/end times, locations,
   and the dates they will not meet. Use the approved academic calendar. Ask
   me about missing details; do not assign times to TBA items."*
3. **Check it** — compare one included meeting and one excluded break or
   holiday against the sources (keep the **Labor Day** exclusion as the
   visible check). Glance at first/last meeting, local times, time zone. The
   output needs checking even though a previous import succeeded.
4. **Export it** — the copy-ready prompt below; show the download and one
   previewed event.
5. **Send it** — *"Email that .ics file to my Trinity address."* **Pause on
   the permission prompt.** Point at chip 5, "it asks first": "Steps 1–4
   were saying. This is doing — and it's asking before it acts. Read what
   it wants to do; approve once, never 'always.'" Approve. **Cut before the
   inbox appears.** Then: "The file is ready. It hasn't changed Outlook. I
   review it, then choose whether to import it."

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

File creation does not verify the schedule; the source comparison does.
Import is a snapshot, not a subscription; don't re-import over the real
Google events.

**Retake ladder:** no permission prompt → download the file instead and say
plainly that no prompt appeared; generation stalls → the saved rehearsal
`.ics` and preview, labeled as such on camera.

[Sources]
Microsoft, import a calendar in Outlook on the web (snapshot limitation):
https://support.microsoft.com/en-us/outlook/import-or-subscribe-to-a-calendar-in-outlook-com-or-outlook-on-the-web
Ken's actual schedule; Google Calendar connector result, Sept 5.
[/Sources]

---

## Segment 5 — Two receipts (slides 15–16, 1.5 min)

**Slide 15, Google Calendar.** A magnified detail of the Sept 5 screenshot
(Sept 14–15); no tab switch. "Claude added my classes through my Google
Calendar connection earlier. The Busy entries come separately from my
Outlook calendar feed. Trinity hasn't authorized an Outlook connector, so
we're using a file you can review and import." These events did not come
from the file just generated; the Outlook feed is not an AI connector.

**Slide 16, Moodle course page.** A receipt, not a claim. The real CPSC-415
page, same course as the schedule. Coding agents (Claude Code, Codex,
Antigravity) aren't just for code: one built this page; while preparing
this video one grabbed the screenshot, spotted the cell number and Zoom link,
and blurred them before anything went to GitHub; earlier one checked the
Ave Maria clip's YouTube metadata. "I'm not telling you what AI could do
for a professor. This is what it did for this one."

**Spoken beat — the line that wins over colleagues:** "Every professor has
to set up a Moodle page for every class, every semester. Nobody enjoys it.
When I tell faculty I had my AI tool do mine, the response is always
'Wait, what?'" Automating the thing everyone hates is what converts
skeptics. No tooling detail (no MCP, no product tour); the screenshot is the
proof. Straight into section 4. Cut.

---

## Segment 6 — What it does poorly: the car wash (slides 17–21, 3.5 min)

**Slide 17.** Section turn; the tone shifts. "You've seen useful results.
Now watch what can go wrong." Honest calibration: don't present 2024
failure modes as current.

**Slide 18, the question.** Give the viewer a beat to choose walk or drive.
Full wording in the app: *"I need to wash my car. The carwash is 50m away.
Should I walk or drive?"* Model: `gemma4:12b-mlx` in the Ollama app (it
collapses thinking to "Thought for N seconds"). **Live option:** switch to
Ollama, run it, come back. Or just advance — slide 19 is the answer.

**Slide 19, "You should walk."** Read the verdict aloud: "Grab your keys
(just in case) and enjoy the 1-minute stroll!" It has the keys and still
leaves the car. (Tuesday's rehearsal gave a different reason — "no need to
put unnecessary mileage on it just to get to the starting line" — same wrong
verdict, different reasons.) If the live run got it right, this slide *is*
the demo: "here's what it told me on September 2." Beat: "Sensible-sounding
reasons for walking, but it misses the condition that makes the answer
useful: the car has to get there." **Disclosure, say it:** "One small model
on my laptop, one prompt. This shows a failure, not how often every model fails."

**Slide 20, "Same question, different answers."** Generation is
probabilistic; different wording isn't necessarily an error — the car wash
is wrong because it misses a necessary condition. One sentence on
sycophancy: "These tools can also agree with you when you're wrong." Inputs
matter — the same model behaves differently in different apps (callback to
engine/car).

**Slide 21, "A perfect-looking citation may not exist."** Spoken, no demo.
"A convincing-looking reference still needs checking. A familiar brand or a
paid account is not evidence that this claim is correct." Newer systems
fabricate less; none are immune. The voice clone next is the same lesson in
another medium. Cut.

(Evidence if ever wanted: `ollama run gemma4:12b-mlx --think=false` with the
"five sources on Gounod's reception in 19th-century Paris" prompt → five
confident fabrications. Parked since 9/2; not a beat to bet on.)

---

## Segment 7 — Looking real vs. being real: the voice clone (slide 22, 2.5 min)

Adapted from the workshop's Demo 5 (`demo-script.md`).

1. Say a short, topical sentence about **today** out loud, on camera.
2. In Claude Code, from this repo's folder: *"Say the following in my voice:
   [the identical sentence]."* The voice id comes from `CLAUDE.md`; nothing
   pasted on screen. Keep the sentence visible in the prompt so the viewer
   compares the same words. Narrate the few seconds of delay.
3. Play it. Let the uncanny valley sit for a beat.

**Beats:** "I consented to this — I created that voice clone on purpose."
Voice is no longer proof of identity. **The take-home, slowly: for an urgent
unexpected call, hang up and call the person back on a number you already
know.** A private family phrase can be a second check, not a guarantee.
Looking real — sounding real — is not being real. Cut.

**Fallback:** `demo-assets/voice-clone-demo.mp3`.

[Sources]
FTC, scammers use fake emergencies:
https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money
[/Sources]

---

## Segment 8 — How to verify: Twain and Grant Allen (slides 23–26, 2.5 min)

**Slide 23.** "An answer is not the truth." Callback to §2: prediction, not
knowledge — that is why verification is on you.

**Slide 24.** The habit: choose one claim, open its source, find the passage,
check that it supports the claim. An explanation from the model is just
another generated output; another chatbot agreeing is not independent
confirmation.

**Slide 25, the quote (one click).** "Never let your schooling interfere with
your education" — almost everyone attributes it to Mark Twain, who lived
down the street from Trinity. Because the attribution is repeated all over
the internet, ungrounded prediction repeats it too. **Click:** check the
primary sources and Twain never wrote it. Grant Allen, 1894, *Post-Prandial
Philosophy* ("…compelled to let our boys' schooling interfere with their
education!"); first pinned on Twain in a 1907 Daisy Air Rifle ad.
Optionally open the Quote Investigator page on camera and point to the
passage. Note that a claim from the Pet conversation can be checked the
same way.

**Slide 26, the essential check.** "Can you explain how the evidence
supports the claim? If not, you have an answer — not understanding." Cut.

[Sources]
Quote Investigator: https://quoteinvestigator.com/2010/09/25/schooling-vs-education/
Center for Mark Twain Studies: https://marktwainstudies.com/the-apocryphal-twain-never-let-schooling-interfere-with-your-education/
[/Sources]

---

## Segment 9 — Using AI for learning → close (slides 27–29, 1.5 min)

**Slide 27, "Completing the task is not learning" (three clicks).** Pivot on
the quote just verified: almost everything today was about not letting
schooling interfere with education — clearing the calendar logistics and
following your own curiosity (the Bach/Gounod rabbit hole), not hunting for
a shortcut to an A. AI can produce the artifact without producing the
learning, and the bill comes due on the exam. Click through: "Quiz me" (test
yourself before the exam does) → "Give me a hint" (unstuck without skipping
the struggle) → "Challenge this" (what is my argument assuming?).

**Slide 28, "Know the rules. Own the result."** Every course (and workplace)
sets its own policy — Yes, No, or Sometimes — for good reasons. Check the
syllabus, disclose what you used, and remember you own what you submit.
Say why the rules vary, with candor: a lot of faculty are skeptical about AI
in education, and they're right to be — it is disrupting teaching on a scale
comparable to the arrival of the internet. Professors are working it out in
real time; that's why policy differs course to course.

**Slide 29, close.** "They're like eager toddlers: they want to please you,
and they have a toddler's grasp on reality. Verify anything that matters.
Ask for help thinking, not for a way out of thinking." A metaphor for the
demonstrated failures, not a claim about intentions. Contact and QR are on
the slide. Moodle cut ends here; YouTube cut gets a one-line sign-off.

---

## After recording

- Descript: filler-word pass and captions on both compositions (the Descript
  MCP handled both for the Groovy Podcast Oct 14 project).
- Moodle cut → share link to Andrew for the makeup module.
- YouTube cut → Tales from the jar side, with the intro bumper.
- Nothing from `demo-assets/` gets committed (gitignored; includes voice samples).

---

## Parked demos — not deleted

Older prep notes are in git history. Usable for a faculty/adult version or
the AI Lab:

- **Deep Research bookend** — best "what agents are" demo; doesn't fit the
  six-section brief.
- **Wispr dictation opener** — accessibility beat; a 20-second aside at most.
- **Lyrics trainer** ("nobody typed any code") — reads as marketing under the
  tone guardrail.
- **Ollama fake-citations pair** — parked 9/2; the slide-21 spoken point
  covers it.
- **Pangram detection** — detection adjacency reads as "we'll catch you";
  belongs in the integrity conversation if anywhere.
- **Live browser agent** (Claude in Chrome filling a Moodle page) — slow and
  fiddly on camera; now represented by the slide-16 receipt instead.
- **Persuasion / "argue the opposite" exercises and the quiz** — dropped
  before Sept 6; still out.
