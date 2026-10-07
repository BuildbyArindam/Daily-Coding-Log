"""
Platform   : CodeChef
Problem    : Domination (DOM3)
Link       : https://www.codechef.com/problems/DOM3
Date       : 2026-10-07
Difficulty : Medium
Topics     : Trees, Combinatorics, Counting

Approach:
    The input is a tree with n nodes. Count all C(n, 3) vertex triples,
    then subtract the triples that fail the condition, found by
    complement counting:
      1. Path-centred triples: for each vertex v with degree 2, count the
         single neighbour pair. For degree >= 3, count the neighbour pairs
         that include at least one leaf neighbour, computed as
         C(d, 2) - C(d - leaves, 2).
      2. Leaf-edge triples: for each edge (x, y) with a leaf endpoint, count
         third vertices adjacent to neither endpoint, which is n - deg(x) - deg(y).
    Answer = C(n, 3) - middle_bad - edge_bad.

Complexity:
    Time  : O(n) per test case (each adjacency list is scanned once)
    Space : O(n) for the adjacency lists and edge list
"""


# --------------------------------------- Solution -----------------------------------------------


import sys

def solve():
    raw = sys.stdin.buffer.read().split()
    pos = 0
    cases = int(raw[pos]); pos += 1
    results = []
    for _ in range(cases):
        n = int(raw[pos]); pos += 1
        nbr = [[] for _ in range(n + 1)]
        pair_list = []
        for _ in range(n - 1):
            x = int(raw[pos]); y = int(raw[pos + 1]); pos += 2
            nbr[x].append(y)
            nbr[y].append(x)
            pair_list.append((x, y))
        degree = [0] * (n + 1)
        for v in range(1, n + 1):
            degree[v] = len(nbr[v])
        def choose2(k):
            return k * (k - 1) // 2 if k > 1 else 0
        middle_bad = 0
        for v in range(1, n + 1):
            dv = degree[v]
            if dv == 2:
                middle_bad += 1
            elif dv >= 3:
                leafy = 0
                for w in nbr[v]:
                    if degree[w] == 1:
                        leafy += 1
                middle_bad += choose2(dv) - choose2(dv - leafy)
        edge_bad = 0
        for (x, y) in pair_list:
            dx, dy = degree[x], degree[y]
            if dx == 1 or dy == 1:
                edge_bad += n - dx - dy
        whole = n * (n - 1) * (n - 2) // 6
        answer = whole - middle_bad - edge_bad
        results.append(answer)
    sys.stdout.write('\n'.join(map(str, results)) + '\n')

if __name__ == "__main__":
    solve()
