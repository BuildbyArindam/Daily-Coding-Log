"""
Problem   : The Best Matrix (GOODMATRIX)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GOODMATRIX
Date      : 2026-09-25
Difficulty: 1710
Topics    : Constructive Algorithms, Greedy, Math, Hashing

Approach:
A matrix is "good" if A[i][j] = C + s*i + t*j for some constant C and
signs s, t in {-1, +1}. For each of the 4 (s, t) combinations, compute
key = A[i][j] - s*i - t*j for every cell and count frequency of each
key with a hash map. The most frequent key under any combination tells
us the maximum number of cells that can stay unchanged while the rest
are altered to fit that pattern. Answer = N*M - max_frequency_over_all_4_combos.

Time complexity : O(T * N * M)      -- 4 passes per test case, O(1) hashing per cell
Space complexity: O(N * M)          -- frequency dict, rebuilt per (s, t) combo
"""


# ------------------------------------ Solution ---------------------------------------------


import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(N)]
        best_match = 0
        for s in (-1, 1):
            for t in (-1, 1):
                freq = defaultdict(int)
                current_max = 0
                for i in range(N):
                    for j in range(M):
                        value = A[i][j] - s * i - t * j
                        freq[value] += 1
                        current_max = max(current_max, freq[value])
                best_match = max(best_match, current_max)
        print(N * M - best_match)

if __name__ == "__main__":
    solve()
