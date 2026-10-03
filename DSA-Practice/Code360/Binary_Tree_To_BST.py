"""
Problem   : Binary Tree To BST
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381322?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, BST, Inorder Traversal, Sorting
Date      : 2026-10-03

Approach:
  An inorder traversal of a BST yields sorted values. So:
  1. Inorder-traverse the tree and collect all node values.
  2. Sort the values.
  3. Inorder-traverse again, overwriting each node's data with the next
     sorted value. The tree structure stays unchanged.

Time Complexity : O(n log n)  -> O(n) traversals + O(n log n) sort
Space Complexity: O(n)        -> values list, plus O(h) recursion stack
"""


# ------------------------------------- Solution ------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def binaryTreeToBst(root):
    values = []
    def get_values(node):
        if node is None:
            return
        get_values(node.left)
        values.append(node.data)
        get_values(node.right)
    get_values(root)
    values.sort()
    index = 0

    def update_values(node):
        nonlocal index
        if node is None:
            return
        update_values(node.left)
        node.data = values[index]
        index += 1
        update_values(node.right)
    update_values(root)
    return root
