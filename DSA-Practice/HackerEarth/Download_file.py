"""
Platform   : HackerEarth
Problem    : Download file
Link       : http://hackerearth.com/practice/algorithms/searching/ternary-search/practice-problems/algorithm/download-file-b0fe3520/
Difficulty : Medium
Topics     : Prefix Sums, Binary Search, Math (exact fractions)
Date       : 2026-10-15

Approach:
  Speed is piecewise constant, so the data downloaded as a function of
  time is piecewise linear. For a fixed size s, the download time as a
  function of the start moment is piecewise linear too, so the minimum is
  reached when either the start or the end of the window lies on a
  breakpoint T[i].
    1. Build prefix array P[i] = data downloaded by time T[i].
    2. Start at each breakpoint T[i]: binary search the segment holding
       P[i] + s and compute the finish time.
    3. End at each breakpoint T[j]: binary search the segment holding
       P[j] - s and compute the start time.
    4. Keep the minimum duration as an exact fraction (cross-multiplied
       comparison, no floats) and print it reduced by gcd.

Time  : O(n log n)  (2n binary searches over P)
Space : O(n)
"""


# ---------------------------------------------- Solution ------------------------------------------------------------


import sys
from bisect import bisect_right
from math import gcd

def main():
    data = sys.stdin.read().split()
    n, s = int(data[0]), int(data[1])
    T = [int(data[2 + 2*i]) for i in range(n)]
    D = [int(data[3 + 2*i]) for i in range(n)]
    P = [0] * n
    for i in range(1, n):
        P[i] = P[i-1] + (T[i] - T[i-1]) * D[i-1]
    best = None  
    def consider(num, den):
        nonlocal best
        if best is None or num * best[1] < best[0] * den:
            best = (num, den)
    for i in range(n):
        target = P[i] + s
        k = bisect_right(P, target) - 1   
        num = (T[k] - T[i]) * D[k] + (target - P[k])
        consider(num, D[k])
    for j in range(1, n):
        target = P[j] - s
        if target < 0:
            continue
        k = bisect_right(P, target) - 1
        num = (T[j] - T[k]) * D[k] - (target - P[k])
        consider(num, D[k])
    a, b = best
    g = gcd(a, b)
    print(f"{a // g}/{b // g}")

main()
