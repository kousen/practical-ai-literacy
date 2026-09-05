---
theme: seriph
colorSchema: auto
background: none
layout: center
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## AI Tools for Academic Success

  First-Year Orientation, Trinity College — September 6, 2026

  By Kenneth Kousen
drawings:
  persist: false
transition: slide-left
title: "AI Tools for Academic Success"
mdc: true
fonts:
  sans: Atkinson Hyperlegible
  serif: Bricolage Grotesque
  mono: IBM Plex Mono
css: unocss
htmlAttrs:
  data-deck: freshmen
---

<style>
/* Two palettes, one deck: Slidev's "d" key toggles html.dark. Every color
   below must come from a variable so light and dark can never drift. */
:global(html.dark) {
  --fg: #F2F1ED; --bg: #101114; --muted: #A6ABB5; --faint: #5D636E; --muted-strong: #C8CCD4;
  --lamp-blue: #6E8BFF; --lamp-purple: #C36BFF; --lamp-green: #4ADE80;
  --glow-blue: rgba(110,139,255,0.20); --glow-purple: rgba(195,107,255,0.20); --glow-green: rgba(74,222,128,0.18);
  --tri-blue: rgba(110,139,255,0.21); --tri-purple: rgba(195,107,255,0.17); --tri-green: rgba(74,222,128,0.15);
  --shadow: rgba(0,0,0,0.5);
}
:global(html:not(.dark)) {
  --fg: #15171C; --bg: #FBFAF7; --muted: #4B515C; --faint: #8A9099; --muted-strong: #3A4048;
  --lamp-blue: #3552D6; --lamp-purple: #8B35D6; --lamp-green: #1C8A4C;
  --glow-blue: rgba(53,82,214,0.13); --glow-purple: rgba(139,53,214,0.12); --glow-green: rgba(28,138,76,0.12);
  --tri-blue: rgba(53,82,214,0.14); --tri-purple: rgba(139,53,214,0.11); --tri-green: rgba(28,138,76,0.11);
  --shadow: rgba(0,0,0,0.22);
}
:global(.slidev-layout) {
  background: var(--bg);
  color: var(--fg);
  font-family: 'Atkinson Hyperlegible', Verdana, sans-serif;
}
:global(.slidev-layout h1) {
  font-family: 'Bricolage Grotesque', 'Arial Narrow', sans-serif;
  font-weight: 700;
  font-size: 3.1rem;
  line-height: 1.08;
  letter-spacing: -0.015em;
  text-wrap: balance;
  color: var(--fg) !important;
  background: none !important;
  -webkit-text-fill-color: var(--fg);
}
:global(.slidev-layout h1 .acc-blue)   { -webkit-text-fill-color: var(--lamp-blue); }
:global(.slidev-layout h1 .acc-purple) { -webkit-text-fill-color: var(--lamp-purple); }
:global(.slidev-layout h1 .acc-green)  { -webkit-text-fill-color: var(--lamp-green); }
:global(html[data-deck="freshmen"] .slidev-layout:not(.cover) p) {
  color: var(--muted); opacity: 1; font-size: 1.35rem; line-height: 1.5;
}
:global(.eyebrow) {
  font-family: 'IBM Plex Mono', Menlo, monospace;
  font-size: 0.95rem; letter-spacing: 0.14em; text-transform: uppercase;
  display: flex; align-items: center; gap: 12px; justify-content: center;
  margin-bottom: 1.4rem;
}
:global(.lampdot) { width: 13px; height: 13px; border-radius: 50%; display: inline-block; }
:global(.acc-blue)   { color: var(--lamp-blue); }
:global(.acc-purple) { color: var(--lamp-purple); }
:global(.acc-green)  { color: var(--lamp-green); }
:global(.dot-blue)   { background: var(--lamp-blue); box-shadow: 0 0 16px var(--lamp-blue); }
:global(.dot-purple) { background: var(--lamp-purple); box-shadow: 0 0 16px var(--lamp-purple); }
:global(.dot-green)  { background: var(--lamp-green); box-shadow: 0 0 16px var(--lamp-green); }
:global(.glow-blue)   { background: radial-gradient(1100px 700px at 88% -18%, var(--glow-blue), transparent 62%), var(--bg) !important; }
:global(.glow-purple) { background: radial-gradient(1100px 700px at 88% -18%, var(--glow-purple), transparent 62%), var(--bg) !important; }
:global(.glow-green)  { background: radial-gradient(1100px 700px at 88% -18%, var(--glow-green), transparent 62%), var(--bg) !important; }
:global(.glow-tri) { background:
  radial-gradient(900px 600px at 6% -14%, var(--tri-blue), transparent 60%),
  radial-gradient(900px 600px at 102% 8%, var(--tri-purple), transparent 60%),
  radial-gradient(1000px 560px at 50% 122%, var(--tri-green), transparent 62%),
  var(--bg) !important; }
