"""
Problem   : Largest BST in Binary Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/largest-bst_624686
Date      : 2026-09-04
Difficulty: Hard
Topics    : Binary Tree, BST Validation, Post-order Traversal, DFS (Iterative)

Approach:
Build the tree from level-order input, then do an iterative post-order
traversal using an explicit stack (state 0 = expand children, state 1 =
process node) to avoid recursion depth issues on large trees. For each
node, combine the (is_bst, min, max, height) info of its children:
a node roots a valid BST iff both subtrees are valid BSTs and
left_max < node.data < right_min. Track the max height seen among
valid BST roots as the answer (height in "number of nodes" terms since
leaves start at height 1... actually here height counts levels, matching
node count along the path — confirm against problem's expected output
convention before submitting if it asks for node count vs height).

Time Complexity : O(n) — each node visited once during traversal
Space Complexity: O(n) — recursion stack replacement (explicit stack)
                  + info dict storing per-node (is_bst, min, max, height)
"""


# ------------------------- Solution -------------------------------


import queue
import sys

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

def largestBSTSubtree(root):
    if root is None:
        return 0
    stack = [(root, 0)]
    info = {}
    answer = 0
    while stack:
        node, state = stack.pop()
        if state == 0:
            stack.append((node, 1))
            if node.right is not None:
                stack.append((node.right, 0))
            if node.left is not None:
                stack.append((node.left, 0))
        else:
            if node.left is None:
                left_is_bst = True
                left_min = float('inf')
                left_max = float('-inf')
                left_height = 0
            else:
                left_is_bst, left_min, left_max, left_height = info[node.left]
            if node.right is None:
                right_is_bst = True
                right_min = float('inf')
                right_max = float('-inf')
                right_height = 0
            else:
                right_is_bst, right_min, right_max, right_height = info[node.right]
            if (left_is_bst and right_is_bst and
                    left_max < node.data < right_min):
                current_height = max(left_height, right_height) + 1
                current_min = min(left_min, node.data)
                current_max = max(right_max, node.data)
                info[node] = (
                    True,
                    current_min,
                    current_max,
                    current_height
                )
                answer = max(answer, current_height)
            else:
                info[node] = (
                    False,
                    float('-inf'),
                    float('inf'),
                    0
                )
    return answer
sys.setrecursionlimit(10**6)
levelOrder = [int(i) for i in input().split()]
root = buildLevelTree(levelOrder)
print(largestBSTSubtree(root))
