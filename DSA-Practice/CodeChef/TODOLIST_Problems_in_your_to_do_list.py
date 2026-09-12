"""
Problem   : Problems in your to-do list
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TODOLIST
Date      : 2026-09-12
Difficulty: 580
Topics    : Arrays, Simple Counting / Simulation

Approach:
    For each test case, read N difficulty values and count how many are
    >= 1000 (i.e., "easy" problems by the problem's threshold). Simple
    single-pass counting, no extra data structures needed.

Time Complexity : O(T * N) — one pass over each test case's array
Space Complexity: O(N) — for storing the difficulty list per test case
"""


# ---------------------------- Solution ---------------------------------


T = int(input())
for _ in range(T):
    N = int(input())
    D = list(map(int, input().split()))
    count = 0
    for difficulty in D:
        if difficulty >= 1000:
            count += 1
    print(count)
