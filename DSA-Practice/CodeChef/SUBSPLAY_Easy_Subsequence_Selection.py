"""
Problem   : Easy Subsequence Selection (SUBSPLAY)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SUBSPLAY
Difficulty: 1732
Topics    : Strings, Greedy
Date      : 2026-10-08

Approach:
    Scan the string once, storing the last index of each lowercase letter.
    When a letter repeats, the gap to its previous occurrence is a candidate,
    and we keep the minimum gap over all repeats. If no letter repeats,
    the answer is 0; otherwise it is N - min_gap.

Time Complexity : O(N) per test case
Space Complexity: O(1) extra (fixed 26-entry array), O(N) for the input string
"""


# ----------------------------------------- Solution ---------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        last = [-1] * 26
        min_gap = N
        for i, ch in enumerate(S):
            c = ord(ch) - ord('a')
            if last[c] != -1:
                min_gap = min(min_gap, i - last[c])
            last[c] = i
        if min_gap == N:
            print(0)
        else:
            print(N - min_gap)

if __name__ == "__main__":
    solve()
