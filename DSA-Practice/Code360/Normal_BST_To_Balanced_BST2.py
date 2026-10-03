"""
Problem   : Normal BST To Balanced BST
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381326?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Tree, Inorder Traversal, Divide and Conquer, Recursion
Date      : 2026-10-03

Approach:
    1. Inorder traversal of a BST yields values in sorted order, so collect
       them into an array.
    2. Rebuild the tree recursively: pick the middle element as the root,
       then build the left subtree from the left half and the right subtree
       from the right half. Picking the middle at every level keeps the
       height at O(log n).

Time Complexity : O(n)  - one traversal plus one node creation per element.
Space Complexity: O(n)  - array of values plus the new tree; recursion stack
                          is O(h) for the traversal and O(log n) for the build.
"""


# -------------------------------------- Solution --------------------------------------------------------


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def balancedBst(root):
    arr = []
    def inorder(node):
        if node is None:
            return
        inorder(node.left)
        arr.append(node.data)
        inorder(node.right)
    inorder(root)

    def buildBalanced(start, end):
        if start > end:
            return None
        mid = (start + end) // 2
        new_node = TreeNode(arr[mid])
        new_node.left = buildBalanced(start, mid - 1)
        new_node.right = buildBalanced(mid + 1, end)
        return new_node
    return buildBalanced(0, len(arr) - 1)
