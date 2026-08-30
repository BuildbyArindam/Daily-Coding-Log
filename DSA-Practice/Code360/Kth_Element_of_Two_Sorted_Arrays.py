"""
Problem   : K-th Element of Two Sorted Arrays
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/k-th-element-of-two-sorted-arrays_1164159
Difficulty: Hard
Date      : 2026-08-30
Topics    : Binary Search on Partitions, Arrays, Divide and Conquer

Approach:
    Binary search on the smaller array to find a valid partition point
    (cut1, cut2) such that cut1 + cut2 = k, and the max of the left
    halves is <= the min of the right halves across both arrays.
    Once found, the k-th element is max(l1, l2). Always binary search
    on the smaller array to keep the search space O(log(min(n, m))).

Time complexity : O(log(min(n, m)))
Space complexity: O(1)  (O(log n) recursion stack for the swap call)
"""


# ---------------------------- Solution ----------------------------------


def kthElement(arr1: [int], n: int, arr2: [int], m: int, k: int) -> int:
    if n > m:
        return kthElement(arr2, m, arr1, n, k)
    low = max(0, k - m)
    high = min(k, n)
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        l1 = arr1[cut1 - 1] if cut1 > 0 else float('-inf')
        r1 = arr1[cut1] if cut1 < n else float('inf')
        l2 = arr2[cut2 - 1] if cut2 > 0 else float('-inf')
        r2 = arr2[cut2] if cut2 < m else float('inf')
        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        if l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return -1
