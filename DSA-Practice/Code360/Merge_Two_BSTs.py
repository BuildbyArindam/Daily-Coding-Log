"""
Problem   : Merge Two BSTs
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381327?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Inorder Traversal, Two Pointers, Divide and Conquer
Date      : 2026-10-03

Approach:
  1. Iterative inorder traversal of both BSTs gives two sorted arrays.
  2. Merge the arrays with two pointers into one sorted array.
  3. Build a height-balanced BST from the merged array by recursively
     picking the middle element as the root.

Complexity (n = nodes in BST 1, m = nodes in BST 2):
  Time  : O(n + m). Traversals, merge and rebuild are each linear.
  Space : O(n + m) for the arrays and the new tree, plus O(log(n + m))
          recursion depth for the balanced build.
"""


# ----------------------------------- Solution --------------------------------------------------


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

def mergeBST(root1, root2):
    def inorder(root):
        result = []
        stack = []
        curr = root
        while curr is not None or stack:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.data)
            curr = curr.right
        return result
    arr1 = inorder(root1)
    arr2 = inorder(root2)
    merged = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    def buildBST(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(merged[mid])
        root.left = buildBST(left, mid - 1)
        root.right = buildBST(mid + 1, right)
        return root
    return buildBST(0, len(merged) - 1)
