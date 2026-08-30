"""
Problem: Second Best
Platform: FreeCodeCamp - Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-28
Date Solved: 2026-08-30
Difficulty: Easy
Topics: Arrays, Sorting, Greedy, Set/Deduplication

Approach:
    Dedupe the laptop prices and sort in descending order. The second-best
    (2nd highest distinct price) is preferred if it fits the budget; if it
    doesn't (or fewer than 2 distinct prices exist), fall back to scanning
    from the highest price down and return the first one within budget.
    Returns 0 if nothing fits.

Time Complexity:  O(n log n)  -- dominated by sort() on the deduped set
Space Complexity: O(n)        -- storage for the deduped/sorted list
"""


# ----------------------- Solution --------------------------------


def get_laptop_cost(laptops, budget):
    laptops = sorted(set(laptops), reverse=True)
    if len(laptops) == 0:
        return 0
    if len(laptops) >= 2 and laptops[1] <= budget:
        return laptops[1]
    for laptop in laptops:
        if laptop <= budget:
            return laptop
    return 0
