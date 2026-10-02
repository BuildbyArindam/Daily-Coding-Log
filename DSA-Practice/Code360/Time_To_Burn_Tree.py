"""
Problem   : Time To Burn Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381530?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Hard
Topics    : Binary Tree, BFS, Hashing (parent map)
Date      : 2026-10-02

Approach:
  1. BFS from the root to build a parent map and locate the start node.
  2. BFS outward from the start node level by level, burning the left child,
     right child and parent (unvisited only) at each step.
  3. Each level that burns at least one new node adds 1 minute. The final
     count is the time to burn the whole tree.

Time Complexity : O(N), each node is enqueued at most twice (once per BFS).
Space Complexity: O(N), parent map, visited set and queues.
"""


# --------------------------------------- Solution ---------------------------------------------------------


from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)

class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

def timeToBurnTree(root, start):
    if root is None:
        return 0
    parent = {}
    startNode = None
    q = Queue()
    q.put(root)
    parent[root] = None
    while not q.empty():
        current = q.get()
        if current.data == start:
            startNode = current
        if current.left is not None:
            parent[current.left] = current
            q.put(current.left)
        if current.right is not None:
            parent[current.right] = current
            q.put(current.right)
    visited = set()
    burnQueue = Queue()
    burnQueue.put(startNode)
    visited.add(startNode)
    time = 0
    while not burnQueue.empty():
        size = burnQueue.qsize()
        burned_new_node = False
        for _ in range(size):
            current = burnQueue.get()
            if current.left is not None and current.left not in visited:
                visited.add(current.left)
                burnQueue.put(current.left)
                burned_new_node = True
            if current.right is not None and current.right not in visited:
                visited.add(current.right)
                burnQueue.put(current.right)
                burned_new_node = True
            if parent[current] is not None and parent[current] not in visited:
                visited.add(parent[current])
                burnQueue.put(parent[current])
                burned_new_node = True
        if burned_new_node:
            time += 1
    return time

def takeInput() :
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]
    n = len(arr)
    if(rootData == -1) :
        start = int(input().strip())
        return None, start
    root = BinaryTreeNode(rootData)
    q = Queue()
    q.put(root)
    index = 1
    while(q.qsize() > 0) :
        currentNode = q.get()  
        leftChild = arr[index]
        if(leftChild != -1) :
            leftNode =  BinaryTreeNode(leftChild)  
            currentNode.left = leftNode  
            q.put(leftNode)  
        index += 1
        rightChild = arr[index]
        if(rightChild != -1) :
            rightNode = BinaryTreeNode(rightChild)
            currentNode .right = rightNode  
            q.put(rightNode)  
        index += 1
    start = int(input().strip())
    return root, start

root, start = takeInput()
print(timeToBurnTree(root, start))
