"""
Problem   : Total Number of BSTs using array elements as root node
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381320?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Dynamic Programming, Catalan Numbers, Combinatorics
Date      : 2026-10-03

Approach:
  If arr[i] is the root, the k elements smaller than it form the left subtree
  and the remaining n-1-k elements form the right subtree. The number of BSTs
  is therefore Catalan(k) * Catalan(n-1-k).
  - Precompute Catalan numbers up to MAXN with the DP recurrence
    C(n) = sum(C(i) * C(n-1-i)) mod 1e9+7.
  - Sort the array and map each value to its rank, which is k.
  - Answer each element in O(1) using the precomputed table.

Complexity:
  Time  : O(MAXN^2) one-time precomputation + O(n log n) per call (sorting)
  Space : O(MAXN) for the Catalan table + O(n) for the rank map and result
"""


# ---------------------------------------------- Solution --------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

MOD = 10**9 + 7
MAXN = 1001
_catalan = [0] * (MAXN + 1)
_catalan[0] = 1
for _n in range(1, MAXN + 1):
    _s = 0
    for _i in range(_n):
        _s += _catalan[_i] * _catalan[_n - 1 - _i]
    _catalan[_n] = _s % MOD

def totalBST(arr):
    # Write your code here.
    n = len(arr)
    sorted_arr = sorted(arr)
    rank = {}
    for idx, val in enumerate(sorted_arr):
        if val not in rank:
            rank[val] = idx
    result = []
    for x in arr:
        k = rank[x]
        result.append(_catalan[k] * _catalan[n - 1 - k] % MOD)
    return result
