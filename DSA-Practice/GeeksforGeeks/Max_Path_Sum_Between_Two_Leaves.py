"""
Problem   : Max Path Sum Between Two Leaves
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/maximum-path-sum/1
Difficulty: Hard
Topics    : Tree, DFS, Recursion
Date      : 2026-10-07

Approach:
    Post-order DFS. For each node, return the best downward path sum from
    that node to any leaf in its subtree.
    - Leaf: return its value.
    - Node with one child: the path can't "turn" here, so just extend the
      child's path (node.data + child_sum).
    - Node with two children: this node can be the turning point of a
      leaf-to-leaf path, so update the answer with left + node + right,
      then return node.data + max(left, right) to the parent.
    If the tree has fewer than 2 leaves (e.g. a skewed tree), no
    leaf-to-leaf path exists, so return -1.

Time Complexity : O(N), each node is visited once
Space Complexity: O(H), recursion stack, where H is the tree height
                  (O(N) worst case for a skewed tree)
"""


# ------------------------------------------------ Solution ---------------------------------------------------------


'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''
class Solution:        
    def maxPathSum(self, root):
        # code here
        if root is None:
            return -1
        import sys
        sys.setrecursionlimit(20000)
        max_sum = float('-inf')
        leaf_count = 0
        def dfs(node):
            nonlocal max_sum, leaf_count
            if node is None:
                return float('-inf')
            if node.left is None and node.right is None:
                leaf_count += 1
                return node.data
            if node.left is None:
                return node.data + dfs(node.right)
            if node.right is None:
                return node.data + dfs(node.left)
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            max_sum = max(max_sum, left_sum + node.data + right_sum)
            return node.data + max(left_sum, right_sum)
        dfs(root)
        return max_sum if leaf_count >= 2 else -1
