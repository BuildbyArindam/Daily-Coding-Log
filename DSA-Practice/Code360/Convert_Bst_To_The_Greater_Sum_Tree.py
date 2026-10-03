"""
Problem   : Convert BST To The Greater Sum Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381330?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Reverse Inorder Traversal, Recursion
Date      : 2026-10-03

Approach:
    In a BST, an inorder traversal visits nodes in ascending order, so a
    reverse inorder traversal (right -> node -> left) visits them in
    descending order. Keep a running `total` of all values seen so far.
    At each node, save its old value, set node.val = total (the sum of all
    strictly greater keys), then add the old value to `total`.
    The tree is modified in place in a single pass.

Complexity:
    Time  : O(N), each node is visited exactly once.
    Space : O(H) recursion stack, where H is the tree height
            (O(log N) balanced, O(N) for a skewed tree).
"""


# ------------------------------------- Solution -----------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from sys import stdin, setrecursionlimit
from queue import Queue
setrecursionlimit(10**7)

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def convertBstToGreaterSum(root):
    total = 0
    def reverse_inorder(node):
        nonlocal total
        if node is None:
            return
        reverse_inorder(node.right)
        old_value = node.val
        node.val = total
        total += old_value
        reverse_inorder(node.left)
    reverse_inorder(root)
    return root

def takeInput():
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]
    n = len(arr)
    if(rootData == -1):
        return None
    root = TreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0):
        currentNode = q.get()
        leftChild = arr[index]
        if(leftChild != -1):
            leftNode = TreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        index += 1
        rightChild = arr[index]
        if(rightChild != -1):
            rightNode = TreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
        index += 1
    return root

def printLevelOrder(root):
    q = Queue()
    if(root == None):
        return
    q.put(root)
    while(q.qsize() > 0):
        currentNode = q.get()
        print(currentNode.val, end=" ")
        if(currentNode.left != None):
            q.put(currentNode.left)
        if(currentNode.right != None):
            q.put(currentNode.right)
    print()

t = int(input().strip())
for i in range(t):
    root = takeInput()
    bstToGreaterSum = convertBstToGreaterSum(root)
    printLevelOrder(bstToGreaterSum)
