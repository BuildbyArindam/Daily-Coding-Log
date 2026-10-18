"""
Problem   : Signal Corridor Review
Platform  : Unstop
Link      : https://unstop.com/code/practice/663526
Difficulty: Medium
Topics    : Array, Sliding Window, Monotonic Deque, Hashing
Date      : 2026-10-18

Approach:
    Compute the maximum of every window of size k using a monotonic
    decreasing deque of indices. For each index i:
      1. Pop from the front if the index has left the window (<= i - k).
      2. Pop from the back while the value there is smaller than arr[i],
         since those elements can never be a window maximum again.
      3. Push i; the front of the deque is the current window maximum.
    Then count how often each window maximum occurs with a Counter and
    pick the "dominant" value: highest frequency, ties broken by the
    smaller value.

Complexity:
    Time  : O(n) for the sliding window (each index is pushed and popped
            at most once) + O(m) for counting and selecting the dominant
            value, where m = n - k + 1. Overall O(n).
    Space : O(k) for the deque + O(m) for the result list and Counter.
"""


# --------------------------------------------------- Solution ------------------------------------------------------------


from collections import deque, Counter
import sys

data = list(map(int, sys.stdin.read().split()))
n, k = data[0], data[1]
arr = data[2:2 + n]
dq = deque()
max_values = []

for i in range(n):
    while dq and dq[0] <= i - k:
        dq.popleft()
    while dq and arr[dq[-1]] < arr[i]:
        dq.pop()
    dq.append(i)
    if i >= k - 1:
        max_values.append(arr[dq[0]])
freq = Counter(max_values)
dominant = min(freq, key=lambda x: (-freq[x], x))

print(*max_values)
print(dominant, freq[dominant])
