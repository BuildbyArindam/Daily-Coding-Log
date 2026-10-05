"""
Problem   : LCA of two nodes (TREELCA)
Platform  : CodeChef (DSAMONDAY023)
Link      : https://www.codechef.com/DSAMONDAY023/problems/TREELCA
Date      : 2026-10-05
Difficulty: Hard
Topics    : Trees, DFS, LCA

Approach:
    Root the tree at node 1 and run an iterative DFS to record each node's
    parent (up[]) and depth (depth[]). To find the LCA of a and b, first lift
    the deeper node until both are at the same depth, then move both up one
    step at a time until they meet. That meeting node is the LCA.
    The DFS is iterative to avoid Python's recursion limit on deep trees.

Complexity:
    Time  : O(N) for building the tree and the DFS, plus O(N) worst case for
            the lifting (skewed tree). Total O(N).
    Space : O(N) for the adjacency list, parent, depth and visited arrays.
"""


# --------------------------------------- Solution ------------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    n, a, b = int(tokens[0]), int(tokens[1]), int(tokens[2])
    graph = [[] for _ in range(n + 1)]
    pos = 3
    for _ in range(n - 1):
        x = int(tokens[pos])
        y = int(tokens[pos + 1])
        pos += 2
        graph[x].append(y)
        graph[y].append(x)
    up = [0] * (n + 1)
    depth = [0] * (n + 1)
    visited = [False] * (n + 1)
    visited[1] = True
    pending = [1]
    while pending:
        node = pending.pop()
        for nb in graph[node]:
            if not visited[nb]:
                visited[nb] = True
                up[nb] = node
                depth[nb] = depth[node] + 1
                pending.append(nb)
    while depth[a] > depth[b]:
        a = up[a]
    while depth[b] > depth[a]:
        b = up[b]
    while a != b:
        a = up[a]
        b = up[b]
    print(a)

main()
