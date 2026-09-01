"""
Problem   : Largest Subarray Sum Minimized (Split Array Largest Sum variant)
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/largest-subarray-sum-minimized_7461751
Date      : 2026-09-01
Difficulty: Hard
Topics    : Binary Search on Answer, Greedy, Arrays

Approach:
    Binary search on the "maximum subarray sum" value (search space:
    [max(a), sum(a)]). For a candidate max_sum, greedily check whether
    the array can be split into <= k subarrays such that no subarray's
    sum exceeds max_sum (can_split helper). Shrink the search space
    toward the smallest feasible max_sum.

Time Complexity : O(n * log(sum(a) - max(a)))   -- binary search * greedy check
Space Complexity: O(1)  extra (excluding input array)
"""


# -------------------------- Solution ----------------------------------


def largestSubarraySumMinimized(a: [int], k: int) -> int:
    low = max(a)
    high = sum(a)
    def can_split(max_sum):
        subarrays = 1
        current_sum = 0
        for num in a:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
                if subarrays > k:
                    return False
            else:
                current_sum += num
        return True
    while low < high:
        mid = (low + high) // 2
        if can_split(mid):
            high = mid
        else:
            low = mid + 1
    return low
