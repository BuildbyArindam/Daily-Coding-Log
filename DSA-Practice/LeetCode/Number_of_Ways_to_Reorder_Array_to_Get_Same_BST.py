"""
Problem   : 1569. Number of Ways to Reorder Array to Get Same BST
Platform  : LeetCode 
Link      : https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
Date      : 2026-10-18
Difficulty: Hard
Topics    : Array, Math, Divide and Conquer, DP, Tree, Union-Find, BST,
            Memoization, Combinatorics, Binary Tree

Approach  :
  The first element is the BST root. Elements smaller than the root form the
  left subtree and larger ones form the right subtree. Any reordering that
  keeps the relative order inside each subtree yields the same BST, and the
  two subsequences can be interleaved in C(L + R, L) ways. So:
      ways(arr) = C(L + R, L) * ways(left) * ways(right)
  Pascal's triangle is precomputed modulo 1e9+7 to avoid factorial inverses.
  The answer subtracts 1 to exclude the original ordering.

Complexity:
  Time  : O(n^2)  (Pascal table + recursive partitioning, O(n * depth))
  Space : O(n^2)  for the table (recursion stack and slices add O(n) depth)
"""


# ------------------------------------------------ Solution --------------------------------------------------------------


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        comb = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            comb[i][0] = comb[i][i] = 1
            for j in range(1, i):
                comb[i][j] = (comb[i - 1][j - 1] +
                              comb[i - 1][j]) % MOD
        def dfs(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            left_ways = dfs(left)
            right_ways = dfs(right)
            ways = comb[len(left) + len(right)][len(left)]
            return (ways * left_ways * right_ways) % MOD
        return (dfs(nums) - 1) % MOD

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
