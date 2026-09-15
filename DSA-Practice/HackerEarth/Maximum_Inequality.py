"""
Problem   : Maximum Inequality
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-inequality-b002b193/
Difficulty: Easy
Topics    : Linear Search, Implementation, Greedy, DP
Date      : 2026-09-15

Approach:
    Split the string into two interleaved subsequences (two "pointers"),
    where each incoming character is appended to either pointer A or
    pointer B. Track state as (last_char_of_A, last_char_of_B) and the
    accumulated count of adjacent unequal transitions. At each character,
    branch into both choices and keep the best value per state (DP over
    a small state space since digits are bounded, 0-9). Answer is the
    max value across all final states.

Complexity:
    Time : O(N * D^2)  where D = number of distinct digits (<=10),
           effectively O(N) since D is constant.
    Space: O(D^2) for the DP dictionary at any step.
"""


# ---------------------------- Solution ---------------------------------------


def solve(N, S):
    dp = {(-1, -1): 0}
    for ch in S:
        x = int(ch)
        ndp = {}
        for (a, b), val in dp.items():
            gain = 0 if a == -1 else (a != x)
            state = (x, b)
            ndp[state] = max(ndp.get(state, -10**9), val + gain)
            gain = 0 if b == -1 else (b != x)
            state = (a, x)
            ndp[state] = max(ndp.get(state, -10**9), val + gain)
        dp = ndp
    return max(dp.values())

T = int(input())
for _ in range(T):
    N = int(input())
    S = input().strip()

    out_ = solve(N, S)
    print(out_)
