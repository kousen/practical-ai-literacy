---
theme: seriph
colorSchema: dark
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
---

<style>
:global(:root) {
  --fg: #F2F1ED;
  --bg: #101114;
  --muted: #A6ABB5;
  --faint: #5D636E;
  --lamp-blue: #6E8BFF;
  --lamp-purple: #C36BFF;
  --lamp-green: #4ADE80;
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
:global(.slidev-layout p) { color: var(--muted); font-size: 1.35rem; line-height: 1.5; }
:global(.eyebrow) {
  font-family: 'IBM Plex Mono', Menlo, monospace;
  font-size: 0.95rem; letter-spacing: 0.14em; text-transform: uppercase;
  display: flex; align-items: center; gap: 12px; justify-content: center;
  margin-bottom: 1.4rem;
}
:global(.section .eyebrow) { justify-content: flex-start; }
:global(.lampdot) { width: 13px; height: 13px; border-radius: 50%; display: inline-block; }
:global(.acc-blue)   { color: var(--lamp-blue); }
:global(.acc-purple) { color: var(--lamp-purple); }
:global(.acc-green)  { color: var(--lamp-green); }
:global(.dot-blue)   { background: var(--lamp-blue); box-shadow: 0 0 16px var(--lamp-blue); }
:global(.dot-purple) { background: var(--lamp-purple); box-shadow: 0 0 16px var(--lamp-purple); }
:global(.dot-green)  { background: var(--lamp-green); box-shadow: 0 0 16px var(--lamp-green); }
:global(.glow-blue)   { background: radial-gradient(1100px 700px at 88% -18%, rgba(110,139,255,0.20), transparent 62%), var(--bg) !important; }
:global(.glow-purple) { background: radial-gradient(1100px 700px at 88% -18%, rgba(195,107,255,0.20), transparent 62%), var(--bg) !important; }
:global(.glow-green)  { background: radial-gradient(1100px 700px at 88% -18%, rgba(74,222,128,0.18), transparent 62%), var(--bg) !important; }
:global(.glow-tri) { background:
  radial-gradient(900px 600px at 6% -14%, rgba(110,139,255,0.21), transparent 60%),
  radial-gradient(900px 600px at 102% 8%, rgba(195,107,255,0.17), transparent 60%),
  radial-gradient(1000px 560px at 50% 122%, rgba(74,222,128,0.15), transparent 62%),
  var(--bg) !important; }
:global(.takeaway) { max-width: 40rem; margin-left: auto; margin-right: auto; text-wrap: pretty; }
:global(.section) { text-align: left; padding-top: 2.2rem; padding-bottom: 2.2rem; }
:global(.section .eyebrow) { margin-bottom: 0.9rem; }
:global(.section h1) { font-size: 2.1rem !important; margin-bottom: 1.1rem; }
:global(.section ul) { font-size: 1.02rem; line-height: 1.42; color: var(--muted); max-width: 46rem; }
:global(.section ul li) { margin-bottom: 0.5rem; }
:global(.section ul li strong) { color: var(--fg); }
:global(.contact) { font-size: 0.95rem !important; line-height: 1.65; color: #C8CCD4 !important; opacity: 1 !important; }
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

<!--
~30 minutes, six sections, demos as evidence. Ewa introduces; she follows with
AI-in-college and the integrity policy, so stay OFF policy and integrity here.
Tone check: mechanism and evidence, never advocacy — this must not read as marketing.
Optional opener (one breath): "When an AI answer sounds polished, what would
make you trust it?" — the closing slide answers it.
-->

---
layout: center
class: section glow-blue
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# AI is not new — <span class="acc-blue">this moment</span> is

- AI research goes back to the **1950s**; what changed recently is **massive data + massive computation** + a few algorithmic breakthroughs landing together
- **Machine learning is one part of AI; generative AI is one kind of machine learning.** You've used other AI for years: **recommendation systems** (Spotify, TikTok, Netflix), autocomplete, spam filters
- Generative AI **creates** text, images, and audio: ChatGPT, Claude, Gemini, image generators
- A **model** is the trained engine; a **system** (ChatGPT, Copilot, BoodleBox) wraps a model with tools, search, and an interface — you interact with systems
- Other kinds of AI exist; today we focus on **generative AI**, because that's what you'll touch

<!--
One or two breaths on history — don't linger. The point: this has been in
progress for decades; they need the context so it doesn't read as unexplainable
magic that just appeared. Familiar examples first: they've been AI users since
middle school without calling it that.
-->

---
layout: center
class: section glow-purple
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How language models generate text</div>

# A very good <span class="acc-purple">prediction machine</span>

- **Training**: a language model learns statistical patterns from large text collections. **Generation**: it predicts one token at a time
- It doesn't see words — it sees **tokens**, numbered fragments of text
- Repeated prediction can produce fluent, polished text; **coherence does not guarantee factual knowledge or human understanding**
- **Context matters**: the prompt and conversation shape the response, alongside training and any tools or search the system can use

<!--
"For language models, text generation happens one token at a time." Sections 4
and 6 come back to the distinction between fluent prediction and verified
knowledge. Then straight into the tokenizer demo as evidence.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · tokens</div>

# What the AI <span class="acc-purple">actually sees</span>

<p class="takeaway">For a language model: numbered text fragments. It generates text one token at a time, which helps explain why tasks like counting can be unexpectedly difficult.</p>

<!--
Tokenizer playground: "Trinity College", a sentence from the syllabus, switch
vendors — common words one token, rare words shatter. Optional quick aside
(the standard trick question): "I need to wash my car. There's a carwash 50m
away. Should I walk or drive?" — many models, even good ones, advise walking;
the car has to be there. Pure prediction, no model of the world. Skip it
without guilt — Bach/Gounod carries the mechanism beat next. Optional if it fits: price per
million tokens is a column on OpenRouter — "free" has a meaning.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · Bach → Gounod, in conversation</div>

# Just keep <span class="acc-purple">asking</span>

<p class="takeaway">You don't ask an AI what you'd ask a search engine. One question becomes ten — and the conversation is where the understanding happens.</p>

<!--
~5 min — the §2 centerpiece, and live evidence for the "context matters"
bullet. Play Bach's Prelude in C major alone, then Gounod's melody over it
(TODO(Ken): audio files + cue points → demo-assets/). Then the Pet in Codex,
BY VOICE, interruptible: "Was this a common practice?" → "Did Gounod do this
with other pieces?" → "Was Bach a common source for this sort of thing?" →
"What are some other examples?" Follow the thread wherever it goes — the
free-association IS the demo. Push back once on purpose ("really? I thought…")
— plants the seed §4's sycophancy demo pays off later.
Mechanism callback, one sentence: every follow-up works because the whole
conversation is the context — that's the "context matters" bullet, live.
META BEAT to close: "Everything you just watched was live. Is this a good way
to use these tools? What would you watch out for?" — one beat of silence, then
hand it forward: "Hold that thought — that's exactly what Ewa's section is
about." (Tell Ewa on the Wed call so she can catch the pass.)
Fallback ladder: pet fails → same conversation typed in a chat window; AV
fails entirely → rehearsal screenshots and narrate one exchange.
Tech check (Tue 5 pm): laptop audio over HDMI (the volume knob), pet input
via laptop mic from stage position, echo/self-hearing, interruption.
-->

---
layout: center
class: section glow-green
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Common strengths — <span class="acc-green">and limits</span>

- **Explain, summarize, rewrite** — within context and output limits; quality still varies
- **Generate options**: counterarguments, questions, or possible ways to organize material
- **Assist with repetitive transformations**: extract, reformat, tabulate, translate
- **Work across mediums**: photograph a page, get a table; text in, speech out
- **Offer practice and feedback**: generate questions and respond to your attempts

<!--
Frame before demos: these are common capabilities, not guarantees; the demos
are evidence. "What works, what you can access, and the quality of the result
all vary by tool and will change while you're here."
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> Demo · one syllabus, four tools</div>

# One syllabus, <span class="acc-green">four tools</span>

<p class="takeaway">It asked permission before touching my calendar. I said yes. Remember that moment.</p>

<p style="margin-top: 0.4rem;"><span class="permchip">⚿ it's asking</span></p>

<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 26px; max-width: 44rem; margin: 1.8rem auto 0;">
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">1</span><br><strong>Photograph it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">2</span><br><strong>Schedule it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">3</span><br><strong>Quiz me on it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">4</span><br><strong>Email about it</strong></div>
</div>

<!--
The centerpiece: photo→table (vision — then check ONE extracted deadline
against the printed syllabus before scheduling anything: verification inside
the successful workflow, not an afterthought), study schedule→calendar (pause
on the permission prompt — point at the ⚿ chip on screen; say "it's asking
before it acts — read what it wants to do, and afterwards check what it
changed"; permission is not the same as privacy or correctness; repeat the
pause on ANY later permission prompt, same beat, same chip), quiz-me in Gemini Notebook —
say "(formerly NotebookLM)" ONCE, then just Gemini Notebook — "quiz me, don't
tell me" (answer one wrong on purpose — the tutoring beat matters most for
this audience), Copilot email draft (edit a sentence live: it proposes, you
decide), then the poster on the next slide (live or static — night-before
call). Full menu by design; Ken trims the night before.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> Demo · same syllabus, one poster</div>

# One more trick — <span class="acc-green">make it a picture</span>

<p class="takeaway">Same document, fifth tool: a study poster generated from this syllabus. Text in, visual out.</p>

<!--
LIVE OR STATIC — night-before call. Live (~2 min): Nano Banana (Gemini image
generation) — "Turn this syllabus into a one-page study poster / six-week
timeline diagram"; the repo's image-prompt skill can pre-write the prompt.
Static (~30 sec): show the pre-generated poster with the honest line "I made
this from the same syllabus during rehearsal — took about a minute" (put the
image on this slide before the final export if going static).
Either way, generate the asset during rehearsal — it's the static option AND
the live fallback. Keeps the one-document story's visual ending.
-->

