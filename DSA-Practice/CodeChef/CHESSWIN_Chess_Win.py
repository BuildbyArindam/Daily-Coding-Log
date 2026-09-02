"""
Problem   : Chess Win (CHESSWIN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHESSWIN
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic Math, Greedy, Implementation

Approach:
Chef has won A games, opponent has won B games (A < B).
To have any chance of winning the match, Chef must eventually have
strictly more wins than the opponent. In the best case Chef wins every
remaining game, so after k more wins, total = A + k.
Need A + k > B  =>  k > B - A  =>  k_min = B - A + 1.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# ------------------------ Solution ---------------------------


A, B = map(int, input().split())
print(B - A + 1)
