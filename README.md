# Practical AI Literacy

A half-day, hands-on workshop for the Trinity College community — moving from
knowing the AI vocabulary to using these tools well in your actual work.

Two ideas run throughout:

1. The important question is no longer *which* tool to use but *how* to use it
2. Because the tools keep changing, the durable skill is learning to evaluate
   them yourself

## Contents

- `slides.md` — the full slide deck ([Slidev](https://sli.dev) format)
- `labs/` — hands-on labs, each with a Microsoft Copilot path and a
  free-tool path (ChatGPT, Claude, or Gemini free accounts)
- `labs/data/` — sample files for the labs. **All data is fictional**,
  including the student-aid scenario — no real students, tickets, or people
- `demo-script.md` — instructor notes for the live demos
- `skills/` — take-home agent skills shown in the workshop, including the
  Nano Banana `image-prompt` generator from the book-cover case study
- `Practical AI Literacy Outline.md` — the original course outline

## Labs

| Lab | Topic | Time |
|-----|-------|------|
| [Lab 1](labs/lab1-messy-notes.md) | From messy notes to useful output | 20 min |
| [Lab 2](labs/lab2-copilot-m365.md) | Copilot in Outlook, Word, Excel, and Chat | 15 min |
| [Lab 3](labs/lab3-vision.md) | Vision: what can it see? | 10 min |
| [Lab 4](labs/lab4-catch-the-hallucination.md) | Catch the hallucination | 15 min |
| [Lab 5](labs/lab5-data-analysis.md) (bonus) | The student-aid data scenario | 20 min |
| [Lab 6](labs/lab6-evaluate-a-tool.md) (homework) | Evaluate a tool yourself | 30 min |

## What you need

- A laptop and your Trinity Microsoft 365 account (for the Copilot paths)
- Optionally, a free account at [claude.ai](https://claude.ai),
  [chatgpt.com](https://chatgpt.com), or [gemini.google.com](https://gemini.google.com)
- No programming experience required

## Running the slides

Just want to read the deck? Grab the always-current PDF:
**[practical-ai-literacy-slides.pdf](https://github.com/kousen/practical-ai-literacy/releases/latest/download/practical-ai-literacy-slides.pdf)**

The first-year orientation talk (*AI Tools for Academic Success*, `slides-freshmen.md`) is built the same way:
**[ai-tools-for-academic-success.pdf](https://github.com/kousen/practical-ai-literacy/releases/latest/download/ai-tools-for-academic-success.pdf)**
(also as a [light-background PDF](https://github.com/kousen/practical-ai-literacy/releases/latest/download/ai-tools-for-academic-success-light.pdf) for bright rooms)
(rebuilt automatically on every slide change)

```bash
npm install
npm run dev      # live presentation at localhost:3030
npm run export   # PDF export
```

## About

Presented by [Ken Kousen](https://www.kousenit.com), Professor of Practice,
Computer Science, Trinity College (kenneth.kousen@trincoll.edu)

Questions afterward? The AI Lab holds ongoing sessions at the Elting
Innovation and Entrepreneurship Center.
