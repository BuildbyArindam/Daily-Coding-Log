"""
Problem   : Bon Appetit
Platform  : CodeChef (FGFS)
Link      : https://www.codechef.com/problems/FGFS
Difficulty: 1734
Date      : 2026-10-09
Topics    : Greedy, Sorting, Interval Scheduling

Approach:
    Each customer wants one specific dish p for the interval [s, f), and a
    dish can serve only one customer at a time. Dishes never interact, so
    the problem splits into independent classic activity-selection problems,
    one per dish. For each dish, sorting by finish time and greedily taking
    every customer whose start >= the last accepted finish maximizes the
    count. Sorting tuples as (p, f, s) groups customers by dish and orders
    them by finish time in one pass.

Complexity:
    Time : O(N log N) per test case (dominated by the sort)
    Space: O(N)
"""


# ------------------------------------------------- Solution ------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        customers = []
        for _ in range(N):
            s, f, p = map(int, input().split())
            customers.append((p, f, s))
        customers.sort()
        last_finish = {}
        count = 0
        for p, f, s in customers:
            if s >= last_finish.get(p, 0):
                count += 1
                last_finish[p] = f
        print(count)

if __name__ == "__main__":
    solve()
