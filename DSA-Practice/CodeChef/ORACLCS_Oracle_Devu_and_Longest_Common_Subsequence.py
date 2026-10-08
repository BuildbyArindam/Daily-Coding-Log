"""
Problem   : Oracle Devu and Longest Common Subsequence (ORACLCS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ORACLCS
Difficulty: 1726
Topics    : Strings, Counting, Greedy
Date      : 2026-10-08

Approach  : Only the counts of 'a' and 'b' in each string matter. For every
            string, count its 'a's and 'b's, and keep the minimum count of
            each letter across all strings. The answer is
            min(min_a, min_b).

Complexity: Time  O(total length of all strings), a single pass with str.count
            Space O(1) extra (one string held at a time)
"""


# ------------------------------------- Solution --------------------------------------------------


import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    min_a = 10**9
    min_b = 10**9
    for _ in range(n):
        s = input().strip()
        cnt_a = s.count('a')
        cnt_b = len(s) - cnt_a
        min_a = min(min_a, cnt_a)
        min_b = min(min_b, cnt_b)
    print(min(min_a, min_b))
