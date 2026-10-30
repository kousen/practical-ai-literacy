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
~25-minute target, six sections, demos as evidence — advance briskly; the
slides are backdrops, not documents.
Tone check: mechanism and evidence, never advocacy — this must not read as marketing.
0:00–0:20 opener: "These tools can help with difficult things and make
surprising mistakes on easy ones. I want to show you how both happen."

TO-CAMERA INTRO (~30 s, before this slide; DRAFT, Ken to tune):
"This is the talk I gave Trinity's incoming class in September 2026: what
these tools actually are, what they're good and bad at, and how to tell the
difference. I recorded this version for students who missed it — and for
everyone who isn't eighteen and has asked me the same questions. The
schedule you'll see is my real one. I built it the same way."
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# Predictive AI vs. <span class="acc-blue">generative AI</span>

<p class="takeaway">Predictive AI picks an existing song you’ll probably like.<br>Generative AI produces text, images, or audio in response to your request.</p>

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

<img src="/images/tokenizer-input.png" style="width: 780px; max-width: 90%; margin: 0.6rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="OpenAI Tokenizer (GPT-5.x & O1/3) with the typed sentence: Welcome to Trinity Collge. Let's learn something about AI" />
<img src="/images/tokenizer-tokens.png" style="width: 780px; max-width: 90%; margin: 1rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="Tokenizer output: 12 tokens, 58 characters. Collge splits into Coll and ge; the period is a separate token; Let's is a single token in GPT-5.x." />

<p class="takeaway" style="margin-top: 0.8rem; font-size: 1.25rem; color: var(--muted-strong) !important; opacity: 1 !important;">Tokens can be whole words, parts of words, or punctuation.</p>
<div style="margin-top: 0.35rem; font-family: 'IBM Plex Mono', monospace; font-size: 0.85rem; color: var(--faint);"><a href="https://platform.openai.com/tokenizer" target="_blank" rel="noopener noreferrer">platform.openai.com/tokenizer</a></div>

