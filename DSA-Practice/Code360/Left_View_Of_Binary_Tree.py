"""
Problem   : Left View Of Binary Tree
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381007?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, BFS, Level Order Traversal
Date      : 2026-10-02

Approach:
    Level-order traversal (BFS) using a list as a queue with a moving
    `front` pointer, so there are no O(n) pop(0) calls. At the start of each
    level, the node at `front` is the leftmost node, so print it. Then
    process exactly `level_size` nodes, enqueueing their children for the
    next level.

Complexity:
    Time : O(N), each node is visited once.
    Space: O(N), the list keeps every node because nothing is popped.
           A deque would reduce this to O(W), where W is the max level width.
"""


# --------------------------------------- Solution --------------------------------------------


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def leftView(root: BinaryTreeNode) -> None:
    if root is None:
        return
    queue = [root]
    front = 0
    while front < len(queue):
        level_size = len(queue) - front
        node = queue[front]
        if hasattr(node, 'data'):
            print(node.data, end=' ')
        else:
            print(node.val, end=' ')
        for i in range(level_size):
            node = queue[front]
            front += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
