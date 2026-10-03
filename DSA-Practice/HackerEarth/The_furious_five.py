"""
Problem   : The Furious Five
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-furious-five-69521576/
Difficulty: Easy
Topics    : Binary Search, Searching, Math
Date      : 2026-10-03

Approach:
    The number of trailing zeros in p! is floor(p/5) + floor(p/25) + floor(p/125) + ...
    This count never decreases as p grows, so binary search works. We search
    for the smallest p whose count is >= n. The upper bound 5*n is always
    enough, since (5n)! has at least n trailing zeros.

Complexity (per test case):
    Time  : O(log^2 n). The binary search takes O(log n) steps and each
            count takes O(log_5 n).
    Space : O(1)
"""


# -------------------------------------- Solution -------------------------------------------


import sys

def sum_f(p):
    total = 0
    while p > 0:
        p //= 5
        total += p
    return total

def find_p(n):
    low = 1
    high = 5 * n
    while low < high:
        mid = (low + high) // 2
        if sum_f(mid) >= n:
            high = mid
        else:
            low = mid + 1
    return low

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(find_p(n))
