"""
Problem   : Distance between two nodes of a Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381014
Difficulty: Medium
Topics    : Binary Tree, LCA, DFS, Recursion
Date      : 02-Oct-2026

Approach:
  1. Check that both nodes exist by finding each one's depth from the root
     (return -1 if either is missing).
  2. Find the Lowest Common Ancestor (LCA) of the two nodes with a single DFS.
  3. Measure the depth of each node from the LCA.
     dist(a, b) = depth(a from LCA) + depth(b from LCA)

Time Complexity : O(N) - a constant number of full-tree traversals
Space Complexity: O(H) - recursion stack, where H is the tree height
                  (O(N) for a skewed tree, O(log N) for a balanced one)
"""


# ----------------------------------------- Solution ----------------------------------------------------


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
        
def findDistanceBetweenNodes(root, node1, node2):
    def findLCA(root, a, b):
        if root is None:
            return None
        if root.data == a or root.data == b:
            return root
        leftLCA = findLCA(root.left, a, b)
        rightLCA = findLCA(root.right, a, b)
        if leftLCA is not None and rightLCA is not None:
            return root
        if leftLCA is not None:
            return leftLCA
        return rightLCA

    def findDistance(root, target, distance):
        if root is None:
            return -1
        if root.data == target:
            return distance
        leftDistance = findDistance(root.left, target, distance + 1)
        if leftDistance != -1:
            return leftDistance
        return findDistance(root.right, target, distance + 1)
    dist1_from_root = findDistance(root, node1, 0)
    dist2_from_root = findDistance(root, node2, 0)
    if dist1_from_root == -1 or dist2_from_root == -1:
        return -1
    lca = findLCA(root, node1, node2)
    d1 = findDistance(lca, node1, 0)
    d2 = findDistance(lca, node2, 0)
    return d1 + d2

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
    
def inorder(root):
    if root == None:
        return -1
    li = []
    qq = queue.Queue()
    qq.put(root)
    while not qq.empty():
        cur = qq.get()
        if cur == None:
            li.append(-1)
            continue
        li.append((cur.data))
        qq.put(cur.left)
        qq.put(cur.right)
    return li
    
t = int(sys.stdin.readline().strip())
while t >0:
    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    node = list(map(int, sys.stdin.readline().strip().split(" ")))
    node1 = node[0]
    node2 = node[1]
    print(findDistanceBetweenNodes(root, node1, node2))
    t -= 1
