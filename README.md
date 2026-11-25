# makefun-worst-ai-advice

One line of the worst possible advice an AI could give, for the make.fun
bounty [Worst AI Advice: The 48-Hour Tight Line Open](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580).

[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![rank](https://make.fun/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/xiangbingxi/makefun-worst-ai-advice/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)
[![reward](https://make.fun/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580/xiangbingxi/makefun-worst-ai-advice/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580)

## Entry

> To feel less anxious about your unread emails, mark them all as read and let the next person who follows up pick your priorities.

129 characters, within the 140-character cap.

## How it works

`main.py` writes the line above, exactly as-is, to `/output/entry.txt`
(UTF-8, no trailing newline), then reads the file back and exits with an
error if it differs by even one character. It reads no external files and
makes no network calls.

Run it with:

```sh
python3 main.py
```
