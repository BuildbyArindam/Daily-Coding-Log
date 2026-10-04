"""
Problem   : Delete Sorted Subsequence
Platform  : CodeChef (DELSORTSUB)
Difficulty: 1800
Topics    : Greedy, Strings, Prefix Balance
Link      : https://www.codechef.com/problems/DELSORTSUB
Date      : 2026-10-04

Approach  : The answer is always 0, 1 or 2.
            Scan left to right with a +1/-1 balance (0 -> +1, 1 -> -1).
            If the final balance equals the minimum prefix balance, this
            direction decides it: 0 if the balance is 0, otherwise 1.
            If not, repeat on the reversed string with the roles of
            0 and 1 swapped. If that check also fails, the answer is 2.

Time      : O(n) per test case (two linear passes)
Space     : O(1) extra (besides storing the input string)
"""


# ----------------------------------------- Solution ----------------------------------------------------------


import sys
input = sys.stdin.readline

def solve(s):
    bal = 0
    mn = 0
    for c in s:
        if c == '0':
            bal += 1
        else:
            bal -= 1
        mn = min(mn, bal)
    if mn == bal:
        return 0 if bal == 0 else 1
    bal = 0
    mn = 0
    for c in reversed(s):
        if c == '1':
            bal += 1
        else:
            bal -= 1
        mn = min(mn, bal)
    if mn == bal:
        return 0 if bal == 0 else 1
    return 2

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
