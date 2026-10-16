"""
Platform   : CodeChef
Problem    : Maximum Product Walk (MXPRWA)
Link       : https://www.codechef.com/problems/MXPRWA
Difficulty : 2005
Date       : 2026-10-16
Topics     : Trees, Dynamic Programming, Parity, Math

Approach:
  Each node's value is split into a sign (parity) and a magnitude, and a
  bottom-up tree DP keeps two states per node: e[v] is the best total
  magnitude on a walk with an even number of negatives (positive product),
  and o[v] is the best with an odd number of negatives. Nodes are processed
  in reverse BFS order, so every child is final before it is merged into
  its parent. Merging a child into the parent uses the combine rule
  (even+even -> even, odd+odd -> even, even+odd -> odd), which also joins
  branches from different children. The answer is the maximum e[v] over all
  nodes, printed as 2^best mod 998244353.

Complexity:
  Time  : O(N) per test case (BFS + one reverse pass)
  Space : O(N) for adjacency lists and the DP arrays
"""


# ---------------------------------------------- Solution -------------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    MOD = 998244353
    NEG = -(10 ** 18)
    t = int(rd[0])
    ptr = 1
    res = []
    while t:
        t -= 1
        n = int(rd[ptr]); ptr += 1
        vals = rd[ptr:ptr + n]; ptr += n
        g = [[] for _ in range(n)]
        for _ in range(n - 1):
            x = int(rd[ptr]) - 1
            y = int(rd[ptr + 1]) - 1
            ptr += 2
            g[x].append(y)
            g[y].append(x)
        e = [NEG] * n         
        o = [NEG] * n         
        for i in range(n):
            w = int(vals[i])
            if w > 0:
                e[i] = w
            else:
                o[i] = -w
        up = [-1] * n
        seq = [0]
        k = 0
        while k < len(seq):
            u = seq[k]
            k += 1
            for z in g[u]:
                if z != up[u]:
                    up[z] = u
                    seq.append(z)
        top = NEG
        for idx in range(n - 1, -1, -1):
            v = seq[idx]
            if e[v] > top:
                top = e[v]
            p = up[v]
            if p < 0:
                continue
            pe, po = e[p], o[p]
            ce, co = e[v], o[v]
            ne = max(pe, pe + ce, po + co)
            no = max(po, pe + co, po + ce)
            e[p] = ne
            o[p] = no
        res.append(pow(2, top, MOD))
    sys.stdout.write("\n".join(map(str, res)) + "\n")

main()
