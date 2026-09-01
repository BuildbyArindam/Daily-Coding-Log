"""
Problem   : Champagne Tower
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHPWR
Date      : 2026-09-01
Difficulty: Cakewalk / Easy
Topics: Dynamic Programming, Simulation, Matrix/Grid DP, Basic Math

Approach  : Simulate liquid overflow through a triangular tower of glasses using
            a 2D DP table. dp[r][c] holds the amount of champagne (in glass-units)
            that has flowed into the glass at row r, column c. Any amount over 1.0
            overflows equally to the two glasses below it in the next row.
            Answer is min(1.0, dp[R][C]) since a glass can hold at most 1 unit.
Complexity: Time  O(R^2)  — R rows, up to R glasses per row
            Space O(R^2)  — fixed 100x100 DP table (could be reduced to O(R) with
                            two rolling rows if memory were tight)
"""


# ------------------------ Solution ---------------------------------


P, R, C = map(int, input().split())
dp = [[0.0] * 100 for _ in range(100)]
dp[0][0] = float(P)
for r in range(R):
    for c in range(r + 1):
        if dp[r][c] > 1.0:
            overflow = dp[r][c] - 1.0
            dp[r + 1][c] += overflow / 2.0
            dp[r + 1][c + 1] += overflow / 2.0
answer = min(1.0, dp[R][C])
print(f"{answer:.5f}")
