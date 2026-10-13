"""
Problem   : Reachable Wards
Platform  : Unstop
Link      : https://unstop.com/code/practice/662452
Difficulty: Medium
Topics    : DSU, Graphs, Sorting, Offline Queries, Hashing
Date      : 2026-10-13

Approach:
    Each query asks how many wards are reachable from a ward using only
    edges with cost <= cap. Answering each query with its own BFS/DFS would
    be too slow, so the queries are handled offline:
      1. Map ward names to integer ids with a hash map.
      2. Sort edges by cost and queries by cap.
      3. Process queries in increasing cap order. Before each query, union
         every edge with cost <= cap (a pointer into the sorted edges means
         each edge is added once).
      4. The answer is the size of the component containing the query ward.
    The DSU uses path compression (halving) and union by size.

Complexity:
    Time : O(E log E + Q log Q + (E + Q) * α(N))
    Space: O(N + E + Q)
"""


# -------------------------------------------- Solution -------------------------------------------------------------


import sys

def main():
    input = sys.stdin.buffer.readline
    N, E, Q = map(int, input().split())
    ward_id = {}
    for i in range(N):
        name = input().strip().decode()
        ward_id[name] = i
    edges = []
    for _ in range(E):
        u, v, cost = input().split()
        edges.append((int(cost), ward_id[u.decode()], ward_id[v.decode()]))
    queries = []
    for i in range(Q):
        name, cap = input().split()
        queries.append((int(cap), i, ward_id[name.decode()]))
    edges.sort()
    queries.sort()
    parent = list(range(N))
    size = [1] * N
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b:
            return
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]
    answers = [0] * Q
    edge_index = 0
    for cap, query_index, ward in queries:
        while edge_index < E and edges[edge_index][0] <= cap:
            _, u, v = edges[edge_index]
            union(u, v)
            edge_index += 1
        root = find(ward)
        answers[query_index] = size[root]
    sys.stdout.write("\n".join(map(str, answers)))

if __name__ == "__main__":
    main()
