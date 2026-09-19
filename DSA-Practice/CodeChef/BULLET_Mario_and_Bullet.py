"""
Problem   : Mario and Bullet
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/BULLET
Difficulty: 650
Date      : 2026-09-19
Topics    : Math, Simulation

Approach:
    Mario needs Z seconds to reach the target. The bullet travels at speed X units/sec
    over distance Y, taking (Y // X) seconds to arrive. If the bullet arrives before
    Mario reaches the target (travel_time < Z), Mario must wait out the difference
    before it's safe; otherwise no wait is needed. Answer = max(0, Z - travel_time).

Time Complexity : O(1) per test case -> O(T) overall
Space Complexity: O(1)
"""


# --------------------------------------- Solution ------------------------------------------------------


T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    travel_time = Y // X
    answer = max(0, Z - travel_time)
    print(answer)
