'''
Problem: Minimum Absolute Difference In BST
Link: https://www.geeksforgeeks.org/problems/minimum-absolute-difference-in-bst-1665139652/1
Platform: GeeksforGeeks | Difficulty: Medium | Topic: Binary Search Tree
Date: 2026-09-18

Approach:
Iterative in-order traversal using an explicit stack. Since an in-order
traversal of a BST visits nodes in sorted order, the minimum absolute
difference between any two node values must occur between some pair of
consecutive nodes in that traversal. Track the previously visited node's
value and update the running minimum difference as each new node is visited.

Time Complexity: O(N) — each node is pushed/popped exactly once
Space Complexity: O(H) — H = height of the tree, for the stack
                          (O(N) worst case for a skewed tree)
'''


# ---------------------------------- Solution -----------------------------------------


'''
Binary Tree Node Structure
class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
'''

class Solution:
    def absDiff(self, root):
        stack = []
        curr = root
        prev = None
        min_diff = float('inf')
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if prev is not None:
                min_diff = min(min_diff, curr.data - prev)
            prev = curr.data
            curr = curr.right
        return min_diff
