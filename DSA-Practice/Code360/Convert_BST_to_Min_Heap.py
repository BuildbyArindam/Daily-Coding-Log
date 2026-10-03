"""
Problem   : Convert BST to Min Heap
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381324
Difficulty: Medium
Topics    : Binary Search Tree, Heap, Tree Traversal, Recursion
Date      : 2026-10-03

Approach:
  1. Inorder traversal of a BST yields values in sorted (ascending) order.
  2. Overwrite the nodes in preorder with those sorted values. Each node
     then holds a value smaller than everything in its subtrees, and the
     whole left subtree holds smaller values than the right subtree, which
     is exactly the required min-heap property.

Complexity:
  Time  : O(N), one inorder pass plus one preorder pass
  Space : O(N) for the values list, plus O(H) recursion stack
"""


# -------------------------------------- Solution ------------------------------------------------------


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

def convertBST(root):
    values = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        values.append(node.data)
        inorder(node.right)
    inorder(root)
    index = [0]
    def preorder(node):
        if node is None:
            return
        node.data = values[index[0]]
        index[0] += 1
        preorder(node.left)
        preorder(node.right)
    preorder(root)
    return root
