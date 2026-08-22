'''
Problem: Number of Turns in Binary Tree
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/number-of-turns-in-binary-tree/1
Difficulty: Hard
Topic: Tree
Date: 2026-08-22

Approach:
Find root-to-node paths for both p and q as direction sequences ('L'/'R').
Strip the common prefix (up to and including the LCA), reverse p's remaining
path (since we travel *up* from p to the LCA) and append q's remaining path
(travelling *down* to q). Count direction changes ('L'->'R' or 'R'->'L')
in this combined sequence — each change is a turn.

Time Complexity: O(N) — two O(N) tree traversals to build the paths, plus
                  O(N) to compare/count turns.
Space Complexity: O(N) — recursion stack + path lists in the worst case
                  (skewed tree).
'''


# ---------------------------- Solution ----------------------------------


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def numberOfTurns(self, root, p, q):
        def find_path(node, target, path):
            if node is None:
                return False
            if node.data == target:
                return True
            path.append('L')
            if find_path(node.left, target, path):
                return True
            path.pop()
            path.append('R')
            if find_path(node.right, target, path):
                return True
            path.pop()
            return False

        path_p = []
        path_q = []
        find_path(root, p, path_p)
        find_path(root, q, path_q)

        i = 0
        while i < len(path_p) and i < len(path_q) and path_p[i] == path_q[i]:
            i += 1

        directions = path_p[i:][::-1] + path_q[i:]
        turns = 0
        for j in range(1, len(directions)):
            if directions[j] != directions[j - 1]:
                turns += 1

        return turns if turns > 0 else -1
