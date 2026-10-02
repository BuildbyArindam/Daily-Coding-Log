"""
Problem   : Diameter Of Binary Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381015?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, DFS, Recursion
Date      : 2026-10-02

Approach:
    The diameter is the longest path (counted in edges) between any two nodes.
    Every such path has a "highest" node, and the path through it has length
    left_height + right_height. A single post-order DFS computes each node's
    height and, at every node, updates a running maximum with that sum.
    This avoids recomputing heights at each node, which would be O(n^2) on a
    skewed tree.

Complexity:
    Time : O(n), each node is visited once.
    Space: O(h) recursion stack, where h is the tree height
           (O(n) worst case for a skewed tree, O(log n) for a balanced one).
"""


# ---------------------------------------- Solution --------------------------------------------------


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0
    def height(node):
        nonlocal diameter
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = max(diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
    height(root)
    return diameter
