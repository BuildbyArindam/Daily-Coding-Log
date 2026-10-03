"""
Problem   : Construct BST from Level Order
Platform  : Code360
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381317
Difficulty: Easy
Topics    : Binary Search Tree, Queue, BFS, Tree Construction
Date      : 2026-10-03

Approach:
    Process the level-order values in sequence while keeping a queue of open
    child slots. Each slot is (parent, side, low, high), where (low, high) is
    the exclusive range a value must fall in to occupy that slot.
    For each value:
      1. Discard slots at the front whose range doesn't contain it (those
         children are null).
      2. Attach the value to the first valid slot.
      3. Push two new slots for the new node: left (low, value) and
         right (value, high).
    Each slot is pushed once and popped once.

Time Complexity : O(n)
Space Complexity: O(n)  -> queue of open slots plus the tree itself
"""


# ------------------------------------- Solution ------------------------------------------------


from sys import *
from collections import *
from math import *

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
def constructBst(levelOrder):
    n = len(levelOrder)
    if n == 0:
        return None
    root = BinaryTreeNode(levelOrder[0])
    q = deque()
    q.append((root, 0, None, root.data))
    q.append((root, 1, root.data, None))
    for i in range(1, n):
        value = levelOrder[i]
        while q:
            parent, side, low, high = q[0]
            if ((low is None or value > low) and
                    (high is None or value < high)):
                break
            q.popleft()
        parent, side, low, high = q.popleft()
        node = BinaryTreeNode(value)
        if side == 0:
            parent.left = node
        else:
            parent.right = node
        q.append((node, 0, low, value))
        q.append((node, 1, value, high))
    return root
