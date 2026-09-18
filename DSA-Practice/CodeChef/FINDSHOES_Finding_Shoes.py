"""
Problem   : Finding Shoes
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FINDSHOES
Difficulty: 646 (Cakewalk)
Topics    : Basic Math, Greedy, Implementation

Approach:
For each test case, N and M represent the required count and the available
count. Every unit needs a matching extra, and any shortfall in M beyond N
adds further requirement. Total extra shoes needed = N + max(0, N - M).

Time Complexity : O(1) per test case -> O(T) overall
Space Complexity: O(1)

Date Solved: 2026-09-18
"""


# ------------------------------ Solution ----------------------------------------


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    extra_shoes = N + max(0, N - M)
    print(extra_shoes)
