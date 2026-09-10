"""
Problem: Kabir's Freight Yard Ledger
Link: https://unstop.com/code/practice/659450
Platform: Unstop | Difficulty: Medium
Topics: Array, Monotonic Stack, Hashing
Date Solved: 2026-09-10

Approach:
    For each wagon, find the distance to the nearest wagon to its right
    with a strictly greater weight (next greater element), using a
    monotonic decreasing stack traversed right-to-left. Sum these gaps
    per destination using a hash map to get the ledger totals.

Time Complexity:  O(N)  - each index pushed/popped from the stack once
Space Complexity: O(N)  - stack, gaps array, and destination hash map
"""


# ----------------------------- Solution ------------------------------------


import sys
input = sys.stdin.readline
N = int(input())
weights = [0] * N
dests = [0] * N
for i in range(N):
    weights[i], dests[i] = map(int, input().split())
stack = []
gaps = [0] * N
for i in range(N - 1, -1, -1):
    while stack and weights[stack[-1]] <= weights[i]:
        stack.pop()
    if stack:
        gaps[i] = stack[-1] - i
    else:
        gaps[i] = 0
    stack.append(i)
totals = {}
for i in range(N):
    dest = dests[i]
    if dest not in totals:
        totals[dest] = 0
    totals[dest] += gaps[i]
for dest, total in totals.items():
    print(dest, total)
