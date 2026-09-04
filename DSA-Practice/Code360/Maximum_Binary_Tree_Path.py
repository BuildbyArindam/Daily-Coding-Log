"""
Problem   : Maximum Binary Tree Path
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/maximum-binary-tree-path_624839
Difficulty: Medium
Date      : 2026-09-04
Topics    : Binary Tree, DFS, Recursion, Tree Path Sum

Approach:
Iterative DFS using an explicit stack. Each stack entry carries
(node, running_sum_to_node, path_list_to_node). On reaching a leaf,
compare running_sum against the best sum found so far and update
max_path if it's larger. Avoids recursion depth issues on skewed trees.

Time Complexity : O(N) to visit every node once.
Space Complexity: O(N) for the stack, path lists, and (in the worst case,
                  a skewed tree) O(N) for the longest path stored.
"""


----------------------------- Solution ----------------------------------


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

def maximumSumPath(root):
    if root is None:
        return []
    stack = [(root, root.data, [root.data])]
    max_sum = -inf
    max_path = []
    while stack:
        node, current_sum, path = stack.pop()
        if node.left is None and node.right is None:
            if current_sum > max_sum:
                max_sum = current_sum
                max_path = path[:]
        if node.right is not None:
            stack.append(
                (node.right, current_sum + node.right.data,
                 path + [node.right.data])
            )
        if node.left is not None:
            stack.append(
                (node.left, current_sum + node.left.data,
                 path + [node.left.data])
            )
    return max_path

def buildTree():
    data = list(map(int, input().split()))
    if not data or data[0] == -1:
        return None
    root = BinaryTreeNode(data[0])
    queue = deque([root])
    i = 1
    while queue and i < len(data):
        node = queue.popleft()
        if i < len(data) and data[i] != -1:
            node.left = BinaryTreeNode(data[i])
            queue.append(node.left)
        i += 1
        if i < len(data) and data[i] != -1:
            node.right = BinaryTreeNode(data[i])
            queue.append(node.right)
        i += 1
    return root

root = buildTree()
ans = maximumSumPath(root)
print(*ans)
