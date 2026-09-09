"""
Problem   : Email Address
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/41/C
Difficulty: *1300
Date Solved: 2026-09-09

Approach:
    DP over string positions, tracking whether '@' has been used yet.
    dp[i][j] = lexicographically smallest, then shortest, valid decoded
    prefix after consuming i input characters, having placed j '@' signs
    (j in {0, 1}). At each position we try three transitions:
        1. Keep the current character as-is (a normal letter/digit).
        2. If the substring "dot" starts here (and isn't at position 0
           or flush against the end), replace it with '.'.
        3. If the substring "at" starts here, no '@' used yet, and it
           isn't at position 0 or flush against the end, replace it
           with '@' (only one allowed, per email format rules).
    "better()" enforces the tie-break: prefer shorter strings, and among
    equal-length strings prefer the lexicographically smaller one — this
    greedily builds the required output ordering.
    Answer is dp[n][1] (must have consumed the whole string with exactly
    one '@' used).

Time Complexity : O(n^2) worst case
    - n+1 positions x 2 states = O(n) DP cells.
    - Each transition builds a new string via cur + ch, which is O(len(cur));
      strings can grow up to O(n), so total work is O(n^2) in the worst case.

Space Complexity: O(n^2) worst case
    - Each of the O(n) DP cells can hold a string of length up to O(n).
"""


# ------------------------ Solution ---------------------------------


import sys

def solve():
    s = input().strip()
    n = len(s)
    dp = [[None] * 2 for _ in range(n + 1)]
    dp[0][0] = ""
    def better(a, b):
        if b is None:
            return True
        if len(a) != len(b):
            return len(a) < len(b)
        return a < b
    for i in range(n + 1):
        for at_count in range(2):
            cur = dp[i][at_count]
            if cur is None:
                continue
            if i < n:
                new = cur + s[i]
                if better(new, dp[i + 1][at_count]):
                    dp[i + 1][at_count] = new
            if s.startswith("dot", i):
                if i != 0 and i + 3 != n:
                    new = cur + "."
                    if better(new, dp[i + 3][at_count]):
                        dp[i + 3][at_count] = new
            if s.startswith("at", i) and at_count == 0:
                if i != 0 and i + 2 != n:
                    new = cur + "@"
                    if better(new, dp[i + 2][1]):
                        dp[i + 2][1] = new
    print(dp[n][1])

if __name__ == "__main__":
    solve()
