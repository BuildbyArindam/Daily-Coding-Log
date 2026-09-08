"""
Problem   : Interesting Sequence
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/40/D
Date      : 2026-09-08
Difficulty: *2600
Topic     : Math

Approach:
    Every value in the sequence has the form 12^a + 12^b (a <= b).
    Given A, find (k, m) with 12^k + 12^m == A by generating all
    powers of 12 up to A (at most ~O(log_12 A) of them, since 12^k
    grows fast) and checking all (i, j) pairs. If found, the "year"
    is k + m + 1, and every valid value for that year has exponent
    pair (a, b) with a + b == k + m, i.e. all 12^a + 12^(s-a) for
    a in [0, s]. Collect and dedupe those, capped at 1000, and print.

Complexity:
    Let P = number of powers of 12 generated (P = O(log_12 A), tiny
    even for large A, e.g. ~19 for A up to 10^20).
    Time  : O(P^2) for the pair search + O(s) = O(P) for building the
            year's answer set -> O(P^2) overall.
    Space : O(P) for the powers list and the collected values.
"""


# ------------------------ Solution -----------------------------


import sys

def solve():
    A = int(sys.stdin.readline().strip())
    powers = [1]
    while powers[-1] <= A:
        powers.append(powers[-1] * 12)
    k = m = -1
    for i in range(len(powers)):
        for j in range(i, len(powers)):
            value = powers[i] + powers[j]
            if value == A:
                k, m = i, j
                break
            if value > A:
                break
        if k != -1:
            break
    if k == -1:
        print("NO")
        return
    year = k + m + 1
    print("YES")
    print(1)
    print(year)
    s = k + m
    while len(powers) <= s:
        powers.append(powers[-1] * 12)
    values = []
    for a in range(s + 1):
        b = s - a
        value = powers[a] + powers[b]
        if value != A:
            values.append(value)
    values = sorted(set(values))
    values = values[:1000]
    print(len(values))
    for value in values:
        print(value)

if __name__ == "__main__":
    solve()
