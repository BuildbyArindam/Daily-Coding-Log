"""
Problem   : Floodgate Relief Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/668005
Difficulty: Hard
Date      : 2026-10-29
Topics    : Graph, DSU, Kruskal, Kruskal Reconstruction Tree, Binary Lifting, Fenwick Tree

Approach:
  1. Sort canals by cost and run Kruskal with DSU. Each successful merge creates a
     new internal node (cost = canal cost) whose children are the two merged
     components. This builds a Kruskal Reconstruction Tree (KRT), where the
     component of x using canals with cost <= y is the subtree of x's highest
     ancestor with lim <= y.
  2. Iterative DFS over the KRT assigns each leaf a contiguous slot, so every
     subtree maps to a range [lo, hi) of slots.
  3. A Fenwick tree over the slots stores each node's money. This supports point
     updates (type 1) and subtree range sums (type 2).
  4. Binary lifting on the KRT jumps from x to its highest ancestor with
     lim <= y. The answer is the Fenwick range sum plus the leaf count (hi - lo).

Complexity:
  Time : O(M log M + N log N + Q log N)
  Space: O(N log N)  (binary lifting table over ≤ 2N-1 KRT nodes)
"""


# ---------------------------------------- Solution -----------------------------------------------------------


import sys

def solve():
    tok = sys.stdin.buffer.read().split()
    n, m, q = int(tok[0]), int(tok[1]), int(tok[2])
    money = [int(t) for t in tok[3:3 + n]]
    ptr = 3 + n
    canals = []
    for _ in range(m):
        a = int(tok[ptr]) - 1
        b = int(tok[ptr + 1]) - 1
        c = int(tok[ptr + 2])
        ptr += 3
        canals.append((c, a, b))
    canals.sort()
    size = 2 * n
    dsu = list(range(size))
    up0 = list(range(size))
    lim = [0] * size
    kid1 = [-1] * size
    kid2 = [-1] * size
    made = n
    for c, a, b in canals:
        while dsu[a] != a:
            dsu[a] = dsu[dsu[a]]
            a = dsu[a]
        while dsu[b] != b:
            dsu[b] = dsu[dsu[b]]
            b = dsu[b]
        if a == b:
            continue
        dsu[a] = dsu[b] = made
        up0[a] = up0[b] = made
        kid1[made] = a
        kid2[made] = b
        lim[made] = c
        made += 1
    lo = [0] * made
    hi = [0] * made
    slot = [0] * n
    cnt = 0
    for r in range(made):
        if up0[r] != r:
            continue
        st = [r]
        while st:
            v = st.pop()
            if v < 0:
                hi[~v] = cnt
                continue
            lo[v] = cnt
            if v < n:
                slot[v] = cnt
                cnt += 1
                hi[v] = cnt
            else:
                st.append(~v)
                st.append(kid2[v])
                st.append(kid1[v])
    fw = [0] * (n + 1)
    for i in range(n):
        fw[slot[i] + 1] += money[i]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            fw[j] += fw[i]
    jump = [up0[:made]]
    levels = max(1, made.bit_length())
    for _ in range(levels):
        prev = jump[-1]
        jump.append([prev[prev[i]] for i in range(made)])
    jump.reverse()
    out = []
    for _ in range(q):
        t = tok[ptr]
        x = int(tok[ptr + 1]) - 1
        y = int(tok[ptr + 2])
        ptr += 3
        if t == b'1':
            d = y - money[x]
            money[x] = y
            i = slot[x] + 1
            while i <= n:
                fw[i] += d
                i += i & -i
        else:
            cur = x
            for row in jump:
                nxt = row[cur]
                if lim[nxt] <= y:
                    cur = nxt
            total = 0
            i = hi[cur]
            while i > 0:
                total += fw[i]
                i -= i & -i
            i = lo[cur]
            while i > 0:
                total -= fw[i]
                i -= i & -i
            out.append("%d %d" % (total, hi[cur] - lo[cur]))
    sys.stdout.write("\n".join(out) + "\n")

solve()
