"""
Problem   : Remaining Money (REMMON)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/REMMON
Date      : 2026-08-22
Topics    : Math, Implementation, Basic Programming
Difficulty: Easy (Basic tier)

Approach:
Given initial amount N, price per item A, and quantity B, total spent
is A * B. Remaining money is simply N - (A * B). No edge cases beyond
straightforward arithmetic — direct formula computation.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution ----------------------------


N, A, B = map(int, input().split())
spent = A * B
remaining = N - spent
print(remaining)
