"""
Problem   : Bottom View Of Binary Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381009?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, BFS, Hashing
Date      : 2026-10-02

Approach:
    Level-order traversal (BFS) while tracking each node's horizontal
    distance (hd) from the root: left child = hd - 1, right child = hd + 1.
    For every hd, keep the most recently visited node. BFS visits nodes
    top to bottom, so the last node seen at an hd is the bottom-most one.
    Within the same depth, the later (right-side) node wins. Finally, read
    the values in increasing hd order (left to right).

Time Complexity : O(N log N) -- BFS is O(N), sorting the hd keys is O(K log K), K <= N
Space Complexity: O(N) -- queue and hd map
"""


# ---------------------------------------- Solution -----------------------------------------------------------


from typing import List
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    if root is None:
        return []
    nodes = {}
    from collections import deque
    q = deque()
    q.append((root, 0, 0))
    while q:
        node, hd, depth = q.popleft()
        if hd not in nodes or depth >= nodes[hd][0]:
            nodes[hd] = (depth, node.data)
        if node.left:
            q.append((node.left, hd - 1, depth + 1))
        if node.right:
            q.append((node.right, hd + 1, depth + 1))
    return [nodes[hd][1] for hd in sorted(nodes)]
