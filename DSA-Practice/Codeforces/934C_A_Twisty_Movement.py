"""
Problem   : A Twisty Movement (934C)
Platform  : Codeforces
Link      : https://codeforces.com/contest/934/problem/C
Solved    : 2026-08-15
Difficulty: 1800
Topics    : brute force, dp, implementation

Approach:
Reversing a subsegment never changes the multiset of the array — it only
lets us reorder elements freely within that window. So the real question
becomes: what's the longest subsequence we can "assemble" that matches the
pattern 1*2*1* (some 1s, then some 2s, then some 1s again)? Everything
outside that subsequence gets removed, and the answer is n minus the
removed count (equivalently, we just maximize the kept length here and the
final answer follows from it).

We track this with a 4-state rolling DP over the pattern's phases:
  dp[0] -> run of leading 1s
  dp[1] -> 1s followed by 2s
  dp[2] -> 1s, then 2s, then 1s again
  dp[3] -> closing/terminal state, captures the best across the pattern

Each state is updated greedily by either extending the current phase or
transitioning in from the previous phase, taking the max.

Time complexity : O(n) — single pass over the array
Space complexity: O(1) — fixed-size dp array of length 4
"""


# --------------------- Solution ---------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    a = [int(x) for x in input_data[1:n + 1]]
    dp = [0, 0, 0, 0]
    for x in a:
        if x == 1:
            dp[0] += 1
            dp[1] = max(dp[1], dp[0])
            dp[2] = max(dp[2] + 1, dp[1])
            dp[3] = max(dp[3], dp[2])
        else:
            dp[1] = max(dp[1] + 1, dp[0])
            dp[2] = max(dp[2], dp[1])
            dp[3] = max(dp[3] + 1, dp[2])
    print(max(dp))

if __name__ == "__main__":
    solve()
