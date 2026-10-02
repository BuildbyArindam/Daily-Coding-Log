"""
Problem   : Top View Of Binary Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381006
Difficulty: Medium
Topics    : Binary Tree, BFS (Level Order), Hashing, Horizontal Distance
Date      : 02-Oct-2026

Approach:
    Assign each node a horizontal distance (hd): root = 0, left child = hd - 1,
    right child = hd + 1. Traverse level by level (BFS) so that the first node
    seen at each hd is the topmost one. Store only that first node per hd in a
    dict, then read the values in sorted hd order (left to right).

Time Complexity : O(N + W log W), where W is the number of distinct hds
                  (W <= N, so O(N log N) worst case on a skewed tree)
Space Complexity: O(N) for the queue and the hd map
"""


# ---------------------------------------- Solution ------------------------------------------------------


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

def getTopView(root):
    top_view = {}
    if root is None:
        return []
    q = Queue()
    q.put((root, 0))
    while q.qsize() > 0:
        currentNode, hd = q.get()
        if hd not in top_view:
            top_view[hd] = currentNode.val
        if currentNode.left is not None:
            q.put((currentNode.left, hd - 1))
        if currentNode.right is not None:
            q.put((currentNode.right, hd + 1))
    ans = []
    for hd in sorted(top_view.keys()):
        ans.append(top_view[hd])
    return ans

def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]
    n = len(arr)
    if(rootData == -1):
        return None
    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()
        leftChild = arr[index]
        if(leftChild != -1):
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        index += 1
        rightChild = arr[index]
        if(rightChild != -1):
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode
            q.put(rightNode)
        index += 1
    return root

def printAns(ans):
    for x in ans:
        print(x, end=" ")
    print()

T = 1
for i in range(T):
    root = takeInput()
    ans = getTopView(root)
    printAns(ans)
