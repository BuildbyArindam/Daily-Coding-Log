"""
Problem   : Draw Match (GOALS)
Platform  : CodeChef (DSAMONDAY026)
Link      : https://www.codechef.com/DSAMONDAY026/problems/GOALS
Difficulty: Easy
Topics    : Implementation, Math
Date      : 2026-10-26

Approach:
    A match is liked only if it is a draw (home == away) AND at least one
    goal was scored (home + away > 0), which rules out 0-0.
    Read all input at once, check each pair, and print the verdicts joined
    in a single write.

Complexity:
    Time  : O(T), constant work per test case
    Space : O(T) for the input tokens and the output list
"""


# ------------------------------------------- Solution ----------------------------------------------------------


import sys

def likes_match(goals):
    home, away = goals
    return (home - away == 0) and (home + away > 0)

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    verdicts = []
    for i in range(cases):
        pair = (int(tokens[1 + 2 * i]), int(tokens[2 + 2 * i]))
        verdicts.append("YES" if likes_match(pair) else "NO")
    sys.stdout.write("\n".join(verdicts) + "\n")

main()
