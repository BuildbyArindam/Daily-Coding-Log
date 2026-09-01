"""
Problem   : Minimum Smoke (MISMO)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MISMO
Date      : 2026-09-01
Difficulty: Medium-Hard
Topics    : Dynamic Programming, Interval DP, Prefix Sum

Approach  :
    Interval DP over subarrays [i..j]. dp[i][j] = minimum total smoke
    produced when merging the segment a[i..j] into one "color" through
    repeated pairwise merges. For every split point k in [i, j-1],
    the smoke added by combining the left part [i..k] and right part
    [k+1..j] is (color(i,k) * color(k+1,j)), where a segment's color
    is the sum of its elements mod 100 (via prefix sums for O(1) range
    sums). Take the split minimizing dp[i][k] + dp[k+1][j] + that
    product. Base case: single elements have dp = 0.

Complexity:
    Time  : O(n^3)  -- O(n^2) states, O(n) transition per state
    Space : O(n^2)  -- dp table (+ O(n) prefix sum array)
"""


# ----------------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    def color(i, j):
        return (prefix[j + 1] - prefix[i]) % 100
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            best = float('inf')
            for k in range(i, j):
                left_color = color(i, k)
                right_color = color(k + 1, j)
                smoke = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + left_color * right_color
                )
                best = min(best, smoke)
            dp[i][j] = best
    print(dp[0][n - 1])

if __name__ == "__main__":
    solve()
