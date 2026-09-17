"""
Problem   : Tug of War
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380924
Difficulty: Easy
Date      : 2026-09-17
Topic     : Dynamic Programming - Subset Sum / Balanced Partition

Approach:
Split array into two subsets of size n//2 (k) and n-k such that the
absolute difference of subset sums is minimized. For each count j
(0..k), maintain dp[j] = set of all achievable sums using exactly j
elements. Iterate elements and update counts in decreasing order
(0/1 knapsack style) to avoid reusing an element twice. Answer is
min over all sums s in dp[k] of |total - 2*s|.

Time complexity : O(n * k * S), where S = sum(arr)
                   (bounded by number of distinct achievable sums)
Space complexity: O(k * S)  -- k+1 sets, each up to S+1 elements
"""


# ---------------------------------- Solution ------------------------------------------


from sys import *
from collections import *
from math import *

def tugOfWar(arr, n):
    total = sum(arr)
    k = n // 2
    dp = [set() for _ in range(k + 1)]
    dp[0].add(0)
    for x in arr:
        for j in range(k, 0, -1):
            for s in list(dp[j - 1]):
                dp[j].add(s + x)
    ans = float('inf')
    for s in dp[k]:
        ans = min(ans, abs(total - 2 * s))
    return ans
