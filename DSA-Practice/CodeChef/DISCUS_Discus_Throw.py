"""
Problem: Discus Throw
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/DISCUS
Date Solved: 2026-09-18
Difficulty: 622
Topics: Basic Programming, Implementation, Conditional Statements / Comparisons, Math

Approach:
For each test case, read three distances (A, B, C) and print the maximum
of the three, since the winner is whoever threw the farthest.

Time Complexity: O(T) — O(1) work per test case
Space Complexity: O(1) — no extra storage beyond input variables
"""


# ------------------------------- Solution --------------------------------------------


T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())
    print(max(A, B, C))
