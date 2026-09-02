"""
Problem   : Five Dice
Platform  : FreeCodeCamp — Daily Coding Challenge
Link      : https://www.freecodecamp.org/learn/daily-coding-challenge/07-11
Date      : 2026-09-02
Difficulty: Easy
Topics    : Hashing, Frequency Counting, Arrays, Simulation

Approach:
    Count occurrences of each die value with a dict, then classify the
    hand by the sorted multiset of frequencies (e.g. [5], [4,1], [3,2]).
    Straights are detected separately by checking if the sorted set of
    distinct values matches one of the four/five consecutive-run windows.
    Checks run in order from most to least specific (five of a kind ->
    no pair) so the first match wins.

Time Complexity : O(n) — n = len(dice) (fixed at 5, so effectively O(1))
Space Complexity: O(n) — for the counts dict, values, and frequencies lists
"""


# ----------------------- Solution -------------------------------


def five_dice(dice):
    counts = {}
    for die in dice:
        counts[die] = counts.get(die, 0) + 1
    values = sorted(counts.keys())
    frequencies = sorted(counts.values(), reverse=True)
    if frequencies == [5]:
        return "five of a kind"
    if frequencies == [4, 1]:
        return "four of a kind"
    if frequencies == [3, 2]:
        return "full house"
    if values == [1, 2, 3, 4, 5] or values == [2, 3, 4, 5, 6]:
        return "large straight"
    if any(all(x in values for x in straight)
           for straight in ([1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6])):
        return "small straight"
    if frequencies == [3, 1, 1]:
        return "three of a kind"
    if frequencies == [2, 2, 1]:
        return "two pair"
    if frequencies == [2, 1, 1, 1]:
        return "pair"
    return "no pair"
