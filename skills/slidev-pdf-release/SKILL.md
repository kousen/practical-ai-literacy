---
name: slidev-pdf-release
description: Add a GitHub Action to a Slidev training-course repo that builds a PDF of the slides on every push to main and publishes it to a rolling "latest" GitHub release. Use when Ken asks to "set up the PDF release action", "add slide PDF publishing", or replicate the Spring AI slides workflow in another repo.
---

# Slidev PDF Release Workflow

Sets up CI so every push to `main` that touches `slides.md` rebuilds the deck
as a PDF and attaches it to a rolling `slides-latest` GitHub release. The
download URL is then permanent:
`https://github.com/<owner>/<repo>/releases/latest/download/<name>.pdf`

Reference implementations: `Spring_AI_Training_Course` and
`practical-ai-literacy`.

## If the repo already has the workflow

Re-running this skill is an update pass, not a no-op. When
`.github/workflows/build-slides-pdf.yml` already exists:

0. Check the current branch first. Ken's course repos often sit on a
   per-delivery branch (`codex_jul2026`, `junie_jun2026`, `solutions`)
   while the workflow triggers only on `main`. A push to a delivery
   branch won't fire the workflow. If the target files are identical on
   `main`, do the work on `main` and restore the original checkout;
   otherwise commit where you are and flag the merge/cherry-pick as
   Ken's decision.
1. Read it and diff against the template below. Report the differences
   before changing anything.
2. Update stale pieces in place: action versions (`checkout`, `setup-node`,
   `action-gh-release`), Node version, missing `workflow_dispatch`,
   missing PDF-verification step, missing `concurrency` block.
3. Preserve deliberate local customizations (different trigger paths, PDF
   name, release tag) — reconcile, don't overwrite.
4. Still run the audit-overrides check at the bottom of this file; older
   setups predate it.
5. If everything already matches, say so and change nothing.

## Prerequisites (check before writing anything)

1. Repo is a Slidev project with `slides.md` at the root and a `package.json`
   with `@slidev/cli` in devDependencies.
