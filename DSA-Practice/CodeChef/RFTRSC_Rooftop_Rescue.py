"""
Problem   : Rooftop Rescue
Platform  : CodeChef
Link      : https://www.codechef.com/problems/RFTRSC
Date      : 2026-10-12
Difficulty: Hard
Topics    : Graphs, BFS, Shortest Path

Approach:
    Treat the rooftops as nodes of an undirected graph and each connection as
    an edge. Run a level-by-level BFS from the source, counting one jump per
    level. The first time the destination is reached, that level is the
    minimum number of jumps. Self-loops and duplicate edges are removed by
    storing neighbours in sets. If the source equals the destination, or the
    destination is unreachable, the program prints 0.

Complexity:
    Time  : O(N + M) for building the graph and BFS
    Space : O(N + M) for adjacency sets, visited array, and frontier
"""


# ------------------------------------------ Solution ----------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    n, m = int(tokens[0]), int(tokens[1])
    src = int(tokens[2 + 2 * m])
    dst = int(tokens[3 + 2 * m])
    if src == dst:
        print(0)
        return
    nbr = [set() for _ in range(n + 1)]
    pos = 2
    for _ in range(m):
        a = int(tokens[pos])
        b = int(tokens[pos + 1])
        pos += 2
        if a != b:
            nbr[a].add(b)
            nbr[b].add(a)
    unseen = [True] * (n + 1)
    unseen[src] = False
    frontier = [src]
    jumps = 0
    while frontier:
        jumps += 1
        upcoming = []
        for cur in frontier:
            for nxt in nbr[cur]:
                if unseen[nxt]:
                    if nxt == dst:
                        print(jumps)
                        return
                    unseen[nxt] = False
                    upcoming.append(nxt)
        frontier = upcoming
    print(0)

main()
