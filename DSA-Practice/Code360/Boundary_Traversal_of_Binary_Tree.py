"""
Problem   : Boundary Traversal of Binary Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380976
Difficulty: Hard
Topics    : Binary Tree, Tree Traversal, DFS
Date      : 02-Oct-2026

Approach:
    The boundary is built in three parts, in anti-clockwise order:
      1. Left boundary: walk down from root.left, preferring the left child
         and falling back to the right. Skip leaves.
      2. Leaves: recursive left-to-right DFS that collects every leaf.
      3. Right boundary: walk down from root.right, preferring the right
         child and falling back to the left. Skip leaves, collect into a
         temp list, then append it reversed (bottom-up).
    If the root itself is a leaf, return [root.data] directly.
    Leaves are excluded from parts 1 and 3 so they are never duplicated.

Time Complexity : O(N), each node is visited a constant number of times
Space Complexity: O(N), O(H) recursion stack for leaves plus the output list
                  (N = number of nodes, H = height of the tree)
"""


# ------------------------------------- Solution ---------------------------------------------


# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def traverseBoundary(root):
    # Write your code here.
    if root is None:
        return []
    ans = []
    def isLeaf(node):
        return node.left is None and node.right is None
    def addLeftBoundary(node):
        curr = node.left
        while curr:
            if not isLeaf(curr):
                ans.append(curr.data)
            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    def addLeaves(node):
        if node is None:
            return
        if isLeaf(node):
            ans.append(node.data)
            return
        addLeaves(node.left)
        addLeaves(node.right)
    def addRightBoundary(node):
        temp = []
        curr = node.right
        while curr:
            if not isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left
        ans.extend(temp[::-1])
    if not isLeaf(root):
        ans.append(root.data)
    else:
        return [root.data]
    addLeftBoundary(root)
    addLeaves(root)
    addRightBoundary(root)
    return ans
