"""
Problem   : Maximum Path Sum Between Two Leaves
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381012?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Hard
Topics    : Binary Tree, DFS, Recursion
Date      : 2026-10-02

Approach:
    Post-order DFS where dfs(node) returns the max root-to-leaf sum
    starting at that node.
      - Leaf: return its value.
      - One child: no leaf-to-leaf path can bend here, so just extend the
        child's path (node.val + dfs(child)).
      - Two children: a candidate answer is left + node.val + right, so
        update the global max, then return node.val + max(left, right)
        to the parent.
    If no node has two children (empty, single-node, or skewed tree),
    no leaf-to-leaf path exists, so return -1.

Time Complexity : O(N), each node is visited once.
Space Complexity: O(H) recursion stack, where H is the tree height
                  (O(N) worst case for a skewed tree).
"""


# --------------------------------------- Solution -----------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def findMaxSumPath(root):
    max_sum = [float('-inf')]
    def dfs(node):
        if node is None:
            return float('-inf')
        if node.left is None and node.right is None:
            return node.val
        if node.left is None:
            return node.val + dfs(node.right)
        if node.right is None:
            return node.val + dfs(node.left)
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        max_sum[0] = max(
            max_sum[0],
            left_sum + node.val + right_sum
        )
        return node.val + max(left_sum, right_sum)
    dfs(root)
    if max_sum[0] == float('-inf'):
        return -1
    return max_sum[0]

def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    length = len(levelOrder)
    if length == 1:
        return None
    root = BinaryTreeNode(levelOrder[start])
    start += 1
    q = Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelOrder[start]
        start += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelOrder[start]
        start += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

t = int(input())
for i in range(t):
    root = takeInput()
    maxSum = findMaxSumPath(root)
    print(maxSum)