2. `playwright-chromium` is in devDependencies (Slidev's export needs it).
   If missing: `npm install -D playwright-chromium`.
3. A `package-lock.json` exists (the workflow uses `npm ci`).
4. Pick the PDF name from the repo name, kebab-case: `<repo-name>-slides.pdf`.

## Steps

### 1. Export script in package.json

```json
"export": "slidev export --output <repo-name>-slides.pdf"
```

If `slides.md` is not the default entry file, name it explicitly:
`slidev export slides.md --output ...`.

### 2. Gitignore the local artifact

Append `<repo-name>-slides.pdf` to `.gitignore` — CI builds it fresh; it
should never be committed.

### 3. The workflow file

Write `.github/workflows/build-slides-pdf.yml`, replacing
`<repo-name>-slides.pdf` (3 places):

```yaml
name: Build & publish slides PDF

on:
  push:
    branches: [main]
    paths:
      - 'slides.md'
      - 'public/**'
      - 'package.json'
      - 'package-lock.json'
      - '.github/workflows/build-slides-pdf.yml'
  workflow_dispatch:

concurrency:
  group: slides-pdf
  cancel-in-progress: true

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7

      - uses: actions/setup-node@v6
        with:
          node-version: 24
          cache: npm

      - run: npm ci

      - name: Install Chromium for Playwright
        run: npx playwright install --with-deps chromium

      - name: Export slides to PDF
        run: npm run export

      - name: Verify PDF was produced
        # Fail loudly: action-gh-release only warns on a missing file, so without
        # this a renamed/missing export would publish a release with no asset.
        run: |
          test -s <repo-name>-slides.pdf \
            || { echo "::error::<repo-name>-slides.pdf is missing or empty — export failed or the output name changed"; exit 1; }

      - name: Publish rolling "latest" release
        uses: softprops/action-gh-release@v3
        with:
          tag_name: slides-latest
          name: Latest slides PDF
          body: |
            Auto-built from `slides.md` at commit ${{ github.sha }}.

            Download: [`<repo-name>-slides.pdf`](https://github.com/${{ github.repository }}/releases/latest/download/<repo-name>-slides.pdf)
          files: <repo-name>-slides.pdf
          make_latest: true
```

If the repo keeps images somewhere other than `public/` (e.g. `images/`),
adjust the `paths:` trigger list to match.

### 4. Verify locally before committing

Run `npm run export` and confirm the named PDF appears and is non-empty
(expect one to a few MB), then delete it. This is the exact command CI runs,
so a local pass means the action will work.

### 5. Hand off

Show Ken the changed files; let him commit and push (or commit if he asks).
After the first push to `main`, confirm the run at the repo's Actions tab and
the `slides-latest` release.

## Notes

- The release is a single rolling tag (`slides-latest`), overwritten each
  build — no version clutter, and `releases/latest/download/...` always
  serves the current deck.
- Repos with GitHub-hosted images or private assets: the PDF bakes them in,
  so the release makes them public if the repo is public. Flag anything
  sensitive before setting this up.

## Dependabot noise from the Slidev chain

Slidev repos routinely show anywhere from a handful to ~75 audit findings.
Don't run `npm audit fix --force` (it downgrades Slidev). A July 2026 sweep
of seven of Ken's course repos found three distinct root-cause patterns —
diagnose which one you have before reaching for a fix:

1. **Stale lockfile (most common — fixed 4 of 7 repos outright).** The
   declared semver ranges already permit patched versions; the lockfile
   just predates them. Fix: regenerate (`rm -rf node_modules
   package-lock.json && npm install`, or the pnpm equivalent). Do this
   FIRST — in several repos it alone went to 0 with no overrides.
2. **Old nested pins surviving regeneration.** The two known offenders:
   `slidev-component-progress` pinning ancient `@slidev/client@0.48.x`
   (nests old vite/unocss/unhead/mermaid), and `monaco-editor` pinning a
   vulnerable `dompurify`. Diagnose with `npm ls @slidev/client dompurify`,
   then override only what the repo actually has:

   ```json
   "overrides": {
     "slidev-component-progress": {
       "@slidev/client": "$@slidev/cli"
     },
     "dompurify": "^3.4.12"
   }
   ```
3. **The repo itself pins an ancient `@slidev/cli` (e.g. ^0.47).** No
   override can fix that — the old chain hangs off the direct dependency.
   The remedy is a major Slidev upgrade, which is its own task (and may
   involve removing Node-version pinning workarounds). Report it; don't
   attempt it inside a maintenance pass.

After any fix, verify `slidev build` + the export still pass. The
Dependabot banner on push lags; it rescans after the new lockfile lands.
Also note Dependabot counts the whole repo (lab exercise manifests in other
languages included) while `npm audit` sees only package.json — big gaps
between the two numbers are usually that.

## pnpm repos (claude-code-training, LangChain4j course)

- pnpm 11 ignores the `pnpm` field in package.json — overrides and build
  approvals live in `pnpm-workspace.yaml` now.
- The `$@slidev/cli` reference syntax prints a deprecation warning under
  pnpm; use a catalog entry instead (warnings matter in repos Ken runs
  live in front of students).
- pnpm 11 blocks dependency build scripts until approved and appends a
  placeholder scaffold to `pnpm-workspace.yaml` on every install until you
  answer. Set `allowBuilds` explicitly for `esbuild` and
  `playwright-chromium` to stop the churn.
- Workflow equivalents: `pnpm/action-setup@v6` with pnpm 11, and add
  `pnpm-workspace.yaml` to the trigger paths since it affects resolution.

## Multi-branch publishing caveat

If the workflow triggers on more than one branch (e.g. `main` and
`solutions`) and the branches carry different slide content, both publish
to the same rolling `slides-latest` tag — last push silently wins the
permanent download link. Flag it: either one trigger branch, or distinct
tags/PDF names per branch.
