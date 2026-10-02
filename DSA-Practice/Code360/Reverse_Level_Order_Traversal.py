"""
Problem   : Reverse Level Order Traversal
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380977?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, BFS, Queue
Date      : 2026-10-02

Approach:
    Run a standard level-order (BFS) traversal using a list as a queue with a
    moving front pointer, so each dequeue is O(1) instead of the O(n) cost of
    list.pop(0). Collect node values in visit order, then reverse the result.

Complexity:
    Time  : O(N), each node is visited once, plus one O(N) reverse
    Space : O(N), the queue and result list each hold up to N nodes
"""


# ------------------------------------- Solution --------------------------------------------


class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    # Write your code here.
    if root is None:
        return []
    queue = [root]
    result = []
    front = 0
    while front < len(queue):
        node = queue[front]
        front += 1
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    result.reverse()
    return result
