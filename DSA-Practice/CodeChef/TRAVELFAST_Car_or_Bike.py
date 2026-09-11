"""
Problem   : Car or Bike
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/TRAVELFAST
Date      : 2026-09-11
Difficulty: Easy (rating 571)
Topics    : Basic Math, Conditional Logic, Implementation

Approach:
For each test case, compare travel times X (car) and Y (bike).
Whichever value is smaller means that mode of transport is faster.
If both are equal, neither has an advantage -> "SAME".
Simple if-elif-else comparison, no data structures needed.

Time Complexity : O(T) — one comparison per test case
Space Complexity: O(1) — only a few integer variables used
"""


# --------------------------- Solution ------------------------------------


T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    if X < Y:
        print("BIKE")
    elif Y < X:
        print("CAR")
    else:
        print("SAME")
