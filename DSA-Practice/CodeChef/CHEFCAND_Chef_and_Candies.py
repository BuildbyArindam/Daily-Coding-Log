"""
Problem   : Chef and Candies
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFCAND
Date      : 2026-09-11
Difficulty: 570 (Easy)
Topics    : Math, Greedy, Ad-hoc

Approach:
Chef needs N candies and already has X. If X >= N, no more packets
are needed. Otherwise, find the shortfall (N - X) and since each
packet holds 4 candies, compute the minimum packets via ceiling
division: ceil((N - X) / 4), done as (remaining + 3) // 4 to avoid
floating point.

Time complexity : O(T) — O(1) per test case
Space complexity: O(1)
"""


# ------------------------- Solution ---------------------------------


T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    if X >= N:
        print(0)
    else:
        remaining = N - X
        packets = (remaining + 3) // 4
        print(packets)
