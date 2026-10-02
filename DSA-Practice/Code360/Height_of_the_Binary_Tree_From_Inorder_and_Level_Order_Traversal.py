"""
Problem   : Height of the Binary Tree From Inorder and Level Order Traversal
Platform  : Code360 (Coding Ninjas)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118521/offering/1381013?goalRedirection=true&leftPanelTabValue=PROBLEM&customSource=studio_nav
Difficulty: Medium
Topics    : Binary Tree, Segment Tree, Divide and Conquer, Range Minimum Query
Date      : 2026-10-02

Approach:
  - In any subtree, the root is the node that appears earliest in the level order.
  - Map each value to its level-order position, then convert the inorder array
    into a "priority" array (lower = closer to the root).
  - Build an iterative segment tree over priority that returns the index of the
    minimum priority in a range, which gives the root of any inorder range.
  - Recursively split on that root: solve(l, root) and solve(root + 1, r).
    Height = 1 + max(left, right), with an empty range returning -1,
    so height is counted in edges (a single node has height 0).
  - The tree is never built explicitly, only its height is computed.

Complexity:
  - Time : O(N log N)  -> O(N) segment tree build + N range-min queries of O(log N)
  - Space: O(N)        -> segment tree + priority array, plus O(H) recursion stack
                          (O(N) worst case for a skewed tree)
"""


# --------------------------------------- Solution -------------------------------------------------------


from os import *
from sys import *
from collections import *
from math import *
import sys
sys.setrecursionlimit(10**7)

def heightOfTheTree(inorder, levelOrder, N):
    levelPos = [0] * (N + 1)
    for i in range(N):
        levelPos[levelOrder[i]] = i
    priority = [levelPos[x] for x in inorder]
    size = 1
    while size < N:
        size <<= 1
    tree = [-1] * (2 * size)
    for i in range(N):
        tree[size + i] = i
    for i in range(size - 1, 0, -1):
        left = tree[2 * i]
        right = tree[2 * i + 1]
        if left == -1:
            tree[i] = right
        elif right == -1:
            tree[i] = left
        elif priority[left] < priority[right]:
            tree[i] = left
        else:
            tree[i] = right
    def query(l, r):
        l += size
        r += size
        ans = -1
        while l < r:
            if l & 1:
                idx = tree[l]
                if idx != -1 and (ans == -1 or priority[idx] < priority[ans]):
                    ans = idx
                l += 1
            if r & 1:
                r -= 1
                idx = tree[r]
                if idx != -1 and (ans == -1 or priority[idx] < priority[ans]):
                    ans = idx
            l >>= 1
            r >>= 1
        return ans
    def solve(l, r):
        if l >= r:
            return -1
        root = query(l, r)
        leftHeight = solve(l, root)
        rightHeight = solve(root + 1, r)
        return 1 + max(leftHeight, rightHeight)
    return solve(0, N)

def takeInput() :
    n = int(input().strip())
    inorder = list(map(int, sys.stdin.readline().strip().split(" ")))
    levelOrder = list(map(int, sys.stdin.readline().strip().split(" ")))
    return n, inorder, levelOrder

t = int(input().strip())
for i in range(t):
    n, inorder, levelOrder = takeInput()
    print(heightOfTheTree(inorder, levelOrder, n))
