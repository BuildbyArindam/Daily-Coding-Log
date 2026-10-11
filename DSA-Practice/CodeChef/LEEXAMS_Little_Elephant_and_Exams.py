"""
Platform   : CodeChef
Problem    : Little Elephant and Exams (LEEXAMS)
Link       : https://www.codechef.com/problems/LEEXAMS
Difficulty : 1810
Topics     : Bitmask DP, Probability
Date       : 2026-10-11

Approach:
    Each exam i has a ticket with number A_i (probability P_i%) or B_i
    (probability 100-P_i %). We need the probability that all N tickets
    are distinct. Ticket numbers are at most 16, so we track the set of
    numbers already used as a bitmask. dp[mask] = probability of reaching
    that set of used numbers. For each exam, try A (if unused) and B (if
    unused), adding the weighted probability to the new mask. Branches
    that hit a used number are dropped, so the final answer is the sum of
    all remaining dp values. If N > 16, no valid state survives and the
    answer is 0.

Complexity:
    Time  : O(N * 2^M), M = 16 (max distinct ticket numbers),
            in practice far fewer states since masks after step k
            have exactly k bits set.
    Space : O(2^M) for the dp dictionary.
"""


# ----------------------------------------- Solution -------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        tickets = []
        for i in range(n):
            P, A, B = map(int, input().split())
            tickets.append((P / 100.0, A, B))
        dp = {0: 1.0}
        for P, A, B in tickets:
            ndp = {}
            for mask, prob in dp.items():
                bitA = 1 << (A - 1)
                if not (mask & bitA):
                    new_mask = mask | bitA
                    ndp[new_mask] = (
                        ndp.get(new_mask, 0.0) + prob * P
                    )
                bitB = 1 << (B - 1)
                if not (mask & bitB):
                    new_mask = mask | bitB
                    ndp[new_mask] = (
                        ndp.get(new_mask, 0.0) + prob * (1.0 - P)
                    )
            dp = ndp
        print(f"{sum(dp.values()):.9f}")

if __name__ == "__main__":
    solve()
