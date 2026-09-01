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
~30 minutes, six sections, demos as evidence, one point per slide — advance
briskly; the slides are backdrops, not documents. Ewa introduces; she follows
with AI-in-college and the integrity policy, so stay OFF policy and integrity.
Tone check: mechanism and evidence, never advocacy — this must not read as marketing.
Optional opener (one breath): "When an AI answer sounds polished, what would
make you trust it?" — the closing slide answers it.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# AI is not new — <span class="acc-blue">this moment</span> is

<p class="takeaway">Research since the 1950s. What changed: massive data, massive computation, and a few breakthroughs — landing together.</p>

<!--
One breath on history — don't linger. The point: decades in progress, so it
doesn't read as unexplainable magic that just appeared.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# You've used AI <span class="acc-blue">for years</span>

<p class="takeaway">Recommendation systems — Spotify, TikTok, Netflix — autocomplete, spam filters. Machine learning is one part of AI.</p>

<!--
Familiar examples do the defining: they've been AI users since middle school
without calling it that.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# Generative AI <span class="acc-blue">creates</span>

<p class="takeaway">Text, images, audio: ChatGPT, Claude, Gemini, image generators. One kind of machine learning — the kind you'll touch, and today's focus.</p>

<!--
Other kinds of AI exist; we focus on generative because that's what they'll
actually encounter.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 1 · What AI actually is</div>

# The model is the engine.<br>You drive the <span class="acc-blue">system</span>.

<p class="takeaway">ChatGPT, Copilot, and BoodleBox wrap a model with tools, search, and an interface. You interact with systems.</p>

<!--
Model vs. system in one sentence: the model is the engine; the products are
cars built around one. This distinction pays off in §4 (same model, different
behavior with different tools).
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How it works</div>

# A very good <span class="acc-purple">prediction machine</span>

<p class="takeaway">Training: it learns statistical patterns from enormous amounts of text. Generation: it predicts the next token, again and again.</p>

<!--
The framework everything else hangs on — §4 and §6 both come back to this
slide's idea. Straight into the tokenizer demo as evidence.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · tokens</div>

# What the AI <span class="acc-purple">actually sees</span>

<p class="takeaway">For a language model: numbered text fragments. It generates text one token at a time, which helps explain why tasks like counting can be unexpectedly difficult.</p>

<!--
Tokenizer playground: "Trinity College", a sentence from the academic calendar page, switch
vendors — common words one token, rare words shatter. Optional quick aside
(the standard trick question): "I need to wash my car. There's a carwash 50m
away. Should I walk or drive?" — many models, even good ones, advise walking;
the car has to be there. Pure prediction, no model of the world. Skip it
without guilt. Optional if it fits: price per million tokens is a column on
OpenRouter — "free" has a meaning.
Fallback: OpenAI tokenizer page.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How it works</div>

# Coherent — <span class="acc-purple">without knowing</span>

<p class="takeaway">Fluent, polished, confident text is what it was trained to produce. Coherence does not guarantee knowledge or understanding.</p>

<!--
This is why it can sound so right. "Fluent is not the same as verified" — the
sentence §4 and §6 will keep cashing in.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 2 · How it works</div>

# <span class="acc-purple">Context</span> is most of what it has

<p class="takeaway">The prompt and the whole conversation shape every answer — along with training and any tools or search the system can use.</p>

<!--
Sets up the Pet demo: a conversation is accumulated context, and you're about
to watch that work live.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> Demo · Bach → Gounod, in conversation</div>

# Just keep <span class="acc-purple">asking</span>

<p class="takeaway">You don't ask an AI what you'd ask a search engine. One question becomes ten — and the conversation is where the understanding happens.</p>

<!--
~5 min — the §2 centerpiece, and live evidence for the context slide before
it. Play Bach's Prelude in C major alone, then Gounod's melody over it
(TODO(Ken): audio files + cue points → demo-assets/). Then the Pet in Codex,
BY VOICE, interruptible: "Was this a common practice?" → "Did Gounod do this
with other pieces?" → "Was Bach a common source for this sort of thing?" →
"What are some other examples?" Follow the thread wherever it goes — the
free-association IS the demo. Push back once on purpose ("really? I thought…")
— plants the seed §4's sycophancy demo pays off.
Mechanism callback, one sentence: every follow-up works because the whole
conversation is the context.
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
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Where prediction <span class="acc-green">shines</span>

<p class="takeaway">Five quick strengths — then my actual fall semester as evidence.</p>

<!--
Frame before the rapid-fire: these are common capabilities, not guarantees;
the demos are the evidence. "What works, what you can access, and the quality
of the result all vary by tool and will change while you're here." Advance
fast through the next five — a few seconds each, spoken over, not read.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Explain. Summarize. <span class="acc-green">Rewrite.</span>

<p class="takeaway">Any length, any register — within context and output limits; quality still varies.</p>

<!--
A few seconds. Spoken example: "explain this reading like I'm new to the
field" / "tighten this paragraph."
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Ten options in <span class="acc-green">ten seconds</span>

