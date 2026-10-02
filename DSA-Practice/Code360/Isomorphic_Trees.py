"""
Problem   : Isomorphic Trees
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381525?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, Recursion, DFS
Date      : 2026-10-02

Approach:
    Two trees are isomorphic if one can be turned into the other by swapping
    the left and right children of any number of nodes. Recursively:
      - both nodes None -> True; exactly one None -> False
      - data differs -> False
      - otherwise the trees are isomorphic if either
          (a) left~left and right~right (no swap), or
          (b) left~right and right~left (swap at this node)

Complexity:
    Time  : O(N^2) worst case (each call branches into up to 4 sub-calls,
            e.g. balanced trees); O(N) when no swaps are needed or
            mismatches are found early. Tree building is O(N).
    Space : O(H) recursion stack, where H is the tree height
            (O(N) for a skewed tree).
"""


# ----------------------------------- Solution ------------------------------------------------


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
        
def isIsomorphic(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    if t1.data != t2.data:
        return False
    same = isIsomorphic(t1.left, t2.left) and \
           isIsomorphic(t1.right, t2.right)
    swapped = isIsomorphic(t1.left, t2.right) and \
              isIsomorphic(t1.right, t2.left)
    return same or swapped

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
    
t = int(input())
while t > 0:
    li = [int(i) for i in input().split()]
    t1 = buildLevelTree(li)
    li2 = [int(i) for i in input().split()]
    t2 = buildLevelTree(li2)
    if isIsomorphic(t1, t2):
        print('yes')
    else:
        print('no')
    t = t - 1
