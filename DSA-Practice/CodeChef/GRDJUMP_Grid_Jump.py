"""
Problem: Grid Jump
Platform: CodeChef
Link: https://www.codechef.com/problems/GRDJUMP
Date: 2026-08-27

Approach:
Standard bottom-up 2D DP. dp[i][j] = minimum cost to reach cell (i, j)
starting from (0, 0), where moves allowed are:
    - jump 1 or 2 steps along the A-axis, cost P
    - jump 1 or 2 steps along the B-axis, cost Q
    - diagonal jump (1,1), cost R
For each cell, take the minimum over all valid incoming transitions.
Answer is dp[A][B].

Time Complexity:  O(A * B) per test case
Space Complexity: O(A * B) per test case (can be optimized to O(B) with rolling rows)
"""


# -------------------------- Solution --------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    out = []
    for _ in range(T):
        A = int(data[idx])
        B = int(data[idx+1])
        P = int(data[idx+2])
        Q = int(data[idx+3])
        R = int(data[idx+4])
        idx += 5
        INF = float('inf')
        dp = [[INF] * (B + 1) for _ in range(A + 1)]
        dp[0][0] = 0
        for i in range(A + 1):
            for j in range(B + 1):
                if i == 0 and j == 0:
                    continue
                res = INF
                if i - 1 >= 0:
                    res = min(res, dp[i - 1][j] + P)
                if i - 2 >= 0:
                    res = min(res, dp[i - 2][j] + P)
                if j - 1 >= 0:
                    res = min(res, dp[i][j - 1] + Q)
                if j - 2 >= 0:
                    res = min(res, dp[i][j - 2] + Q)
                if i - 1 >= 0 and j - 1 >= 0:
                    res = min(res, dp[i - 1][j - 1] + R)
                dp[i][j] = res
        out.append(str(dp[A][B]))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
