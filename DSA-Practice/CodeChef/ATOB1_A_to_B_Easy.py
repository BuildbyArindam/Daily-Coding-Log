"""
Problem   : A to B (Easy)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ATOB1
Difficulty: 2004
Topics    : Strings, Observation
Date      : 2026-10-16

Approach:
    Compare the two strings by how uniform each one is (all characters
    identical). If a == b, no operations are needed (0). If neither string
    is uniform, the answer is 0. In every other case the answer is 1.

Complexity:
    Time  : O(N) per test case (one count() pass per string)
    Space : O(1) extra per test case (input tokens are read up front)
"""


# -------------------------------------------------- Solution ----------------------------------------------------------


import sys

def uniform(s):
    return s.count(s[0]) == len(s)

def solve(n, a, b):
    if a == b:
        return 0
    if not uniform(a) and not uniform(b):
        return 0
    return 1

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    pos = 1
    res = []
    for _ in range(t):
        n = int(tokens[pos]); a = tokens[pos + 1]; b = tokens[pos + 2]
        pos += 3
        res.append(str(solve(n, a, b)))
    print("\n".join(res))

main()
