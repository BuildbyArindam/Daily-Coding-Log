"""
Problem   : LCA of Two Nodes In A BST
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381331?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Trees
Date      : 2026-10-03

Approach:
    Use the BST ordering property and walk down iteratively from the root.
    - If both P and Q are smaller than the current node, the LCA is in the left subtree.
    - If both are larger, the LCA is in the right subtree.
    - Otherwise the two values split here (or one equals the current node),
      so the current node is the LCA.

Complexity:
    Time  : O(H), where H is the height of the tree
            (O(log N) balanced, O(N) skewed)
    Space : O(1), iterative with no recursion stack
"""


# ---------------------------------------- Solution ---------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def LCAinaBST(root, P, Q):
    p = P.data
    q = Q.data
    while root is not None:
        if p < root.data and q < root.data:
            root = root.left
        elif p > root.data and q > root.data:
            root = root.right
        else:
            return root
    return None
