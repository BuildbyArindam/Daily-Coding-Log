"""
Problem   : Except Boundary
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381526?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, DFS, Boundary Traversal
Date      : 02-Oct-2026

Approach:
    Return the sum of all nodes that are NOT on the tree's boundary.
    1. Collect boundary nodes into a set (keyed by node identity):
       root, all leaves (DFS), left boundary (non-leaf nodes walking
       down, preferring left child), right boundary (non-leaf nodes
       walking down, preferring right child).
    2. Traverse the whole tree and add up the data of every node
       that is not in the boundary set.

Complexity:
    Time  : O(N), each node is visited a constant number of times
    Space : O(N), boundary set (up to N nodes) + O(H) recursion stack
"""


# ------------------------------------- Solution -----------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

import queue

class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def exceptBoundary(root):
    if root is None:
        return 0
    boundary = set()
    boundary.add(root)
    def addLeaves(node):
        if node is None:
            return
        if node.left is None and node.right is None:
            boundary.add(node)
            return
        addLeaves(node.left)
        addLeaves(node.right)
    addLeaves(root)
    node = root.left
    while node is not None:
        if not (node.left is None and node.right is None):
            boundary.add(node)
        if node.left is not None:
            node = node.left
        else:
            node = node.right
    node = root.right
    while node is not None:
        if not (node.left is None and node.right is None):
            boundary.add(node)
        if node.right is not None:
            node = node.right
        else:
            node = node.left
    ans = 0

    def calculate(node):
        nonlocal ans
        if node is None:
            return
        if node not in boundary:
            ans += node.data
        calculate(node.left)
        calculate(node.right)
    calculate(root)
    return ans
    
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

t=int(input())
while t>0:
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    ans=exceptBoundary(root)
    print(ans)
    t-=1
