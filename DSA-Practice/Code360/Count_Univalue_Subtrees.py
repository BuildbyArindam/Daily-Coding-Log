"""
Problem   : Count Univalue Subtrees
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381521?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, DFS, Recursion
Date      : 02-Oct-2026

Approach:
    Post-order DFS. Each call returns True if the subtree rooted at that node
    is a univalue subtree. A node qualifies when:
      1. both child subtrees are univalue (or empty), and
      2. each existing child has the same value as the node.
    Every qualifying node increments a shared counter. Empty nodes count as
    univalue, so they never block their parent.

Complexity:
    Time  : O(N)  - each node is visited exactly once.
    Space : O(H)  - recursion stack, where H is the tree height
                    (O(N) for a skewed tree, O(log N) for a balanced one).
"""


# ----------------------------------- Solution -----------------------------------------------------------


import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def countUnivalTrees(root):
    count = 0
    def dfs(node):
        nonlocal count
        if node is None:
            return True
        left_unival = dfs(node.left)
        right_unival = dfs(node.right)
        if (left_unival and right_unival and
            (node.left is None or node.left.data == node.data) and
            (node.right is None or node.right.data == node.data)):
            count += 1
            return True
        return False
    dfs(root)
    return count

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
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
    root = buildLevelTree(li)
    print(countUnivalTrees(root))
    t = t - 1
