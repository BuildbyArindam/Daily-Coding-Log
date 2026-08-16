"""
Problem   : Iskander and Drawings
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/2244/A
Rating    : 800
Tags      : dp, games, greedy, strings
Date      : 2026-08-16

Approach:
    For each test case, scan the string once and track the length of the
    longest contiguous run of '#' characters (a "line"). Since the line is
    erased from both ends simultaneously (1 cm removed from each side per
    second), the number of seconds to fully erase a line of length L is
    ceil(L / 2), computed here as (L + 1) // 2. Track the running max as
    we scan and apply the formula once at the end for the longest run.

Complexity:
    Time  : O(n) per test case, O(sum of n) overall
    Space : O(1) extra (excluding input storage)
"""


# --------------------- Solution ------------------------


import sys

def solve():
    data = sys.stdin.read().split()
    idx = 1
    t = int(data[0])
    results = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        max_len = 0
        current_len = 0
        for char in s:
            if char == '#':
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0
        results.append((max_len + 1) // 2)
    print('\n'.join(map(str, results)))

if __name__ == '__main__':
    solve()
