"""
Problem   : K Devices
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/k-devices-96ab1c02/
Difficulty: Easy
Topic     : Basic Programming / Implementation
Date      : 2026-08-20

Approach:
    For each device i, compute its squared Euclidean distance from origin
    (x[i]^2 + y[i]^2) to avoid floating point error during comparison.
    Sort all squared distances, pick the k-th smallest (0-indexed k-1).
    Take sqrt of that value and round up (ceil) to get the minimum radius
    needed to cover at least k devices.

Time Complexity : O(n log n)  -> dominated by sorting the distance array
Space Complexity: O(n)        -> storing x, y, and dist_sq arrays
"""


# --------------------------- Solution --------------------------------


import math
import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    k = int(input_data[1])
    x = [int(val) for val in input_data[2 : 2 + n]]
    y = [int(val) for val in input_data[2 + n : 2 + 2 * n]]
    dist_sq = [x[i] ** 2 + y[i] ** 2 for i in range(n)]
    dist_sq.sort()
    kth_dist_sq = dist_sq[k - 1]
    ans = math.ceil(math.sqrt(kth_dist_sq))
    print(ans)

if __name__ == "__main__":
    solve()
