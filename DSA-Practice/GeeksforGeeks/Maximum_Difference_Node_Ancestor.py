"""
Problem   : Maximum Difference Between Node and its Ancestor
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/maximum-difference-between-node-and-its-ancestor/1
Difficulty: Medium
Topic     : Tree (Binary Tree, DFS)
Date      : 2026-08-20

Approach:
    Single post-order DFS. For each subtree, return (min_value_in_subtree,
    max_ancestor_diff_in_subtree). At each node, compare node.data against
    the minimum value returned from its left/right subtrees (this covers
    node vs. any descendant, which is equivalent to ancestor vs. descendant
    since we check it at every level going down). Bubble up the running
    max_diff alongside the running min so parents can do the same check.

Time Complexity : O(N) — each node visited once
Space Complexity: O(H) — recursion stack, H = height of tree
                  (O(N) worst case for skewed tree, O(log N) if balanced)
"""


# ------------------------------ Solution ----------------------------------


''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # code here
        def solve(node):
            if node is None:
                return float('inf'), float('-inf')
            min_val = node.data
            max_diff = float('-inf')
            if node.left:
                left_min, left_diff = solve(node.left)
                max_diff = max(max_diff, left_diff, node.data - left_min)
                min_val = min(min_val, left_min)
            if node.right:
                right_min, right_diff = solve(node.right)
                max_diff = max(max_diff, right_diff, node.data - right_min)
                min_val = min(min_val, right_min)
            return min_val, max_diff
        return solve(root)[1]
