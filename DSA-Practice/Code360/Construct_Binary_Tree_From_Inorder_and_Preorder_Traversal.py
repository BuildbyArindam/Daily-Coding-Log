"""
Problem   : Construct Binary Tree From Inorder and Preorder Traversal
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380993
Date      : 2026-10-02
Difficulty: Easy
Topics    : Binary Tree, Hash Map, Recursion, Divide and Conquer

Approach:
    The first element of preorder is always the root of the current subtree.
    Find that root in inorder: everything to its left is the left subtree,
    everything to its right is the right subtree. A hash map of
    value -> inorder index makes each lookup O(1). A running preorder pointer
    advances as nodes are created, and we build left before right, which
    matches preorder order. (Assumes all node values are unique.)

Complexity:
    Time : O(n), each node is created once with an O(1) index lookup.
    Space: O(n), for the hash map plus O(h) recursion stack (O(n) worst case
           for a skewed tree).
"""


# ----------------------------------- Solution --------------------------------------------------


class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

from typing import List
import sys
sys.setrecursionlimit(10000)
def buildBinaryTree(preorder: List[int], inorder: List[int]) -> TreeNode:
    inorder_index = {value: i for i, value in enumerate(inorder)}
    preorder_index = 0
    def build(left: int, right: int):
        nonlocal preorder_index
        if left > right:
            return None
        root_value = preorder[preorder_index]
        preorder_index += 1
        root = TreeNode(root_value)
        mid = inorder_index[root_value]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root
    return build(0, len(inorder) - 1)
