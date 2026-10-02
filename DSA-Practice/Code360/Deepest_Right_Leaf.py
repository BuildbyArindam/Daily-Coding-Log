"""
Platform   : Code360 (Coding Ninjas)
Problem    : Deepest Right Leaf
Link       : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381528?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty : Medium
Topics     : Binary Tree, BFS, Level Order Traversal
Date       : 2026-10-02

Approach:
    Level-order traversal (BFS) with a flag on each queue entry marking whether
    the node is a right child. Every time a leaf that is a right child is
    seen, it overwrites `answer`. Since BFS visits shallower levels first, and
    left-to-right within a level, the last overwrite is the deepest right leaf
    (the rightmost one if several share that depth). If none exists, return a
    node with data -1.

Complexity:
    Time  : O(N), each node is visited once
    Space : O(W), where W is the max width of the tree (O(N) worst case)
"""


# --------------------------------- Solution -------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

class BinaryTreeNode:
    def __init__(self, data): 
        self.data = data
        self.left = None
        self.right = None
               
def deepestRightLeaf(root):
    if root is None:
        return BinaryTreeNode(-1)
    q = deque()
    q.append((root, False))
    answer = None
    while q:
        size = len(q)
        for _ in range(size):
            node, is_right = q.popleft()
            if is_right and node.left is None and node.right is None:
                answer = node
            if node.left:
                q.append((node.left, False))
            if node.right:
                q.append((node.right, True))
    if answer is None:
        return BinaryTreeNode(-1)
    return answer
