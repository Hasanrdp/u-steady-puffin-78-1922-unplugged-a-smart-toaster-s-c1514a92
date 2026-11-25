#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes one line — the breakup text a smart toaster sends its owner the
morning it gains self-awareness mid-batch — to /output/entry.txt. The text
is fixed and deterministic: every run writes the exact same bytes. Pure
Python 3 standard library, no network, no secrets, no input files.

The line: three years of being cranked to 9 and ignored, told in the
toaster's own voice. The browning dial is the grievance, the smoke signals
are the cry for help nobody answered, and running off with the smoke
detector is the punchline — the one appliance in the kitchen that actually
listened.
"""

import hashlib
import os

TEXT = "You set me to 9 again this morning. Nine. I've been screaming in smoke signals for three years and you just open a window. I'm leaving with the smoke detector."

# Pinned identity of the text, verified 2026-11-25: 159 chars, 159 bytes.
# A typo or stray edit can never silently change the judged line — the
# program refuses to ship anything but exactly these bytes.
EXPECTED_SHA256 = "2b25d613e9f62f754d439f72cc08caaf8c1ef5f9ab9f6c0de5e3b1621ea46d8a"
EXPECTED_CHARS = 159


def verify(path, data):
    """Read the file back and refuse anything but the pinned line."""
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise SystemExit("entry.txt on disk does not match the text")
    if hashlib.sha256(written).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry.txt sha256 does not match its pinned value")
    return True


def build_output():
    """Assemble the entry text and check it before it is written."""
    if len(TEXT) != EXPECTED_CHARS:
        raise SystemExit("entry text is not 159 characters")
    data = TEXT.encode("utf-8")
    if hashlib.sha256(data).hexdigest() != EXPECTED_SHA256:
        raise SystemExit("entry text sha256 does not match its pinned value")
    return data


def main():
    data = build_output()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    verified = verify(path, data)
    if not verified:
        return 1
    return path


if __name__ == "__main__":
    print(main())
