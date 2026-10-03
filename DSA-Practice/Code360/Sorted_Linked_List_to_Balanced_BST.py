"""
Problem   : Sorted Linked List to Balanced BST
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118512/offering/1381323?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Linked List, BST, Recursion, Divide and Conquer
Date      : 2026-10-03

Approach:
    Simulate an inorder traversal. A BST's inorder sequence is sorted, so the
    list nodes can be consumed in order as the tree is built.
    1. Count the nodes (n) in one pass.
    2. build(left, right) recurses on index ranges: build the left subtree
       from [left, mid-1], create the root from the current list node and
       advance the pointer, then build the right subtree from [mid+1, right].
    Choosing mid as the middle index keeps subtree sizes within 1 of each
    other, so the tree is height-balanced.

Complexity:
    Time  : O(n) - one pass to count, one pass to build; each node used once.
    Space : O(log n) - recursion depth of a balanced tree
            (excluding the O(n) output tree itself).
"""


# ----------------------------------------- Solution ------------------------------------------------------


import sys
sys.setrecursionlimit(10**7)

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class TreeNode:
	def __init__(self, data):
		self.val = data
		self.left = None
		self.right = None

def sortedListToBST(head):
	''' 
		Write your code here
		Return the root of balanced BST
		Verdict: 'CORRECT' or 'INCORRECT'
	'''
	if head is None:
		return None
	n = 0
	temp = head
	while temp is not None:
		n += 1
		temp = temp.next
	current = [head]
	def build(left, right):
		if left > right:
			return None
		mid = (left + right) // 2
		left_child = build(left, mid - 1)
		root = TreeNode(current[0].data)
		current[0] = current[0].next
		right_child = build(mid + 1, right)
		root.left = left_child
		root.right = right_child
		return root
	return build(0, n - 1)

ind = []
data1 = []

def takeInput():
	arr = list(map(int, sys.stdin.readline().strip().split(" ")))
	head = None
	if(arr[0] != -1):
		head = Node(arr[0])
		data1.append(arr[0])
		last = head
		for data in arr[1:]:
			if(data == -1):
				break
			data1.append(data)
			last.next = Node(data)
			last = last.next
	return head

def print1(poi):
	if poi == None:
		return
	print1(poi.left)
	ind.append(poi.val)
	print1(poi.right)

def isValid(root, height):
	if root == None:
		height[0] = 0
		return 1
	lh, rh, l, r = 0, 0, 0, 0
	l = isValid(root.left, [lh])
	r = isValid(root.right, [rh]);
	height[0] = max(l, r) + 1 
	if abs(l-r) >= 2:
		return 0
	else:
		return l & r

t = int(input().strip())
for i in range(t):
	ind.clear()
	data1.clear()
	head = takeInput()
	root = sortedListToBST(head)
	poi = root
	print1(poi)
	if data1 != ind:
		print('INCORRECT')
		continue
	h = 0
	if isValid(root, [h]) == 0:
		print('INCORRECT')
		continue
	print('CORRECT')
