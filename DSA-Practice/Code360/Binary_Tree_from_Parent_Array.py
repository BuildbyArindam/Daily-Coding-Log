"""
Problem   : Binary Tree from Parent Array
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380997
Difficulty: Easy
Topics    : Binary Tree, Arrays, Level-Order Traversal (BFS)
Date      : 2026-10-02

Approach:
  1. Create one node per index i (the node's value is i).
  2. Use parent[i] to build a children list for every node; parent[i] == -1 marks the root.
  3. For each node, attach its children in ascending index order (smaller index -> left, larger -> right).
  4. Print the tree in level order, using -1 for missing children.

Time Complexity : O(n) to build the tree. The level-order print is O(n) with a deque (see note below).
Space Complexity: O(n) for the nodes, the children lists and the BFS queue.
"""


# -------------------------------------- Solution ---------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin

class BinaryTreeNode:
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None    

def createTree(parent):
    n = len(parent)
    nodes = [BinaryTreeNode(i) for i in range(n)]
    root = None
    children = [[] for _ in range(n)]
    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        else:
            children[parent[i]].append(i)
    for i in range(n):
        if len(children[i]) == 1:
            nodes[i].left = nodes[children[i][0]]
        elif len(children[i]) == 2:
            if children[i][0] < children[i][1]:
                nodes[i].left = nodes[children[i][0]]
                nodes[i].right = nodes[children[i][1]]
            else:
                nodes[i].left = nodes[children[i][1]]
                nodes[i].right = nodes[children[i][0]]
    return root

def printLevelorder(root):
    pendingNodes = []
    if root is None:
        print(-1)
        return 
    sb = []
    sb.append(root.data)
    pendingNodes.append(root)
    while (len(pendingNodes)>0):
        currentNode = pendingNodes.pop(0)
        if currentNode.left != None:
            sb.append(currentNode.left.data)
            pendingNodes.append(currentNode.left)
        else:
            sb.append(-1)
        if currentNode.right != None:
            sb.append(currentNode.right.data)
            pendingNodes.append(currentNode.right)
        else:
            sb.append(-1)
    print(*sb)

t = int(stdin.readline().rstrip())
while t>0:
    n = int(stdin.readline().rstrip())
    parent = list(map(int, stdin.readline().rstrip().split(" ")))
    root = createTree(parent)
    printLevelorder(root)
    t -= 1
