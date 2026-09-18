"""
Problem   : Police and Thief
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/POLTHIEF
Date      : 2026-09-18
Difficulty: 639 (Cakewalk/Easy)
Topics    : Basic Math, Absolute Value, Implementation

Approach:
For each test case, the minimum number of moves for the thief to be caught
(or the distance to cover) is simply the absolute difference between the
police's position X and the thief's position Y, since they move toward
each other one step at a time along a line.

Time Complexity : O(T) — one O(1) computation per test case
Space Complexity: O(1) — no extra data structures used
"""


# ------------------------------ Solution ----------------------------------------


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    print(abs(X - Y))
