import os
import sys

ENTRY = "To feel less anxious about your unread emails, mark them all as read and let the next person who follows up pick your priorities."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    written = f.read()
if written != ENTRY:
    print("ERROR: entry.txt does not match ENTRY exactly", file=sys.stderr)
    sys.exit(1)
