"""
Problem   : To Take or Not To Take
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/totakeornottotake/
Date      : 2026-08-26
Difficulty: Medium
Topics    : Implementation, Simulation, Ad-Hoc, Min-Max Range Tracking

Approach:
For each block of operations, maintain a running [min_val, max_val] range
representing all possible outcomes depending on take/not-take choices at
each step. For an arithmetic op (+, -, *, /), apply it to both the current
min and max and take the new min/max of the four candidates (since scaling
by a negative or division can flip which endpoint is smaller). The "no-op"
branch negates both endpoints (represents the take/skip choice equivalent
to negation). After processing all B operations in a block, max_val holds
the best achievable result.

Time complexity : O(sum of B) — each operation processed in O(1)
Space complexity: O(1) extra (excluding input storage)
"""


# ----------------------------- Solution -----------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    T = int(data[0])
    idx = 1
    for _ in range(T):
        B = int(data[idx])
        idx += 1
        min_val = 1
        max_val = 1
        for _ in range(B):
            op = data[idx]
            idx += 1
            if op in ('+', '-', '*', '/'):
                X = int(data[idx])
                idx += 1
                if op == '+':
                    cand1, cand2 = min_val + X, max_val + X
                elif op == '-':
                    cand1, cand2 = min_val - X, max_val - X
                elif op == '*':
                    cand1, cand2 = min_val * X, max_val * X
                elif op == '/':
                    cand1, cand2 = int(min_val / X), int(max_val / X)
            else:
                cand1, cand2 = -min_val, -max_val
            new_min = min(min_val, max_val, cand1, cand2)
            new_max = max(min_val, max_val, cand1, cand2)
            min_val, max_val = new_min, new_max
        print(max_val)

if __name__ == '__main__':
    solve()
