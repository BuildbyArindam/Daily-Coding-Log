"""
Problem   : LCA of three Nodes
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381011?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, BFS, Hash Map, LCA
Date      : 2026-10-02

Approach:
  1. BFS from the root to build a parent map (node value -> parent value).
  2. LCA of two nodes: store all ancestors of `a` in a set, then walk up
     from `b` until hitting a node in that set.
  3. LCA of three nodes = LCA(LCA(node1, node2), node3).

Complexity:
  Time  : O(N) - one BFS plus at most O(H) ancestor walks, with H <= N
  Space : O(N) - parent map, BFS queue and ancestor set

Assumption: node values are unique (they are used as dictionary keys).
"""


# ------------------------------------- Solution -----------------------------------------------


import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def lcaOfThreeNodes(root, node1, node2, node3):
    parent = {root.data: None}
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current = q.get()
        if current.left is not None:
            parent[current.left.data] = current.data
            q.put(current.left)
        if current.right is not None:
            parent[current.right.data] = current.data
            q.put(current.right)
    
    def lca_two_nodes(a, b):
        ancestors = set()
        while a is not None:
            ancestors.add(a)
            a = parent[a]
        while b not in ancestors:
            b = parent[b]
        return b
    lca12 = lca_two_nodes(node1, node2)
    return lca_two_nodes(lca12, node3)

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
t = int(input())
while t > 0:
    arr = [int(i) for i in input().split()][:3]
    li = [int(i) for i in input().split()]
    root = buildLevelTree(li)
    print(lcaOfThreeNodes(root, arr[0], arr[1], arr[2]))
    t = t - 1
