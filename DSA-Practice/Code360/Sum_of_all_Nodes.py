"""
Problem: Sum of all Nodes
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/sum-of-all-nodes_5656?kunjiRedirection=true
Difficulty: Easy
Date: 2026-09-04
Topics: Tree Traversal (DFS/Recursion), Generic/N-ary Trees, Level-order Tree Construction, Subtree Aggregation

Approach:
Given a generic (n-ary) tree built level-wise from an input array, recursively
sum each node's value with the sum of all its children's subtrees. Base case
returns 0 for a null root.

Time Complexity: O(N) — every node visited exactly once
Space Complexity: O(H) — recursion stack depth, H = height of the tree
                  (O(N) worst case for a skewed tree)
"""


# -------------------------------- Solution -----------------------------------------


import sys
import queue

class TreeNode :
    def __init__(self, data) :
        self.data = data
        self.children = list()

def inputLevelWise(li) :
    i = 0
    data = li[i] 
    i += 1
    if data == -1 :
        return None
    root = TreeNode(data) 
    q = queue.Queue()
    q.put(root)
    while (not q.empty()) :
        frontNode = q.get()
        noOfChildren = li[i]
        i += 1
        childrenArray = li[i : i+noOfChildren]
        for childData in childrenArray :
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)
        i = i+noOfChildren
    return root
        
def sumOfAllNodes(root) :
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if root is None:
        return 0
    
    total = root.data
    
    for child in root.children:
        total += sumOfAllNodes(child)
    
    return total
    
#main
sys.setrecursionlimit(10**6)
li = [int(elem) for elem in list(input().strip().split())]
root = inputLevelWise(li)
print(sumOfAllNodes(root))
