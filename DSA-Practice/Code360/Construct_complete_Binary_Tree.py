"""
Problem   : Construct Complete Binary Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380998?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, Array, Level-Order Indexing
Date      : 2026-10-02

Approach:
    A complete binary tree stored in level order maps directly to array indices.
    For the node at index i:
        left child  -> 2*i + 1
        right child -> 2*i + 2
    Create a TreeNode for every element first, then link each node to its
    children whenever those indices fall within the array bounds.
    Return nodes[0] as the root (or None for an empty array).

Complexity:
    Time  : O(n), one pass to create nodes and one pass to link them
    Space : O(n), the node list (the tree itself needs O(n) anyway)
"""


# ----------------------------------- Solution ------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

'''
  ----Binary tree node class for reference-----
    class TreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

'''

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructCBT(arr):
    n = len(arr)
    if n == 0:
        return None
    nodes = [TreeNode(value) for value in arr]
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n:
            nodes[i].left = nodes[left]
        if right < n:
            nodes[i].right = nodes[right]
    return nodes[0]
