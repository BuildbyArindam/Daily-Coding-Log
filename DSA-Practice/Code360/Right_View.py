"""
Problem   : Right View
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381008?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, BFS, Level Order Traversal
Date      : 2026-10-02

Approach:
    Level-order traversal (BFS) with a queue. At each level, process exactly
    `level_size` nodes. The last node dequeued at that level is the rightmost
    one visible from the right side, so its value goes into the answer.

Complexity:
    Time  : O(N), each node is visited once.
    Space : O(W), where W is the maximum width of the tree (queue size).
            O(N) in the worst case.
"""


# ---------------------------------------- Solution -------------------------------------------------------


class BinaryTreeNode:    
    def __init__ (self,data):
        self.data=data
        self.left=None
        self.right=None    

def printRightView(root):
    # Write your code here.
    if root is None:
        return []
    from collections import deque
    queue = deque([root])
    ans = []
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                ans.append(node.data)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return ans
