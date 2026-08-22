"""
Problem   : N-dates with Lili
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/n-dates-with-lili_3624159
Date      : 2026-08-22
Difficulty: Medium
Topics    : Sliding Window, Monotonic Deque

Approach:
Treat the input as a circular/extended sequence of length (n + k - 1).
Maintain a monotonic decreasing deque of indices over the array so that
dq[0] always holds the index of the maximum element in the current
window of size k. Slide the window across all n valid starting
positions, popping out-of-window indices from the front and smaller
trailing elements from the back before pushing the new index. Sum the
window maximum (arr[dq[0]]) each time the window reaches size k.

Time complexity : O(n + k) — each index is pushed and popped from the
                  deque at most once.
Space complexity: O(k) — deque holds at most k indices at any point.
"""


# ---------------------- Solution --------------------------


from sys import *
from collections import *
from math import *
from typing import *

def maxTotalCoins(arr: List[int], n: int, k: int) -> int:
    dq = deque()
    total = 0
    for i in range(n + k - 1):
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        if i >= k - 1:
            total += arr[dq[0]]
    return total
