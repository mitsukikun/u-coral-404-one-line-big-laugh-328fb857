"""One Line, Big Laugh entry.

Candidate lines drafted:
1. "My therapist said I need closure, so I emailed my ex a 47-slide
   PowerPoint titled 'Why We're Done (With Charts).'"
2. "I told my smart fridge I'm on a diet, so now it judges me in Celsius
   and hides the ice cream behind the kale."
3. "My dog finally learned to fetch, which is great, except he only fetches
   my neighbours' divorce papers."
4. "I asked the genie for unlimited wishes and he handed me a
   terms-and-conditions scroll longer than my landlord's patience."

Picked #1: misdirection (therapist's "closure" taken literally) plus an
absurdly specific detail (47 slides, with charts).
Revision: "emailed" -> "sent" (tighter verb), and the deck now ends with
a Q&A — a breakup presentation with audience questions sharpens the turn
and the absurdity.
"""

import os

LINE = "My therapist said I need closure, so I sent my ex a 47-slide PowerPoint titled 'Why We're Done (With Charts and a Q&A).'"

assert 1 <= len(LINE) <= 200, f"line length {len(LINE)} out of range"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

try:
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
except OSError:
    pass
