"""
Problem   : Festival Stall Fairness
Platform  : Unstop
Link      : https://unstop.com/code/practice/657854
Difficulty: Medium
Date      : 2026-08-25
Topics    : Sliding Window, Two Pointers, Monotonic Deque

Approach:
Maintain a sliding window [left, right] using two monotonic deques —
one tracking indices of decreasing prices (max_dq, front = window max)
and one tracking indices of increasing prices (min_dq, front = window min).
For each right, push into both deques, then shrink from the left while
(window max - window min) > d, popping stale front indices from either
deque when they fall out of the window. Track the max valid window size.

Time complexity : O(n) — each index pushed/popped from each deque at most once
Space complexity: O(n) — two deques, worst case holding all n indices
"""


# ------------------------ Solution -----------------------------


from collections import deque
n, d = map(int, input().split())
prices = list(map(int, input().split()))
min_dq = deque()
max_dq = deque()
left = 0
ans = 0
for right in range(n):
    while max_dq and prices[max_dq[-1]] <= prices[right]:
        max_dq.pop()
    max_dq.append(right)
    while min_dq and prices[min_dq[-1]] >= prices[right]:
        min_dq.pop()
    min_dq.append(right)
    while prices[max_dq[0]] - prices[min_dq[0]] > d:
        if min_dq[0] == left:
            min_dq.popleft()
        if max_dq[0] == left:
            max_dq.popleft()
        left += 1
    ans = max(ans, right - left + 1)
print(ans)
