"""
Problem: Platforms
Link: https://codeforces.com/problemset/problem/18/B
Date: 2026-08-25
Difficulty: *1700
Topics: Brute Force, Math

Approach:
Simulate jumps platform by platform. For each platform k, compute the
earliest point (platform_end) the frog could be at if it uses all of
platform k, then find the next jump position that's a multiple of d
strictly greater than platform_end. If that jump lands before the start
of platform (k+1) (i.e., cur_jump < k*m), the frog can land there safely
mid-jump — print and stop. Otherwise keep advancing platform by platform.

Time Complexity:  O(n)      — single pass over platforms
Space Complexity: O(1)      — constant extra space
"""


# ------------------------ Solution -----------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    d = int(input_data[1])
    m = int(input_data[2])
    l = int(input_data[3])
    cur_jump = 0
    for k in range(1, n + 1):
        platform_end = (k - 1) * m + l
        cur_jump = ((platform_end // d) + 1) * d
        if cur_jump < k * m:
            print(cur_jump)
            return
    print(cur_jump)

if __name__ == "__main__":
    solve()
