"""
Problem   : Remove Keys Outside Range
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381328
Difficulty: Medium
Topics    : Binary Search Tree, Recursion, Trees
Date      : 2026-10-03

Approach:
    Use the BST property to prune recursively:
      - If root.data < min, the node and its entire left subtree are out of
        range, so the answer is the trimmed right subtree.
      - If root.data > max, the node and its entire right subtree are out of
        range, so the answer is the trimmed left subtree.
      - Otherwise the node is valid: trim both children and reattach them.

Complexity:
    Time  : O(N) worst case. Whole subtrees are skipped, but in the worst
            case every node is visited once.
    Space : O(H) recursion stack, where H is the tree height
            (O(log N) balanced, O(N) skewed).
"""


# -------------------------------------- Solution -----------------------------------------------------------


''' 
Following is the Binary Tree node structure

class BinaryTreeNode:

    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
'''

def removeOutsideRange(root, min, max):
    if root is None:
        return None
    if root.data < min:
        return removeOutsideRange(root.right, min, max)
    if root.data > max:
        return removeOutsideRange(root.left, min, max)
    root.left = removeOutsideRange(root.left, min, max)
    root.right = removeOutsideRange(root.right, min, max)
    return root
