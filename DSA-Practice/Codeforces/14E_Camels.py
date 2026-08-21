"""
Problem   : Camels
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/14/E
Difficulty: *1900
Topic     : Dynamic Programming
Date      : 2026-08-21

Approach:
Count sequences of camel heights (1-4, no two adjacent equal) of length n
that have exactly t humps and t-1 valleys. State tracked via DP over
(prev_height, curr_height, humps_so_far, valleys_so_far), transitioning by
appending next_height and checking the local pattern (prev < curr > next
= hump, prev > curr < next = valley). Final answer sums dp[prev][curr][t][t-1]
over all valid (prev, curr) pairs after processing all n elements.

Complexity:
Time  : O(n * 4 * 4 * t^2) -> effectively O(n) since t is small/bounded
Space : O(4 * 4 * 11 * 11) = O(1) per layer (rolling DP array)

Note: humps/valleys arrays are hardcoded to size 11, so this assumes t <= 10.
If t can exceed 10 per constraints, bump the array bound accordingly.
"""


# --------------------------- Solution -----------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    t = int(data[1])
    dp = [[[[0] * 11 for _ in range(11)] for _ in range(5)] for _ in range(5)]
    for prev in range(1, 5):
        for curr in range(1, 5):
            if prev != curr:
                dp[prev][curr][0][0] = 1
    for i in range(3, n + 1):
        next_dp = [[[[0] * 11 for _ in range(11)] for _ in range(5)] for _ in range(5)]
        for prev in range(1, 5):
            for curr in range(1, 5):
                if prev == curr:
                    continue
                for humps in range(t + 1):
                    for valleys in range(t + 1):
                        count = dp[prev][curr][humps][valleys]
                        if count == 0:
                            continue
                        for next_val in range(1, 5):
                            if next_val == curr:
                                continue
                            is_hump = 1 if (prev < curr and curr > next_val) else 0
                            is_valley = 1 if (prev > curr and curr < next_val) else 0
                            new_humps = humps + is_hump
                            new_valleys = valleys + is_valley
                            if new_humps <= t and new_valleys <= t:
                                next_dp[curr][next_val][new_humps][new_valleys] += count
        dp = next_dp
    ans = 0
    for prev in range(1, 5):
        for curr in range(1, 5):
            if prev != curr:
                ans += dp[prev][curr][t][t - 1]
    print(ans)

if __name__ == '__main__':
    solve()
