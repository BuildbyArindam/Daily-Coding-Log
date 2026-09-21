"""
Problem: Check Level Anagrams in Binary Trees
Link: https://www.geeksforgeeks.org/problems/check-if-all-levels-of-two-trees-are-anagrams-or-not/1
Platform: GeeksforGeeks
Difficulty: Medium
Topic: Tree
Date Solved: 2026-09-21

Approach:
Level-order (BFS) traversal of both trees in lockstep, using two queues.
At each level, collect node values into a Counter for each tree and compare
the two Counters — if they match, the level is an anagram of the other.
Fail fast if level sizes differ or any level's frequency counts don't match.
Trees are considered anagrams overall if all levels match and both queues
empty out simultaneously (same height).

Time Complexity: O(n) — each node visited once across both trees
Space Complexity: O(w) — w = max nodes at any single level (queue + Counter size)
"""


# ------------------------------------ Solution ----------------------------------------


"""
Structure of binary tree Node
class Node:
    def __init__(self, x: int):
        self.data = x
        self.left = self.right = None
"""
from collections import deque, Counter

class Solution:

    def areAnagrams(self, root1, root2):
        """ code here """
        if root1 is None or root2 is None:
            return root1 is root2
        q1 = deque([root1])
        q2 = deque([root2])
        while q1 and q2:
            n1 = len(q1)
            n2 = len(q2)
            if n1 != n2:
                return False
            freq1 = Counter()
            freq2 = Counter()
            for _ in range(n1):
                node = q1.popleft()
                freq1[node.data] += 1
                if node.left:
                    q1.append(node.left)
                if node.right:
                    q1.append(node.right)
            for _ in range(n2):
                node = q2.popleft()
                freq2[node.data] += 1
                if node.left:
                    q2.append(node.left)
                if node.right:
                    q2.append(node.right)
            if freq1 != freq2:
                return False
        return not q1 and not q2
