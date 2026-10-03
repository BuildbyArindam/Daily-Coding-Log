"""
Problem   : Normal BST To Balanced BST
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381325?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Search Tree, Inorder Traversal, Divide and Conquer, Recursion
Date      : 2026-10-03

Approach:
    1. Run an inorder traversal of the BST. This yields the node values in
       sorted order.
    2. Rebuild the tree recursively from the sorted list. Pick the middle
       element as the root, then build the left subtree from the left half
       and the right subtree from the right half. Splitting at the middle
       keeps the subtree sizes within 1 of each other, so the height is
       O(log n).

Complexity:
    Time  : O(n) - one pass for inorder, one pass to rebuild.
    Space : O(n) - inorder list plus the new tree. Recursion stack is
            O(h) for the rebuild (O(log n)) and up to O(n) for the inorder
            pass on a skewed input tree.
"""


# --------------------------------------- Solution -------------------------------------------------


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
    inorder = []
    def store_inorder(node):
        if node is None:
            return
        store_inorder(node.left)
        inorder.append(node.data)
        store_inorder(node.right)
    store_inorder(root)

    def build_balanced(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        new_node = TreeNode(inorder[mid])
        new_node.left = build_balanced(left, mid - 1)
        new_node.right = build_balanced(mid + 1, right)
        return new_node
    return build_balanced(0, len(inorder) - 1)