:global(.takeaway) { max-width: 40rem; margin-left: auto; margin-right: auto; text-wrap: pretty; }
:global(.contact) { font-size: 0.95rem !important; line-height: 1.65; color: var(--muted-strong) !important; opacity: 1 !important; }
:global(.permchip) {
  font-family: 'IBM Plex Mono', Menlo, monospace;
  font-size: 0.85rem;
  color: var(--lamp-green);
  border: 1px solid var(--lamp-green);
  border-radius: 999px;
  padding: 4px 14px;
  display: inline-block;
}
</style>

<div class="eyebrow">
  <span class="lampdot dot-blue"></span><span class="lampdot dot-purple"></span><span class="lampdot dot-green"></span>
</div>

# <span class="acc-blue">AI Tools</span> for Academic <span class="acc-green">Success</span>

<p>What these tools actually are, what they're good and bad at,<br>and how to tell the difference.</p>

<p style="font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem; color: var(--faint);">
Ken Kousen · Trinity College · First-Year Orientation · September 2026</p>

<div style="position: absolute; right: 36px; bottom: 30px; text-align: center;">
  <img src="/images/qr-freshmen-pdf.svg" style="width: 96px; height: 96px; background: #fff; padding: 5px; border-radius: 6px;" alt="QR code linking to the slides PDF" />
  <div style="font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; color: var(--faint); margin-top: 3px;">slides (PDF)</div>
</div>

<!--
QR (title + close) → the rolling "latest" release asset; the URL is stable
across rebuilds, so it stays valid no matter how often the deck changes.
~25-minute rehearsal target in a 30-minute slot, five sections, demos as evidence — advance
briskly; the slides are backdrops, not documents. Ewa introduces; she follows
with AI-in-college and the integrity policy, so stay OFF policy and integrity.
Tone check: mechanism and evidence, never advocacy — this must not read as marketing.
0:00–0:20 opener: "These tools can help with difficult things and make
surprising mistakes on easy ones. I want to show you how both happen."
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# Familiar AI, <span class="acc-blue">generative AI</span>

<p class="takeaway">Spotify can recommend an existing song.<br>A generator produces text, images, or audio in response to your request.</p>

<!--
0:20–0:45. One sentence of background: "AI research goes back decades, and
you've used it in recommendations and spam filters. Today we're looking at
generative AI." The comparison describes two tasks, not everything either
product can do. Then: "Let's look at how a language model represents text."
Go directly to the tokenizer. Save model/system and agents for §3.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · tokens</div>

# Text becomes <span class="acc-purple">tokens</span>

<img src="/images/tokenizer-input.png" style="width: 780px; max-width: 90%; margin: 0.6rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="The typed sentence: Welcome to Trinity Collge. Let's learn something about AI" />
<img src="/images/tokenizer-tokens.png" style="width: 780px; max-width: 90%; margin: 1rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="Tokenizer output: 12 tokens, 57 characters. Collge splits into Coll and ge; Let's splits into Let and apostrophe-s; the period is a separate token." />

