"""
Problem   : Chess Ratings
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/C_RATING
Difficulty: 651 (Cakewalk)
Topics    : Basic Math, Ceiling Division, Conditional Statements, Implementation
Date      : 2026-09-19

Approach:
Chef's rating X needs to reach or exceed Y. Each win adds at most 8 points,
so the minimum number of wins is simply the ceiling of (Y - X) / 8.
If X == Y already, 0 wins are needed. Using integer ceiling division
((Y - X + 7) // 8) avoids floating point and handles the case cleanly.

Time complexity : O(1) per test case, O(T) overall
Space complexity: O(1)
"""


# --------------------------------------- Solution -----------------------------------------------


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    if X == Y:
        print(0)
    else:
        print((Y - X + 7) // 8)
