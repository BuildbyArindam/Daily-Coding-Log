"""
Problem: Candlelight
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-29
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Simulation, Math, Iterative Accumulation, Modular Division

Approach:
Simulate burning candles one round at a time. Each round, burn all
current candles, add their stubs to the leftover pile, then convert
as many leftovers as possible into new candles (leftovers // leftovers_needed),
keeping the remainder for the next round. Repeat until no candles
remain to burn. Track total candles burned across all rounds.

Time Complexity: O(log(candles)) — the candle count shrinks roughly
by a factor of leftovers_needed each round.
Space Complexity: O(1) — only a few running counters, no extra storage.
"""


# ----------------------- Solution --------------------------------


def burn_candles(candles, leftovers_needed):
    total_burned = 0
    leftovers = 0
    while candles > 0:
        total_burned += candles
        leftovers += candles
        candles = leftovers // leftovers_needed
        leftovers = leftovers % leftovers_needed
    return total_burned
