"""
Platform   : CodeChef
Problem    : Equal Chocolates (SNCO)
Link       : https://www.codechef.com/problems/SNCO
Date       : 2026-10-22
Difficulty : Easy
Topics     : Math, Implementation

Approach:
    Read the four integers P, Q, R, S. Compute the two totals P*Q and R*S
    and print "YES" if they are equal, otherwise "NO".

Complexity:
    Time  : O(1)
    Space : O(1)
"""


# ------------------------------------------------ Solution ----------------------------------------------------------


import sys

def _totals(vals):
    p, q, r, s = vals
    return (p * q, r * s)

def _verdict(pair):
    left, right = pair
    return ("NO", "YES")[left == right]

def entry():
    raw = sys.stdin.read().split()
    nums = list(map(int, raw[:4]))
    print(_verdict(_totals(nums)))

if __name__ == "__main__":
    entry()
