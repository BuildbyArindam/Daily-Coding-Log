"""
Problem   : Nisha and the Coupling Yard
Platform  : Unstop
Link      : https://unstop.com/code/practice/657147
Difficulty: Medium
Topics    : Sliding Window, Monotonic Deque, Min-Max Queue
Date      : 2026-08-22

Approach:
Maintain two monotonic deques over a sliding window of size m —
one keeping indices in increasing order of weight (front = min),
one keeping indices in decreasing order of weight (front = max).
Slide the window across the array; at each valid window, the
front of each deque gives the current min/max in O(1), so the
window's max-min difference is tracked without rescanning.
Track the window start with the smallest difference seen.

Time Complexity : O(n)  — each index pushed/popped from each deque once
Space Complexity: O(m)  — deques hold at most m indices each
"""


# ------------------------ Solution ------------------------------


from collections import deque
import sys

n, m = map(int, input().split())
weights = list(map(int, input().split()))
min_q = deque()
max_q = deque()
best_diff = float('inf')
best_pos = 1
for i in range(n):
    while min_q and min_q[0] <= i - m:
        min_q.popleft()
    while max_q and max_q[0] <= i - m:
        max_q.popleft()
    while min_q and weights[min_q[-1]] >= weights[i]:
        min_q.pop()
    min_q.append(i)
    while max_q and weights[max_q[-1]] <= weights[i]:
        max_q.pop()
    max_q.append(i)
    if i >= m - 1:
        diff = weights[max_q[0]] - weights[min_q[0]]
        start_pos = i - m + 2
        if diff < best_diff:
            best_diff = diff
            best_pos = start_pos
print(best_diff, best_pos)
