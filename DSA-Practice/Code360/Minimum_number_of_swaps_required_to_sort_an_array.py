"""
Problem   : Minimum Number of Swaps Required to Sort an Array
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382144
Difficulty: Easy
Topics    : Array, Sorting, Graph (Cycle Detection)
Date      : 2026-09-18

Approach:
    Treat the array as a permutation. Pair each value with its original
    index, then sort by value to get the target position for each index.
    Walk through unvisited indices, following the permutation cycles
    (i -> target position of element at i -> ...). Each cycle of length k
    needs (k - 1) swaps to place every element correctly, so summing
    (cycle_size - 1) over all cycles gives the minimum total swaps.

Time complexity : O(n log n)   -- dominated by the sort
Space complexity: O(n)         -- for the (value, index) pairs and visited array
"""


# ------------------------------------ Solution ------------------------------------------


def minSwaps(arr):
    # Write your code here.
    n = len(arr)
    nums = sorted((arr[i], i) for i in range(n))
    visited = [False] * n
    swaps = 0
    for i in range(n):
        if visited[i] or nums[i][1] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = nums[j][1]
            cycle_size += 1
        swaps += cycle_size - 1
    return swaps
