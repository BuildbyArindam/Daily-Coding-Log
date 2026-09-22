"""
Problem: Alice and Customer Satisfaction
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/alice-and-customer-satisfaction-b6dc3745/
Date: 2026-09-22
Difficulty: Medium
Topics: Binary Search, Algorithms

Approach:
    Each order has a deadline R and demand Z. Group orders by their
    deadline and accumulate total demand up to each deadline in
    increasing order of R. For every deadline, the minimum required
    processing rate is ceil(total_demand_so_far / R) — since R units
    of time are available by that deadline to clear all demand due
    by then. The answer is the maximum such required rate across all
    deadlines (the bottleneck rate that satisfies every deadline).

Time Complexity:  O(N log N)  — dominated by sorting the distinct deadlines
Space Complexity: O(N)        — for the demand dictionary
"""


# ---------------------------------------- Solution ---------------------------------------------


import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    demand = {}
    for _ in range(N):
        L, R, Z = map(int, input().split())
        demand[R] = demand.get(R, 0) + Z
    total_demand = 0
    answer = 0
    for R in sorted(demand):
        total_demand += demand[R]
        required_rate = (total_demand + R - 1) // R
        answer = max(answer, required_rate)
    print(answer)
