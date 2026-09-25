"""
Problem   : Summary Power
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUMPOWER
Difficulty: 1709
Date Solved: 2026-09-25
Topics    : Strings, Sliding Window, Prefix Sum / Running Sum, Two Pointers

Approach:
    For a binary/character string S of length N, build a "transition" array
    diff[i] = 1 if S[i] != S[i+1] else 0, for i in [0, N-2].
    Each window of K consecutive characters corresponds to a window of
    (K-1) transition values. We need the sum of transitions over every
    window of size K across the string — computed via a sliding window
    (running sum), adding the new diff entering the window and removing
    the one leaving it, giving each window's answer in O(1) amortized.

Time Complexity : O(N) per test case  ->  O(sum(N)) overall
Space Complexity: O(N) for the diff array
"""


# -------------------------------------- Solution -----------------------------------------------


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input().strip()
    diff = [1 if S[i] != S[i + 1] else 0 for i in range(N - 1)]
    current = sum(diff[:K])
    answer = current
    for i in range(K, N - 1):
        current += diff[i]
        current -= diff[i - K]
        answer += current
    print(answer)
