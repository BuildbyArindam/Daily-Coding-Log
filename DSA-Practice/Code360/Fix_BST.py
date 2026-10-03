"""
Problem   : Fix BST
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381329
Date      : 2026-10-03
Difficulty: Easy
Topics    : Binary Search Tree, Morris Traversal, Inorder Traversal

Approach  : Two nodes of the BST were swapped by mistake. An inorder traversal of a
            valid BST is sorted, so the swap shows up as inversions (prev > curr).
            I use Morris inorder traversal (temporary threads to the inorder
            predecessor) so no recursion or stack is needed.
            - First inversion: first = prev, middle = curr
            - Second inversion (if any): last = curr
            If two inversions exist, swap first and last (non-adjacent nodes).
            Otherwise swap first and middle (adjacent nodes).
            The threads are removed as the traversal goes, so the tree is restored.

Time      : O(N)  (each edge is visited a constant number of times)
Space     : O(1)  (no recursion stack or auxiliary storage)
"""


# ---------------------------------------- Solution --------------------------------------------------


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

def fixBST(root):
    first = None
    middle = None
    last = None
    prev = None
    curr = root
    while curr is not None:
        if curr.left is None:
            if prev is not None and prev.data > curr.data:
                if first is None:
                    first = prev
                    middle = curr
                else:
                    last = curr
            prev = curr
            curr = curr.right
        else:
            pred = curr.left
            while pred.right is not None and pred.right != curr:
                pred = pred.right
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                pred.right = None
                if prev is not None and prev.data > curr.data:
                    if first is None:
                        first = prev
                        middle = curr
                    else:
                        last = curr
                prev = curr
                curr = curr.right
    if first is not None and last is not None:
        first.data, last.data = last.data, first.data
    elif first is not None and middle is not None:
        first.data, middle.data = middle.data, first.data
    return root
