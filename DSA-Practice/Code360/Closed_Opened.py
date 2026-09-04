"""
Problem: Closed/Opened
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/closed-opened_7187531?kunjiRedirection=true
Date: 2026-09-04
Difficulty: Medium
Topics: Tree, BFS, Level-Order Traversal, Boundary Nodes

Approach:
BFS level by level. For each level, a node is "opened" if it's the
leftmost/rightmost node of that level OR a leaf; all other nodes in
the level are "closed". Track running sums of opened vs closed node
values across the whole tree, then return |closed_sum - opened_sum|.

Time Complexity:  O(n) — each node visited once
Space Complexity: O(n) — BFS queue in the worst case (last level of a
                  complete/balanced tree can hold ~n/2 nodes)
"""


# ---------------------------- Solution ------------------------------------


"""
Binary tree node class for reference

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
from typing import *
from collections import deque

def closedOpened(root) -> int:
    if root is None:
        return 0
    total_sum = 0
    opened_sum = 0
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            total_sum += node.data
            is_leaf = node.left is None and node.right is None
            is_left_boundary = (i == 0)
            is_right_boundary = (i == level_size - 1)
            if is_leaf or is_left_boundary or is_right_boundary:
                opened_sum += node.data
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    closed_sum = total_sum - opened_sum
    return abs(closed_sum - opened_sum)
