"""
Platform   : CodeChef (Starters 261, Div A)
Problem    : Exun Handshake (EXSHAKE)
Link       : https://www.codechef.com/START261A/problems/EXSHAKE
Date       : 2026-10-21
Difficulty : Medium
Topics     : Greedy, Sorting, Math

Approach:
    We want the maximum number of groups whose combined handshakes stay
    within `limit`. With P total people, handshakes = P*(P-1)/2, which
    only grows as P grows. So the best choice is always the smallest
    groups first: sort the sizes, add them one by one to a running
    total, and stop at the first group that pushes the handshake
    count past the limit.

Complexity:
    Time  : O(N log N) per test case (sorting dominates; the scan is O(N))
    Space : O(N) for the sizes list
"""


# ------------------------------------------------ Solution -------------------------------------------------------------


import sys

def solve_case(limit, sizes):
    sizes.sort()
    best = 0
    people = 0
    for idx, s in enumerate(sizes):
        people += s
        if people * (people - 1) // 2 > limit:
            break
        best = idx + 1
    return best

def main():
    tokens = sys.stdin.read().split()
    pos = 0
    t = int(tokens[pos])
    pos += 1
    out = []
    for _ in range(t):
        n = int(tokens[pos])
        limit = int(tokens[pos + 1])
        pos += 2
        sizes = [int(x) for x in tokens[pos:pos + n]]
        pos += n
        out.append(str(solve_case(limit, sizes)))
    print("\n".join(out))

main()
