"""
Problem: Bear and Medals
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/bear-and-medals/
Date: 2026-08-27
Difficulty: Easy
Topics: Ad-Hoc, Implementation

Approach:
For each test case, sum the gold, silver, and bronze medals across all
friends separately, and also track the max total medals held by any
single friend. The answer is the maximum among these four values —
either one medal type collectively beats individual totals, or one
friend's combined haul is the largest.

Time Complexity: O(N) per test case, O(sum of N) overall
Space Complexity: O(1) extra (excluding input buffer)
"""


# ------------------------- Solution -----------------------------


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
        N = int(data[idx])
        idx += 1
        total_g = 0
        total_s = 0
        total_b = 0
        max_friend_medals = 0
        for _ in range(N):
            g = int(data[idx])
            s = int(data[idx+1])
            b = int(data[idx+2])
            idx += 3
            total_g += g
            total_s += s
            total_b += b
            max_friend_medals = max(max_friend_medals, g + s + b)
        ans = max(total_g, total_s, total_b, max_friend_medals)
        out.append(str(ans))
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
