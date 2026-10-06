"""
Problem   : The Yard-Master's Ledger
Platform  : Unstop 
Link      : https://unstop.com/code/practice/661680
Date      : 2026-10-06
Difficulty: Hard
Topics    : Greedy, DSU, Sorting, Scheduling 

Approach  : Greedy + Disjoint Set Union (DSU).
            - Sort requests by priority (descending) so the most valuable ones are placed first.
            - For each request, assign it to the latest day <= its deadline that still has
              capacity. Choosing the latest slot leaves earlier days free for tighter deadlines.
            - DSU "find" jumps to the nearest earlier day with remaining capacity.
              When a day's capacity hits 0, link it to day-1. Day 0 is a sentinel meaning
              "no slot available".
            - Days with zero initial capacity are pre-linked.

Time      : O(T log T + (D + T) * α(D))
Space     : O(D + T)
"""


# ----------------------------------------- Solution ------------------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    D, T = map(int, input().split())
    capacity = list(map(int, input().split()))
    requests = []
    for i in range(T):
        deadline, priority = map(int, input().split())
        requests.append((-priority, i, deadline))
    requests.sort()
    parent = list(range(D + 1))
    def find(x):
        if x == 0:
            return 0
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    for day in range(1, D + 1):
        if capacity[day - 1] == 0:
            parent[day] = find(day - 1)
    answer = [0] * T
    total = 0
    for neg_priority, idx, deadline in requests:
        day = find(deadline)
        if day == 0:
            continue
        answer[idx] = day
        total += -neg_priority
        capacity[day - 1] -= 1
        if capacity[day - 1] == 0:
            parent[day] = find(day - 1)
    print(total)
    print(*answer)

if __name__ == "__main__":
    solve()
