"""
Problem   : Compare and Connect (COM_AND_CON)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/COM_AND_CON
Difficulty: 1719
Topics    : Constructive, Strings 
Date      : 2026-10-02

Approach:
    Constructive problem. The answer string is built directly from N and M,
    with no search or simulation. Three cases:
      - N == 0 : ">" + "<>" * (M - 2) + "=>"
      - M == 0 : "<" * (2N - 3) + "=<"   (N >= 2)
      - otherwise: "<" * (2N) + "><" * (M - 1) + ">"
    Output is collected in a list and written once for fast I/O.

Complexity:
    Time : O(N + M) per test case (string construction)
    Space: O(N + M) for the output string
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        N, M = map(int, input().split())
        if N == 0:
            ans = ">" + "<>" * (M - 2) + "=>"
        elif M == 0:
            ans = "<" * (2 * N - 3) + "=<"
        else:
            ans = "<" * (2 * N) + "><" * (M - 1) + ">"
        out.append(ans)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
