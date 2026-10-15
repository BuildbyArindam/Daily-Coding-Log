"""
Problem : c8kbf and Tree (CodeChef - C8KBFTREE)
Link    : https://www.codechef.com/problems/C8KBFTREE
Date    : 2026-10-15
Rating  : 2001
Topics  : Trees, DFS, Pigeonhole Principle, Graphs, Set Theory

Approach:
  - Root the tree at 1 and compute px[v] = XOR of edge weights on the path 1 -> v.
    The path XOR between u and v is then px[u] ^ px[v].
  - If two nodes x, y share the same px value, use a helper node z (not x or y):
    pairs (x, z) and (y, z) have equal path XOR, so we output them immediately.
  - Otherwise all px values are distinct. The pairwise XORs of the first
    m = min(n, 2100) nodes then outnumber the possible XOR values, so by the
    pigeonhole principle two distinct pairs must collide. Find the collision
    by sorting all pair XORs (numpy). If none exists, print -1.

Complexity (per test case):
  Time  : O(n) for the iterative DFS + O(m^2 log m) for the pair sort, m = min(n, 2100)
  Space : O(n + m^2)
"""


# -------------------------------------------------- Solution ----------------------------------------------------------


import sys
import numpy as np

def solve_case(n, edges_u, edges_v, edges_w):
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b, c = edges_u[i], edges_v[i], edges_w[i]
        adj[a].append((b, c))
        adj[b].append((a, c))
    px = [-1] * (n + 1)
    px[1] = 0
    stack = [1]
    while stack:
        cur = stack.pop()
        base = px[cur]
        for nb, wt in adj[cur]:
            if px[nb] < 0:
                px[nb] = base ^ wt
                stack.append(nb)
    first_at = {}
    for node in range(1, n + 1):
        val = px[node]
        if val in first_at:
            x = first_at[val]
            y = node
            z = 1
            while z == x or z == y:
                z += 1
            p1 = (min(x, z), max(x, z))
            p2 = (min(y, z), max(y, z))
            return "%d %d %d %d" % (p1[0], p1[1], p2[0], p2[1])
        first_at[val] = node
    m = min(n, 2100)
    arr = np.array(px[1:m + 1], dtype=np.int64)
    ii, jj = np.triu_indices(m, 1)
    xs = arr[ii] ^ arr[jj]
    order = np.argsort(xs, kind="stable")
    srt = xs[order]
    eq = np.nonzero(srt[1:] == srt[:-1])[0]
    if eq.size == 0:
        return "-1"
    k = int(eq[0])
    f = int(order[k])
    g = int(order[k + 1])
    return "%d %d %d %d" % (ii[f] + 1, jj[f] + 1, ii[g] + 1, jj[g] + 1)

def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    t = int(tokens[pos]); pos += 1
    out = []
    for _ in range(t):
        n = int(tokens[pos]); pos += 1
        us = [0] * (n - 1)
        vs = [0] * (n - 1)
        ws = [0] * (n - 1)
        for i in range(n - 1):
            us[i] = int(tokens[pos])
            vs[i] = int(tokens[pos + 1])
            ws[i] = int(tokens[pos + 2])
            pos += 3
        out.append(solve_case(n, us, vs, ws))
    sys.stdout.write("\n".join(out) + "\n")

main()
