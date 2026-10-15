"""
Problem   : Tidying Posters (POSTERS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/POSTERS
Date      : 2026-10-15
Difficulty: 2001
Topics    : Bipartite Graphs, Maximum Bipartite Matching, Data Structures, Graphs, Advanced Algorithms, Advanced Graph Algos, Flow Networks

Approach:
    The relation crosses(p, q) is a strict partial order, so a pair
    (i -> j) means i and j can be chained together. The answer is the
    minimum chain cover = n - (maximum bipartite matching) (Dilworth /
    minimum path cover). Build the edges, then run Kuhn's augmenting-path
    algorithm on the left/right copies of each rectangle.

Complexity:
    Time : O(n^2) to build edges + O(n * E) = O(n^3) worst case for Kuhn's
    Space: O(n^2) for the adjacency lists, O(n) for matching/recursion
"""


# -------------------------------------------------- Solution ----------------------------------------------------------


import sys

sys.setrecursionlimit(10000)

def solve_case(rects):
    cnt = len(rects)
    nxt = [[] for _ in range(cnt)]
    def crosses(p, q):
        return p[0] < q[0] and p[1] > q[1] and p[2] > q[2] and p[3] < q[3]
    for i in range(cnt):
        for j in range(cnt):
            if i != j and crosses(rects[i], rects[j]):
                nxt[i].append(j)
    owner = [-1] * cnt
    def augment(u, seen):
        for v in nxt[u]:
            if seen[v]:
                continue
            seen[v] = True
            if owner[v] < 0 or augment(owner[v], seen):
                owner[v] = u
                return True
        return False
    matched = 0
    for u in range(cnt):
        if augment(u, [False] * cnt):
            matched += 1
    return cnt - matched

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    tests = int(tokens[pos]); pos += 1
    out = []
    for _ in range(tests):
        n = int(tokens[pos]); pos += 1
        rects = []
        for _ in range(n):
            x0 = int(tokens[pos]); x1 = int(tokens[pos + 1])
            y0 = int(tokens[pos + 2]); y1 = int(tokens[pos + 3])
            pos += 4
            rects.append((x0, x1, y0, y1))
        out.append(str(solve_case(rects)))
    print("\n".join(out))

main()
