"""
Problem: Equal Diverse Teams
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-diverse-teams-cbdb8fe2/
Difficulty: Easy
Topics: Greedy, Linear Search, Algorithms
Date Solved: 2026-08-31

Approach:
Count frequency of each distinct value. Let D = number of distinct
values, R = number of values that appear >= 2 times (can be "shared"
between two teams). To split N elements into 2 teams of size K each
where every value appears in both teams' diversity requirement,
distinct count D must satisfy K <= D <= 2K (each team needs at most K
distinct values, together at most 2K, but must cover at least K each).
needed_shared = 2*K - D values must be duplicated across both teams,
so R >= needed_shared is required. Answer YES iff both conditions hold.

Time Complexity: O(N) per test case — one pass to build frequency map.
Space Complexity: O(N) — frequency dictionary in the worst case (all distinct).
"""


# ------------------------- Solution ----------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        A = list(map(int, input().split()))
        freq = {}
        for x in A:
            freq[x] = freq.get(x, 0) + 1
        D = len(freq)
        R = sum(1 for v in freq.values() if v >= 2)
        needed_shared = 2 * K - D
        if K <= D <= 2 * K and R >= needed_shared:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
