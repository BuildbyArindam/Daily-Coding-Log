"""
Problem   : Maximum length subsequence
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/maximum-length-subsequence-f5f9c13d/
Difficulty: Easy
Topics    : Implementation, Sorting, Algorithms, 2D DP
Date      : 2026-10-22

Approach  : Order doesn't matter for the subsequence, so sort the array.
            For each index i, binary search (bisect_right) for the first
            element greater than A[i] + 10. The window [i, stop) is the
            longest valid subsequence starting at A[i]. Track the maximum
            window size.

Time      : O(N log N)  (sort + N binary searches)
Space     : O(N)        (sorted copy of the array)
"""


# --------------------------------------------- Solution ---------------------------------------------------------------


def solve (N, A):
    # Write your code here
    from bisect import bisect_right
    vals = sorted(A)
    limit = 10
    best = 0
    idx = 0
    while idx < N:
        stop = bisect_right(vals, vals[idx] + limit)
        span = stop - idx
        if span > best:
            best = span
        idx += 1
    return best

N = int(input())
A = list(map(int, input().split()))
out_ = solve(N, A)
print (out_)
