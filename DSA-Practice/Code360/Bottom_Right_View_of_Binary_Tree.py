"""
Problem   : Bottom Right View of Binary Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381010
Difficulty: Easy
Topics    : Binary Tree, DFS, Recursion, Diagonal Traversal
Date      : 2026-10-02

Approach:
  Treat "level" as a diagonal index: moving right keeps the same diagonal,
  moving left starts the next one. A right-first DFS records the first node
  it reaches on each new diagonal (tracked via maxLevel). The collected
  values are sorted before returning, as the output requires.

Complexity:
  Time : O(N + K log K), where K = number of diagonals (K <= N), so O(N log N) worst case
  Space: O(H) recursion stack + O(K) for the answer, so O(N) worst case
"""


# ---------------------------------------- Solution ------------------------------------------


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

def bottomRightView(root):
    if root is None:
        return []
    ans = []
    maxLevel = [-1]
    def brViewUtil(node, level):
        if node is None:
            return
        brViewUtil(node.right, level)
        if level > maxLevel[0]:
            ans.append(node.data)
            maxLevel[0] = level
        brViewUtil(node.left, level + 1)
    brViewUtil(root, 0)
    ans.sort()
    return ans
