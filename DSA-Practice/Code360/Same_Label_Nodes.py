"""
Problem: Same Label Nodes
Platform: Code360
Link: https://www.naukri.com/code360/problems/same-label-nodes_1264994?kunjiRedirection=true
Date Solved: 2026-09-04
Difficulty: Easy
Topics: Tree, DFS, Subtree Aggregation, Frequency Counting

Approach:
Build an undirected adjacency list from the edges, then find a parent/traversal
order for the tree rooted at node 0 using an iterative BFS-style walk (order
list doubles as a valid post-order when reversed, since every node's parent
appears before it). Walk nodes in reverse order (children before parents) and
maintain a 26-length letter-count array per node, initializing each node's own
label count then merging each child's count array into the parent's. Finally,
for each node, the answer is its own label's count within its subtree count
array.

Time Complexity:  O(n * 26)  — each node's count array (size 26) is merged
                   into its parent exactly once.
Space Complexity: O(n * 26)  — cnt array for all nodes, plus O(n) for graph,
                   parent, and order arrays.
"""


# ------------------------- Solution ---------------------------------


from os import *
from sys import *
from collections import *
from math import *
from builtins import open

def findSameLabelNodes(n, edges, labels):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    parent = [-1] * n
    parent[0] = 0
    order = [0]
    for node in order:
        for nei in graph[node]:
            if nei != parent[node]:
                parent[nei] = node
                order.append(nei)
    cnt = [[0] * 26 for _ in range(n)]
    for node in reversed(order):
        letter = ord(labels[node]) - ord('a')
        cnt[node][letter] = 1
        for nei in graph[node]:
            if parent[nei] == node:
                child_cnt = cnt[nei]
                cur_cnt = cnt[node]
                for c in range(26):
                    cur_cnt[c] += child_cnt[c]
    ans = [0] * n
    for node in range(n):
        letter = ord(labels[node]) - ord('a')
        ans[node] = cnt[node][letter]
    return ans