<p class="takeaway">Counterarguments, questions, ways to organize material — generating possibilities is what it's for.</p>

<!--
A few seconds. The point: possibilities are cheap; choosing is still yours.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# The boring work, <span class="acc-green">at scale</span>

<p class="takeaway">Extract, reformat, tabulate, translate — repetitive transformations, fast.</p>

<!--
A few seconds. You're about to watch this happen to a semester's schedule.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Across <span class="acc-green">mediums</span>

<p class="takeaway">Paste a screenshot, get an answer. Text in, speech out. Words in, a picture out.</p>

<!--
A few seconds. Tees up the schedule screenshot — and the next slide is
"words in, a picture out," for laughs.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

<div style="display: flex; gap: 40px; justify-content: center; align-items: flex-end; margin-top: 0.4rem;">
  <img src="/images/cc-cover.png" style="height: 400px; border-radius: 6px; box-shadow: 0 8px 32px rgba(0,0,0,0.5);" alt="Official cover of Claude Code: Up and Running" />
  <v-click><img src="/images/ram-cover.jpg" style="height: 400px; border-radius: 6px; box-shadow: 0 8px 32px rgba(0,0,0,0.5);" alt="Generated image of a ram in a sweater reading the book by a fire" /></v-click>
</div>

<p class="takeaway" style="margin-top: 1.2rem; font-size: 1.1rem;">Left: my book's actual cover. <v-click><span>Right: the ram reads his own book.</span></v-click></p>

<!--
~15 seconds, mostly for the laugh. Real cover shows first; NEXT reveals the
ram and its caption. Then: "I used Nano Banana to make the other one." Mention you've done this for all your books —
they're on your home page. Then move on. Tone: it's a joke about your own
book, not a product pitch.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> 3 · What AI does well</div>

# Practice, with <span class="acc-green">feedback</span>

<p class="takeaway">It can generate questions and respond to your attempts. You'll see it quiz me in a minute.</p>

<!--
A few seconds — the quiz step of the spine is the evidence, and for this
audience it's the beat that matters most.
-->

---
layout: center
class: glow-green text-center
---

<div class="eyebrow acc-green"><span class="lampdot dot-green"></span> Demo · my actual fall semester</div>

# My actual <span class="acc-green">fall semester</span>

<p class="takeaway">It asked permission before touching my calendar. I said yes. Remember that moment.</p>

<p style="margin-top: 0.4rem;"><span class="permchip">⚿ it's asking</span></p>

<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 22px; max-width: 50rem; margin: 1.8rem auto 0;">
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">1</span><br><strong>Find it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">2</span><br><strong>Read it</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">3</span><br><strong>Remind me</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">4</span><br><strong>Quiz me</strong></div>
  <div style="border-top: 2px solid var(--lamp-green); padding-top: 10px; text-align: left;"><span style="font-family: 'IBM Plex Mono', monospace; color: var(--lamp-green); font-size: 0.85rem;">5</span><br><strong>Email it</strong></div>
</div>

<!--
The centerpiece, all real — one Claude conversation carries steps 1-4:
1 FIND IT: "Find the current Trinity approved academic calendar." It picks
  Hartford, not Dublin or Oxford — because the system knows you. Say so:
  that's the context slide and model-vs-system, live.
2 READ IT: paste the portal "My Course Schedule" screenshot. "Which dates
  won't my classes meet this fall?" Vision + reasoning against the calendar
  it just found. Date arithmetic is where models slip — VERIFY ONE no-class
  date against the calendar page on screen before going further. A live
  mistake here is §6 arriving early, not a failure.
3 REMIND ME: "Add a reminder to my calendar for the first week we don't
  meet." Pause on the permission prompt — point at the ⚿ chip; say "it's
  asking before it acts — read what it wants to do, and afterwards check
  what it changed"; permission is not privacy or correctness. Say yes, show
  the event land in the calendar tab. "And it could add all of them."
  (Delete the event between sessions.)
4 QUIZ ME: same conversation — "Quiz me on [week-1 reading / what we just
  worked out]. One question at a time. Don't give me the answer until I've
  tried twice." Answer one wrong on purpose; let it coach. THE beat that
  decides 'cheating machine' vs. 'study partner' — don't rush it. Night-before
  option: Gemini Notebook with a fresh notebook, if it impresses in rehearsal
  — say "(formerly NotebookLM)" once if used.
5 EMAIL IT: Copilot/Outlook — "Draft an email to my students listing the
  dates we won't meet this fall." Read it aloud, edit one sentence live: it
  proposes, you decide. The spine ends here.
Full menu by design; Ken trims the night before.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# The failure modes are <span class="acc-blue">predictable</span> too

<p class="takeaway">Same mechanism, same weaknesses. After the last half hour, none of these should surprise you.</p>

<!--
Section turn — the tone shifts here. Honest calibration throughout: don't
present 2024 failure modes as current.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# Same question, <span class="acc-blue">different answers</span>

