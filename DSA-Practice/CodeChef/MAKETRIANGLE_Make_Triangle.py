"""
Platform   : CodeChef
Problem    : Make Triangle (MAKETRIANGLE)
Link       : https://www.codechef.com/problems/MAKETRIANGLE
Difficulty : 714
Topics     : Math, Triangle Inequality 
Date       : 2026-10-22

Approach:
    Three sides form a non-degenerate triangle iff the largest side is
    strictly less than the sum of the other two. Sort the sides in
    descending order (a >= b >= c). If a < b + c, nothing is needed.
    Otherwise, the shortfall is a - (b + c) + 1, so that is the answer.

Complexity:
    Time  : O(1) per test case (sorting 3 elements), O(T) overall
    Space : O(T) for the buffered output
"""


# ------------------------------------------------- Solution -----------------------------------------------------


import sys

def _gap(trio):
    trio = sorted(trio, reverse=True)
    need = trio[0] - trio[1] - trio[2] + 1
    return need if need > 0 else 0

def _run():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    pos = 1
    out = []
    for _ in range(cases):
        triple = list(map(int, tokens[pos:pos + 3]))
        pos += 3
        out.append(str(_gap(triple)))
    print("\n".join(out))

if __name__ == "__main__":
    _run()
