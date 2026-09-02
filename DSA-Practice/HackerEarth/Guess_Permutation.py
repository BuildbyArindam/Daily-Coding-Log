"""
Problem: Guess Permutation
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/permutation-swaps-2-01766245/
Difficulty: Hard
Topics: Binary Search, Linear Search, Algorithms
Date Solved: 2026-09-02

Approach:
    Reconstruct a permutation P (1..N+1 values over N+1 positions, effectively
    a permutation of 0..N after shifting) from its array of adjacent differences A,
    where A[i] = P[i+1] - P[i].
    Build the prefix-sum sequence starting from an arbitrary anchor (prefix = 0):
    prefix[0] = 0, prefix[i] = prefix[i-1] + A[i-1].
    A valid permutation exists iff:
      1. All prefix values are distinct (no repeated position value), and
      2. max(prefix) - min(prefix) == N (exactly N+1 distinct consecutive-range values,
         matching the required permutation size).
    If valid, shift all prefix values by (1 - min_prefix) so they map onto 1..N+1.

Time Complexity:  O(N) per test case — single pass to build prefixes + O(1) set/dict ops
Space Complexity: O(N) per test case — for the seen set and prefixes list
"""


# --------------------------- Solution -------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        prefix = 0
        min_prefix = 0
        max_prefix = 0
        seen = {0}
        prefixes = [0]
        possible = True
        for x in A:
            prefix += x
            if prefix in seen:
                possible = False
                break
            seen.add(prefix)
            prefixes.append(prefix)
            min_prefix = min(min_prefix, prefix)
            max_prefix = max(max_prefix, prefix)
        if not possible:
            print(-1)
            continue
        if max_prefix - min_prefix != N:
            print(-1)
            continue
        shift = 1 - min_prefix
        P = [x + shift for x in prefixes]
        print(*P)

if __name__ == "__main__":
    solve()
