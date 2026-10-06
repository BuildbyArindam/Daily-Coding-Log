"""
Problem   : Random Merging (IC26AM)
Platform  : CodeChef (ICPCOL26POST)
Link      : https://www.codechef.com/ICPCOL26POST/problems/IC26AM
Date      : 2026-10-06
Difficulty: Medium (~1600-1900 rated)
Topics    : Math, Probability, Expected Value, Modular Inverse, Prefix Sums

Approach  : Linearity of expectation. Each element a[j] contributes with a
            coefficient of H[j] + H[n-1-j], where H[k] is the k-th harmonic
            number mod 998244353 (0-indexed j). Modular inverses 1..maxN are
            precomputed in O(maxN) using inv[v] = -(M//v) * inv[M % v], then
            turned into prefix sums (harmonic numbers). Each test case is
            answered as sum(a[j] * (H[j] + H[n-1-j])) mod M.

Complexity: Time  O(maxN + sum of N) over all test cases
            Space O(maxN + N)
"""


# ----------------------------------------- Solution ------------------------------------------------


import sys

def main():
    M = 998244353
    raw = sys.stdin.buffer.read().split()
    T = int(raw[0])
    pos = 1
    biggest = 1
    for _ in range(T):
        m = int(raw[pos])
        if m > biggest:
            biggest = m
        pos += m + 1
    inv = [0, 1] + [0] * (biggest)
    for v in range(2, biggest + 1):
        inv[v] = (M - (M // v) * inv[M % v] % M) % M
    harm = [0] * (biggest + 2)
    acc = 0
    for v in range(1, biggest + 1):
        acc += inv[v]
        if acc >= M:
            acc -= M
        harm[v] = acc
    out = []
    pos = 1
    while T:
        T -= 1
        n = int(raw[pos])
        arr = raw[pos + 1: pos + 1 + n]
        pos += n + 1
        total = 0
        for j in range(n):
            w = harm[j] + harm[n - 1 - j]
            total = (total + int(arr[j]) * w) % M
        out.append(total)
    sys.stdout.write("\n".join(map(str, out)) + "\n")

main()
