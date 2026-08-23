"""
Problem: Monitor
Platform: Codeforces
Link: https://codeforces.com/problemset/problem/16/C
Difficulty: *1800
Topics: Binary Search, Number Theory
Date: 2026-08-23

Approach:
Reduce x:y to lowest terms using gcd(x, y). The largest valid monitor
size (w, h) with w:h == x:y and w <= a, h <= b is k*(x, y), where
k = min(a // x, b // y) after reduction. If k == 0, no valid monitor
exists, so output "0 0".

Time Complexity: O(log(min(x, y))) — dominated by the gcd computation
Space Complexity: O(1)
"""


# --------------------------- Solution ------------------------------


import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    a, b, x, y = map(int, input_data)
    g = math.gcd(x, y)
    x //= g
    y //= g
    k = min(a // x, b // y)
    if k > 0:
        print(f"{k * x} {k * y}")
    else:
        print("0 0")

if __name__ == "__main__":
    solve()
