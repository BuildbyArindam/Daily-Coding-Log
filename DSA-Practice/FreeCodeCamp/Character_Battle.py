"""
Problem: Character Battle
Platform: FreeCodeCamp — Daily Coding Challenge
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/08-24
Date Solved: 2026-08-30
Difficulty: Easy
Topics: String Manipulation, Character Encoding, Conditional Logic, Simulation

Approach:
Compare army sizes first — an unequal size means the larger side backs off before
any fighting happens ("Opponent retreated" / "We retreated"). If sizes match, pair
up characters positionally and score each character: a-z -> 1-26, A-Z -> 27-52,
0-9 -> its digit value, anything else -> 0. Tally wins per position and compare
total wins to decide "We won" / "We lost" / "It was a tie".

Time Complexity: O(n) — one pass over the paired characters (n = army length)
Space Complexity: O(1) — only counters and a per-char score are kept
"""


# -------------------------- Solution -------------------------------


def battle(my_army, opposing_army):
    if len(my_army) > len(opposing_army):
        return "Opponent retreated"
    elif len(opposing_army) > len(my_army):
        return "We retreated"
    def strength(char):
        if 'a' <= char <= 'z':
            return ord(char) - ord('a') + 1
        elif 'A' <= char <= 'Z':
            return ord(char) - ord('A') + 27
        elif '0' <= char <= '9':
            return int(char)
        else:
            return 0
    my_wins = 0
    opponent_wins = 0
    for mine, opponent in zip(my_army, opposing_army):
        my_strength = strength(mine)
        opponent_strength = strength(opponent)
        if my_strength > opponent_strength:
            my_wins += 1
        elif opponent_strength > my_strength:
            opponent_wins += 1
    if my_wins > opponent_wins:
        return "We won"
    elif opponent_wins > my_wins:
        return "We lost"
    else:
        return "It was a tie"
