"""
Problem   : Partitions
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/partitions-5fd40ffc/
Difficulty: Medium
Topics    : Binary Search, Searching, Two Pointers, DP, Prefix Sums
Date      : 2026-10-05

Approach:
    Count the ways to split the array into contiguous segments whose sums
    all lie in [L, R]. Let dp[i] be the number of ways to partition the
    first i elements. Then dp[i] = sum of dp[j] over all j < i with
    L <= prefix[i] - prefix[j] <= R.
    Since prefix sums are non-decreasing (positive elements), the valid j
    values form a contiguous window [left, right - 1], which two moving
    pointers track. A prefix sum over dp (pref_dp) answers each window sum
    in O(1).

Complexity:
    Time  : O(n)  (each pointer moves at most n times)
    Space : O(n)  (prefix, dp, pref_dp arrays)
"""


# -------------------------------------- Solution ----------------------------------------------------


MOD = 1000000007
n, L, R = map(int, input().split())
a = list(map(int, input().split()))
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + a[i - 1]
dp = [0] * (n + 1)
dp[0] = 1
pref_dp = [0] * (n + 1)
pref_dp[0] = 1
left = 0
right = 0
for i in range(1, n + 1):
    while left < i and prefix[left] < prefix[i] - R:
        left += 1
    while right < i and prefix[right] <= prefix[i] - L:
        right += 1
    if left < right:
        dp[i] = (pref_dp[right - 1] - (pref_dp[left - 1] if left > 0 else 0)) % MOD
    pref_dp[i] = (pref_dp[i - 1] + dp[i]) % MOD
print(dp[n] % MOD)
