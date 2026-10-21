"""
Problem   : Path to Iron Man - A
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/path-to-iron-man-1-02245c26/
Difficulty: Easy
Topics    : Math, Arithmetic Series
Date      : 2026-10-21

Approach:
    Sum all integers from (N // 2 + 1) to N. Instead of looping, use the
    arithmetic series formula: sum = (first + last) * count / 2.

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ---------------------------------------------- Solution ------------------------------------------------------


import sys

raw = sys.stdin.read().split()
top = int(raw[0]) if raw else 74361491
start = top // 2 + 1
how_many = top - start + 1
total = (start + top) * how_many // 2
print(total)
