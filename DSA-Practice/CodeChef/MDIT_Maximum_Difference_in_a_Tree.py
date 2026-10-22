"""
Problem   : Maximum Difference in a Tree (MDIT)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MDIT
Difficulty: 1450
Topics    : Trees, DFS, Ancestor-Descendant Pairs
Date      : 2026-10-22

Approach:
    The answer is the max |val[u] - val[v]| over all pairs where u is an
    ancestor of v. For each node, the best partner among its ancestors is
    either the min or the max value on its root path, so the best difference
    is max(x - path_min, path_max - x).
    Run an iterative DFS from the root, carrying path_min and path_max
    down to each child, and update the global best at every node.
    The DFS is iterative to avoid Python's recursion limit.

Complexity:
    Time : O(N), each node is visited once
    Space: O(N), child adjacency arrays plus the DFS stack
"""


# ----------------------------------------------- Solution -------------------------------------------------------


import sys

def main():
    rd = sys.stdin.read().split()
    n = int(rd[0])
    vals = [int(t) for t in rd[1:1 + n]]
    par = [int(t) for t in rd[1 + n:1 + 2 * n]]
    head = [-1] * n
    nxt = [-1] * n
    top = -1
    for i in range(n):
        p = par[i]
        if p == -1:
            top = i
        else:
            p -= 1
            nxt[i] = head[p]
            head[p] = i
    lo = [0] * n
    hi = [0] * n
    best = 0
    pile = [top]
    first = True
    lo[top] = hi[top] = vals[top]
    while pile:
        cur = pile.pop()
        c = head[cur]
        while c != -1:
            x = vals[c]
            a, b = lo[cur], hi[cur]
            d1 = x - a
            d2 = b - x
            if d1 < 0:
                d1 = -d1
            if d2 < 0:
                d2 = -d2
            if d1 > best:
                best = d1
            if d2 > best:
                best = d2
            lo[c] = x if x < a else a
            hi[c] = x if x > b else b
            pile.append(c)
            c = nxt[c]
    sys.stdout.write(str(best) + "\n")

main()
