"""
Problem   : Binary Tree Zigzag Traversal
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380983?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Date      : 2026-10-02
Difficulty: Easy
Topics    : Binary Tree, BFS, Level Order Traversal, Queue

Approach  : Standard level-order (BFS) traversal using a deque. Process one
            level at a time, collecting node values into a list. A boolean
            flag tracks direction: on right-to-left levels the collected
            list is reversed before being appended to the answer. The flag
            flips after every level.

Time      : O(N) - every node is visited once (reversals total O(N) across levels)
Space     : O(N) - queue holds up to one level (O(W)) plus the output list
"""


# ------------------------------------ Solution ---------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

# BinaryTreeNode class definition
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#

def zigZagTraversal(root):
    if root is None:
        return []
    ans = []
    queue = deque([root])
    left_to_right = True
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not left_to_right:
            level.reverse()
        ans.extend(level)
        left_to_right = not left_to_right
    return ans