---
layout: center
class: section glow-blue
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# The failure modes are <span class="acc-blue">predictable too</span>

- **Outputs vary**: probabilistic generation can produce different or inconsistent answers
- **Sycophancy**: models may mirror your view or yield to confident pushback
- **Looking real ≠ being real**: a plausible-looking citation may not exist
- **Fabrication persists**: newer systems reduce it; price and model size are not guarantees
- **Inputs matter**: training data, prompts, instructions, and tools can introduce errors

<!--
Both §4 demos hang off this slide (sycophancy, then the voice clone). PENDING
ASSET: add the rehearsal screenshot of a local model inventing five
perfect-looking scholarly sources as rendered slide content before the final
export. Until then, describe the example while giving the looking-real bullet,
one breath, move on. Calibrate it as one model and prompt, not a model tier.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · sycophancy</div>

# Watch it <span class="acc-blue">fold</span>

<p class="takeaway">It gave the right answer. I insisted it was wrong. It apologized — and agreed with me.</p>

<!--
Rehearsed pushback demo: ask something with a checkable right answer, get it,
then insist confidently on a wrong one and see whether the response follows
the pressure instead of the evidence. Behavior varies by model and prompt;
rehearse the exact example. Confidence in the answer is not evidence.
Fallback: show the rehearsal screenshot and describe the exchange.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · looking real vs. being real</div>

