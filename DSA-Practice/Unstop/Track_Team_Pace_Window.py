"""
Problem: Track Team Pace Window
Platform: Unstop
Link: https://unstop.com/code/practice/660829
Date: 2026-09-18
Difficulty: Medium
Topics: Array, Sliding Window, Two Pointers, Monotonic Queue, Deque

Approach:
Sliding window with two monotonic deques (min_q, max_q) to track the
min and max of the current window in O(1) amortized. Expand `right`
each iteration, maintaining monotonic deques; while the window's
max - min exceeds L, shrink from the left, popping deque fronts when
they equal the shrinking `left` pointer. Track the max valid window
length seen.

Time Complexity: O(n) — each index pushed/popped from each deque once
Space Complexity: O(n) — deques hold at most n indices total
"""


# ------------------------------- Solution -----------------------------------------------


from collections import deque

n, L = map(int, input().split())
a = list(map(int, input().split()))
min_q = deque()
max_q = deque()  
left = 0
answer = 0
for right in range(n):
    while min_q and a[min_q[-1]] >= a[right]:
        min_q.pop()
    min_q.append(right)
    while max_q and a[max_q[-1]] <= a[right]:
        max_q.pop()
    max_q.append(right)
    while a[max_q[0]] - a[min_q[0]] > L:
        if min_q[0] == left:
            min_q.popleft()
        if max_q[0] == left:
            max_q.popleft()
        left += 1
    answer = max(answer, right - left + 1)
print(answer)
