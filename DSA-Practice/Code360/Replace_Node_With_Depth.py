"""
Problem   : Replace Node With Depth
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381523
Difficulty: Easy
Topics    : Binary Tree, DFS, Recursion
Date      : 2026-10-02

Approach:
    Do a preorder DFS from the root, passing the current depth down as an
    argument. Each node's data is overwritten with its depth (root = 0), and
    the children are visited with depth + 1. The tree is modified in place.

Complexity:
    Time  : O(N), each node is visited exactly once.
    Space : O(H) recursion stack, where H is the tree height
            (O(log N) balanced, O(N) skewed).
"""


# ---------------------------------- Solution -------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def changeToDepthTree(root):
    def change(node, depth):
        if node is None:
            return
        node.data = depth
        change(node.left, depth + 1)
        change(node.right, depth + 1)
    change(root, 0)

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

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
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

t = int(input())
while t > 0:
    levelOrder = [int(i) for i in input().strip().split()]
    root = buildLevelTree(levelOrder)
    changeToDepthTree(root)
    inorder(root)
    print()
    t = t - 1
