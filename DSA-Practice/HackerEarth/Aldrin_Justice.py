"""
Problem   : Aldrin Justice
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/aldrin-justice/
Difficulty: Easy
Topics    : Geometry, Math, Implementation
Date      : 2026-09-09

Approach:
    Treat each spaceship's two given values as an interval on a number line
    (its angular range). The overlap between the two intervals is:
        intersection_start = max(min(bt1,bt2), min(mt1,mt2))
        intersection_end   = min(max(bt1,bt2), max(mt1,mt2))
    - If intersection_start > intersection_end  -> no overlap  -> "Nothing"
    - If intersection_start == intersection_end -> single point -> "Point"
    - Otherwise                                  -> range overlap -> "Line"

Time Complexity : O(1) per test case  -> O(T) overall
Space Complexity: O(1)
"""


# ------------------------ Solution -------------------------------------


T = int(input())
for _ in range(T):
    bt1, bt2, mt1, mt2 = map(int, input().split())
    left = min(max(bt1, bt2), max(mt1, mt2))
    right = max(min(bt1, bt2), min(mt1, mt2))
    if left > right:
        print("Nothing")
    elif left == right:
        print("Point")
    else:
        print("Line")
