"""
Problem   : Count unique BSTs
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381319?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Hard
Topics    : Dynamic Programming, Catalan Numbers, Binary Search Tree, Combinatorics
Date      : 2026-10-03

Approach:
    The number of structurally unique BSTs with n nodes is the nth Catalan number.
    Pick each of the n values as the root. The root splits the remaining n-1 nodes
    into a left subtree of size `root` and a right subtree of size `n-1-root`.
    The two sides are independent, so
        C(n) = sum over root=0..n-1 of C(root) * C(n-1-root),  with C(0) = 1.
    Build the table bottom-up and take every step modulo 10^9 + 7.

Complexity:
    Time  : O(n^2)
    Space : O(n)
"""


# ----------------------------------- Solution --------------------------------------------


MOD = 10**9 + 7

def totalTrees(num):
    # Write your code here.
    catalan = [0] * (num + 1)
    catalan[0] = 1
    for n in range(1, num + 1):
        for root in range(n):
            catalan[n] = (catalan[n] +
                          catalan[root] * catalan[n - 1 - root]) % MOD
    return catalan[num]
