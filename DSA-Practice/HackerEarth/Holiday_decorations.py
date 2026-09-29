"""
Problem   : Holiday Decorations
Platform  : HackerEarth (Hard)
Link      : https://www.hackerearth.com/practice/data-structures/queues/basics-of-queues/practice-problems/algorithm/holiday-decorations-b53daa12/
Date      : 2026-09-29
Topics    : Graph, Implementation, Data Structures, Sqrt Decomposition

Approach  : Maintain "beauty" (number of edges whose endpoints share a color)
            under point recolor queries, using degree-based sqrt decomposition.
            - Heavy nodes (degree >= B) keep a dict of neighbor color counts,
              so their own recolor is O(1).
            - Light nodes (degree < B) scan their neighbors directly: O(B).
            - On recolor, every heavy neighbor's color-count dict is updated.
              A tree has at most 2N/B heavy nodes, so this is O(N/B).
            - Beauty changes by (same_new - same_old) for the recolored node.

Time      : O(N) preprocessing + O(M * (B + N/B)) queries, i.e. ~O(M * sqrt(N))
            when B ~ sqrt(N) (B = 550 here).
Space     : O(N) for adjacency lists and heavy-node color dicts.
"""


# ------------------------------------- Solution ----------------------------------------------


import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
adj = [[] for _ in range(N)]
adj[0].append(1)
adj[1].append(0)
parents = list(map(int, input().split()))
for j, p in enumerate(parents, start=2):
    p -= 1
    adj[j].append(p)
    adj[p].append(j)
beauty = 0
for v in range(N):
    for u in adj[v]:
        if u < v and A[u] == A[v]:
            beauty += 1
B = 550
heavy = []
heavy_id = [-1] * N
for v in range(N):
    if len(adj[v]) >= B:
        heavy_id[v] = len(heavy)
        heavy.append(v)
H = len(heavy)
color_count = [dict() for _ in range(H)]
for hid, h in enumerate(heavy):
    d = color_count[hid]
    for v in adj[h]:
        c = A[v]
        d[c] = d.get(c, 0) + 1
heavy_neighbors = [[] for _ in range(N)]
for hid, h in enumerate(heavy):
    for v in adj[h]:
        heavy_neighbors[v].append(hid)
for _ in range(M):
    x, new_color = map(int, input().split())
    x -= 1
    old_color = A[x]
    if old_color == new_color:
        print(beauty)
        continue
    if heavy_id[x] != -1:
        d = color_count[heavy_id[x]]
        same_old = d.get(old_color, 0)
        same_new = d.get(new_color, 0)
    else:
        same_old = 0
        same_new = 0
        for v in adj[x]:
            if A[v] == old_color:
                same_old += 1
            if A[v] == new_color:
                same_new += 1
    beauty -= same_old
    beauty += same_new
    for hid in heavy_neighbors[x]:
        d = color_count[hid]
        cnt = d.get(old_color, 0) - 1
        if cnt == 0:
            del d[old_color]
        else:
            d[old_color] = cnt
        d[new_color] = d.get(new_color, 0) + 1
    A[x] = new_color
    print(beauty)
