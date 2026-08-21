"""
Problem   : Squid Game - Piggy Bank (SQUIDBANK)
Platform  : CodeChef (Starters 171, Division 4 - Problem A)
Link      : https://www.codechef.com/problems/SQUIDBANK
Date      : 2026-08-21
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
    N participants play, K survive till the end, so (N - K) are
    eliminated. Each eliminated participant adds a fixed ₹10,000
    to the prize pool. Answer = (N - K) * 10000.

Complexity:
    Time  : O(1)  -- constant arithmetic
    Space : O(1)  -- no extra data structures
"""


# ---------------------- Solution -------------------------


N, K = map(int, input().split())
eliminated = N - K
prize = eliminated * 10000
print(prize)
