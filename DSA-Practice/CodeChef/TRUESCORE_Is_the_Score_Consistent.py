"""
Problem   : Is the Score Consistent
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRUESCORE
Date      : 2026-09-11
Difficulty: 572 (Beginner)
Topics    : Implementation, Conditional Logic

Approach:
For each test case, we're given a baseline pair (A, B) and a claimed/updated
pair (C, D). The score is "consistent" only if neither component decreased,
i.e. C >= A AND D >= B. A single failed condition makes it IMPOSSIBLE.

Time Complexity : O(T) — constant work per test case
Space Complexity: O(1) — no extra storage beyond input variables
"""


# ------------------------------- Solution -----------------------------------


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    if C >= A and D >= B:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
