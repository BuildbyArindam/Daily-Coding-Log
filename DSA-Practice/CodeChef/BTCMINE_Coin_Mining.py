"""
Problem: Coin Mining
Platform: CodeChef
Link: https://www.codechef.com/problems/BTCMINE
Date solved: 2026-09-10
Difficulty: Easy-Medium
Topics: Math, Greedy, Simulation

Approach:
For each test case (X = upgrade cost/level, Y = revenue per hash-unit/day),
find the smallest `day` such that some upgrade level k (1 <= k <= day)
yields positive profit:
    revenue = Y * (sum of squares 1..k  +  (day - k) * k^2)
    cost    = X * k
    profit  = revenue - cost
Brute-force day by day, and for each day, brute-force every possible k.

Time complexity:  O(D^2) per test case, where D is the answer day
                   (recomputes sum_sq for k=1..day on every day iteration)
Space complexity: O(1) extra space per test case
"""


# --------------------------- Solution ---------------------------------------


T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    day = 1
    while True:
        best_profit = 0
        sum_sq = 0
        for k in range(1, day + 1):
            sum_sq += k * k
            revenue = Y * (sum_sq + (day - k) * k * k)
            cost = X * k
            profit = revenue - cost
            best_profit = max(best_profit, profit)
        if best_profit > 0:
            print(day)
            break
        day += 1