<!--
0:45–1:30. First demo: show the colored fragments, then name them "tokens."
Use EITHER the live OpenAI Tokenizer (https://platform.openai.com/tokenizer)
OR this screenshot (GPT-5.x & O1/3 tokenizer).
Live: type "Trinity College" and one short sentence. If the tab is slow,
use this image immediately. After a successful live run, advance past this
slide without repeating the explanation. No vendor tour or pricing aside.
On the screenshot, point out "Collge" (splits into "Coll" and "ge"), the
separate period, and how "Let's" is a single token in GPT-5.x (whereas the
legacy GPT-4 tab splits "Let" and "'s").
The count belongs to this example and tokenizer, not a general word rule.
"These chunks are represented by numbers. This shows how text is encoded;
next we'll look at how the model generates more of it."
[Sources]
OpenAI Tokenizer screenshots: /images/tokenizer-input.png and
/images/tokenizer-tokens.png (https://platform.openai.com/tokenizer, GPT-5.x & O1/3).
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
class: glow-purple text-center music-demo
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · Bach → Gounod, in conversation</div>

# Just keep <span class="acc-purple">asking</span>

<p class="takeaway">Watch what changes when I ask a follow-up.</p>

<div class="music-clip">
  <RenderWhen context="print">
    <a href="https://www.youtube.com/watch?v=MZKKeKTa-cU" aria-label="Watch Ave Maria performed by Rusanda Panfili on YouTube">
      <img src="/images/bach-gounod-video.jpg" alt="Rusanda Panfili playing violin, with the title Ave Maria" width="520" height="293" />
    </a>
    <template #fallback>
      <Youtube id="MZKKeKTa-cU" :width="520" :height="293" title="Ave Maria — Gounod/Bach — Rusanda Panfili" referrerpolicy="strict-origin-when-cross-origin" />
    </template>
  </RenderWhen>
</div>
<div class="music-credit"><a href="https://www.youtube.com/watch?v=MZKKeKTa-cU" target="_blank" rel="noopener noreferrer">Ave Maria · Rusanda Panfili · Watch on YouTube</a></div>

<style>
.music-demo .eyebrow { margin-bottom: 0.5rem; }
.music-demo .takeaway { margin: 0.5rem auto 1rem; }
.music-clip { width: 520px; height: 293px; margin: 0 auto; }
.music-clip iframe, .music-clip img { display: block; width: 100%; height: 100%; }
.music-clip img { object-fit: cover; }
.music-credit { margin-top: 0.5rem; font-size: 0.95rem; color: var(--muted); }
</style>

<!--
Start around 2:00; allow ~5 min including the clip. Give the audience its
observation task: "Watch what changes when I ask a follow-up."
Click Play in the embedded Ave Maria video (Rusanda Panfili), from the start.
Play ~30 sec: the opening bars are Bach's prelude alone — say "that's Bach, 1722"
— then the melody enters: "and that's Gounod, 1852, on top."
(Quick aside while introducing the clip: when preparing this video for YouTube,
you asked your coding agent to check whether playing 30 seconds of this clip
would trigger a Content ID claim — it inspected the YouTube page metadata,
confirmed there is no Content ID license block because Rusanda Panfili recorded
it at home during the pandemic, and even pulled her description noting it was
published in 1853.)
Pause the player before switching to the Pet. If embedding fails, use the
Watch on YouTube link or the queued YouTube Music tab; offline phone copy is
the final fallback. Rehearse this exact video and its opening before the talk.
Video and thumbnail: https://www.youtube.com/watch?v=MZKKeKTa-cU
Then the Pet in Codex,
BY VOICE, interruptible: "Was this a common practice?" → "Did Gounod do this
with other pieces?" → "Was Bach a common source for this sort of thing?" →
"What are some other examples?" Follow the thread wherever it goes — the
free-association IS the demo. Challenge one claim: "What evidence supports that?"
The question asks for support rather than simply pressuring it to agree.
Then, still by voice: "What haven't I asked you about?" Let it offer two or
three directions and pick one. This is the first of the "three asks" slide
coming in §3 — the room sees it work before it's named.
Save the context explanation for the debrief slide immediately afterward.
META BEAT to close — ask the Pet itself, live: "Everything we just did was
live. Is this a good way to use a tool like you? What should I watch out
for?" Let it answer (interrupt if it rambles) — an AI listing its own
failure modes IS the demo. Then: "Hold onto that list — in a few minutes
we're going to test one of the claims it just made against an actual archive."
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
"What haven't I asked?" worked the same way: this thread, matched against
patterns from everything it has read.
Remembering the discussion doesn't establish that its claims are true.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# A conversation, <span class="acc-green">not a search box</span>

<p class="takeaway">A fact, you can look up.<br>Bring it your situation — this passage, this problem, this draft — and ask for an interpretation.</p>

<!--
~30 seconds. Name the principle the music demo just showed: "Don't ask it
what you'd ask Google. Google is free, and it still gives a decent answer
to a question you can phrase." (Spoken only — comparative asides stay off
the slide.) The point of a language model is the conversation: it reads
the nuance in YOUR context — the passage you're stuck on, the problem, the
draft — and applies what it absorbed from everything it has read. You're
not asking for a fact; you're asking for an interpretation.
Examples in one breath: an explanation of a difficult passage, practice
questions, another way to approach a problem, a table of dates pulled from
a screenshot. Quality varies; the semester demo will show extraction and
checking in use. Next slide: three asks that only work on a machine.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Three asks you'd never <span class="acc-green">make of a person</span>

<p class="takeaway">It doesn't get tired, bored, or offended. Use that.</p>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; max-width: 46rem; margin: 1.8rem auto 0;">
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“What haven't I asked?”</strong><br><span style="font-size: 1rem; color: var(--muted);">What others do that hasn't occurred to you</span></div></v-click>
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“Give me ten more”</strong><br><span style="font-size: 1rem; color: var(--muted);">Say what was wrong with the first ten</span></div></v-click>
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“What can you do with this?”</strong><br><span style="font-size: 1rem; color: var(--muted);">Stuck? Give it the context and ask</span></div></v-click>
</div>

<!--
~40 seconds. Click through the three. The room just watched the first one
in the Bach/Gounod conversation — point back to it.
1. "What haven't I asked? What am I forgetting? What do other people do
   that hasn't occurred to me yet?" This leans on pattern-matching across
   everything it has read: things others have already done that simply
   weren't in your experience base yet — and you'd like them to be.
2. "Give me ten titles for this." None of them work? "Give me ten more."
   Then ten more. You wouldn't do that to a person; you can do it to this
   all afternoon, especially if you say what was wrong with the last batch.
3. Sitting at a problem thinking "how could this thing even help?" Ask it.
   "Here's what I'm dealing with — what can you do for me here?" The more
   context you give it, the better it knows what to try.
Tone: habits, not features — no product names. Then the ram-cover gag.
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

# Start with the part you <span class="acc-green">don't want to do</span>

<p class="takeaway">Automate what you dislike. That's where it pays off first.<br>I didn't want to type my semester into a calendar. So I didn't.</p>

<!--
~15 seconds. The answer to "what should I even use this for?": look for
the parts of the job you don't want to do — the tedious, the repetitive —
and try handing those over first. You already don't want to do them, so
the bar is low and the win is immediate. The next few minutes are that
principle in practice: the semester schedule I did not want to type in by
hand. (The Moodle course page later in the talk is the same principle
applied to my own job — save the "wait, what?" story for that slide.)
Straight into "the model is the engine."
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
as they appear instead of giving another advance tour. Next slide plants
the say/do distinction the send step will pay off.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Some say things. Some <span class="acc-green">do</span> things.

<p class="takeaway">A chat answers you. An agent acts for you — searches, sends the email. When it's about to <em>do</em>, it should ask. Watch for that moment.</p>

<!--
~15 seconds. Say the word "agent" ONCE, plainly: a system that wraps a model
with tools and takes actions. Saying needs no permission; doing does — the
send step in the next demo is where you'll see it ask (tested 9/5: a real
approval prompt, approved once, not "always"). Tone: mechanism, not hype —
"does things for you" is where the marketing lives. Define it, name the
permission consequence, move on. Optional clause, no demo: "agents can also
drive a browser — I used one yesterday to fill in a course page."
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# A calendar file is ready <span class="acc-green">for review</span>

