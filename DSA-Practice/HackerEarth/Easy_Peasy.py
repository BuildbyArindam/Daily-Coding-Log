"""
Problem: Easy Peasy
Platform: HackerEarth
Link: https://www.hackerearth.com/problem/algorithm/easy-peasy-1/
Difficulty: Medium
Topic: Implementation
Date: 2026-08-25

Approach:
Given a and b, reduce them by their GCD to get the smallest pair (x, y)
in the same ratio as (b, a) — i.e., swap and divide each by gcd(a, b).

Time Complexity: O(log(min(a, b))) per test case, for the GCD computation
Space Complexity: O(1) extra (excluding output buffer)
"""


# -------------------------- Solution -------------------------------


import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2
        common_gcd = math.gcd(a, b)
        x = b // common_gcd
        y = a // common_gcd
        out.append(f"{x} {y}")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
