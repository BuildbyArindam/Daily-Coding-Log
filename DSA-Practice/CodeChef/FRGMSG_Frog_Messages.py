"""
Problem   : Frog Messages (FRGMSG)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FRGMSG
Difficulty: 1668
Topics    : Hashmaps, Dynamic Programming, Sorting, Data Structures, Algorithms
Date      : 2026-10-12

Approach:
    Two frogs can exchange messages if a chain of frogs links them, where
    each consecutive hop is at most K apart. After sorting frogs by position,
    that chain exists exactly when no gap larger than K lies between them.
    So I sort once, sweep left to right, and start a new group id whenever
    the gap to the previous frog exceeds K. Each query is then an O(1)
    check of whether the two frogs share a group id.

Time Complexity : O(N log N + P)  (sorting + one sweep + P queries)
Space Complexity: O(N + P)        (group ids, output buffer)
"""


# -------------------------------------------- Solution -------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    n, k, p = int(rd[0]), int(rd[1]), int(rd[2])
    pos = rd[3:3 + n]
    qs = rd[3 + n:]
    order = sorted(range(n), key=lambda i: int(pos[i]))
    group = [0] * n
    cur = 0
    prev = int(pos[order[0]])
    for idx in order:
        here = int(pos[idx])
        if here - prev > k:
            cur += 1
        group[idx] = cur
        prev = here
    out = []
    add = out.append
    for j in range(p):
        a = int(qs[2 * j]) - 1
        b = int(qs[2 * j + 1]) - 1
        add("Yes" if group[a] == group[b] else "No")
    sys.stdout.write("\n".join(out) + "\n")

main()
