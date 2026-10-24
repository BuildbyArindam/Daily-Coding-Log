"""
Problem   : Chef and Minimum Colouring (CAMC)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CAMC
Difficulty: 2014
Date      : 2026-10-24
Topics    : Sorting, Two Pointers, Sliding Window

Approach:
    Element i belongs to group (i % M). We must pick one element from every
    group so that (max - min) of the picks is minimized. Sort all elements by
    value, tagging each with its group, then slide a window over the sorted
    list. Expand the right end until all M groups are present, record
    (right - left) value difference, then shrink from the left to look for a
    smaller window. The smallest window covering every group is the answer.

Complexity:
    Time  : O(N log N) per test case (sorting dominates; the window pass is O(N))
    Space : O(N + M)
"""


# ----------------------------------------------- Solution ---------------------------------------------------


import sys

def main():
    rd = sys.stdin.buffer.read().split()
    p = 0
    t = int(rd[p]); p += 1
    out = []
    for _ in range(t):
        n = int(rd[p]); m = int(rd[p + 1]); p += 2
        vals = rd[p:p + n]; p += n
        items = sorted((int(v), i % m) for i, v in enumerate(vals))
        seen = [0] * m
        have = 0
        best = 1 << 62
        lo = 0
        for hi in range(n):
            c = items[hi][1]
            if seen[c] == 0:
                have += 1
            seen[c] += 1
            while have == m:
                d = items[hi][0] - items[lo][0]
                if d < best:
                    best = d
                k = items[lo][1]
                seen[k] -= 1
                if seen[k] == 0:
                    have -= 1
                lo += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")

main()
