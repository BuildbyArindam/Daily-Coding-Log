"""
Problem   : Chef and Pepperoni Pizza (PEPPERON)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/PEPPERON
Difficulty: 1810
Topics    : Implementation, Math
Date      : 2026-10-11

Approach:
    Split each row into a left half and a right half. Let d_i = (pepperoni in
    left half) - (pepperoni in right half) for row i, and diff = sum of all d_i.
    Swapping the two halves of row i changes the total difference by -2 * d_i.
    Start with |diff| as the baseline, then try every row and keep the minimum
    of |diff - 2 * d_i|.

Complexity:
    Time : O(n^2) per test case (each cell is counted a constant number of times)
    Space: O(n^2) to store the grid, O(1) extra
"""


# ------------------------------------------------ Solution --------------------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())
    grid = [input().strip() for _ in range(n)]
    diff = 0
    for row in grid:
        left = row[:n // 2].count('1')
        right = row[n // 2:].count('1')
        diff += left - right
    ans = abs(diff)
    for row in grid:
        left = row[:n // 2].count('1')
        right = row[n // 2:].count('1')
        new_diff = diff - 2 * (left - right)
        ans = min(ans, abs(new_diff))
    print(ans)
