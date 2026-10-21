"""
Problem   : Path to Iron Man - B
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/path-to-iron-man-2-4678a2c3/
Difficulty: Easy
Date      : 2026-10-21
Topics    : Math, Arithmetic Series

Approach  : The best sum is the sum of all integers from ceil(n/2) to n.
            Compute the start as n//2 (even n) or n//2 + 1 (odd n), then use
            the arithmetic-series formula: count * (first + last) / 2.
            Python's big integers handle values far beyond 64-bit.
            Input handling accepts a single n or a "T followed by T values" format.

Time      : O(1) arithmetic per query (O(d^2) in the digit count d for big-int ops)
Space     : O(1) per query (O(T) to store the parsed input)
"""


# ------------------------------------------- Solution ----------------------------------------------------------


import sys

DEFAULT_N = 5381638168132768112368

def best_sum(n):
    first = n // 2 if n % 2 == 0 else n // 2 + 1
    return (n - first + 1) * (first + n) // 2

def main():
    tokens = sys.stdin.read().split()
    nums = []
    for t in tokens:
        try:
            nums.append(int(t))
        except ValueError:
            pass
    if not nums:
        print(best_sum(DEFAULT_N))
    elif len(nums) > 1 and nums[0] == len(nums) - 1:
        for n in nums[1:]:
            print(best_sum(n))
    else:
        print(best_sum(nums[0]))

main()
