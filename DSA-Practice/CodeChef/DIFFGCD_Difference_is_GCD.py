"""
Problem   : Difference is GCD
Platform  : CodeChef (DIFFGCD)
Link      : https://www.codechef.com/problems/DIFFGCD
Date      : 2026-10-14
Difficulty: Easy
Topics    : Math, Number Theory

Approach  : The answer reduces to D(m) - m, where D(m) = sum(m // i for i in 1..m).
            D(m) is computed with the hyperbola method: floor(m/i) takes only
            O(sqrt(m)) distinct values, so
            D(m) = 2 * sum(m // j for j in 1..r) - r^2, where r = isqrt(m).
            Subtracting m removes the i = 1 term.

Time      : O(sqrt(N)) per test case, O(T * sqrt(N)) overall
Space     : O(1) extra per test case (O(T) to store inputs and outputs)
"""


# ------------------------------------------- Solution ------------------------------------------------------


import sys
from math import isqrt

def harmonic_floor_total(m):
    r = isqrt(m)
    acc = 0
    for j in range(1, r + 1):
        acc += m // j
    return (acc << 1) - r * r

def solve_one(m):
    return harmonic_floor_total(m) - m

def main():
    tokens = sys.stdin.read().split()
    cases = int(tokens[0])
    values = [int(v) for v in tokens[1:1 + cases]]
    results = list(map(solve_one, values))
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
