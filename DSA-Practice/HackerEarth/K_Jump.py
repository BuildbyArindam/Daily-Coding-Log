"""
Problem   : K - Jump
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/long-jump-1-7d02705a/
Date      : 2026-08-29
Difficulty: Medium
Topics    : Arrays, Data Structures, One-dimensional, STL

Approach:
    Find the longest subsequence of the array such that each consecutive
    pair of chosen elements (a[i], a[j], i < j) satisfies a[j] - a[i] >= K.
    This is a patience-sorting / LIS-style greedy using binary search:
    maintain `dp`, where dp[i] is the smallest possible "last value" of a
    valid chain of length i+1 (each step advancing by at least K over the
    previous). For each new value, binary search for the rightmost
    position whose value is <= (val - K); that tells us how long a valid
    chain we can extend, and we greedily keep the tail value as small as
    possible to leave room for future extensions.

Time complexity : O(N log N)  -- one binary search (bisect_right) per element
Space complexity: O(N)        -- the dp array, worst case one entry per element
"""


# ------------------------------ Solution -------------------------------------


import sys
from bisect import bisect_right

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    k = int(input_data[0])
    n = int(input_data[1])
    arr = list(map(int, input_data[2:2 + n]))
    dp = []
    for val in arr:
        target = val - k
        idx = bisect_right(dp, target)
        if idx == 0:
            if not dp:
                dp.append(val)
            else:
                dp[0] = min(dp[0], val)
        else:
            if idx == len(dp):
                dp.append(val)
            else:
                dp[idx] = min(dp[idx], val)
    print(len(dp))

if __name__ == '__main__':
    solve()
