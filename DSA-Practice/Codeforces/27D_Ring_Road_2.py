"""
Problem   : Ring Road 2
Link      : https://codeforces.com/problemset/problem/27/D
Date      : 2026-08-28
Difficulty: *2200
Topics    : 2-SAT, DFS and similar, DSU, Graphs

Approach:
    Each road connects two points on a circle; two roads "cross" iff their
    endpoints interleave around the circle. If road A gets direction "in"
    (clockwise) and road B crosses it, B must be forced to "out" (and vice
    versa) — this is exactly a graph 2-coloring problem. Build a conflict
    graph where crossing roads are connected, then BFS/DFS-color each
    connected component with 2 colors ('i'/'o'). If a component is
    non-bipartite (an edge connects two same-colored nodes), print
    "Impossible".

Complexity:
    Time : O(m^2) to detect all crossing pairs (m = number of roads,
           up to a few thousand) + O(m^2) for the coloring BFS/DFS in the
           worst case (dense conflict graph) => O(m^2) overall.
    Space: O(m^2) worst case for the adjacency lists (dense graph),
           O(m) for color/stack arrays.
"""


# --------------------------------- Solution ------------------------------------


import sys

def inside(a, b, x):
    """Return True if x is strictly between a and b on the linear order."""
    return a < x < b

def roads_cross(e1, e2):
    a, b = sorted(e1)
    c, d = sorted(e2)
    if a == c or a == d or b == c or b == d:
        return False
    return inside(a, b, c) != inside(a, b, d)

def solve():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    graph = [[] for _ in range(m)]
    for i in range(m):
        for j in range(i + 1, m):
            if roads_cross(roads[i], roads[j]):
                graph[i].append(j)
                graph[j].append(i)
    color = [-1] * m
    for start in range(m):
        if color[start] != -1:
            continue
        color[start] = 0
        stack = [start]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    print("Impossible")
                    return
    print(''.join('i' if c == 0 else 'o' for c in color))

if __name__ == "__main__":
    solve()
