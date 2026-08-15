"""
Problem   : Flow Control (CF 990F)
Link      : https://codeforces.com/contest/990/problem/F
Date      : 2026-08-15
Tags      : dfs and similar, dp, greedy, trees | Rating: *2400

Approach:
    Model the pipe network as a tree rooted at node 0 (guaranteed connected,
    n nodes, n-1... here m edges with possible redundancy handled via edge ids
    for both directions). Each node has a required net flow a[i] (source if
    positive, sink if negative). Root the graph via BFS/DFS from node 0,
    building parent/parent_edge pointers.

    Process nodes in reverse BFS/DFS order (leaves -> root). For each node u,
    the flow on the edge connecting u to its parent must exactly satisfy u's
    remaining demand a[u] (since u's subtree has already been resolved).
    Push that flow value onto the parent edge, then fold a[u] into the
    parent's demand (a[parent] += a[u]) so the parent "absorbs" the subtree's
    net requirement.

    After processing, if the root's accumulated demand a[0] != 0, the flow
    network cannot be balanced -> "Impossible". Otherwise reconstruct the
    signed flow for each original edge index using the forward/reverse edge
    id trick (edge i stored as i for u->v, i+m for v->u).

Complexity:
    Time  : O(n + m)  -- one BFS/DFS pass + one reverse pass over visited nodes
    Space : O(n + m)  -- adjacency list, flow array, visited/parent arrays
"""


# -------------------------- Solution -----------------------------


import sys

def solve():
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    adj = [[] for _ in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append((v, i))
        adj[v].append((u, i + m))
    f = [0] * (2 * m)
    vis = [False] * n
    parent = [-1] * n
    parent_edge = [-1] * n
    order = []
    stack = [0]
    vis[0] = True
    while stack:
        u = stack.pop()
        order.append(u)
        for v, edge_id in adj[u]:
            if vis[v]:
                continue
            vis[v] = True
            parent[v] = u
            parent_edge[v] = edge_id
            stack.append(v)
    for u in reversed(order):
        if u == 0:
            continue
        edge_id = parent_edge[u]
        f[edge_id] = a[u]
        p = parent[u]
        a[p] += a[u]
    if a[0] != 0:
        print("Impossible")
        return
    print("Possible")
    out = []
    for i in range(m):
        if f[i] != 0:
            out.append(str(f[i]))
        else:
            out.append(str(-f[i + m]))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
