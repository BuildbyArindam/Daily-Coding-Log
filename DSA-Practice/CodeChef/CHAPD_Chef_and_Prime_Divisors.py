"""
Problem   : Chef and Prime Divisors (CHAPD)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHAPD
Difficulty: 1720
Date      : 2026-10-02
Topics    : Number Theory, Math, Modular Exponentiation

Approach:
    Every prime divisor of B must also divide A.
    B <= 1e18 < 2^60, so any prime in B's factorization has an exponent of
    at most 59. If all of B's primes divide A, then A^59 contains every
    such prime with exponent >= 59, so B | A^59. Conversely, if some prime
    of B doesn't divide A, it can't divide A^59 either.
    So the check is pow(A, 59, B) == 0, with B == 1 handled as a special case.
    This avoids factorizing B entirely.

Complexity:
    Time : O(T * log 59) modular multiplications, effectively O(T)
    Space: O(1)
"""


# ----------------------------------- Solution -------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        if B == 1:
            print("Yes")
        else:
            if pow(A, 59, B) == 0:
                print("Yes")
            else:
                print("No")

if __name__ == "__main__":
    solve()
