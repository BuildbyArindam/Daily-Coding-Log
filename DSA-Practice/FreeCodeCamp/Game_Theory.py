"""
Problem: Game Theory
Platform: FreeCodeCamp — Daily Coding Challenge (07-23)
Link: https://www.freecodecamp.org/learn/daily-coding-challenge/07-23
Date Solved: 2026-09-04

Approach:
    Simulate an Iterated Prisoner's Dilemma-style scoring game between two
    players (p1, p2), where each element is a move ('C' = Cooperate,
    'D' = Defect). Walk both move sequences in lockstep with zip() and
    apply the standard payoff matrix:
        C,C -> 3 / 3   (mutual cooperation)
        D,D -> 1 / 1   (mutual defection)
        D,C -> 5 / 0   (defector exploits cooperator)
        C,D -> 0 / 5   (cooperator gets exploited)
    Accumulate each player's score and return as [score1, score2].

Time Complexity:  O(n) — single pass over the move sequences (n = len(p1))
Space Complexity: O(1) — only two running score accumulators
"""


# -------------------------- Solution -----------------------------


def play_game(p1, p2):
    score1 = 0
    score2 = 0
    for a, b in zip(p1, p2):
        if a == "C" and b == "C":
            score1 += 3
            score2 += 3
        elif a == "D" and b == "D":
            score1 += 1
            score2 += 1
        elif a == "D" and b == "C":
            score1 += 5
            score2 += 0
        else: 
            score1 += 0
            score2 += 5
    return [score1, score2]
