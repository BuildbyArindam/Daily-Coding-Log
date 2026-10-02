"""
Problem   : Deepest Leaves Sum
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381520?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, DFS, Recursion
Date      : 2026-10-02

Approach:
    Single DFS pass that carries the current depth. At each leaf, compare its
    depth with the deepest seen so far:
      - deeper leaf  -> reset the sum to this leaf's value
      - same depth   -> add the leaf's value to the sum
      - shallower    -> ignore
    The deepest level's nodes are always leaves, so tracking leaves alone is
    enough.

Complexity:
    Time  : O(N), each node is visited once
    Space : O(H) recursion stack, where H is the tree height
            (O(N) worst case for a skewed tree, O(log N) for a balanced one)
"""


# ----------------------------------------- Solution -------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def deepestLeavesSum(root):
    if root is None:
        return 0
    maxDepth = -1
    ans = 0
    def dfs(node, depth):
        nonlocal maxDepth, ans
        if node is None:
            return
        if node.left is None and node.right is None:
            if depth > maxDepth:
                maxDepth = depth
                ans = node.data
            elif depth == maxDepth:
                ans += node.data
            return
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)
    dfs(root, 0)
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
            currentNode.right = rightNode
            q.put(rightNode)
        index += 1
    return root

T = int(stdin.readline().strip())
for i in range(T):
    root = takeInput()
    ans = deepestLeavesSum(root)
    print(ans)
