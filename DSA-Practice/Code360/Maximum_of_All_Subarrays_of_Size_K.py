"""
Problem: Maximum of All Subarrays of Size K
Platform: Code360
Link: https://www.naukri.com/code360/problems/maximum-of-all-subarrays-of-size-k_1071161
Difficulty: Easy
Topics: Sliding Window, Monotonic Deque

Approach:
Maintain a monotonically decreasing deque of indices over the current
window of size k. Before processing index i, drop the front index if
it has fallen out of the window (dq[0] <= i - k). Then pop indices
from the back whose values are <= arr[i], since they can never be the
max while arr[i] is in the window. Push i. Once the window reaches
size k (i >= k-1), the front of the deque holds the index of the
window's maximum.

Time complexity: O(n) — each index is pushed and popped at most once.
Space complexity: O(k) — deque holds at most k indices.
"""


# ------------------------- Solution ---------------------------------


from collections import deque
from typing import List

def maximumInAllSubarraysOfSizeK(arr: List[int], n: int, k: int) -> List[int]:
    dq = deque() 
    result = []
    for i in range(n):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result
