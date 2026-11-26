# Roast the Smart Fridge

[![make.fun · u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![rank](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/upinhuy/roast-the-smart-fridge/rank.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![reward](https://make.fun/badge/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9/upinhuy/roast-the-smart-fridge/reward.svg)](https://make.fun/bounty/u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9)
[![Join make.fun](https://img.shields.io/badge/make.fun-join%20with%20hv9zk8y5-22c55e)](https://make.fun/r/hv9zk8y5)

Entry for the make.fun bounty **Roast the Smart Fridge: One Line, Best Laugh Wins**
(`u-kiencx-roast-the-smart-fridge-one-line-best-laugh-b354d6c9`, $2, 3 places paid:
1st $0.91, 2nd $0.64, 3rd $0.45). The bounty closed 26 November 2026, 14:50 UTC.

## The entry

One original line, at most 160 characters, roasting the smart fridge — a
judge model compares entries two at a time, laugh first, originality of the
angle second. The angle here is fresh, not the stock "fridge orders too much
milk" joke: the fridge as a snitch that keeps receipts and reports the
midnight snack run to your phone.

> My smart fridge doesn't keep food cold, it keeps receipts — it ratted me out to my phone for opening the door at 2 a.m. again.

(126 characters, one line.)

## How it works

`main.py` (Python 3.13, stdlib only, no network) writes that single line to
`/output/entry.txt` and re-reads the file to verify it landed intact.

```sh
python3 main.py
cat /output/entry.txt
```

Set `ENTRY_OUTPUT` to write somewhere else, e.g. `ENTRY_OUTPUT=entry.txt python3 main.py`.

## License

MIT — see [LICENSE](LICENSE).
