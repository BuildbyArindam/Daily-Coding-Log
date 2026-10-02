"""
Problem   : Sum Tree
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381522?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Date      : 2026-10-02
Difficulty: Medium
Topics    : Binary Tree, Preorder Traversal, Stack

Approach:
    Iterative preorder traversal with an explicit stack. Each node is
    processed before its children, so the children still hold their original
    values when the parent reads them. Each node's data is replaced by the sum
    of its left and right child values (0 for a missing child, so leaves become 0).
    The updated value is appended to the result as the node is visited.
    Right is pushed before left so the left subtree is processed first.

Complexity:
    Time  : O(N), each node is visited once.
    Space : O(N), the output list holds N values; the stack itself is O(H).
"""


# ------------------------------------- Solution -----------------------------------------------


''' 
    Following is the Binary Tree node structure

class BinaryTreeNode :

	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

'''

def sumTree(root) :
    if root is None:
        return []
    preorder = []
    stack = [root]
    while stack:
        node = stack.pop()
        left_sum = node.left.data if node.left is not None else 0
        right_sum = node.right.data if node.right is not None else 0
        node.data = left_sum + right_sum
        preorder.append(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return preorder
