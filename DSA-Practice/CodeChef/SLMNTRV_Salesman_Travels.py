"""
Problem   : Salesman Travels (SLMNTRV)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SLMNTRV
Date      : 2026-10-07
Difficulty: Hard
Topics    : Graph Matching, Blossom Algorithm, Number Theory	

Approach  :
  - Treat each index 1..n as a graph vertex. Connect i and j if i*j is within
    k of a perfect square (checked against the nearest integer roots of i*j
    via math.isqrt).
  - Find a maximum matching in this general (non-bipartite) graph using
    Edmonds' Blossom algorithm.
  - If n is odd, add a dummy vertex connected to every node so a perfect
    matching can exist. Whichever node pairs with the dummy goes last.
  - If any vertex is unmatched, print -1. Otherwise output the matched
    pairs one after another, with the leftover node at the end.

Time      : O(n^2) to build the graph + O(V^3) for blossom matching, V = n or n+1
Space     : O(n^2) worst case for the adjacency lists
"""


# ------------------------------------------ Solution ---------------------------------------------


import sys
import math

def is_near_square(a, b, k):
    product = a * b
    root = math.isqrt(product)
    for x in range(max(1, root - 1), root + 3):
        if abs(product - x * x) <= k:
            return True
    return False

class GeneralMatcher:
    def __init__(self, size):
        self.size = size
        self.adj = [[] for _ in range(size)]

    def link(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def run(self):
        n = self.size
        partner = [-1] * n
        parent = [-1] * n
        root_of = list(range(n))
        visited = [False] * n
        in_blossom = [False] * n

        def find_lca(x, y):
            seen = [False] * n
            cur = x
            while True:
                cur = root_of[cur]
                seen[cur] = True
                if partner[cur] == -1:
                    break
                cur = parent[partner[cur]]
            cur = y
            while True:
                cur = root_of[cur]
                if seen[cur]:
                    return cur
                cur = parent[partner[cur]]

        def shrink(v, base, child):
            while root_of[v] != base:
                in_blossom[root_of[v]] = True
                in_blossom[root_of[partner[v]]] = True
                parent[v] = child
                child = partner[v]
                v = parent[partner[v]]

        def augmenting_search(start):
            nonlocal visited, parent, root_of, in_blossom
            visited = [False] * n
            parent = [-1] * n
            for i in range(n):
                root_of[i] = i
            visited[start] = True
            frontier = [start]
            pos = 0
            while pos < len(frontier):
                cur = frontier[pos]
                pos += 1
                for nxt in self.adj[cur]:
                    if root_of[cur] == root_of[nxt] or partner[cur] == nxt:
                        continue
                    if nxt == start or (partner[nxt] != -1 and parent[partner[nxt]] != -1):
                        base = find_lca(cur, nxt)
                        for i in range(n):
                            in_blossom[i] = False
                        shrink(cur, base, nxt)
                        shrink(nxt, base, cur)
                        for i in range(n):
                            if in_blossom[root_of[i]]:
                                root_of[i] = base
                                if not visited[i]:
                                    visited[i] = True
                                    frontier.append(i)
                    elif parent[nxt] == -1:
                        parent[nxt] = cur
                        if partner[nxt] == -1:
                            return nxt
                        visited[partner[nxt]] = True
                        frontier.append(partner[nxt])
            return -1
        for v in range(n):
            if partner[v] == -1:
                reached = augmenting_search(v)
                if reached != -1:
                    while reached != -1:
                        p = parent[reached]
                        pp = partner[p]
                        partner[reached] = p
                        partner[p] = reached
                        reached = pp
        return partner

def build_route(n, k):
    extra_node = None
    total = n
    if n % 2 == 1:
        total = n + 1
        extra_node = n  
    matcher = GeneralMatcher(total)
    for i in range(n):
        for j in range(i + 1, n):
            if is_near_square(i + 1, j + 1, k):
                matcher.link(i, j)
    if extra_node is not None:
        for i in range(n):
            matcher.link(i, extra_node)
    pairing = matcher.run()
    if any(x == -1 for x in pairing):
        return None
    done = [False] * total
    blocks = []
    odd_one_out = None
    for v in range(total):
        if done[v]:
            continue
        w = pairing[v]
        done[v] = done[w] = True
        if extra_node is not None and (v == extra_node or w == extra_node):
            odd_one_out = (w if v == extra_node else v) + 1
        else:
            blocks.append((v + 1, w + 1))
    sequence = []
    for a, b in blocks:
        sequence.extend([a, b])
    if odd_one_out is not None:
        sequence.append(odd_one_out)
    return sequence

def main():
    data = sys.stdin.read().split()
    pos = 0
    t = int(data[pos]); pos += 1
    output_lines = []
    for _ in range(t):
        n = int(data[pos]); k = int(data[pos + 1]); pos += 2
        route = build_route(n, k)
        output_lines.append(' '.join(map(str, route)) if route else "-1")
    sys.stdout.write('\n'.join(output_lines) + '\n')

if __name__ == "__main__":
    main()
