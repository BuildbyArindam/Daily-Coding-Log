"""
Problem   : Optimal BST
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381318?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Hard
Topics    : Dynamic Programming, Interval DP, Binary Search Tree
Date      : 2026-10-03

Approach:
    Interval DP. dp[i][j] is the minimum search cost of a BST built from
    keys i..j. Trying each key `root` in [i, j] as the root, the cost is
    dp[i][root-1] + dp[root+1][j] + sum(freq[i..j]). The sum is added
    because every key in the range moves one level deeper under the new
    root. A prefix-sum array gives each range sum in O(1). Ranges are
    filled in increasing length, so the subproblems are always ready.
    Answer: dp[0][n-1].

Time Complexity : O(n^3) -> O(n^2) states x O(n) roots per state
Space Complexity: O(n^2) for the dp table (+ O(n) for prefix sums)
"""


# ------------------------------------------- Solution --------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def optimalCost(keys, freq, n):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + freq[i]
    dp = [[0] * n for _ in range(n)]
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total_freq = prefix[j + 1] - prefix[i]
            dp[i][j] = float('inf')
            for root in range(i, j + 1):
                left_cost = dp[i][root - 1] if root > i else 0
                right_cost = dp[root + 1][j] if root < j else 0
                cost = left_cost + right_cost + total_freq
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        keys = list(map(int, input().split()))
        freq = list(map(int, input().split()))
        print(optimalCost(keys, freq, n))
