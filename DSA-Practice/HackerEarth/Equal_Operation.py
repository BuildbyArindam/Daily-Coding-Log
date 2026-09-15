"""
Problem: Equal Operation
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/equal-operation-2-95be3ed1/
Difficulty: Easy
Topic: Math, Algorithms, Linear Search
Date Solved: 2026-09-15

Approach:
Compute the GCD (g) of all elements and their sum (total). Since every
element must eventually become a multiple of g, the minimum number of
final elements needed to sum to 'total' using value g each is total // g.
The number of operations (merges) required to go from N elements down to
that count is therefore (total // g) - N.

Time Complexity: O(N log(max(A))) per test case (GCD computation dominates)
Space Complexity: O(1) extra space (excluding input storage O(N))
"""


# -------------------------- Solution ---------------------------------------


import sys
from math import gcd
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    g = 0
    total = 0
    for x in A:
        g = gcd(g, x)
        total += x
    ans = total // g - N
    print(ans)
