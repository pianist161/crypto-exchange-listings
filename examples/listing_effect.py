"""Recompute the "listing effect" table from listings.csv with the standard library only.

    python examples/listing_effect.py [path/to/listings.csv]

Groups the events by exchange, kind and the point the price is counted from (never mix the
three starting points in one average) and prints, for every group of 10 or more events, the
median change after 5 minutes, 1 hour, 24 hours and 7 days, the median best price within the
first hour and the share of coins that were higher after 7 days.

The numbers match listing-effect.csv of the same export to a tenth of a percent (the changes in
listings.csv are rounded to two decimals).
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path
from statistics import median

path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "listings.csv"
COLS = ["change_5m_pct", "change_1h_pct", "change_24h_pct", "change_7d_pct", "peak_1h_pct"]

groups = defaultdict(list)
with open(path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["counted_from"]:  # empty: no market to measure the price on
            groups[(row["exchange"], row["kind"], row["counted_from"])].append(row)


def values(rows, col):
    return [float(r[col]) for r in rows if r[col] != ""]


def fmt(xs):
    return f"{median(xs):+7.1f}" if xs else "    n/a"


print(f"{'exchange':10} {'kind':8} {'counted from':17} {'n':>4} {'5 min':>7} {'1 h':>7} {'24 h':>7} {'7 d':>7} {'best 1h':>7} {'up 7d':>6}")
for (exchange, kind, start), rows in sorted(groups.items(), key=lambda kv: -len(kv[1])):
    if len(rows) < 10:
        continue
    d7 = values(rows, "change_7d_pct")
    up = f"{100 * sum(x > 0 for x in d7) / len(d7):5.0f}%" if d7 else "   n/a"
    print(f"{exchange:10} {kind:8} {start:17} {len(rows):4d} " + " ".join(fmt(values(rows, c)) for c in COLS) + f" {up}")
