"""
Problem: The River Watch Log
Platform: Unstop
Link: https://unstop.com/code/practice/661017
Date Solved: 2026-09-21
Difficulty: Medium
Topics: Array, Sliding Window, Monotonic Queue, Hashing, Frequency Map

Approach:
Single-pass sliding window using a monotonic deque (indices, decreasing by value)
to track the window maximum in O(1) amortized, paired with a Counter to track
the number of distinct values currently in the window. As the window slides,
expire the outgoing element from both the deque and the frequency map before
recording the (max, distinct_count) pair for each valid window.

Time Complexity: O(n) — each index is pushed/popped from the deque at most once
Space Complexity: O(W) — deque and frequency map bounded by window size
"""


# ------------------------------------- Solution -------------------------------------------


from collections import deque, Counter
n, W = map(int, input().split())
a = list(map(int, input().split()))
max_deque = deque()
freq = Counter()
result = []
for i in range(n):
    freq[a[i]] += 1
    while max_deque and a[max_deque[-1]] <= a[i]:
        max_deque.pop()
    max_deque.append(i)
    if max_deque[0] <= i - W:
        max_deque.popleft()
    if i >= W:
        old = a[i - W]
        freq[old] -= 1
        if freq[old] == 0:
            del freq[old]
    if i >= W - 1:
        maximum = a[max_deque[0]]
        distinct = len(freq)
        result.append(f"{maximum} {distinct}")
print("\n".join(result))
