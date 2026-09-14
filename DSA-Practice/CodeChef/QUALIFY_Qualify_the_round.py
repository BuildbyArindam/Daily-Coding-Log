"""
Problem   : Qualify the round
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/QUALIFY
Date      : 2026-09-14
Difficulty: 594
Topics    : Basic Math, Implementation, Conditional Logic

Approach:
    For each test case, read the qualifying score X and the marks
    A (1-point questions correct) and B (2-point questions correct).
    Compute total score = A + 2*B. If score >= X, the player qualifies,
    else they don't. Straightforward simulation, no edge cases beyond
    reading input correctly.

Time Complexity : O(T)  -- constant work per test case
Space Complexity: O(1)  -- no extra data structures used
"""


# -------------------------- Solution ----------------------------


T = int(input())

for _ in range(T):
    X, A, B = map(int, input().split())
    score = A + 2 * B
    if score >= X:
        print("Qualify")
    else:
        print("NotQualify")
