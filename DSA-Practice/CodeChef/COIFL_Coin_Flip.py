"""
Problem   : Coin Flip (COIFL)
Platform  : CodeChef (DSAMONDAY026)
Link      : https://www.codechef.com/DSAMONDAY026/problems/COIFL
Date      : 2026-10-26
Difficulty: Medium
Topics    : Math, Fibonacci, Iteration

Approach  : The answer follows the Fibonacci recurrence f(1) = f(2) = 1,
            f(n) = f(n-1) + f(n-2). Compute it iteratively, keeping only the
            last two values instead of a full DP table.

Complexity: Time  O(n) big-integer additions
            Space O(1) extra (beyond the size of the result itself)
"""


# ------------------------------------------------ Solution -------------------------------------------------------------


import sys

def main():
    data = sys.stdin.read().split()
    target = int(data[0])
    prev, curr = 1, 1
    for _ in range(target - 1):
        prev, curr = curr, prev + curr
    sys.stdout.write(str(curr) + "\n")

main()
