"""
Problem   : Candy Distribution
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CANDYDIST
Difficulty: 668 (Cakewalk)
Date      : 2026-09-19
Topics    : Basic Math, Parity, Conditional Statements, Implementation

Approach:
    N candies are to be split equally among M people (N // M each).
    Answer is "Yes" only if:
        1. N is exactly divisible by M (equal split is possible), AND
        2. The resulting share (N // M) is even (so it can be split
           evenly again into two halves, e.g. for two hands/days).
    Otherwise "No".

Complexity:
    Time  : O(1) per test case -> O(T) overall
    Space : O(1)
"""


# ----------------------------------- Solution ----------------------------------------------


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    if N % M == 0 and (N // M) % 2 == 0:
        print("Yes")
    else:
        print("No")
