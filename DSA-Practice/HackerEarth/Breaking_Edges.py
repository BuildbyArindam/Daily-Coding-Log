"""
Problem   : Breaking Edges
Platform  : HackerEarth (March Circuits)
Link      : https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/breaking-edges-march-circuits-ca482e2a/
Difficulty: Easy
Topics    : Graphs, Trees, DFS
Date      : 2026-10-31

Approach:
  Count the edges whose removal splits the tree into two components with
  equal bitwise OR of node values.
  1. Run an iterative DFS from node 0 to get a preorder (seq), parents (up)
     and each node's position in that order (where).
  2. In preorder, every subtree is a contiguous range [pos, pos + size).
     Build subtree sizes (width) and subtree ORs (inside) bottom-up by
     walking seq in reverse.
  3. Build prefix (head) and suffix (tail) ORs over the preorder, so the OR
     of everything outside a subtree is head[pos] | tail[pos + size].
  4. Each non-root node represents the edge to its parent. Count it if
     outside OR == inside OR.

Time Complexity : O(N)
Space Complexity: O(N)
"""


# ------------------------------------------------ Solution ---------------------------------------------------------------------


import sys

def count_equal_cuts(n, vals, graph):
    up = [-1] * n
    seq = []
    pile = [0]
    while pile:
        cur = pile.pop()
        seq.append(cur)
        for nb in graph[cur]:
            if nb != up[cur]:
                up[nb] = cur
                pile.append(nb)
    where = [0] * n
    for idx, node in enumerate(seq):
        where[node] = idx
    width = [1] * n
    inside = vals[:]
    for node in reversed(seq):
        p = up[node]
        if p >= 0:
            width[p] += width[node]
            inside[p] |= inside[node]
    head = [0] * (n + 1)
    for i in range(n):
        head[i + 1] = head[i] | vals[seq[i]]
    tail = [0] * (n + 2)
    for i in range(n - 1, -1, -1):
        tail[i] = tail[i + 1] | vals[seq[i]]
    ans = 0
    for node in range(1, n):
        if up[node] < 0:
            continue
        s = where[node]
        outside = head[s] | tail[s + width[node]]
        if outside == inside[node]:
            ans += 1
    return ans

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    vals = [int(x) for x in tokens[1:n + 1]]
    graph = [[] for _ in range(n)]
    pos = n + 1
    for _ in range(n - 1):
        a = int(tokens[pos]) - 1
        b = int(tokens[pos + 1]) - 1
        pos += 2
        graph[a].append(b)
        graph[b].append(a)
    print(count_equal_cuts(n, vals, graph))

main()
