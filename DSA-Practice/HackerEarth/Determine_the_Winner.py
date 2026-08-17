"""
Problem: Determine the Winner
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/problem-16-b45b3a5d/
Difficulty: Medium
Topic: Basic Programming, Implementation

Date Solved: 2026-08-17

Approach:
For each of the 4 problems, compute the penalized score for both Flash and 
Cisco: score = max(min_score, s[i] - penalty[i] * d[i]), where min_score is 
half the original score (score can't drop below 50%). Sum penalized scores 
per team across all 4 problems. Higher total score wins; on a tie, compare 
the max time taken (max of the four per-problem times) — lower time wins; 
if still tied, declare "Tie".

Time Complexity: O(T) — each test case does O(1) work (fixed 4 problems)
Space Complexity: O(1) extra space per test case (excluding input storage)
"""


# ----------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    t = int(input_data[0])
    idx = 1
    out = []
    for _ in range(t):
        s = [int(x) for x in input_data[idx : idx + 4]]
        d = [int(x) for x in input_data[idx + 4 : idx + 8]]
        f = [int(x) for x in input_data[idx + 8 : idx + 12]]
        c = [int(x) for x in input_data[idx + 12 : idx + 16]]
        idx += 16
        flash_score = 0
        cisco_score = 0
        for i in range(4):
            min_score = s[i] // 2
            flash_p_score = max(min_score, s[i] - f[i] * d[i])
            cisco_p_score = max(min_score, s[i] - c[i] * d[i])
            flash_score += flash_p_score
            cisco_score += cisco_p_score
        flash_time = max(f)
        cisco_time = max(c)
        if flash_score > cisco_score:
            out.append("Flash")
        elif cisco_score > flash_score:
            out.append("Cisco")
        else:
            if flash_time < cisco_time:
                out.append("Flash")
            elif cisco_time < flash_time:
                out.append("Cisco")
            else:
                out.append("Tie")
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
