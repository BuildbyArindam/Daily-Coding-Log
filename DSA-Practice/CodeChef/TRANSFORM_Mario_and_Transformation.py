"""
Problem: Mario and Transformation
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRANSFORM
Date: 2026-09-19
Difficulty: 649
Topics: Basic Math, Modular Arithmetic, Conditional Statements

Approach:
Each number X, when reduced mod 3, falls into one of three buckets.
Classify directly using X % 3 — no transformation loop needed since the
result only depends on the residue class:
    X % 3 == 0 -> NORMAL
    X % 3 == 1 -> HUGE
    X % 3 == 2 -> SMALL

Time Complexity: O(1) per query, O(T) overall
Space Complexity: O(1)
"""


# ------------------------------------- Solution --------------------------------------------------


T = int(input())

for _ in range(T):
    X = int(input())

    if X % 3 == 0:
        print("NORMAL")
    elif X % 3 == 1:
        print("HUGE")
    else:
        print("SMALL")
