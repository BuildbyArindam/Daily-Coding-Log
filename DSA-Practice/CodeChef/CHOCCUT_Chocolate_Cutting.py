"""
Platform   : CodeChef
Problem    : Chocolate Cutting (CHOCCUT)
Link       : https://www.codechef.com/START258B/problems/CHOCCUT
Contest    : Starters 258 (Div B)
Date       : 2026-09-30
Difficulty : Easy 
Topics     : Math, Parity, Implementation

Approach:
    The answer is "Yes" if at least one of the two dimensions is even, since
    the bar can then be cut along that dimension into two equal halves.
    It is "No" only when both dimensions are odd. So each test case is a
    parity check on N and M.

Time Complexity  : O(T), constant work per test case
Space Complexity : O(T) for the buffered outputs
"""


# --------------------------------------- Solution ---------------------------------------------


import sys

def can_split(rows, cols):
    ok = False
    if rows % 2 == 0:
        ok = True
    if cols % 2 == 0:
        ok = True
    return ok

def main():
    data = sys.stdin.read().split()
    idx = 0
    total_cases = int(data[idx]); idx += 1
    results = []
    for _ in range(total_cases):
        n = int(data[idx]); idx += 1
        m = int(data[idx]); idx += 1
        verdict = "Yes" if can_split(n, m) else "No"
        results.append(verdict)
    print("\n".join(results))

if __name__ == "__main__":
    main()
