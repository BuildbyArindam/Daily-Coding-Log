"""
Problem   : Max Mex (MAXMEX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAXMEX
Difficulty: 1714
Topics    : Ad-hoc, Constructive
Date      : 2026-09-29

Approach:
    Every element equal to M has to be removed, so count those.
    Mark which values below M appear in the array. If any value in
    1..M-1 is missing, the target can't be reached, so print -1.
    Otherwise the answer is N minus the count of elements equal to M.

Complexity:
    Time  : O(N + M) per test case
    Space : O(M) for the presence array
"""


# ------------------------------------- Solution ---------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        present = [False] * M
        count_m = 0
        for x in A:
            if x == M:
                count_m += 1
            elif x < M:
                present[x] = True
        possible = True
        for x in range(1, M):
            if not present[x]:
                possible = False
                break
        if not possible:
            print(-1)
        else:
            print(N - count_m)

if __name__ == "__main__":
    solve()
