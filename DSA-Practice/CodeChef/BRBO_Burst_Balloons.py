"""
Problem   : Burst Balloons
Platform  : CodeChef
Link      : https://www.codechef.com/DSAMONDAY021/problems/BRBO
Date      : 2026-09-21
Difficulty: Hard
Topics    : Dynamic Programming, Interval DP

Approach:
    Pad the balloon array with 1s on both ends (virtual boundary balloons).
    For every subrange (left_idx, right_idx), try each balloon k as the LAST
    one burst in that range — its neighbors at burst time are the padded
    boundaries left_idx and right_idx, since everything between them has
    already been cleared. Build up answers over increasing interval widths
    (gap) so smaller subproblems are solved before larger ones.

    Recurrence:
        dp[l][r] = max over k in (l, r) of:
                   padded[l]*padded[k]*padded[r] + dp[l][k] + dp[k][r]

Complexity:
    Time : O(n^3)  -> three nested loops (gap, left_idx, k)
    Space: O(n^2)  -> dp_table of size (n+2) x (n+2)
"""


# ---------------------------------------- Solution --------------------------------------------


import sys

def compute_max_coins(balloon_values):
    total_balloons = len(balloon_values)
    if total_balloons == 0:
        return 0
    padded = [1] + balloon_values + [1]
    size = total_balloons + 2
    dp_table = [[0] * size for _ in range(size)]
    for gap in range(2, size):
        left_idx = 0
        while left_idx + gap < size:
            right_idx = left_idx + gap
            best_here = 0
            k = left_idx + 1
            while k < right_idx:
                gained = padded[left_idx] * padded[k] * padded[right_idx]
                gained += dp_table[left_idx][k] + dp_table[k][right_idx]
                if gained > best_here:
                    best_here = gained
                k += 1
            dp_table[left_idx][right_idx] = best_here
            left_idx += 1
    return dp_table[0][size - 1]

def read_input_and_solve():
    data = sys.stdin.read().split()
    if not data:
        return
    idx = 0
    n = int(data[idx]); idx += 1
    arr = []
    for _ in range(n):
        arr.append(int(data[idx])); idx += 1
    answer = compute_max_coins(arr)
    print(answer)

if __name__ == "__main__":
    read_input_and_solve()
