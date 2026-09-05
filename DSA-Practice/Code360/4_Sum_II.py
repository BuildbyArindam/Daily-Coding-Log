"""
Problem   : 4 Sum II
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/4-sum-ii_2221639
Difficulty: Medium
Topic     : Hashing, Frequency Counting, Arrays
Date      : 2026-09-05

Approach:
Split the 4 arrays into two pairs (arr1, arr2) and (arr3, arr4).
Precompute all pairwise sums of arr1[i] + arr2[j] into a frequency
table (offset by 200 to handle negative sums safely as array indices).
Then for every pair (arr3[k], arr4[l]), look up how many pairs from
the first half sum to the negation of arr3[k] + arr4[l]. Add that
count to the answer. This avoids the naive O(n^4) brute force by
trading it for O(n^2) time using a hash/frequency table.

Time Complexity : O(n^2)  — two O(n^2) passes (build freq table, then query)
Space Complexity: O(n^2) worst case for distinct sums (bounded here to O(401)
                  since sums are constrained to a fixed offset range; adjust
                  freq array size if input constraints allow larger sums)
"""


# --------------------------- Solution ---------------------------------


from typing import List

def fourSum(n: int, arr1: List[int], arr2: List[int], arr3: List[int], arr4: List[int]) -> int:
    freq = [0] * 401
    for i in range(n):
        for j in range(n):
            freq[arr1[i] + arr2[j] + 200] += 1
    ans = 0
    for k in range(n):
        for l in range(n):
            required = -(arr3[k] + arr4[l])
            ans += freq[required + 200]
    return ans
