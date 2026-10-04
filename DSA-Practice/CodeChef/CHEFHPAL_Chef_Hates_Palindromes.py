"""
Problem   : Chef Hates Palindromes (CHEFHPAL)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHEFHPAL
Difficulty: 1804
Topics    : String, Observation, Brute Force, Data Structures, Algorithms
Date      : 2026-10-04

Approach:
    Build a length-N string over an alphabet of size A that minimizes the
    length of its longest palindromic substring, using a case split on A.
      - A == 1: only one letter exists, so the whole string is a palindrome
                (answer N).
      - A == 2: small N uses hand-found optimal patterns ("ab", "aabb",
                "aaababbb", giving answers 1, 2, 3). For N > 8 the periodic
                pattern "aababb" repeated keeps the longest palindrome at 4.
      - A >= 3: repeat "abc". It has no palindromes of length 2 or 3, so
                the answer is 1.

Time Complexity : O(N) per test case (string construction)
Space Complexity: O(N) for the output string
"""


# --------------------------------------- Solution ------------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, A = map(int, input().split())
        if A == 1:
            s = 'a' * N
            print(N, s)
        elif A == 2:
            if N <= 2:
                s = 'ab'[:N]
                print(1, s)
            elif N <= 4:
                s = 'aabb'[:N]
                print(2, s)
            elif N <= 8:
                s = 'aaababbb'[:N]
                print(3, s)
            else:
                s = ('aababb' * ((N + 5) // 6))[:N]
                print(4, s)
        else:
            s = ''.join(chr(ord('a') + (i % 3)) for i in range(N))
            print(1, s)

if __name__ == "__main__":
    solve()
