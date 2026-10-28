"""
Platform   : CodeChef
Problem    : Sum this up (EVOFWEIRDSUM)
Link       : https://www.codechef.com/problems/EVOFWEIRDSUM
Difficulty : 2018
Topics     : Basic Math, Contribution Trick, Probability, Expected Value
Date       : 2026-10-28

Approach:
    Using linearity of expectation and the contribution trick, the answer
    reduces to floor(sum(A) / N), so no simulation or pair enumeration is
    needed. Read all input at once for speed.

Complexity:
    Time  : O(N) per test case (one pass to sum), O(sum of N) overall
    Space : O(N) per test case for the input slice, O(1) extra
"""


# ---------------------------------------------------- Solution -------------------------------------------------------------------


import sys

def solve_case(n, vals):
    total = 0
    for v in vals:
        total += v
    return total // n

def main():
    raw = sys.stdin.buffer.read().split()
    ptr = 1
    out = []
    for _ in range(int(raw[0])):
        n = int(raw[ptr])
        ptr += 1
        chunk = raw[ptr:ptr + n]
        ptr += n
        out.append(str(solve_case(n, map(int, chunk))))
    sys.stdout.write("\n".join(out) + "\n")

main()