<p class="takeaway">The AI prepares the events.<br>I check them and choose whether to import them into Outlook.</p>

<!--
The school has not authorized an AI connector to Trinity's Outlook calendar. This demo uses
a downloadable .ics file and a human-controlled import. Preparing a file
does not change Outlook. Two moments of human control, name both: the one
action the AI takes — emailing me the file — asks permission first (the ⚿
moment on the next slide); the calendar write itself stays mine, after review.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> Demo · my actual fall semester</div>

# My actual <span class="acc-green">fall semester</span>

<p class="takeaway">It asked permission before sending the file. I said yes. Remember that moment.</p>

<p style="margin-top: 0.4rem;"><span class="permchip">⚿ it's asking</span></p>

<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 22px; max-width: 50rem; margin: 1.6rem auto 0;">
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">1<br><strong>Find it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">2<br><strong>Read it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">3<br><strong>Check it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">4<br><strong>Export it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px;">5<br><strong>Send it</strong></div>
</div>

<!--
RECORDING: laptop only, no phone. Cold-start the chat (incognito or memory
off) so rehearsals don't leak into the answers. Reset the email "always
allow" before this segment. Step 2 is a paste of the cropped portal schedule
screenshot (demo-assets/portal-course-schedule.png). One Claude conversation:
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
5 SEND: "Email that .ics file to my Trinity address." → the permission
  prompt. Point at the ⚿ chip: "Steps 1-4 were saying. This is doing — and
  it's asking before it acts. Read what it wants to do; approve once, never
  'always.'" Yes → the file lands in the Outlook inbox, which is exactly where
  it gets imported from. (Tested 9/5 from Claude Desktop: real approval
  prompt, file arrived.) NEVER show the Outlook inbox on camera — cut right
  after the approval. Fallback: download the file instead — no prompt, say so.
