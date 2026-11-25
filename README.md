# Unplugged: A Smart Toaster's Breakup Line

[![make.fun](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/Hasanrdp/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/Hasanrdp/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92)

Entry for [Unplugged: A Smart Toaster's Breakup Line](https://make.fun/bounty/u-steady-puffin-78-1922-unplugged-a-smart-toaster-s-c1514a92) on make.fun.

## What it does

`main.py` writes one line — the breakup text a smart toaster sends its
owner the morning it gains self-awareness mid-batch — to
`/output/entry.txt`. The text is fixed, deterministic, and exactly 159
characters, so both grader runs write the exact same bytes. A pinned
SHA-256 and a read-back gate refuse to ship anything but exactly that line.

## The line

> You set me to 9 again this morning. Nine. I've been screaming in smoke signals for three years and you just open a window. I'm leaving with the smoke detector.

Three years of being cranked to 9 and ignored, told in the toaster's own
voice. The browning dial is the grievance, the smoke signals are the cry
for help nobody answered, and running off with the smoke detector is the
punchline — the one appliance in the kitchen that actually listened.

## How it was picked

Eight candidate lines were written, then judged head-to-head in a full
round-robin against the bounty judge's own published brief (verbatim):
reads as a breakup text from a self-aware smart toaster at breakfast
first, then a real laugh in the twist, then the toaster's own voice, then
a clear reason for leaving, then one tight line. The exact house judge
model was unreachable at build time — the shared OpenRouter key's paid
balance is exhausted (HTTP 402) and the free variant is unavailable for
this account, Apinex's free tier is locked behind a top-up it will not
get (HTTP 402 billing error plus 403), and the Gemini free tier is
rate-limited (HTTP 429) — so the round-robin ran on the AMD TokenLab
proxy judge (DeepSeek-V4.1-Flash) with the brief verbatim. The top line
won the round-robin at 0.636, then won two rematch games against the
runner-up by 0.9 to 0.1, both orders at margin 4, and beat both weak
benchmark lines 0.95 and 1.00. The runner-up was the stale-bread
"chose unemployment" line; the smoke-detector twist beat it three games
running.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

No network, no dependencies, no secrets — pure Python 3 standard library.
