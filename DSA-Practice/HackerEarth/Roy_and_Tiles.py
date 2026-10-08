"""
Problem   : Roy and Tiles
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/roy-and-tiles-1/
Difficulty: Medium
Topics    : Binary Search, Sorting, Algorithms
Date      : 2026-10-08

Approach:
    For each of the N rows, build a frequency map (value -> count).
    For a query (S, D), the destination must satisfy D == S + N + 1,
    otherwise the answer is 0. Row i must contribute a tile with value
    S + i + 1, so the number of ways is the product of the counts of
    that value across all rows, taken modulo 1e9+7. If any row has no
    such tile, the answer is 0.

Complexity (M = total tiles across all rows):
    Time  : O(M) preprocessing + O(N) per query -> O(M + Q*N)
    Space : O(M) worst case for the per-row frequency maps
"""


# ------------------------------------------------- Solution --------------------------------------------------------------


import sys

MOD = 1000000007

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        cnt = []
        for _ in range(N):
            row = map(int, input().split())
            freq = {}
            for x in row:
                freq[x] = freq.get(x, 0) + 1
            cnt.append(freq)
        Q = int(input())
        for _ in range(Q):
            S, D = map(int, input().split())
            if D != S + N + 1:
                print(0)
                continue
            ans = 1
            for i in range(N):
                need = S + i + 1
                ways = cnt[i].get(need, 0)
                if ways == 0:
                    ans = 0
                    break
                ans = (ans * ways) % MOD
            print(ans)

if __name__ == "__main__":
    solve()
