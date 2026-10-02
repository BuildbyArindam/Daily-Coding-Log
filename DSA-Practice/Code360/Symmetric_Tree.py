'''
Problem    : Symmetric Tree
Platform   : Code360
Link       : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381529?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty : Easy
Topics     : Binary Tree, BFS, Queue
Date       : 2026-10-02

Approach:
    Iterative BFS on mirrored node pairs. Start with (root.left, root.right).
    For each pair: both None -> fine, skip; only one None or values differ -> not
    symmetric. Otherwise enqueue the mirror pairs (left.left, right.right) and
    (left.right, right.left). If the queue empties with no mismatch, the tree is symmetric.

Time Complexity  : O(N), each node is visited once.
Space Complexity : O(W), where W is the maximum width of the tree (O(N) worst case).
'''


# -------------------------------------- Solution -----------------------------------------------


'''
    Following is the representation for the Binary Tree Node:

    class BinaryTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
'''

def isSymmetric(root) :
    if root is None:
        return True
    queue = [(root.left, root.right)]
    while queue:
        left, right = queue.pop(0)
        if left is None and right is None:
            continue
        if left is None or right is None or left.data != right.data:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))
    return True