Say: "The file is ready. It hasn't changed Outlook. I review it, then import."
Claude already added the actual meetings through Ken's Google Calendar connector;
that is a separate workflow, not proof of Outlook compatibility.
Optional rehearsed finish: import into a separate Outlook
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

<h1 style="font-size: 2.5rem; margin: 0 0 0.5rem;">Claude added my classes<br>to <span class="acc-green">Google Calendar</span></h1>

<p style="font-size: 1rem !important; margin: 0 0 0.6rem;">Monday, September 14 &amp; Tuesday, September 15</p>

<svg viewBox="174 420 355 120" role="img" aria-label="Detail of Google Calendar for September 14–15, 2026. Monday shows a 1:30pm Busy entry and a 1:30pm CPSC-415 class. Tuesday shows CPSC-403 classes at 1:30pm and 2:55pm." style="display: block; width: 760px; height: 257px; max-width: 100%; margin: 0 auto; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow); overflow: hidden;">
  <image href="/images/google-calendar-trinity.png" width="1240" height="805" />
</svg>

<p style="font-size: 1.2rem !important; line-height: 1.4 !important; margin: 0.8rem 0 0;">Class meetings: created by Claude<br>“Busy” entries: Outlook calendar feed</p>

<!--
No tab switch: this is a magnified detail of the Sept 5 Google Calendar screenshot,
showing September 14–15. The original image is preserved; Slidev crops the view.
Say: "Claude added my classes through my Google Calendar connection earlier.
The Busy entries come separately from my Outlook calendar feed. Trinity hasn't
authorized an Outlook connector, so we're using a file you can review and import."
These events did not come from the file just generated. The Outlook feed is
not an AI connector and does not give Claude permission to write to Outlook.
Keep the Labor Day exclusion check in the live demo; it is outside this crop.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# I built my own course pages <span class="acc-green">the same way</span>

<p class="takeaway">Agents with tools aren't just for writing code.<br>One built this page — and blurred my phone and Zoom link here.</p>

<svg viewBox="0 0 2474 960" role="img" aria-label="The CPSC-415 AI Integration course page in Moodle, fall 2026, with cell phone number and Zoom link blurred" style="display: block; width: 680px; height: 264px; max-width: 90%; margin: 0.6rem auto 0; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow); overflow: hidden;">
  <image href="/images/moodle-cpsc415.png" width="2474" height="1446" />
</svg>

<!--
RECORDING-ONLY slide. It is a receipt, not a claim — a finished artifact on screen.
Screenshot: public/images/moodle-cpsc415.png (the real CPSC-415 Moodle course
page, with cell phone and Zoom ID blurred; same course as the schedule, one story).
Key point — using coding agents (Claude Code, Codex, Antigravity) for
productive educational work, not just programming:
1. An agent helped build this CPSC-415 Moodle course page.
2. While preparing this video, you asked the agent to grab a screenshot of the
   open Moodle window — it spotted your cell phone number and class Zoom link
   on the page and blurred those two boxes before committing to GitHub.
3. Earlier, when you wondered if the Ave Maria clip would trigger a YouTube
   copyright claim, it inspected the YouTube page source to verify it was an
   independent home recording with no Content ID block.
