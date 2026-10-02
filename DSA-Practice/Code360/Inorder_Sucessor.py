"""
Problem   : Inorder Successor
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380982
Difficulty: Medium
Date      : 2026-10-02
Topics    : Binary Tree, Inorder Traversal, Stack

Approach:
    Iterative inorder traversal using an explicit stack. Push the left spine,
    pop a node, and visit it. Once the target node is visited, set a flag,
    so the next node popped is its inorder successor. If the target is the
    last node in the inorder sequence, return None (printed as "NULL").
    This works for any binary tree, not just a BST.

Time Complexity : O(N), in the worst case every node is visited once.
Space Complexity: O(H), the stack holds at most one root-to-leaf path
                  (O(N) for a skewed tree).
"""


# ------------------------------------ Solution ------------------------------------------------------------


from sys import stdin
import queue

class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

def inorderSuccesor(root, node):
    stack = []
    curr = root
    found = False
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        if found:
            return curr.data
        if curr.data == node:
            found = True
        curr = curr.right
    return None

def buildTree(arr):
    if len(arr) == 0 or arr[0] == -1:
        return None
    root = BinaryTreeNode(arr[0])
    q = queue.Queue()
    q.put(root)
    i = 0
    while q.empty() is False:
        curr = q.get()
        i = i + 1
        if arr[i] != -1:
            left_Node = BinaryTreeNode(arr[i])
            curr.left = left_Node
            q.put(curr.left)
        i = i + 1
        if arr[i] != -1:
            right_Node = BinaryTreeNode(arr[i])
            curr.right = right_Node
            q.put(curr.right)
    return root

# Main Code.
t = int(input())
for i in range(t):
    arr = [int(i) for i in input().strip().split()]
    node = int(input().strip())
    root = buildTree(arr)
    ans = inorderSuccesor(root, node)
    if ans is None:
        print("NULL")
    else:
        print(ans)
