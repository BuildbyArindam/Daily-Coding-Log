"""
Problem   : Minimize Max Min Diff with Subarray Removal
Link      : https://www.geeksforgeeks.org/problems/minimize-the-difference/1
Platform  : GeeksforGeeks 
Difficulty: Medium
Date      : 2026-10-26

Approach  : Remove one contiguous subarray of length k so that the
            max - min of the remaining elements is minimized.
            The remaining elements are always a prefix plus a suffix.
            1. Precompute suffix max/min arrays (tail_hi, tail_lo).
            2. Slide the removal window left to right, keeping a running
               prefix max/min (head_hi, head_lo) of everything before it.
            3. For each window, spread = max(head_hi, tail_hi[end])
               - min(head_lo, tail_lo[end]); track the minimum.

Time      : O(n)
Space     : O(n) for the suffix arrays
"""


# ------------------------------------------------ Solution -----------------------------------------------------------


class Solution:
    def minDiff(self, k: int, arr: list[int]) -> int:
        # code here
        size = len(arr)
        POS, NEG = float('inf'), float('-inf')
        tail_hi = [NEG] * (size + 1)
        tail_lo = [POS] * (size + 1)
        for j in range(size - 1, -1, -1):
            v = arr[j]
            tail_hi[j] = v if v > tail_hi[j + 1] else tail_hi[j + 1]
            tail_lo[j] = v if v < tail_lo[j + 1] else tail_lo[j + 1]
        head_hi, head_lo = NEG, POS 
        answer = POS
        for start in range(size - k + 1):
            end = start + k
            top = max(head_hi, tail_hi[end])
            bottom = min(head_lo, tail_lo[end])
            spread = top - bottom
            if spread < answer:
                answer = spread
            if start < size:
                x = arr[start]
                head_hi = max(head_hi, x)
                head_lo = min(head_lo, x)
        return answer
