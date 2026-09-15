"""
Problem: Visit Leaves with Budget
Platform: GeeksforGeeks
Link: https://www.geeksforgeeks.org/problems/leaf-under-budget/1
Difficulty: Easy
Topic: Tree
Date Solved: 2026-09-15

Approach:
Iterative DFS (stack) to find every leaf and bucket leaf counts by depth
level. Then greedily consume the budget k starting from the shallowest
level: since all leaves have equal value (1) and cost equal to their
level, taking as many cheap (shallow) leaves as possible before
expensive (deep) ones always maximizes the total count for a fixed
budget - so level-ascending greedy is optimal here.

Time Complexity: O(n + k)  -> O(n) to traverse the tree, O(k) for the
                              greedy pass over levels.
Space Complexity: O(n + k) -> O(h) to O(n) for the DFS stack in the
                              worst case, plus O(k) for the count array.
"""


# ---------------------------------- Solution ------------------------------------------


''' Binary Tree Node Structure
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def getCount(self, root, k):
        # code here
        if root is None:
            return 0
        count = [0] * (k + 1)
        stack = [(root, 1)]
        while stack:
            node, level = stack.pop()
            if node.left is None and node.right is None:
                if level <= k:
                    count[level] += 1
                continue
            if node.left is not None:
                stack.append((node.left, level + 1))
            if node.right is not None:
                stack.append((node.right, level + 1))
        answer = 0
        for level in range(1, k + 1):
            if count[level] == 0:
                continue
            can_take = min(count[level], k // level)
            answer += can_take
            k -= can_take * level
            if k == 0:
                break
        return answer
