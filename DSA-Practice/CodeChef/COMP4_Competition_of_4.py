"""
Problem   : Competition of 4 (COMP4)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/COMP4
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic Math, Exponentiation, Conditional Statements, Implementation

Approach:
    The prize pool halves for each rank after 1st place, starting from 1000.
    Rank X gets prize = 1000 * 2^(4-X).
    Simply read X and compute directly using the formula — no loops needed.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ------------------------ Solution --------------------------------


X = int(input())
prize = 1000 * (2 ** (4 - X))
print(prize)
