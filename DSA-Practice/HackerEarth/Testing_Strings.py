"""
Problem   : Testing Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/testing-strings-d1f28949/
Difficulty: Easy
Topic     : One-dimensional Arrays / String Manipulation
Date      : 2026-08-29

Approach:
  For each character z, collect its forbidden [l, r] index ranges and merge
  overlapping intervals. Use a difference array over positions 1..M to mark
  where each character becomes forbidden (+1 at l, -1 at r+1). Sweep the
  difference array left to right, accumulating how many characters are
  forbidden at each position; the number of valid choices there is
  K - forbidden_count. Multiply valid choice counts across all M positions
  under MOD. If any position has zero or negative allowed choices, the
  answer is 0.

Time complexity : O(N log N + M)  -- sorting intervals per char + one sweep
Space complexity: O(N + M)        -- interval lists + difference array
"""


# ---------------------------- Solution -------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    N = int(data[0])
    M = int(data[1])
    K = int(data[2])
    MOD = 1000003 
    diff = [0] * (M + 2)
    from collections import defaultdict
    char_intervals = defaultdict(list)
    idx = 3
    for _ in range(N):
        l = int(data[idx])
        r = int(data[idx+1])
        z = int(data[idx+2])
        idx += 3
        char_intervals[z].append((l, r))
    for z, intervals in char_intervals.items():
        intervals.sort()
        merged = []
        for l, r in intervals:
            if not merged:
                merged.append([l, r])
            else:
                if l <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], r)
                else:
                    merged.append([l, r])
        for l, r in merged:
            diff[l] += 1
            diff[r + 1] -= 1
    ans = 1
    current_forbidden = 0
    for i in range(1, M + 1):
        current_forbidden += diff[i]
        allowed_choices = K - current_forbidden
        if allowed_choices <= 0:
            ans = 0
            break
        ans = (ans * allowed_choices) % MOD
    print(ans)

if __name__ == '__main__':
    solve()
