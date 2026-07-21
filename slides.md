---
theme: seriph
colorSchema: light
background: https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80

addons:
  - slidev-component-progress
  - slidev-addon-qrcode

class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## Practical AI Literacy

  A half-day hands-on workshop for the Trinity College community

  By Kenneth Kousen

  Learn more at [KousenIT](https://kousenit.com)
drawings:
  persist: false
transition: slide-left
title: "Practical AI Literacy"
mdc: true
slidev:
  slide-number: true
  controls: true
  progress: true
css: unocss
---

<style>
.slidev-page-num {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  position: fixed !important;
  bottom: 1rem !important;
  right: 1rem !important;
  z-index: 100 !important;
  color: #666 !important;
  font-size: 0.875rem !important;
}
</style>

# Practical AI Literacy

### Using AI tools well in your actual work

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-gray-400 bg-opacity-10">
    Press Space to begin <carbon:arrow-right class="inline"/>
  </span>
</div>

<!--
Open with the Wispr Flow demo BEFORE introducing yourself: dictate your own intro
into a text editor faster than you could type it. Then say "that was an AI tool.
Let's talk about what just happened." Sets the tone: practical, not philosophical.
-->

---

# Contact Info

Ken Kousen
Kousen IT, Inc.

- ken.kousen@kousenit.com
- https://www.kousenit.com
- https://kousenit.org (blog)
- LinkedIn: [kenkousen](https://www.linkedin.com/in/kenkousen/)
- Newsletter: [Tales from the jar side](https://kenkousen.substack.com)
- Social: [@kenkousen](https://twitter.com/kenkousen) (X), [@kousenit.com](https://bsky.app/profile/kousenit.com) (Bluesky)

---

# Today's Plan

<style>
table { font-size: 0.85rem; }
td, th { padding: 0.3rem 0.8rem !important; }
</style>

| Time | Topic |
|------|-------|
| 0:00 | Getting started — what AI literacy means now |
| 0:15 | How AI tools actually work |
| 0:45 | Working conversationally with AI |
| 1:10 | **Lab 1:** From messy notes to useful output |
| 1:40 | Connected AI and your own data |
| 2:10 | **Lab 2:** Copilot where you already work |
| 2:25 | Multimodal AI (+ **Lab 3:** vision) |
| 2:45 | Using AI without fooling yourself (+ **Lab 4:** catch the hallucination) |
| 3:10 | Equity, classroom questions, wrap-up |
| 3:30 | Done — but the repo stays with you |

<div class="text-sm text-gray-500 mt-2">Plus a 10-minute break when a natural pause arrives</div>

<!--
All labs, data files, and these slides live in the GitHub repo.
Anything we skip today, they can do later.
-->

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:idea class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Getting Started</span>

## What AI Literacy Means Now

---

# The Question Has Changed

<v-clicks>

**Two years ago:** "Which AI tool should I use?"

**Now:** "How should I use the tools I have?"

- The major tools have converged on similar core abilities
- The differences that matter are in *workflow*: where the tool lives, what data it can see, what it's allowed to do
- Skill with one tool largely transfers to the others

</v-clicks>

---

# Why the Tools Keep Changing

<v-clicks>

- New models ship every few months; features move between products constantly
- Anything specific I tell you today has a shelf life measured in weeks
- **That's not a problem — it's the lesson**

The durable skill isn't knowing Tool X.
It's knowing how to **evaluate any tool yourself**:

1. Give it a task you already know the answer to
2. Push on it until it fails
3. Notice *where* the boundary is — that's what you learned

</v-clicks>

<!--
This is the course thesis. Everything else hangs off this slide.
-->

---
layout: image-right
image: /images/mic.jpg
---

# Demo: Speech to Clean Text

**Wispr Flow** — system-wide dictation that produces edited text, not transcripts

- Works in any application: email, documents, chat
- Removes filler words, fixes grammar, follows your formatting habits
- Faster than typing for most people, most of the time

<br>

> The point isn't this tool. The point is noticing how much of your day
> is *typing things you could have said*.

<!--
Demo: dictate a reply to a realistic IT-helpdesk email in front of them.
Include an "um" and a self-correction so they see the cleanup happen.
-->

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:machine-learning-model class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">How AI Tools Actually Work</span>

## The mental model that explains the weird behavior

---

# What a Model Is

<v-clicks>

- A **large language model** (LLM) is a program trained on enormous amounts of text to predict what comes next
- Training bakes knowledge into the model — then training **stops** at a cutoff date
- The model doesn't look things up unless you (or the product around it) give it a way to
- Everything it "knows" is patterns, not a database — which explains both its fluency and its failures

</v-clicks>

---

# One Word at a Time

<div class="text-xl mt-4 mb-6">"The Trinity College library will be closed for <span class="border-b-2 border-blue-900 px-8 text-blue-900 font-bold">?</span>"</div>

<div class="space-y-2 max-w-130">
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono">renovations</span><div class="h-5 rounded bg-amber-500" style="width: 28%"></div><span class="text-sm text-gray-500">28%</span></div>
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono">the</span><div class="h-5 rounded bg-blue-900" style="width: 17%"></div><span class="text-sm text-gray-500">17%</span></div>
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono">maintenance</span><div class="h-5 rounded bg-blue-900" style="width: 14%"></div><span class="text-sm text-gray-500">14%</span></div>
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono">summer</span><div class="h-5 rounded bg-blue-900" style="width: 11%"></div><span class="text-sm text-gray-500">11%</span></div>
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono">repairs</span><div class="h-5 rounded bg-blue-900" style="width: 8%"></div><span class="text-sm text-gray-500">8%</span></div>
  <div class="flex items-center gap-3"><span class="w-28 text-right font-mono italic">all others</span><div class="h-5 rounded bg-gray-300" style="width: 22%"></div><span class="text-sm text-gray-500">22%</span></div>
</div>

<div class="text-xs text-gray-400 mt-2">Illustrative probabilities — real numbers vary by model and context</div>

<v-clicks>

- The model scores **every possible next token**, picks one, appends it, and repeats
- It doesn't always pick the favorite — controlled randomness keeps text from sounding robotic (and is why the same question gets different answers)
- A whole report is just this loop, run thousands of times

</v-clicks>

<!--
Point at "the" in second place: even function words compete. And note there's
no step where it checks facts — just plausibility, which sets up hallucination.
-->

---

# Tokens: The Unit of Everything

<v-clicks>

- Models read and write **tokens** — word fragments, roughly ¾ of a word each
- "Trinity College" ≈ 3–4 tokens; this slide ≈ 100 tokens
- Everything is metered in tokens:
  - What you send (input) and what it writes (output)
  - API pricing is quoted **per million tokens**
  - The model's memory is measured in tokens too →

</v-clicks>

<v-click>

> **Live demo:** [The Tokenizer Playground](https://huggingface.co/spaces/Xenova/the-tokenizer-playground) —
> paste your own text and watch it split into tokens

</v-click>

---

# Context Windows

The model's **working memory** for your conversation

<v-clicks>

- Everything it can currently see: your messages, its replies, attached files
- Modern tools accept hundreds of thousands of tokens — hundreds of pages
- But the window is finite, and here's what that explains:
  - **Forgetting:** early parts of long chats fall out of view or get summarized
  - **Drift:** the conversation's accumulated text starts steering the answers
  - **"Start a new chat" fixes things** because it empties the window

</v-clicks>

<!--
Practical rule of thumb: one task, one chat. Long-running chats degrade.
-->

---

# Why Tools Confidently Invent Things

<v-clicks>

- The model always produces *plausible* text — that's the only thing it does
- When it knows the answer, plausible = correct
- When it doesn't, plausible = **a confident, fluent, wrong answer**
- It has no internal "I don't know" signal — no feeling of uncertainty to report
- This is called **hallucination**, and it is a property of the technology, not a bug that will be patched next release

</v-clicks>

<br>

<v-click>

> We'll spend a whole section on defending against this. For now:
> **fluency is not evidence.**

</v-click>

---

# The Commercial Landscape

| Product | Company | Where you meet it |
|---------|---------|-------------------|
| ChatGPT | OpenAI | Web/app; Codex agent now built into the ChatGPT UI |
| Claude | Anthropic | Web/app/desktop; Claude Code for terminal work |
| Copilot | Microsoft | **Inside Outlook, Word, Excel, Teams — and your M365 data** |
| Gemini | Google | Web/app; inside Google Workspace |

<v-click>

All four are capable general assistants. The practical difference is **where they live and what they can see** — which is why Copilot matters at Trinity even if another tool tops today's benchmarks.

</v-click>

<!--
Current model names (July 2026): GPT-5.x, Claude 5 family (Fable 5), Gemini 3.
Say them aloud but note they'll be stale in months — reinforces the thesis.
-->

---

# Open-Weights Models

Models you can download and run on your own hardware

<v-clicks>

- Examples: **Gemma** (Google), **Qwen** (Alibaba), **Llama** (Meta)
- Tools like **Ollama** and **LM Studio** make running them a five-minute install
- Why an institution might care:
  - Data never leaves the machine
  - No per-use cost
  - Smaller models are genuinely useful for summarizing, drafting, classifying
- Trade-off: you manage it, and small local models are less capable than the frontier commercial ones

</v-clicks>

---

# Cost Literacy

<v-clicks>

**Subscriptions** (ChatGPT Plus, Claude Pro, M365 Copilot): flat monthly fee, usage limits, per-seat

**API pricing:** metered per million tokens, input and output priced separately

Why you should care even if you never touch an API:

- Explains vendor behavior: long documents and long conversations are *expensive*, so tools summarize, truncate, and limit
- At institutional scale, "everyone pastes the handbook into every chat" is a real cost line
- Free tiers exist because your usage is worth something — know what you're trading

</v-clicks>

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:chat class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Working Conversationally with AI</span>

## It's a dialogue, not a search box

---

# Iteration, Not One-Shot

<v-clicks>

The single biggest usage mistake: treating it like Google — one query, take whatever comes back

The productive loop:

1. **Ask** — with context
2. **Refine** — "shorter," "more formal," "for an audience that hasn't seen the budget"
3. **Challenge** — "what's weakest about this?" "what did you assume?"
4. **Add context** — paste the policy, the previous email, the actual data

First drafts from AI are like first drafts from anyone: a starting point

</v-clicks>

---

# Generation, Not Just Summarization

Most people discover summarization first. The bigger win is often **generation**:

<v-clicks>

- Status reports and recommendations from bullet points
- Meeting agendas from a goal and a list of attendees
- First-draft emails — especially the awkward ones
- Rubrics, checklists, runbooks, documentation
- Excel formulas and explanations of formulas someone else wrote

**The pattern:** AI absorbs tedious, repetitive, and blank-page work.
You supply judgment, facts, and the final read-through.

</v-clicks>

---

# Prompting That Actually Helps

No magic words — just information the model can't guess:

<v-clicks>

- **Context:** who you are, who it's for, what happened before
  - *"I'm writing to a faculty member whose ticket has been open for three weeks"*
- **Examples:** paste one of yours — "match this tone and format"
- **Format:** "as a table," "one paragraph," "bullet points, no preamble"
- **Steps:** for anything with logic in it, "walk through this step by step"
- **Role:** "act as a patient help-desk tech explaining to a non-technical user"

</v-clicks>

<v-click>

> Rule of thumb: if a competent new hire couldn't do the task from your prompt,
> the model can't either.

</v-click>

---

# What to Delegate, What to Keep

| Delegate freely | Keep your hands on |
|-----------------|--------------------|
| First drafts | Final sends |
| Reformatting, restructuring | Anything with names, numbers, dates |
| Summarizing long material | Judgment calls and commitments |
| Boilerplate and templates | Facts you haven't verified |
| "What am I missing?" reviews | Sensitive or regulated data (later section) |

---
layout: center
---

# Lab 1: From Messy Notes to Useful Output

**`labs/lab1-messy-notes.md`** — 20 minutes

1. Take the provided raw meeting notes (or your own)
2. Produce a status email, an action-item list, and an agenda for the follow-up
3. Do **not** accept the first draft — refine at least twice
4. If you finish: run the same prompt in a second tool and compare

Two paths in the lab document: **Copilot** or **any free chat tool**

<!--
Circulate during the lab. The teachable moment is almost always someone
accepting a mediocre first draft — push them to iterate.
-->

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:plug class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Connected AI and Your Own Data</span>

## From "chat with a model" to "AI that can see your work"

---
layout: image-right
image: /images/library.jpg
---

# The Grounding Idea

<v-clicks>

- A bare model knows only its training data — nothing about Trinity
- **Grounding:** the tool retrieves *your* documents, email, or data and feeds the relevant parts into the context window alongside your question
- The model isn't "trained on your data" — it's *reading it right now*, per question
- This is why grounded answers can cite sources — and why they're only as good as what was retrieved

</v-clicks>

---

# Microsoft Copilot at Trinity

Copilot's real advantage here: it sits **inside the institution's boundary**

<v-clicks>

- Grounded in your Trinity mailbox, calendar, OneDrive, SharePoint, Teams
- Honors existing M365 permissions — it can only see what *you* can see
- Microsoft's enterprise commitment: institutional prompts and data are not used to train the underlying models
- Practical consequence: **work data belongs in Copilot**, not in consumer chat tools — more on this in the privacy section

</v-clicks>

<!--
Be precise here: cite this as Microsoft's documented commitment, not your guarantee.
IT staff in the room may know their tenant's specific configuration better than we do.
-->

---

# Copilot Where You Already Work

| App | What it does well |
|-----|-------------------|
| **Outlook** | Summarize long threads; draft and tune replies |
| **Word** | First drafts from an outline; rewrite for tone or length |
| **Excel** | Suggest formulas; analyze tables; explain inherited spreadsheets |
| **Teams** | Meeting recaps with action items; "what did I miss?" |
| **Chat (M365 Copilot)** | Cross-cutting: "summarize everything about project X this week" |

<v-click>

Lab 2 walks through several of these with practice files — pick the apps you actually use.

</v-click>

---

# Connectors

Bridges between an AI tool and outside systems

<v-clicks>

- Modern chat tools can connect to: Google Drive, calendars, GitHub, Slack, databases, search…
- Once connected, the tool can *pull that data into the conversation on demand*
- Same grounding idea, generalized beyond one vendor's ecosystem
- The question to ask about any connector — and this is an IT instinct you already have:
  **what exactly can it read, and what can it do?**
- Under the hood, more and more of these bridges are built on one open standard: **MCP** — coming up in two slides

</v-clicks>

---

# Skills: Packaged Expertise

A **skill** is a reusable instruction package a tool loads when relevant

<v-clicks>

- Example: a document-review skill that knows your checklist, your formatting standards, your tone
- Written once (in plain language!), used by everyone on the team
- Turns "prompting well" from an individual craft into shared infrastructure
- Available today in Claude (and the pattern is spreading across vendors)

</v-clicks>

<v-click>

> Demo: a skill in Claude Desktop that formats any pasted notes
> into a standard status-report template.

</v-click>

---

# MCP: A Standard Way to Connect Tools

**Model Context Protocol** — an open standard for plugging data sources and tools into AI assistants

<v-clicks>

- Think "USB for AI tools": one connector spec, many devices
- An MCP server exposes a capability (search a catalog, query a database, file a ticket); any compatible AI tool can use it
- Growing ecosystem: file systems, GitHub, Google Drive, institutional systems
- Libraries and universities are beginning to experiment with exposing catalogs and repositories this way

</v-clicks>

<!--
Demo in Claude Desktop: one or two live MCP servers (e.g., filesystem + web search
or a public MCP service). Show the tool ASKING PERMISSION before acting — that
permission prompt is the governance story IT people care about.
-->

---

# Agents

<v-clicks>

- An **agent** is a model in a loop: it plans, takes an action, looks at the result, and decides what to do next — until the task is done
- Difference from chat: you describe an *outcome*, not each step
- Examples: "research these five vendors and build a comparison table," "find every file mentioning the old domain and list them"
- The permission model matters: good agent tools ask before acting, and you should know what an agent is *allowed* to touch

</v-clicks>

<v-click>

> **Two words you'll keep hearing:** the **harness** is the software wrapped around the model — the loop, the tools, the permission checks. A **surface** is where a harness meets you: web chat, desktop app, terminal, or inside Outlook and Word.

</v-click>

---

# Coding Agents (Yes, for You Too)

**Claude Code** (Anthropic) and **Codex** (OpenAI, now built into ChatGPT) are agents that work with files and run commands — same models you've been using, in a different **harness** with a different **surface**

<v-clicks>

- "Coding" undersells it — they're general *do-things-on-a-computer* agents:
  - Rename and reorganize 300 files consistently
  - Turn a folder of CSV exports into one clean spreadsheet with a summary
  - Draft a script to automate a task you do weekly — then explain every line
- For IT staff specifically: this is the fastest on-ramp to automation you've ever had

</v-clicks>

<!--
Demo: Claude Code doing a NON-code task live — e.g., point it at a folder of
messy files and have it organize + summarize them. Narrate the permission prompts.
-->

---
layout: center
---

# Live Example: The Student-Aid Scenario

**Entirely invented data** — `labs/data/student-aid-scenario.csv`

Watch the pieces combine:

1. Load a realistic (fake) spreadsheet of aid applications
2. Ask for patterns, outliers, and a summary for a committee
3. Challenge the analysis: "what would make this misleading?"
4. Produce a one-page brief — then verify a few numbers by hand

<v-click>

> The workflow is the lesson: ground it in data, converse, challenge, verify.

</v-click>

---
layout: center
---

# Lab 2: Copilot Where You Already Work

**`labs/lab2-copilot-m365.md`** — 15 minutes

Pick **two** of the four exercises:

- **Outlook:** summarize + draft a reply to the provided thread
- **Word:** turn the provided outline into a one-page draft, then rewrite its tone
- **Excel:** analyze the provided table; get a formula written *and explained*
- **Copilot Chat:** ask a grounded question about your own recent work week

Everyone has a Copilot license — but each exercise also has a free-tool path,
worth trying afterward to see what transfers.

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:camera class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Multimodal AI</span>

## Beyond text in, text out

---
layout: image-right
image: /images/vision.jpg
---

# Image Generation and Editing

<v-clicks>

- Every major tool now generates and edits images from descriptions
- Campus uses: event graphics, documentation, quick mockups
- Editing often beats generation: "remove the background," "make this a diagram"
- Limits: text inside images, brand consistency, factual precision
- Check licensing/policy before official use

</v-clicks>

---

# Vision: Models That Read

Attach an image; the model reads and reasons about it

<v-clicks>

- Screenshots of error messages → diagnosis (an IT classic)
- Photos of whiteboards → clean typed notes
- Scanned forms and handwritten documents → structured data
- Slides and charts → summaries and critiques
- This works *today* and is one of the most underused features in every tool

</v-clicks>

---

# Voice

<v-clicks>

- **Dictation as workflow** — the Wispr Flow demo from this morning: speak anywhere you would have typed
- **Transcription:** meeting recordings → searchable text, minutes, action items
  (Teams does this natively with Copilot)
- **Voice conversations** with chat tools: useful hands-free, and a genuinely different way to think out loud
- Accessibility angle: these tools are transformative for some users — worth deliberate attention in IT planning

</v-clicks>

---

# Video

The fast-moving frontier

<v-clicks>

- Generation from text prompts: short clips, increasingly coherent
- Practical today: AI-assisted *editing* — transcripts, cuts, captions, dubbing
- Coming fast; evaluate it with the same method as everything else:
  give it a task you understand, find the failure boundary

</v-clicks>

---
layout: center
---

# Lab 3: What Can It See?

**`labs/lab3-vision.md`** — 10 minutes

1. Screenshot something real from your work: an error dialog, a dense settings screen, a chart
2. Attach it and ask for an explanation, a fix, or a summary
3. Push further: "turn this into step-by-step instructions for a student worker"
4. Note where it succeeds — and where it misreads

Works in Copilot, ChatGPT, Claude, and Gemini alike

---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:warning-alt class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Using AI Without Fooling Yourself</span>

## The section that keeps you employed

---

# Confident and Wrong

<v-clicks>

Hallucinations cluster in predictable places:

- **Citations and sources** — plausible-looking papers and URLs that don't exist
- **Specifics:** names, dates, version numbers, statistics, quotes
- **Niche topics** — thin training data, maximum improvisation
- **Things that changed recently** — the training cutoff problem
- **Leading questions** — models are agreeable; ask "why is X true?" and you'll get reasons X is true

The tell isn't in the text. Fluent and confident is the *default style* — for correct and incorrect answers alike.

</v-clicks>

---
layout: center
---

# Lab 4: Catch the Hallucination

**`labs/lab4-catch-the-hallucination.md`** — 15 minutes

1. Use the provided prompts designed to invite confident nonsense
   (obscure specifics, fake premises, leading questions)
2. Get an answer that *looks* authoritative
3. Verify it: second tool, web search, primary source
4. Report the best catch to the room

<v-click>

> Goal: everyone leaves having personally caught a tool inventing something.
> That experience is worth more than any warning on a slide.

</v-click>

---

# Building Verification Into the Workflow

<v-clicks>

- **Second-tool cross-check:** paste the output into a different vendor's tool — "verify this; what's wrong or unsupported?"
- **Ask for sources, then open them** — the link existing is step one; the link *saying what was claimed* is step two
- **Spot-check the numbers:** in any table or analysis, hand-verify two or three values
- **Scale scrutiny to stakes:** a brainstorm needs none; anything you'll sign, send, or publish needs all of it
- The stakes decide the workflow — never the other way around

</v-clicks>

---

# Privacy and Confidentiality

<v-clicks>

**The one-question test: "Would I email this to an outside vendor?"**

- **FERPA-covered student records, donor data, personnel matters, health information: never into consumer AI tools.** Free-tier tools may use conversations to improve their models
- Institutional tools (Trinity's M365 Copilot) exist precisely to provide a governed boundary — that's what you're paying for
- De-identification is harder than it looks; "I removed the names" usually isn't enough
- When in doubt: ask before pasting. The retraction workflow doesn't exist

</v-clicks>

<!--
IT staff will field these questions from campus, so frame this section as
"what you'll tell other people" as much as "what you should do."
-->

---

# Equity

<v-clicks>

- Paid tiers are meaningfully better than free tiers — and that gap maps onto who can afford $20/month
- Among **staff**: uneven license access creates uneven productivity, quietly
- Among **students**: assume any AI-permitted assignment is done with wildly unequal tooling
- Institutional licensing (like M365 Copilot) is partly an *equity* decision, not just a productivity one

</v-clicks>

---

# For Instructors in the Room

<v-clicks>

- **AI detection is no longer uniformly bad** — in independent University of Chicago testing, **Pangram** showed essentially zero false positives with ≥99.8% detection, a different class from first-generation tools
- **But detection alone doesn't settle it**: "humanizer" paraphrasing tools exist to evade detectors, hybrid human-plus-AI work confuses the labels, and a false accusation — however rare — carries real cost
- Still more durable than detection: assessment design — process artifacts, drafts, oral components, in-class work
- Many instructors now write explicit AI-use policies per assignment: *forbidden / permitted with citation / expected*
- These are evolving problems, not solved ones — distrust anyone selling certainty

</v-clicks>

<v-click>

> **Demo (if time):** generate a paragraph *designed* to evade detection — then watch Pangram catch it anyway. And then talk about humanizers…

</v-click>

<!--
Pangram evidence: UChicago Booth study (1,992 human + 1,992 AI texts) — only
detector meeting a 0.5% false-positive policy cap without losing detection power.
Caveats are real too: Pangram's own humanizer report shows an arms race, and
hybrid AI-edited text gets flagged wholesale. Verify current state before each
delivery — this moves fast.
-->



---
layout: center
class: text-center
---

<div class="text-6xl mb-4"><carbon:checkmark-outline class="text-amber-500 inline-block" /></div>

# <span class="bg-gradient-to-r from-blue-900 to-sky-500 bg-clip-text text-transparent">Wrap-Up</span>

---

# Continuing the Conversation

- The **AI Lab's ongoing sessions** at the Elting Innovation and Entrepreneurship Center
- Everything from today lives in the GitHub repo — slides, all labs (including ones we skipped), and the sample data
- The tools will be different in six months. Your evaluation method won't be.

<br>

Repo: **[github.com/kousen/practical-ai-literacy](https://github.com/kousen/practical-ai-literacy)**

---
layout: center
class: text-center
---

# Thank You

Ken Kousen
ken.kousen@kousenit.com

*Ask, refine, challenge, verify.*
