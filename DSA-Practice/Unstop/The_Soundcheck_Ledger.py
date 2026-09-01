"""
Problem   : The Soundcheck Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/659172
Difficulty: Medium
Topics    : Array, Sliding Window, Two Pointers, Monotonic Queue, Deque
Date      : 2026-09-01

Approach:
    Sliding window with two monotonic deques (max_dq, min_dq) tracking
    the max and min elements of the current window in O(1) amortized.
    Expand `right` each step, maintaining decreasing/increasing order
    in the deques. While the window's max-min range exceeds L, shrink
    from `left`, popping stale indices off the front of either deque.
    Track the best (right - left + 1) seen.

Complexity:
    Time  : O(n) — each index pushed/popped from each deque at most once
    Space : O(n) — worst case both deques hold all indices (monotonic order)
"""


# ---------------------- Solution ------------------------------


from collections import deque
n, L = map(int, input().split())
a = list(map(int, input().split()))
max_dq = deque()
min_dq = deque()
left = 0
answer = 0
for right in range(n):
    while max_dq and a[max_dq[-1]] <= a[right]:
        max_dq.pop()
    max_dq.append(right)
    while min_dq and a[min_dq[-1]] >= a[right]:
        min_dq.pop()
    min_dq.append(right)
    while a[max_dq[0]] - a[min_dq[0]] > L:
        if max_dq[0] == left:
            max_dq.popleft()
        if min_dq[0] == left:
            min_dq.popleft()
        left += 1
    answer = max(answer, right - left + 1)
print(answer)
