"""
Problem   : Danny !
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/danny/
Date      : 2026-10-07
Difficulty: Medium
Topics    : Binary Search, Two Pointers, Searching

Approach  : Find the K-th smallest pairwise difference.
            1. Sort the array so pair differences are monotonic.
            2. Binary search on the answer x in [0, max - min]: find the smallest x
               such that at least K pairs (i < j) have A[j] - A[i] <= x.
            3. Count pairs for a given x with a two-pointer sliding window,
               exiting early once the count reaches K.

Complexity: Time  - O(N log N + N log(max - min))
            Space - O(1) extra (besides the input array)
"""


# ------------------------------------------- Solution ------------------------------------------------


import sys

def count_pairs(arr, x, k):
    """
    Count pairs (i, j), i < j, such that arr[j] - arr[i] <= x.
    We only need to know whether the count reaches k.
    """
    n = len(arr)
    left = 0
    count = 0
    for right in range(n):
        while arr[right] - arr[left] > x:
            left += 1
        count += right - left
        if count >= k:
            return count
    return count

def solve():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    low = 0
    high = A[-1] - A[0]
    while low < high:
        mid = (low + high) // 2
        if count_pairs(A, mid, K) >= K:
            high = mid
        else:
            low = mid + 1
    print(low)

if __name__ == "__main__":
    solve()