"I'm not telling you what AI could do for a professor. This is what it did
for this one."
SPOKEN BEAT — the line that wins over colleagues: "Every professor has to
set up a Moodle page for every class, every semester. Nobody enjoys it.
When I tell faculty I had my AI tool do mine, the response is always
'Wait, what?'" The lesson for the room: automating the thing everyone
hates is what converts skeptics — and this page is the one that did it.
No tooling detail here (no MCP, no product tour); the screenshot is the proof.
Then straight into section 4.
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

<div style="display: grid; grid-template-columns: 1fr 20rem; gap: 2rem; max-width: 52rem; margin: 1.4rem auto 0; align-items: center;">
  <div style="padding: 1.2rem 1.7rem; border-left: 4px solid var(--lamp-blue); background: rgba(110,139,255,0.08); text-align: left;">
    <p style="margin: 0; color: var(--fg); font-size: 1.75rem; line-height: 1.35;">“I need to wash my car.<br><strong>Should I walk or drive?</strong>”</p>
  </div>
  <img src="/images/carwash.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="A car covered in foam inside a car wash bay" />
</div>

<p style="margin-top: 1rem; font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem; color: var(--faint);">Gemma 4 12B · local model in Ollama</p>

<!--
The setup: the question is reformatted for the room; use the full original
wording in the app. Give students a beat to choose "walk or drive" before the reveal. The model is gemma4:12b-mlx in the Ollama app (the app collapses the
model's thinking to "Thought for N seconds" — no --think flag needed). LIVE
OPTION: switch to the app and run it now; then come back and advance. If not
running it live, just advance — the next slide is the answer.
[Sources]
Photo: Clarence Tioh, Unsplash (Unsplash License):
https://unsplash.com/photos/kQdY2pR-ic8
[/Sources]
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

<div style="display: grid; grid-template-columns: 1fr 15rem; gap: 2.2rem; max-width: 48rem; margin: 1.2rem auto 0; align-items: center;">
  <p class="takeaway" style="text-align: left; margin: 0;">For an urgent unexpected call, hang up and call back using a number you already know.</p>
  <img src="/images/phone-handset.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="A corded telephone handset lying off the hook" />
</div>

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
Photo: Alexander Andrews, Unsplash (Unsplash License):
https://unsplash.com/photos/black-corded-telephone-JYGnB9gTCls
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
Set up the habit: an explanation from the model is just another generated
output — the source is what we inspect. Another chatbot agreeing is not
independent confirmation. Next slide demonstrates this with a famous quote
that ties directly into Section 6.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · check the evidence</div>

<div style="display: grid; grid-template-columns: 13rem 1fr; gap: 2.4rem; max-width: 54rem; margin: 0.4rem auto 0; align-items: center; text-align: left;">
  <img src="/images/mark-twain-1907.jpg" style="width: 100%; border-radius: 8px; box-shadow: 0 6px 24px var(--shadow);" alt="Mark Twain, head-and-shoulders portrait, 1907, by A.F. Bradley" />
  <div>
    <h1 style="font-size: 2.5rem; margin: 0 0 0.8rem;">“Never let your schooling interfere with your <span class="acc-purple">education</span>.”</h1>
    <p class="takeaway" style="margin: 0; max-width: none;">Usually attributed to Hartford's own Mark Twain.<br><v-click>Actually written by <strong>Grant Allen (1894)</strong> — pinned on Twain in a 1907 air-rifle ad.</v-click></p>
  </div>
</div>

<div style="margin-top: 0.9rem; font-family: 'IBM Plex Mono', monospace; font-size: 0.8rem; color: var(--faint);"><a href="https://quoteinvestigator.com/2010/09/25/schooling-vs-education/" target="_blank" rel="noopener noreferrer">quoteinvestigator.com</a> · <a href="https://marktwainstudies.com/the-apocryphal-twain-never-let-schooling-interfere-with-your-education/" target="_blank" rel="noopener noreferrer">marktwainstudies.com</a></div>

<!--
1. Show the quote first: almost everyone attributes "Never let your schooling
   interfere with your education" to Mark Twain, who lived right down the
   street from Trinity in Hartford. Because that attribution is repeated all
   over the internet, ungrounded prediction will happily repeat it too.
2. Click to reveal (and optionally open the linked Quote Investigator or
   Center for Mark Twain Studies page): when you check the primary sources,
   Twain never wrote it. Grant Allen wrote it in 1894 (in Post-Prandial
   Philosophy: "What a misfortune it is that we should thus be compelled to
   let our boys' schooling interfere with their education!"), and it first got
   attached to Mark Twain in a 1907 magazine ad for Daisy Air Rifles.
3. Also note: you can check a specific claim from the earlier Bach/Gounod Pet
   conversation the exact same way.
[Sources]
Quote Investigator: https://quoteinvestigator.com/2010/09/25/schooling-vs-education/
Center for Mark Twain Studies: https://marktwainstudies.com/the-apocryphal-twain-never-let-schooling-interfere-with-your-education/
Portrait: A.F. Bradley, 1907. Library of Congress Prints & Photographs
Division, LC-USZ62-5513, "no known restrictions on publication":
https://www.loc.gov/pictures/item/2004672770/
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
Lands the verification section and sets up the learning vs. task-completion slide.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 6 · Using AI for learning</div>

# Completing the task is not <span class="acc-green">learning</span>

<p class="takeaway">AI can finish the assignment without teaching you anything.<br>Ask questions that make you think <em>more</em>, not less.</p>

<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 28px; max-width: 46rem; margin: 1.8rem auto 0;">
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“Quiz me”</strong><br><span style="font-size: 1rem; color: var(--muted);">Test yourself first</span></div></v-click>
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“Give me a hint”</strong><br><span style="font-size: 1rem; color: var(--muted);">Not the answer</span></div></v-click>
  <v-click><div style="border-top: 2px solid var(--lamp-green); padding-top: 12px;"><strong style="color: var(--fg); font-size: 1.25rem;">“Challenge this”</strong><br><span style="font-size: 1rem; color: var(--muted);">Spot weak assumptions</span></div></v-click>
</div>

<!--
~30 seconds. Pivot on the Grant Allen quote we just verified:
Almost all of today's examples are about not letting your schooling interfere
with your education — getting the calendar logistics out of the way and using
AI to follow your own curiosity (like the Bach/Gounod rabbit hole), rather
than hunting for a shortcut to get an A without learning anything.
Completing the task ≠ learning from the task: AI can produce the artifact
without producing the learning, and the bill comes due on the exam.
Click through the three better asks:
1. "Quiz me" — test yourself before the exam does.
2. "Give me a hint" — get unstuck without skipping the struggle.
3. "Challenge this" — ask what your argument is assuming or leaving out.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 6 · Using AI for learning</div>

# Know the rules. <span class="acc-green">Own the result.</span>

<p class="takeaway">Every course sets its own policy — check before you use it.<br>Disclose what you used, and remember you own what you submit.</p>

<!--
~20 seconds. Distilled from Ewa's policy & accountability slides:
Every professor (and workplace) sets their own policy — Yes, No, or Sometimes
— for good reasons. Check the syllabus before you use it, disclose what you
used and keep the record, and remember that you — not the AI — are
responsible for everything you submit.
Say why the rules vary (candor, not apology): a lot of faculty are
skeptical about AI in education, and they're right to be — it is
disrupting teaching on a scale I'd compare to the arrival of the internet.
Your professors are working this out in real time, which is why the policy
differs from one course to the next. That turns "check the syllabus" from
a rule into an explanation.
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
capabilities or literal intentions of every system.
"They're like eager toddlers: they want to please you, and they have a
toddler's grasp on reality. Verify anything that matters. Ask for help
thinking, not for a way out of thinking."
-->
