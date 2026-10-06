"""
Platform   : CodeChef
Problem    : Furious Farming (IC26MP)
Link       : https://www.codechef.com/ICPCOL26POST/problems/IC26MP
Date       : 2026-10-06
Difficulty : Easy
Topics     : Greedy, Sorting, Case analysis

Approach:
    Sort the m marked positions, then measure the uncovered stretch before
    the first (need_left), the uncovered stretch after the last (need_right),
    and the widest gap between consecutive positions (widest).
    The base cost (span) is max(widest, need_left + need_right).
    A correction term, min over the two ends of min(need, span - need),
    is then added for the cheaper way to split the end segments.

Complexity:
    Time  : O(m log m) per test case, from sorting; the gap scan is O(m)
    Space : O(m) for the sorted positions
"""


# ------------------------------------------ Solution -------------------------------------------------


import sys

def main():
    tokens = sys.stdin.buffer.read().split()
    ptr = 0
    tc = int(tokens[ptr]); ptr += 1
    out = []
    for _ in range(tc):
        n = int(tokens[ptr]); m = int(tokens[ptr + 1]); ptr += 2
        pos = sorted(int(v) for v in tokens[ptr:ptr + m])
        ptr += m
        need_left = pos[0] - 1
        need_right = n - pos[-1]
        widest = 0
        for k in range(1, m):
            gap = pos[k] - pos[k - 1] - 1
            if gap > widest:
                widest = gap
        span = max(widest, need_left + need_right)
        opt1 = min(need_left, span - need_left)
        opt2 = min(need_right, span - need_right)
        out.append(str(span + min(opt1, opt2)))
    sys.stdout.write("\n".join(out) + "\n")

main()
