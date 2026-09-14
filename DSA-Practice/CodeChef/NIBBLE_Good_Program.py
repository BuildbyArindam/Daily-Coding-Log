"""
Problem   : Good Program
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NIBBLE
Difficulty: 593
Topic     : Math, Divisibility (Basic Conditional Logic)
Date      : 2026-09-14

Approach:
    For each test case, read N and check divisibility by 4.
    If N % 4 == 0 -> "Good", else -> "Not Good".
    Straightforward O(1) arithmetic check per test case, no edge cases beyond
    standard integer input.

Complexity:
    Time  : O(T)   -- constant work per test case
    Space : O(1)   -- no extra data structures used
"""


# -------------------------- Solution --------------------------------------


T = int(input())

for _ in range(T):
    N = int(input())

    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
