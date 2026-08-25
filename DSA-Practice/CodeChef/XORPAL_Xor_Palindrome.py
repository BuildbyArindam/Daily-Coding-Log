"""
Problem   : Xor Palindrome (XORPAL)
Platform  : CodeChef (Feb Long Challenge 2022 - II)
Link      : https://www.codechef.com/problems/XORPAL
Date      : 2026-08-25
Difficulty: Easy / Cakewalk (official: Simple)
Topics    : Bit Manipulation (XOR), Parity, String, Math

Approach:
  A binary string is an "xor palindrome" if S[i] ^ S[N+1-i] is constant
  for all i. This reduces to a parity check on the count of 1s ('ones'):
    - N odd  -> ones and (N - ones) always differ in parity, so the
                required condition always holds -> always "YES".
    - N even -> "YES" iff ones is even (both halves balance out) or
                ones == N // 2 (equal split of 1s and 0s).

Time complexity : O(N) per test case (counting '1's)
Space complexity: O(1) extra (excluding input string storage)
"""


# ---------------------- Slution ---------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        ones = S.count('1')
        if N % 2 == 1:
            print("YES")
        else:
            if ones % 2 == 0 or ones == N // 2:
                print("YES")
            else:
                print("NO")

if __name__ == "__main__":
    solve()
