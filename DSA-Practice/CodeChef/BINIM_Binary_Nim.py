"""
Problem   : Binary Nim
Platform  : CodeChef (BINIM)
Link      : https://www.codechef.com/problems/BINIM
Difficulty: 1727
Date      : 2026-10-08
Topics    : Game Theory, Partisan Games, Combinatorial Game Values

Approach:
    Each stack is an independent partisan game, so the whole game is the
    sum of the stack values. Each stack's value is computed from bottom to
    top: a '0' gives a value one above the maximum seen so far, and a '1'
    gives a value one below the minimum seen so far. This is the
    simplest-number rule, and mn/mx track the range of values so far.
    Sum the stack values:
        total > 0 -> Dee wins
        total < 0 -> Dum wins
        total == 0 -> the player who moves first loses

Complexity:
    Time : O(L), where L is the total length of all stacks (one pass each)
    Space: O(1) extra per stack (just mn, mx, v), excluding input storage
"""


# ----------------------------------------- Solution -------------------------------------------------


import sys

def stack_value(b):
    n = len(b)
    mn = mx = 0
    for i in range(n - 1, -1, -1):
        if b[i] == '0':
            v = mx + 1
        else:
            v = mn - 1
        mn = min(mn, v)
        mx = max(mx, v)
    return v

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N, start = input().split()
        total = 0
        for _ in range(int(N)):
            b = input().strip()
            total += stack_value(b)
        if total > 0:
            print("Dee")
        elif total < 0:
            print("Dum")
        else:
            print("Dum" if start == "Dee" else "Dee")

if __name__ == "__main__":
    solve()
