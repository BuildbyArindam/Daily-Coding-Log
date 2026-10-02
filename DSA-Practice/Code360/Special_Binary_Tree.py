"""
Problem   : Special Binary Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381531?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, Recursion, DFS
Date      : 2026-10-02

Approach:
    A "special" binary tree is one where every node has either 0 or 2 children
    (a full binary tree). Recursively:
      - Leaf node (no children)         -> valid
      - Exactly one child               -> invalid
      - Two children                    -> valid only if both subtrees are valid

Complexity:
    Time  : O(N), each node is visited at most once
    Space : O(H), recursion stack, where H is the tree height
"""


# -------------------------------------- Solution ----------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----

    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

def isSpecialBinaryTree(root):
    if root.left is None and root.right is None:
        return True
    if root.left is None or root.right is None:
        return False
    return isSpecialBinaryTree(root.left) and isSpecialBinaryTree(root.right)