<p class="takeaway" style="margin-top: 0.9rem; font-size: 1.25rem; color: var(--muted-strong) !important; opacity: 1 !important;">Tokens can be whole words, parts of words, or punctuation.</p>

<!--
0:45–1:30. First demo: show the colored fragments, then name them "tokens."
Use EITHER the live playground OR this screenshot (Sept 3, gpt-4 tokenizer).
Live: type "Trinity College" and one short sentence. If the tab is slow,
use this image immediately. After a successful live run, advance past this
slide without repeating the explanation. No vendor tour or pricing aside.
On the screenshot, point out "Collge", "Let's", and the separate period.
The count belongs to this example and tokenizer, not a general word rule.
"These chunks are represented by numbers. This shows how text is encoded;
next we'll look at how the model generates more of it."
[Sources]
Ken's Sept 3 tokenizer screenshots: /images/tokenizer-input.png and
/images/tokenizer-tokens.png. Displayed tokenizer: gpt-4.
[/Sources]
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How it works</div>

# What could <span class="acc-purple">come next?</span>

<p class="takeaway" style="font-size: 2rem; color: var(--fg);">“Please pass the…”</p>
<p class="takeaway" style="color: var(--muted-strong) !important; opacity: 1 !important;">An autoregressive language model generates one token at a time, using the preceding context. A convincing continuation can still be wrong.</p>

<!--
1:30–2:00. Ten-second analogy: "If I say 'Please pass the…', several
continuations fit. If we were just talking about dinner, that changes which
continuations fit." A token can be smaller than a word, as we just saw.
Training learns patterns; generation uses them with the current context.
Say "autoregressive just means building on the text so far" if needed.
This illustrates prediction, not a full account of how the model reasons.
Key consequence: "Fluent is not the same as verified." Now play the music.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · Bach → Gounod, in conversation</div>

# Just keep <span class="acc-purple">asking</span>

<p class="takeaway">Watch what changes when I ask a follow-up.</p>

<!--
Start around 2:00; allow ~5 min including the clip. Give the audience its
observation task: "Watch what changes when I ask a follow-up."
Play ~30 sec of the Ave Maria from YouTube Music (tab queued, at the
start): the opening bars are Bach's prelude alone — say "that's Bach, 1722"
— then the melody enters: "and that's Gounod, 1852, on top." Then the Pet in Codex,
BY VOICE, interruptible: "Was this a common practice?" → "Did Gounod do this
with other pieces?" → "Was Bach a common source for this sort of thing?" →
"What are some other examples?" Follow the thread wherever it goes — the
free-association IS the demo. Challenge one claim: "What evidence supports that?"
The question asks for support rather than simply pressuring it to agree.
Save the context explanation for the debrief slide immediately afterward.
META BEAT to close — ask the Pet itself, live: "Everything we just did was
live. Is this a good way to use a tool like you? What should I watch out
for?" Let it answer (interrupt if it rambles) — an AI listing its own
failure modes IS the demo. Then, simply: "Ewa will have more to say about
that." No coordination needed.
Fallback ladder: pet fails → same conversation typed in a chat window; AV
fails entirely → rehearsal screenshots and narrate one exchange.
Tech check (Tue 5 pm): laptop audio over HDMI (the volume knob), pet input
via laptop mic from stage position, echo/self-hearing, interruption.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How it works</div>

# The conversation supplies <span class="acc-purple">context</span>

<p class="takeaway">“Did he do that elsewhere?”<br>The earlier exchange tells us who “he” is and what “that” means.</p>

<!--
Around 7:00–7:30. Refer to an actual follow-up from the conversation; the
sentence on screen is an example, not a claim about the exact words used.
"I didn't need to repeat who we were discussing. The earlier exchange gave
the follow-up its meaning." Training and available tools also shape answers.
Remembering the discussion doesn't establish that its claims are true.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# What can you <span class="acc-green">ask for?</span>

