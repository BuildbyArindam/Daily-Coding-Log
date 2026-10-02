"""
Platform   : Code360
Problem    : Construct a Strict Binary Tree
Link       : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381001?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty : Medium
Topics     : Binary Tree, Stack, Preorder Traversal
Date       : 2026-10-02

Approach:
    A strict binary tree has nodes with either 0 or 2 children. We are given the
    preorder traversal plus an N/L array marking each node as Non-leaf or Leaf.
    Because preorder visits a node before its children, we can rebuild the tree
    in one pass with a stack of "open" non-leaf nodes:
      1. Create the root; if it is 'N', push it.
      2. For each next node, attach it to the stack top: first as the left child,
         and if left is already filled, as the right child (then pop, since that
         parent is complete).
      3. If the new node is 'N', push it so it receives its own children next.

Time Complexity  : O(n), each node is created, attached and pushed/popped once.
Space Complexity : O(h) for the stack, where h is the tree height (O(n) worst case).
"""


# ----------------------------------- Solution -----------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

'''
    # Binary tree node class for reference.
    class BinaryTreeNode:
        def __init__(self, data):
            self.val = data
            self.left = None
            self.right = None
'''

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def constructSBT(pre, typleNL):
    root = BinaryTreeNode(pre[0])
    stack = []
    if typleNL[0] == 'N':
        stack.append(root)
    for i in range(1, len(pre)):
        child = BinaryTreeNode(pre[i])
        parent = stack[-1]
        if parent.left is None:
            parent.left = child
        else:
            parent.right = child
            stack.pop()
        if typleNL[i] == 'N':
            stack.append(child)
    return root