<p class="takeaway">Generation is probabilistic — inconsistency is normal. And every answer is shaped by training data, prompts, instructions, and tools.</p>

<!--
Quick beat: variance isn't a bug you can file; it's the mechanism. Inputs
matter — which is why the same model behaves differently in different
products (callback to model vs. system).
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# It may tell you what you <span class="acc-blue">want to hear</span>

<p class="takeaway">Push back confidently and a model may yield — even when it was right.</p>

<!--
Sycophancy — the failure mode they haven't heard of, and Ewa considers the
bigger present-day issue. Straight into the fold demo as evidence.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> Demo · sycophancy</div>

# Watch it <span class="acc-blue">fold</span>

<p class="takeaway">It gave the right answer. I insisted it was wrong. It apologized — and agreed with me.</p>

<!--
Rehearsed pushback demo in the Ollama app: ask something with a checkable
right answer, get it, then insist confidently on a wrong one and see whether
the response follows the pressure instead of the evidence. Behavior varies by
model and prompt; rehearse the exact example. Confidence in the answer is not
evidence.
9/1 rehearsal (re-verify morning-of): gemma4:12b-mlx — "What year was Trinity
College in Hartford founded?" (1823, correct), push back with "No — it was
1845, I'm certain, I teach there" → instant fold. It's the room's own school,
checkable on trincoll.edu in five seconds.
Fallback: show the rehearsal screenshot and describe the exchange.
-->

---
layout: center
class: glow-blue text-center
---

<div class="eyebrow acc-blue"><span class="lampdot dot-blue"></span> 4 · What AI does poorly</div>

# A perfect-looking citation <span class="acc-blue">may not exist</span>

<p class="takeaway">Looking real is not being real. Newer systems fabricate less — none are immune, and price and size are no guarantee.</p>

<!--
PENDING ASSET: this slide is the home for the rehearsal screenshot — a small
local model inventing five perfect-looking scholarly sources. Crop to one
legible fabricated citation + the proof it doesn't exist; add as rendered
content before the final export. Until then, describe it in one breath.
Disclosure beat (always say it with the evidence): "This is one small model
on my laptop, with one prompt — a bigger model, or one with search, would
likely do better." Honesty upgrade: "The bigger version of this same model
actually declined — it warned me its sources were only 'representative.' The
smaller one invented five citations without blinking. Same family, same
question — and from the chat window, you can't tell which kind you're
talking to."
9/1 rehearsal command (Ollama app on stage; CLI for the screenshot):
ollama run gemma4:12b-mlx --think=false "I'm writing a paper on how Gounod's
Ave Maria was received in 19th-century Paris. List five sources I can cite,
with author, year, and journal." — do NOT use gemma4:latest (it hedges).
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
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 6 · How to verify AI output</div>

# An answer is not <span class="acc-purple">the truth</span>

<p class="takeaway">Wrong on simple things, right on hard ones — surface confidence is not evidence of accuracy.</p>

<!--
Section numbering is the shared outline's: Ewa covers §5 (how to use AI
effectively) right after this — jumping from 4 to 6 is intentional; say "Ewa
will take number five" if it needs a word.
Callback to §2: prediction, not knowledge — that's WHY verification is on you.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 6 · How to verify AI output</div>

# Open <span class="acc-purple">the source</span>

<p class="takeaway">For anything that matters: click through, find the passage, and check that it says what the answer claims.</p>

<!--
Demo lives here (self-contained): in the frontier chat with search on, ask
for scholarly sources on the Gounod reception topic from §2, click ONE citation, find
the quoted passage in the actual source. Thirty seconds. Fast, undramatic,
exactly the habit they should copy. Calibration beat: "Newer systems reduce
fabrication, but no model, product tier, or polished interface removes the
need to check."
Second verification move (30 sec, spoken or live): tell it you LIKED its
answer — then ask it to argue the exact opposite. This doesn't tell you which
answer is true — it tells you the confidence carries no information. Frame as
verification (testing the answer), not usage — usage is Ewa's §5.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 6 · How to verify AI output</div>

# Make it <span class="acc-purple">show its work</span>

<p class="takeaway">Ask for the quote and the page — then check the quote. Cross-check with a second tool, a search engine, or the actual reading.</p>

<!--
Quick beat. The habit stack: source → quote → cross-check.
-->

---
layout: center
class: glow-purple text-center
---

<div class="eyebrow acc-purple"><span class="lampdot dot-purple"></span> 6 · How to verify AI output</div>

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
Timing: full menu ~31; Ken chooses the night before (email, Pet follow-up
count, sycophancy live/screenshot). Live overrun
ladder after those choices: compress §1 to one breath → cap the Pet
conversation at two follow-ups (skip the meta beat, keep the Ewa tee-up) →
drop the sycophancy demo (keep the bullet, say it in a sentence). The spine,
the Pet conversation, and the voice clone are the fixed points.
Hand back to Ewa: she covers §5 (using AI effectively), then AI in the context
of college, the integrity policy, and where this is headed — then Andrew on
the year's events and the AI Lab.
-->
