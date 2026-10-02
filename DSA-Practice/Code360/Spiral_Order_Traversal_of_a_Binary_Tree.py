"""
Problem   : Spiral Order Traversal of a Binary Tree
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1380979?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Easy
Topics    : Binary Tree, BFS, Level Order Traversal, Queue
Date      : 02-Oct-2026

Approach:
    Run a standard level-order (BFS) traversal using a queue. Process the
    tree one level at a time, using the queue size to know how many nodes
    belong to the current level. Collect each level's values in a list and
    reverse it on every alternate level (right-to-left), flipping a
    direction flag after each level. Append each level to the result.

Time Complexity : O(N) - each node is visited once (reversals total O(N) across levels)
Space Complexity: O(N) - queue holds up to one full level, plus the result list
"""


# ----------------------------------- Solution --------------------------------------------


from sys import stdin,setrecursionlimit
from queue import Queue

setrecursionlimit(10**7)
class BinaryTreeNode :
	def __init__(self, data) :
		self.data = data
		self.left = None
		self.right = None

def spiralOrder(root):
    # write your code here
    if root is None:
        return []
    result = []
    q = Queue()
    q.put(root)
    left_to_right = True
    while not q.empty():
        level_size = q.qsize()
        level = []
        for _ in range(level_size):
            current = q.get()
            level.append(current.data)
            if current.left is not None:
                q.put(current.left)
            if current.right is not None:
                q.put(current.right)
        if not left_to_right:
            level.reverse()
        result.extend(level)
        left_to_right = not left_to_right
    return result

def takeInput() :
    arr = list(map(int, stdin.readline().strip().split(" ")))
    rootData = arr[0]
    n = len(arr)
    if(rootData == -1) :
        return None
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
    return root

def printSpiral(List1 ) :
    for x in List1 :
        print(x,end=" ")

root = takeInput()
List1 = spiralOrder(root)
printSpiral(List1)