<p class="takeaway">An explanation of a difficult passage.<br>Practice questions, or another way to approach a problem.<br>A table of dates extracted from a screenshot.</p>

<!--
~20 seconds. These examples replace the five-slide capabilities tour.
Mention rewriting, translating, and generating options in one breath if
useful. "Quiz me, don't tell me" stays a spoken example, not another demo.
Quality varies; the semester demo will show extraction and checking in use.
Next, the short ram-cover reveal shows an image-generation example.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

<div style="display: flex; gap: 40px; justify-content: center; align-items: flex-end; margin-top: 0.4rem;">
  <img src="/images/cc-cover.png" style="height: 400px; border-radius: 6px; box-shadow: 0 8px 32px var(--shadow);" alt="Official cover of Claude Code: Up and Running" />
  <v-click><img src="/images/ram-cover.jpg" style="height: 400px; border-radius: 6px; box-shadow: 0 8px 32px var(--shadow);" alt="Generated image of a ram in a sweater reading the book by a fire" /></v-click>
</div>

<p class="takeaway" style="margin-top: 1.2rem; font-size: 1.1rem;">Left: my book's actual cover. <v-click at="1"><span>Right: the ram reads his own book.</span></v-click></p>

<!--
~15 seconds, mostly for the laugh. Real cover shows first; NEXT reveals the
ram and its caption. Then: "I used Nano Banana to make the other one."
The two-step reveal is deliberate and does double duty: the room registers
"he wrote the book" (an O'Reilly cover, your name) BEFORE the joke, so the
laugh carries the credibility — never deliver this as a single image, and
never recite credentials; the gag does it. Mention you've done this for all your books —
they're on your home page. Then move on. Tone: it's a joke about your own
book, not a product pitch.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# The model is the engine.<br>You use the <span class="acc-green">system</span>.

<p class="takeaway">The model generates responses.<br>The app can connect it to search, your files, and your calendar.</p>

<!--
~15 seconds, immediately before the semester demo. The model is the engine;
the product supplies the interface and connected tools. "Watch the app find
a calendar, read my schedule, and then produce a calendar file for me to review." Name capabilities
as they appear instead of giving another advance tour.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# A calendar file is ready <span class="acc-green">for review</span>

<p class="takeaway">The AI prepares the events.<br>I check them and choose whether to import them into Outlook.</p>

<!--
The school has not authorized a direct AI calendar connector. This demo uses
a downloadable .ics file and a human-controlled import. Preparing a file
does not change Outlook. Do not wait for or describe an AI permission prompt.
An agent can use connected tools to act, but here I perform the calendar write.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> Demo · my actual fall semester</div>

# My actual <span class="acc-green">fall semester</span>

<p class="takeaway">From my class schedule to a calendar file.<br>Check the dates before importing.</p>

<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 26px; max-width: 44rem; margin: 1.8rem auto 0;">
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">1<br><strong>Find it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">2<br><strong>Read it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">3<br><strong>Check it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">4<br><strong>Export it</strong></div>
</div>

<!--
Desktop → connect phone for this demo only → return to desktop afterward.
One Claude conversation on the phone:
1 FIND: "Find the current Trinity College Hartford approved academic calendar."
  Check the institution and academic year; finding Hartford does not prove
  that memory was used.
2 READ: provide the actual course-schedule screenshot. Ask for the meeting
  dates/times and the dates classes will not meet. Do not invent times for TBA.
3 CHECK: compare one included meeting and one excluded holiday/break against
  the source. Review the first/last meeting, local times and time zone.
4 EXPORT: ask for a downloadable Outlook-compatible .ics file for the actual
  class meetings, using America/New_York and excluding confirmed no-class
  dates. Ask for a plain-language preview of its contents. Full prompt and
  daylight-saving check are in the run sheet.
Say: "The file is ready. It hasn't changed Outlook. I review it, then import."
Ken reports already adding the actual meetings to Google Calendar successfully;
that is separate evidence, not proof of Outlook compatibility.
Return to desktop. Optional rehearsed finish: import into a separate Outlook
demo calendar and inspect an event. Otherwise show the file and describe import.
Never re-import over the real Google events. Email is optional, outside the core:
paste the verified dates into Copilot/Outlook before asking for a draft.
Import is a snapshot, not automatic synchronization with future schedule changes.
[Sources]
Microsoft Outlook import guide:
https://support.microsoft.com/en-us/outlook/import-or-subscribe-to-a-calendar-in-outlook-com-or-outlook-on-the-web
Ken's actual schedule and reported Google Calendar success, Sept 5.
[/Sources]
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Here's how they <span class="acc-green">look</span>

<img src="/images/google-calendar-trinity.png" style="width: 900px; max-width: 94%; margin: 0.4rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="Google Calendar, four-week view Aug 30 to Sep 26, 2026, Trinity College calendar only: class meetings on Mondays and Tuesdays, Labor Day on Monday Sept 7 with no class" />

<p class="takeaway" style="margin-top: 0.7rem; font-size: 1.1rem;">Imported earlier. Mondays and Tuesdays — and Labor Day off.</p>

<!--
Replaces switching to the Google Calendar tab: this is the Sept 5 screenshot
of the Trinity calendar alone (sidebar and account cropped out for the
public PDF). Say: "I imported these meetings earlier. Here's how they look."
Point at the Monday/Tuesday rhythm and the Labor Day gap — that's the
no-class date we checked. Don't imply these came from the file just made.
The event text is small from the back; the pattern is the point.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# The failure modes are <span class="acc-blue">predictable</span> too

<p class="takeaway">You've seen useful results. Now watch what can go wrong.</p>

<!--
Section turn — the tone shifts here. Honest calibration throughout: don't
present 2024 failure modes as current. Straight into the car wash as the
first piece of evidence.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · the car wash</div>

# The carwash is <span class="acc-blue">50 meters away</span>

<div style="max-width: 46rem; margin: 1.8rem auto 0; padding: 1.2rem 1.7rem; border-left: 4px solid var(--lamp-blue); background: rgba(110,139,255,0.08); text-align: left;">
  <p style="margin: 0; color: var(--fg); font-size: 1.75rem; line-height: 1.35;">“I need to wash my car.<br><strong>Should I walk or drive?</strong>”</p>
</div>

<p style="margin-top: 1rem; font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem; color: var(--faint);">Gemma 4 12B · local model in Ollama</p>

<!--
The setup: the question is reformatted for the room; use the full original
wording in the app. Give students a beat to choose "walk or drive" before the reveal. The model is gemma4:12b-mlx in the Ollama app (the app collapses the
model's thinking to "Thought for N seconds" — no --think flag needed). LIVE
OPTION: switch to the app and run it now; then come back and advance. If not
running it live, just advance — the next slide is the answer.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · the car wash</div>

# “You should <span class="acc-blue">walk.</span>”

<div style="display: grid; grid-template-columns: 1fr 19rem; gap: 2rem; max-width: 49rem; margin: 1.2rem auto 0; align-items: center;">
  <div style="text-align: left;">
    <p style="margin: 0; color: var(--fg); font-size: 1.55rem; line-height: 1.35;">“Grab your keys <span class="acc-blue">(just in case)</span> and enjoy the 1-minute stroll!”</p>
    <p style="margin: 1rem 0 0; font-size: 1.15rem; color: var(--muted-strong) !important; opacity: 1;">It has the keys — and still leaves the car.</p>
  </div>
  <div>
    <img src="/images/carwash-answer.png" style="width: 100%; margin: 0 auto; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="Screenshot of the actual Gemma 4 12B response in Ollama" />
    <p style="margin: 0.45rem 0 0; font-family: 'IBM Plex Mono', monospace; font-size: 0.65rem; line-height: 1.25; color: var(--muted) !important; opacity: 1;">Actual response · Ollama · Sept. 2 rehearsal</p>
  </div>
</div>

<!--
Wednesday's rehearsal answer (9/2). The exact verdict is typeset large enough
for the room; the full screenshot remains as a small receipt, not reading
material. Read the verdict aloud: "Grab your keys (just in case) and enjoy the
1-minute stroll!" — it has the keys and still leaves the car. (Tuesday's run
said "no need to put unnecessary mileage on it just to get to the starting
line.") Same wrong verdict, different reasons each day → that's the NEXT
slide, "Same question, different answers" — segue straight into it.
If the live run got it right, this slide IS the demo: "here's what it told
me Wednesday."
Beat: "It gives sensible-sounding reasons for walking, but misses the condition
that makes the answer useful: the car has to get there." The output establishes
the mistake, not the model's internal reasoning process.
Disclosure (say it): "This is one small model on my laptop, with one prompt
— this recorded answer shows a failure, not how often every model fails."
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# Same question, <span class="acc-blue">different answers</span>

<p class="takeaway">Generation is probabilistic — inconsistency is normal. And every answer is shaped by training data, prompts, instructions, and tools.</p>

<!--
Quick beat: repeated responses can differ. Different wording is not necessarily
an error; the car-wash answer is wrong because it misses a necessary condition.
One spoken sentence on sycophancy: "These tools can also agree with you when
you're wrong." No pushback demo. Inputs
matter — which is why the same model behaves differently in different
products (callback to model vs. system).
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# A perfect-looking citation <span class="acc-blue">may not exist</span>

<p class="takeaway">Looking real is not being real. Newer systems fabricate less — none are immune, and price and size are no guarantee.</p>

<!--
Spoken point, no demo (the fabrication screenshot was parked 9/2 — Ken
didn't want to bet a beat on a hallucination happening on cue). One breath:
"A convincing-looking reference still needs checking. Tools and models vary;
a familiar brand or a paid account is not evidence that this claim is correct." The voice clone next is the same lesson in a different
medium.
If evidence is ever wanted (9/1 rehearsal): ollama run gemma4:12b-mlx
--think=false "I'm writing a paper on how Gounod's Ave Maria was received in
19th-century Paris. List five sources I can cite, with author, year, and
journal." → five confident fabrications; gemma4:latest hedges, don't use it.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · looking real vs. being real</div>

# That was my voice. <span class="acc-blue">Except it wasn't.</span>

<p class="takeaway">For an urgent unexpected call, hang up and call back using a number you already know.</p>

<!--
~3 min, adapted from the workshop's Demo 5 (full steps in demo-script.md).
Say a topical sentence about THIS morning out loud, then have the clone speak
the identical words — the side-by-side is the demo. Run from this repo's
folder so Claude Code knows the voice id from CLAUDE.md.
Fallback: demo-assets/voice-clone-demo.mp3 through the room speakers.
Beats: "I consented to this — I created that voice clone on purpose." Voice is
no longer proof of identity. THE take-home: for an urgent call, hang up and
call the person back on a number you already know. A private family phrase can
be a second check, but it is not a guarantee. Say it slowly — it's the most
repeatable tip of the day. Keep the spoken sentence short and visible in the
app's prompt so students can compare the same words. This is Ken's consented clone.
[Sources]
https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money
[/Sources]
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 5 · How to verify AI output</div>

# An answer is not <span class="acc-purple">the truth</span>

<p class="takeaway">Wrong on simple things, right on hard ones — surface confidence is not evidence of accuracy.</p>

<!--
Ewa's section (how to use AI effectively) follows right after this. The deck
numbers its sections 1–5 sequentially — the shared planning outline's 4→6
jump was dropped 9/2; students don't care about the planning outline.
Callback to §2: prediction, not knowledge — that's WHY verification is on you.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 5 · How to verify AI output</div>

# Check the <span class="acc-purple">evidence</span>

<p class="takeaway">Choose one claim. Open its source.<br>Find the passage and check that it supports the claim.</p>

<!--
Four-minute section budget including opener, this demonstration, and the essential check.
Use a concrete claim from the earlier Gounod conversation. Prepared example:
"Was the melody composed in 1852 or published in 1853?"
Ask for a source and the relevant passage; open it and compare the claim.
Preload the BnF catalog record:
https://catalogue.bnf.fr/ark:/12148/cb140152042
Its work notes distinguish composition (1852) and first edition (1853).
Point to the two dates and explain the French labels aloud. Do not ask for
five sources or bet the demo on finding an accessible article in 30 seconds.
Allow 60–90 seconds for the check, more if there is a useful correction.
If the live citation is inaccessible, say so and use the prepared record.
If the earlier conversation omitted this date claim, introduce it explicitly
as a check of the date Ken supplied with the clip. Do not invent a past answer.
Takeaway: an explanation from the model is another output; the source is what
we inspect. Another chatbot agreeing is not independent confirmation.
Fallback: save this record locally during rehearsal and label it as a saved page.
[Sources]
BnF catalog, Méditation sur le 1er prélude de piano de S. Bach, CG 89a:
https://catalogue.bnf.fr/ark:/12148/cb140152042 (checked Sept 5).
[/Sources]
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 5 · How to verify AI output</div>

# The essential <span class="acc-purple">check</span>

<p class="takeaway">Can you explain how the evidence supports the claim? If not, you have an answer — not understanding.</p>

<!--
Last beat before the close; lands the section and sets up the toddler frame.
-->

---
layout: center
class: glow-tri text-center
---

<div class="eyebrow">
  <span class="lampdot dot-blue"></span><span class="lampdot dot-purple"></span><span class="lampdot dot-green"></span>
</div>

# They're like eager <span class="acc-green">toddlers</span>

<p class="takeaway">They want to please you — with a toddler's grasp on reality.<br>Verify anything that matters. Ask for help <strong>thinking</strong>, not for a way out of thinking.</p>

<div style="display: flex; gap: 36px; justify-content: center; align-items: center; margin-top: 0.6rem;">
  <p class="contact" style="text-align: right; margin: 0;">
  <strong style="color: var(--fg);">Ken Kousen</strong><br>
  Professor of the Practice, Computer Science Department<br>
  Associate Director, Elting Center for Innovation &amp; Entrepreneurship<br>
  <span style="font-family: 'IBM Plex Mono', monospace;" class="acc-blue">kenneth.kousen@trincoll.edu</span>
  </p>
  <div style="text-align: center;">
    <img src="/images/qr-freshmen-pdf.svg" style="width: 128px; height: 128px; background: #fff; padding: 6px; border-radius: 6px;" alt="QR code linking to the slides PDF" />
    <div style="font-family: 'IBM Plex Mono', monospace; font-size: 0.7rem; color: var(--muted); margin-top: 4px;">these slides (PDF)</div>
  </div>
</div>

<!--
Ken's metaphor describes the failure modes just demonstrated, not the full
capabilities or literal intentions of every system. Keep it short, then:
"That's my part — Ewa takes it from here. Ewa?"
Rehearsal target 25 minutes with five minutes of buffer. Fixed demos: Pet,
schedule-file workflow, voice clone. Email and live Outlook import are optional.
Live cut ladder: Pet to two follow-ups (skip meta), schedule ends at the
downloaded file, car wash uses its recorded answer. Protect the source check.
Hand back to Ewa for effective use, college context and policy, then Andrew.

-->
