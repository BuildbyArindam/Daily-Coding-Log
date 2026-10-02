"""
Problem   : Palindromic Substrings (GPL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GPL
Difficulty: 1723
Topics    : Game Theory, Strings, Observation
Date      : 2026-10-02

Approach:
    The winner depends only on the count of '0's and '1's, not their order.
    Let diff = |zeros - ones|.
      - n == 1: Bob wins (special case).
      - n even: Alice wins iff diff != 0, otherwise Bob.
      - n odd : Alice wins iff diff == 1, otherwise Bob.

Complexity:
    Time  : O(n) per test case (single pass to count characters)
    Space : O(1) extra (besides storing the input string)
"""


# ------------------------------------------- Solution -----------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input().strip()
        if n == 1:
            print("Bob")
            continue
        zeros = s.count('0')
        ones = n - zeros
        diff = abs(zeros - ones)
        if n % 2 == 0:
            print("Alice" if diff != 0 else "Bob")
        else:
            print("Alice" if diff == 1 else "Bob")

if __name__ == "__main__":
    solve()
