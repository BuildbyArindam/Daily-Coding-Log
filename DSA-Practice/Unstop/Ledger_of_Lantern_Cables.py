"""
Problem   : Ledger of Lantern Cables
Platform  : Unstop 
Link      : https://unstop.com/code/practice/670543
Date      : 2026-11-06
Difficulty: Hard
Topics    : DSU, Union Find, Graph, Binary Search

Approach:
  Offline-built "time-aware" DSU. Union by size with NO path compression,
  so the DSU tree has O(log n) depth. Each node records `when[x]`, the day
  it was attached under its parent.
  - Connectivity day for (u, v): climb both nodes toward their common root,
    always moving the node with the smaller `when`, and take the max `when`
    seen. This is the latest edge on the u-v path, which is the earliest day
    they are connected. Return -1 if they never meet.
  - Size day for u (component size >= k): climb from u until the ancestor's
    final size is >= k. At that root, binary search its size history
    (`grow`) and the matching timestamps (`stamp`), then take the max with
    the day u's branch joined that root.
  - Answer = max(connectivity day, size day), or -1 if either is impossible.

Complexity:
  Time  : O((m + q) log n), since union by size keeps depth at O(log n)
          and each size query adds one O(log n) bisect.
  Space : O(n + m) for the parent, size, and history arrays.
"""


# ---------------------------------------- Solution -----------------------------------------------------


import sys
from bisect import bisect_left

BIG = 1 << 60

def solve():
    tok = sys.stdin.buffer.read().split()
    n = int(tok[0]); m = int(tok[1]); q = int(tok[2])
    up = list(range(n + 1))   
    when = [BIG] * (n + 1)  
    cnt = [1] * (n + 1)        
    stamp = [[0] for _ in range(n + 1)]   
    grow = [[1] for _ in range(n + 1)] 

    def top(x):
        while up[x] != x:
            x = up[x]
        return x

    pos = 3
    for _ in range(m):
        day = int(tok[pos]); a = top(int(tok[pos + 1])); b = top(int(tok[pos + 2]))
        pos += 3
        if a == b:
            continue
        if cnt[a] < cnt[b]:
            a, b = b, a
        up[b] = a
        when[b] = day
        cnt[a] += cnt[b]
        stamp[a].append(day)
        grow[a].append(cnt[a])

    def link_day(x, y):
        best = 0
        while x != y:
            if when[x] > when[y]:
                x, y = y, x
            if when[x] == BIG:
                return -1
            if when[x] > best:
                best = when[x]
            x = up[x]
        return best

    def size_day(x, k):
        joined = 0
        while cnt[x] < k:
            if up[x] == x:
                return -1
            joined = when[x]
            x = up[x]
        i = bisect_left(grow[x], k)
        t = stamp[x][i]
        return t if t > joined else joined
    res = []
    for _ in range(q):
        u = int(tok[pos]); v = int(tok[pos + 1]); k = int(tok[pos + 2])
        pos += 3
        s = size_day(u, k)
        if s < 0:
            res.append(-1)
            continue
        c = link_day(u, v)
        if c < 0:
            res.append(-1)
        else:
            res.append(c if c > s else s)
    print(" ".join(map(str, res)))

solve()
