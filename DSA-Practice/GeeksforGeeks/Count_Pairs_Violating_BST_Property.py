"""
Problem   : Count Pairs Violating BST Property
Platform  : GeeksforGeeks 
Link      : https://www.geeksforgeeks.org/problems/pairs-violating-bst-property--212515/1
Date      : 2026-10-23
Difficulty: Medium
Topics    : Binary Search Tree, Merge Sort, Traversal

Approach  : The inorder traversal of a valid BST is sorted, so a pair (i, j)
            violates the BST property exactly when i < j and inorder[i] > inorder[j].
            That makes the answer the inversion count of the inorder array.
            1. Iterative inorder traversal to flatten the tree.
            2. Rank-compress the values (sorted order -> ranks 1..n).
            3. Scan right to left with a Fenwick tree (BIT): for each element,
               query how many smaller ranks are already inserted (these are the
               inversions it forms), then insert its rank.

Time      : O(n log n)  (sorting + n BIT queries/updates)
Space     : O(n)        (inorder list, rank map, BIT, traversal stack)
"""


# ----------------------------------------------- Solution ---------------------------------------------------------


''' BST Node Structure
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def pairsViolatingBST(self, root):
        # code here
        if root is None:
            return 0
        flat = []
        path = []
        node = root
        while path or node is not None:
            if node is not None:
                path.append(node)
                node = node.left
                continue
            node = path.pop()
            flat.append(node.data)
            node = node.right
        size = len(flat)
        order = sorted(flat)
        pos = dict(zip(order, range(1, size + 1)))
        fen = [0] * (size + 1)
        answer = 0
        idx = size - 1
        while idx >= 0:
            k = pos[flat[idx]]
            j = k - 1
            while j:
                answer += fen[j]
                j &= j - 1
            j = k
            while j <= size:
                fen[j] += 1
                j += j & (-j)
            idx -= 1
        return answer
