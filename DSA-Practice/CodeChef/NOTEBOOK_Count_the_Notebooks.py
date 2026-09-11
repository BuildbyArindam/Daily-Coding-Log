"""
Problem   : Count the Notebooks
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NOTEBOOK
Date      : 2026-09-11
Difficulty: Easy (~800)
Topics    : Math, Implementation

Approach:
For each test case, read N and print N * 10 directly — a constant-factor
multiplication with no iteration or extra structure needed.

Complexity:
Time  : O(1) per test case -> O(T) overall
Space : O(1)
"""


# --------------------------- Solution --------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    print(N * 10)
