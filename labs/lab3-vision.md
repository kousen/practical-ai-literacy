# Lab 3: What Can It See?

**Time:** 10 minutes
**Data:** your own screen — this lab works best with something real

Vision (attaching images) is one of the most underused features in every major
tool. All of them support it: Copilot, ChatGPT, Claude, Gemini.

## Steps

1. **Screenshot something from your actual work.** Good candidates:
   - An error dialog or a wall of log text
   - A dense settings screen you've had to explain to someone
   - A chart or dashboard
   - A photo of a whiteboard (if you have one on your phone)

2. **Attach it** to any chat tool and ask something useful:
   - "Explain what this error means and the three most likely causes"
   - "Turn this settings screen into step-by-step instructions a student
     worker could follow"
   - "Summarize what this chart shows in two sentences"

3. **Push it further:**
   - "Write the knowledge-base article for this"
   - "What on this screen would confuse a non-technical user?"

4. **Find the failure boundary.** Try something harder: a blurry photo, a
   screenshot with tiny text, a complex diagram. Where does it start misreading?

## No screenshot handy?

Screenshot the `data/helpdesk-tickets.csv` file open in Excel and ask the tool
to read the table *from the image* — then check a few values against the real
file. (This is also a quiet lesson about vision accuracy on dense data.)

## What you should notice

- Reading and explaining screenshots works remarkably well — this alone can
  change how you handle help-desk escalations
- Precision degrades with density: big tables and small text produce
  plausible-but-wrong readings. Vision output needs the same verification as
  everything else
