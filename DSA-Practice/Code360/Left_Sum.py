"""
Problem: Same Label Nodes (Sum of Left Nodes)
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/left-sum_672?kunjiRedirection=true
Date: 2026-09-04
Difficulty: Easy
Topics: Binary Tree, DFS, Recursion

Approach:
Build the binary tree from level-order input (-1 = null).
Recursively traverse the tree; whenever a node has a left child,
add that child's value to a running total, then recurse into
both left and right subtrees to accumulate contributions from
deeper levels.

Time Complexity: O(N)  — each node visited exactly once
Space Complexity: O(N) for the queue during tree construction,
                  O(H) recursion stack for the DFS (H = tree height,
                  worst case O(N) for a skewed tree)
"""


# -------------------------- Solution --------------------------------


from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def build_tree(values):
    if not values or values[0] == -1:
        return None
    root = BinaryTreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if i < len(values) and values[i] != -1:
            current.left = BinaryTreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] != -1:
            current.right = BinaryTreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root
def sum_of_left_nodes(root):
    if root is None:
        return 0
    total = 0
    if root.left is not None:
        total += root.left.data
    total += sum_of_left_nodes(root.left)
    total += sum_of_left_nodes(root.right)
    return total
values = list(map(int, input().split()))
root = build_tree(values)
print(sum_of_left_nodes(root))
