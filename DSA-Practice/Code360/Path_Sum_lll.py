"""
Problem: Path Sum III
Link: https://www.naukri.com/code360/problems/path-sum-lll_1164407?kunjiRedirection=true
Platform: Code360
Difficulty: Hard
Topics: Binary Tree, DFS, Prefix Sum, HashMap, Backtracking
Date: 2026-09-04

Approach:
Count root-to-node paths (not necessarily starting at root) that sum to k.
Do a single DFS while tracking the running prefix sum from the root to the
current node. At each node, check how many earlier ancestors had prefix
sum equal to (current_sum - k) — each such ancestor marks the start of a
valid downward path ending here. Store prefix sum frequencies in a hashmap
that is updated on entry and rolled back (backtracked) on exit, so only
sums along the current root-to-node path are counted.

Time Complexity: O(N) — each node visited once, O(1) hashmap ops
Space Complexity: O(H) — H = tree height, for recursion stack + hashmap 
                   entries limited to the active path
"""


# -------------------------- Solution ---------------------------------


from sys import *
from collections import *
from math import *

'''
    Following is the TreeNode class structure

    class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

'''

def noWays(root, k):
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1
    def dfs(node, current_sum):
        if node is None:
            return 0
        current_sum += node.data
        ways = prefix_sum_count[current_sum - k]
        prefix_sum_count[current_sum] += 1
        ways += dfs(node.left, current_sum)
        ways += dfs(node.right, current_sum)
        prefix_sum_count[current_sum] -= 1
        return ways
    return dfs(root, 0)
