"""
Problem   : Add Two Numbers
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FLOW001
Date      : 2026-09-05
Difficulty: Cakewalk
Topics    : Basic I/O, Loops

Approach:
Read T test cases; for each, read two integers A and B
and print their sum directly. No edge cases beyond
standard integer input parsing.

Complexity:
Time  : O(T) — O(1) work per test case
Space : O(1) — no extra data structures used
"""


# ------------------------ Solution ----------------------------


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(A + B)
