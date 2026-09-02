"""
Problem: Dice Odds
Platform: FreeCodeCamp - Daily Coding Challenge (07-18)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-18
Date Solved: 2026-09-02
Difficulty: Easy-Medium 
Topics: Dynamic Programming, Combinatorics, Probability

Approach:
    Forward DP over dice sums. Start with {0: 1} way to reach sum 0 with
    0 dice. For each die added, expand every existing (sum, count) pair
    across the 6 possible face values (1-6), accumulating counts into a
    new dict. After processing all dice, the number of ways to hit
    `target` divided into total outcomes (6^dice) gives the odds,
    expressed as "1 in N".

Time Complexity:  O(dice^2)  -- ~5*dice reachable sums per die x 6 rolls
Space Complexity: O(dice)    -- dict holds ~5*dice+1 sum states at once
"""


# ----------------------- Solution -----------------------------


def get_odds(dice, target):
    ways = {0: 1}
    for _ in range(dice):
        new_ways = {}
        for current_sum, count in ways.items():
            for roll in range(1, 7):
                new_sum = current_sum + roll
                new_ways[new_sum] = new_ways.get(new_sum, 0) + count
        ways = new_ways
    favorable = ways[target]
    total = 6 ** dice
    odds = round(total / favorable)
    return f"1 in {odds}"
