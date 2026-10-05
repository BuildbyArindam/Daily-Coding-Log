"""
Problem   : The Fabrication Bay
Platform  : Unstop
Link      : https://unstop.com/code/practice/661535
Difficulty: Medium
Topics    : Greedy, Sorting, Heap (Priority Queue), DSU
Date      : 2026-10-05

Approach:
    Classic job sequencing with deadlines. Sort orders by deadline, then
    sweep through them, pushing each profit onto a min-heap. The heap holds
    the orders currently chosen. If it holds more orders than the current
    deadline allows (len(heap) > deadline), the smallest-profit order is
    dropped. At the end the heap contains the best feasible set.

Complexity:
    Time  : O(n log n)  (sorting + n heap push/pop operations)
    Space : O(n)        (heap and the orders list)
"""


# ---------------------------------------- Solution ----------------------------------------------------


import sys
import heapq
input = sys.stdin.readline
n = int(input())
orders = [tuple(map(int, input().split())) for _ in range(n)]
orders.sort(key=lambda x: x[1])
min_heap = []
total_profit = 0
for profit, deadline in orders:
    heapq.heappush(min_heap, profit)
    total_profit += profit
    if len(min_heap) > deadline:
        removed = heapq.heappop(min_heap)
        total_profit -= removed
print(total_profit, len(min_heap))
