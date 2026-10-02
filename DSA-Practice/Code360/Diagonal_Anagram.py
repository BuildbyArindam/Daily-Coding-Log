"""
Problem   : Diagonal Anagram
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380978?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, Hash Map, Diagonal Traversal, DFS
Date      : 2026-10-02

Approach:
    Two trees are diagonal anagrams if, for every diagonal index, both trees
    hold the same multiset of values. Traverse each tree iteratively with a
    stack, where a right child stays on the same diagonal and a left child
    moves to the next one (diagonal + 1). Build one frequency map per diagonal,
    then compare the two lists of maps. Differing diagonal counts means False.

Complexity:
    Time  : O(N1 + N2). Each node is visited once, and dict comparison is
            bounded by the number of distinct values.
    Space : O(N1 + N2) for the frequency maps, plus O(H) for the stack.
"""


# ----------------------------------- Solution -------------------------------------------------


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diagonalAnagram(root1, root2):
    def get_diagonals(root):
        diagonals = []
        if root is None:
            return diagonals
        stack = [(root, 0)]
        while stack:
            node, diagonal = stack.pop()
            while len(diagonals) <= diagonal:
                diagonals.append({})
            freq = diagonals[diagonal]
            freq[node.data] = freq.get(node.data, 0) + 1
            if node.right is not None:
                stack.append((node.right, diagonal))
            if node.left is not None:
                stack.append((node.left, diagonal + 1))
        return diagonals
    diagonals1 = get_diagonals(root1)
    diagonals2 = get_diagonals(root2)
    if len(diagonals1) != len(diagonals2):
        return False
    for d1, d2 in zip(diagonals1, diagonals2):
        if d1 != d2:
            return False
    return True
