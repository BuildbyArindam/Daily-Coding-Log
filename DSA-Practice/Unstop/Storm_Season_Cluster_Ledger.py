"""
Problem   : Storm Season Cluster Ledger
Platform  : Unstop 
Link      : https://unstop.com/code/practice/672732
Date      : 2026-11-20
Difficulty: Hard
Topics    : DSU, Offline Queries, Reverse Processing, Fenwick Tree, Order Statistics

Approach:
    Cable cuts are hard to handle online, so process them offline in reverse,
    where each cut becomes a merge.
    1. Mark every cable that is ever severed, then build a DSU from the
       cables that are never cut. This gives the component weights at the
       end of all storms.
    2. Replay the cuts from last to first. Each cut cable becomes a union,
       and the pair of weights it merges is recorded for that step.
    3. Coordinate-compress every weight that can ever exist (the initial
       components plus every merged sum). Keep a Fenwick tree of component
       counts over the compressed weights.
    4. In reverse order, answer each query. With `alive` components, the
       k-th largest is the (alive - k + 1)-th smallest, found by binary
       lifting on the Fenwick tree. If alive < k the answer is 0. Then
       apply the recorded merge to the tree (remove the two weights, add
       their sum).
    Answers are printed in the original query order.

Complexity:
    Time  : O((M + C) * alpha(M) + (M + S) * log(M + S))
            DSU work uses path halving and union by size. Sorting the weight
            pool and the Fenwick updates and queries add the log factor.
    Space : O(M + C + S)
"""


# ------------------------------------------------- Solution -----------------------------------------------------------


import sys

def run():
    raw = sys.stdin.buffer.read().split()
    M = int(raw[0]); C = int(raw[1]); S = int(raw[2])
    cursor = 3
    weight = [0] * (M + 1)
    for i in range(1, M + 1):
        weight[i] = int(raw[cursor]); cursor += 1
    left = [0] * C
    right = [0] * C
    for j in range(C):
        left[j] = int(raw[cursor]); right[j] = int(raw[cursor + 1])
        cursor += 2
    cab = [0] * S
    rnk = [0] * S
    for t in range(S):
        cab[t] = int(raw[cursor]) - 1
        rnk[t] = int(raw[cursor + 1])
        cursor += 2
    severed = bytearray(C)
    for t in range(S):
        severed[cab[t]] = 1
    boss = list(range(M + 1))
    heft = [1] * (M + 1)
    def locate(x):
        while boss[x] != x:
            boss[x] = boss[boss[x]]
            x = boss[x]
        return x
    for j in range(C):
        if severed[j]:
            continue
        p = locate(left[j]); q = locate(right[j])
        if p != q:
            if heft[p] < heft[q]:
                p, q = q, p
            boss[q] = p
            heft[p] += heft[q]
            weight[p] += weight[q]
    start_vals = [weight[x] for x in range(1, M + 1) if locate(x) == x]
    merges = [None] * S
    for t in range(S - 1, -1, -1):
        j = cab[t]
        p = locate(left[j]); q = locate(right[j])
        if p != q:
            merges[t] = (weight[p], weight[q])
            if heft[p] < heft[q]:
                p, q = q, p
            boss[q] = p
            heft[p] += heft[q]
            weight[p] += weight[q]
    pool = set(start_vals)
    for m in merges:
        if m is not None:
            pool.add(m[0] + m[1])
    ordered = sorted(pool)
    where = {v: i + 1 for i, v in enumerate(ordered)}
    n = len(ordered)
    bit = [0] * (n + 1)
    def bump(i, d):
        while i <= n:
            bit[i] += d
            i += i & (-i)
    top = 1
    while top * 2 <= n:
        top *= 2
    def nth_smallest(target):
        at = 0
        step = top
        while step:
            nxt = at + step
            if nxt <= n and bit[nxt] < target:
                at = nxt
                target -= bit[nxt]
            step >>= 1
        return ordered[at]
    alive = 0
    for v in start_vals:
        bump(where[v], 1)
        alive += 1
    answers = [None] * S
    for t in range(S - 1, -1, -1):
        k = rnk[t]
        if alive < k:
            answers[t] = "%d 0" % alive
        else:
            answers[t] = "%d %d" % (alive, nth_smallest(alive - k + 1))
        m = merges[t]
        if m is not None:
            bump(where[m[0]], -1)
            bump(where[m[1]], -1)
            bump(where[m[0] + m[1]], 1)
            alive -= 1
    sys.stdout.write("\n".join(answers) + "\n")

run()
