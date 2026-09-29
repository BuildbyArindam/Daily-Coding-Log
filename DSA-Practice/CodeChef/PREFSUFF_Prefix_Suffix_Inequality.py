"""
Problem   : Prefix Suffix Inequality
Platform  : CodeChef (PREFSUFF)
Link      : https://www.codechef.com/problems/PREFSUFF
Difficulty: 1714
Topics    : notsoloud
Date      : 2026-09-29

Approach:
    Constructive, no search needed. For N == 1 print "1". Otherwise print
    (N - 2) copies of 2 followed by 3 and 1.

Complexity:
    Time  : O(N) per test case (building and printing the array)
    Space : O(N) for the output array
"""


# ---------------------------------- Solution -------------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    ans = []
    for _ in range(T):
        N = int(input())
        if N == 1:
            ans.append("1")
        else:
            ans.append(" ".join(["2"] * (N - 2) + ["3", "1"]))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