# That was my voice. <span class="acc-blue">Except it wasn't.</span>

<p class="takeaway">A cloned voice, created from minutes of audio. It sounds like me — and it isn't me. Looking real is not being real.</p>

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
repeatable tip of the day.
-->

---
layout: center
class: section glow-purple
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 6 · How to verify AI output</div>

# An answer is not <span class="acc-purple">the truth</span>

- It can be **wrong on simple things and right on hard ones** — surface confidence is not evidence of accuracy
- **Open the source.** For consequential claims, inspect the actual page
- **Cross-check**: a second tool, a search engine, the actual reading
- Ask it to **show its work** — quote the passage, cite the page — then check the quote
- The essential check: **can you explain how the evidence supports the claim?**

<!--
Section numbering is the shared outline's: Ewa covers §5 (how to use AI
effectively) in her part, right after this — jumping from 4 to 6 is intentional;
say "Ewa will take number five" if it needs a word.
Callback to §2: prediction, not knowledge — that's WHY verification is on you.
Demo (self-contained now that the Ollama contrast is gone): in the frontier
chat with search on, ask for scholarly sources on the niche syllabus topic,
click ONE citation, find the quoted passage in the actual source. Thirty
seconds. Fast, undramatic, exactly the habit they should copy.
Second verification move (30 sec, spoken or live): tell it you LIKED its
answer — then ask it to argue the exact opposite. If it flips with equal
confidence, you've just measured what its confidence is worth. Frame as
verification (testing the answer), not as a usage tip — usage is Ewa's §5.
-->

---
layout: center
class: glow-tri text-center
---

<div class="eyebrow">
  <span class="lampdot dot-blue"></span><span class="lampdot dot-purple"></span><span class="lampdot dot-green"></span>
</div>

# They're eager <span class="acc-green">toddlers</span>

<p class="takeaway">They want you to keep talking, and they want you to be happy — with a toddler's grasp on reality. So verify anything that matters. Ask for help <strong>thinking</strong>, not for a way out of thinking.</p>

<p class="contact">
<strong style="color: var(--fg);">Ken Kousen</strong><br>
Professor of the Practice, Computer Science Department<br>
Associate Director, Elting Center for Innovation &amp; Entrepreneurship<br>
<span style="font-family: 'IBM Plex Mono', monospace;" class="acc-blue">kenneth.kousen@trincoll.edu</span>
</p>

<!--
Ken's framing — the metaphor is a mnemonic, not a mechanism: §2 explained the
mechanism; this is how to REMEMBER the failure modes. Eager toddler = wants
you to keep talking (engagement), wants you to be happy (sycophancy — the
"watch it fold" demo), tenuous grasp on reality (the fabricated citations).
It ties every demo they just saw into one image.
Say the HANDOFF explicitly before the bio registers as "the end" — otherwise
this slide triggers premature applause: "That's my part — and I skipped
number five on purpose, because Ewa owns it. Ewa?"
Timing: full menu ~33; Ken chooses the night before (email, poster
live/static, Pet follow-up count, sycophancy live/screenshot). Live overrun
ladder after those choices: compress §1 to one breath → cap the Pet
conversation at two follow-ups (skip the meta beat, keep the Ewa tee-up) →
drop the sycophancy demo (keep the bullet, say it in a sentence). The spine,
the Pet conversation, and the voice clone are the fixed points.
Hand back to Ewa: she covers §5 (using AI effectively), then AI in the context
of college, the integrity policy, and where this is headed — then Andrew on
the year's events and the AI Lab.
-->
