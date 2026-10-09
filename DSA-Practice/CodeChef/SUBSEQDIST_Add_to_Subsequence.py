"""
Problem   : Ball Game
Platform  : CodeChef (SUBSEQDIST)
Link      : https://www.codechef.com/problems/SUBSEQDIST
Difficulty: 1736
Date      : 2026-10-09
Topics    : Math, Greedy, Frequency Counting

Approach:
    The answer depends only on the highest frequency of any value in the
    array. The most frequent value is the bottleneck, and the number of
    rounds needed is ceil(log2(max_freq)). This is computed as
    (max_freq - 1).bit_length(), which avoids floating-point log.

Complexity:
    Time : O(N) per test case (one pass to count frequencies)
    Space: O(N) for the frequency map
"""


# ------------------------------------------ Solution -----------------------------------------------------


import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        freq = Counter(A)
        max_freq = max(freq.values())
        ans = (max_freq - 1).bit_length()
        print(ans)

if __name__ == "__main__":
    solve()
