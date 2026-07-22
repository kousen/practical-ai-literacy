"""Check plain text against the Pangram AI-detection API.

Trimmed from the AsciiDoc-aware version in the Claude Code: Up and Running
book repo — this one takes plain text, no markup stripping.

Usage:
    python scripts/pangram_check.py file.txt        # check a file
    echo "some text" | python scripts/pangram_check.py   # check stdin

Requires PANGRAM_API_KEY in the environment.
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://text.api.pangram.com/v3"


def call_pangram(text: str, api_key: str) -> dict:
    body = json.dumps({"text": text, "public_dashboard_link": True}).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=body,
        headers={"Content-Type": "application/json", "x-api-key": api_key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit(f"Pangram API error {e.code}: {e.read().decode('utf-8', 'replace')}")


def main() -> int:
    api_key = os.environ.get("PANGRAM_API_KEY")
    if not api_key:
        sys.exit("PANGRAM_API_KEY not set in environment")

    if len(sys.argv) > 1:
        text = open(sys.argv[1], encoding="utf-8").read()
    else:
        text = sys.stdin.read()
    if not text.strip():
        sys.exit("No text to check")

    r = call_pangram(text, api_key)
    print(
        f"Verdict: {r.get('prediction_short', '?')}\n"
        f"  AI:       {r.get('fraction_ai', 0):.1%}\n"
        f"  Assisted: {r.get('fraction_ai_assisted', 0):.1%}\n"
        f"  Human:    {r.get('fraction_human', 0):.1%}"
    )
    if r.get("dashboard_link"):
        print(f"Dashboard: {r['dashboard_link']}")

    # Local history: every check appends a line next to this script's repo,
    # so dashboard links are never lost (demo-assets/ is gitignored).
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "demo-assets")
    os.makedirs(log_dir, exist_ok=True)
    from datetime import datetime
    preview = " ".join(text.split())[:80]
    with open(os.path.join(log_dir, "pangram-log.txt"), "a", encoding="utf-8") as f:
        f.write(
            f"{datetime.now():%Y-%m-%d %H:%M}  {r.get('prediction_short', '?'):<12} "
            f"AI={r.get('fraction_ai', 0):.0%} Human={r.get('fraction_human', 0):.0%}  "
            f"{r.get('dashboard_link', '-')}  | {preview}\n"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
