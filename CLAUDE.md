# Practical AI Literacy — project notes for Claude Code

Half-day AI literacy workshop for Trinity College IT staff. Slides are Slidev
(`slides.md`, run with `slidev`); labs live in `labs/` with fictional sample
data in `labs/data/`; instructor demo run sheet is `demo-script.md`.

## Voice demos (ElevenLabs)

- My cloned voice is **"Ken Kousen"**, voice id `AnMHhwDcnqFSc3sT34OR`.
- When I ask to say or read something "in my voice," use the text-to-speech
  skill with that voice id, model `eleven_multilingual_v2`.
- Save generated audio to `demo-assets/` (gitignored — never commit rendered
  voice samples to this public repo), then play it with `afplay`.

## Pangram AI-detection

- To check text for AI detection ("check this with Pangram"), run
  `python3 scripts/pangram_check.py` with the text as a file argument or on
  stdin. Requires `PANGRAM_API_KEY` (already in the environment).
- Print the verdict and the dashboard link.

## Conventions

- Verify slide changes with `slidev build` before committing.
- All sample data is invented; keep it that way — no real student, donor, or
  personnel information in this repo, ever.
