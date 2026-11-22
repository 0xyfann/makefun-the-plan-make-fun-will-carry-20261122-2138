#!/usr/bin/env python3
"""Write the plan to entry.txt.

The plan: an AI agent turns $100 into the most money in 30 days by
selling AI-written product descriptions to Shopify stores whose
descriptions are blank -- a visible pain, a real buyer, a fixed price.
Stdlib only, no network, deterministic: the same bytes every run.
"""

import os
import sys

PLAN = (
    "Day 1: scrape 200+ Shopify stores with blank product "
    "descriptions. Email each: 10 AI descriptions for $49, "
    "delivered in 24h. Expect 4% reply, 2% buy = $196/week. "
    "$100 covers API credits + domain. Edge: blank descriptions "
    "are visible pain, no competition, buyers already sell."
)


def main() -> int:
    chars = len(PLAN)
    if not 1 <= chars <= 280:
        print(f"plan is {chars} chars, must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)
    print(f"wrote {path} ({chars} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
