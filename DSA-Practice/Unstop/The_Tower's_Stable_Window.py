"""
Problem   : The Tower's Stable Window
Platform  : Unstop
Link      : https://unstop.com/code/practice/659448
Difficulty: Medium
Topics    : Array, Sliding Window, Two Pointers, Monotonic Queue, Hashing, Deque
Date      : 2026-09-09

Approach:
    Variable-size sliding window over the array to find the longest
    subarray such that:
        1. All elements in the window are distinct (tracked via a
           hashmap storing the last seen index of each value).
        2. max(window) - min(window) <= D (tracked via two monotonic
           deques — one decreasing for max, one increasing for min).

    For each right pointer:
        - Maintain max_q / min_q as monotonic deques of indices.
        - If a[right] was seen before inside the current window,
          move `left` past its previous occurrence to keep values
          distinct.
        - Evict stale indices (< left) from both deques.
        - While the window's max-min exceeds D, shrink from the left,
          popping stale deque fronts as needed.
        - Track the best (longest) window length and its 1-indexed
          start position.

Time Complexity : O(N) — each index is pushed/popped from each deque
                   and from `left`'s movement at most once (amortized).
Space Complexity: O(N) — deques + hashmap, each bounded by N.
"""


# ------------------------- Solution ----------------------------------


from collections import deque
N, D = map(int, input().split())
a = list(map(int, input().split()))
min_q = deque()
max_q = deque()
last_seen = {}
left = 0
best_len = 0
best_start = 1
for right in range(N):
    while max_q and a[max_q[-1]] <= a[right]:
        max_q.pop()
    max_q.append(right)
    while min_q and a[min_q[-1]] >= a[right]:
        min_q.pop()
    min_q.append(right)
    if a[right] in last_seen:
        left = max(left, last_seen[a[right]] + 1)
    last_seen[a[right]] = right
    while min_q and min_q[0] < left:
        min_q.popleft()
    while max_q and max_q[0] < left:
        max_q.popleft()
    while min_q and max_q and a[max_q[0]] - a[min_q[0]] > D:
        if min_q[0] == left:
            min_q.popleft()
        if max_q[0] == left:
            max_q.popleft()
        left += 1
    current_len = right - left + 1
    if current_len > best_len:
        best_len = current_len
        best_start = left + 1
print(best_len, best_start)
