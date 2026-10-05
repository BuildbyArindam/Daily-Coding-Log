"""
Problem   : N girls
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/n-girls-bbd50a1d/
Date      : 2026-10-05
Difficulty: Medium
Topics    : Algorithms, Binary Search, Searching

Approach  : Sort the array, then use a two-pointer sliding window to find
            the longest window where Q * a[right] <= P * a[left] (the
            P/Q ratio condition, kept in integer form to avoid float
            error). Then add the k extra allowance to that window size
            and cap the result at n.

Time      : O(n log n) - sorting dominates; the two-pointer pass is O(n)
Space     : O(n) - input list (sorted in place)
"""


# ------------------------------------- Solution ------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n, k, P, Q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    left = 0
    best = 0
    for right in range(n):
        while left <= right and Q * a[right] > P * a[left]:
            left += 1
        best = max(best, right - left + 1)
    print(min(n, best + k))

if __name__ == "__main__":
    solve()
