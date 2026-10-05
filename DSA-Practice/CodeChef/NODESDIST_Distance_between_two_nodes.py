"""
Problem   : Distance between two nodes (NODESDIST)
Platform  : CodeChef (DSAMONDAY023)
Link      : https://www.codechef.com/DSAMONDAY023/problems/NODESDIST
Date      : 2026-10-05
Difficulty: Medium
Topics    : Tree, BFS, Graph

Approach  : The tree is stored as an adjacency list. A level-by-level BFS
            starts at the source node and records each node's step count.
            The BFS stops as soon as the destination gets a distance. In a
            tree there is exactly one path between two nodes, so the first
            time BFS reaches the destination is the answer.

Complexity: Time  - O(N), each node and edge is visited at most once.
            Space - O(N), for the adjacency list, distance array and queue.
"""


# ------------------------------------ Solution ---------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    n, src, dst = int(tokens[0]), int(tokens[1]), int(tokens[2])
    neighbours = [[] for _ in range(n + 1)]
    pos = 3
    for _ in range(n - 1):
        a = int(tokens[pos])
        b = int(tokens[pos + 1])
        pos += 2
        neighbours[a].append(b)
        neighbours[b].append(a)
    steps = [-1] * (n + 1)
    steps[src] = 0
    layer = [src]
    while steps[dst] == -1:
        following = []
        for node in layer:
            base = steps[node] + 1
            for nxt in neighbours[node]:
                if steps[nxt] == -1:
                    steps[nxt] = base
                    following.append(nxt)
        layer = following
    print(steps[dst])

main()
