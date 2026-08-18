"""
Problem   : Maximum Unique Segment
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MAXSEGM
Solved on : 2026-08-18

Approach:
    Sliding window (two pointers) over the array. Maintain a window [left, right]
    such that all colors in the window are unique. `last_seen[color]` tracks the
    most recent index a color appeared at. When we encounter a color already
    present in the current window, shrink the window from the left, subtracting
    weights, until the duplicate is expelled. Track the running sum of weights
    in the window and update max_sum after each expansion.

Time Complexity  : O(n) per test case — each index enters/leaves the window at most once.
Space Complexity : O(n) — for the last_seen array.
"""


# -------------------------------- Solution ---------------------------------

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        c = [int(x) for x in data[idx : idx + n]]
        idx += n
        w = [int(x) for x in data[idx : idx + n]]
        idx += n
        last_seen = [-1] * n
        max_sum = 0
        current_sum = 0
        left = 0
        for right in range(n):
            color = c[right]
            if last_seen[color] >= left:
                prev_duplicate_idx = last_seen[color]
                while left <= prev_duplicate_idx:
                    current_sum -= w[left]
                    left += 1
            current_sum += w[right]
            last_seen[color] = right
            if current_sum > max_sum:
                max_sum = current_sum
        out.append(str(max_sum))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
