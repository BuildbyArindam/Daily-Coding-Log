"""
Problem: Spreading Charges
Platform: CodeChef
Link: https://www.codechef.com/problems/CHRGES
Difficulty: 1708
Date Solved: 2026-09-25
Topics: Greedy, String Processing, Parity/Math

Approach:
Scan the string once, tracking the last non-zero charge seen and the
count of zeros since that charge. Whenever a new charge appears that
differs from the last one AND is separated by an odd number of zeros,
increment the answer (an odd gap means the charges' fields can meet
and cancel/interact at some point; an even gap means they can't).
If the string has no '+' or '-' at all, every position stays neutral,
so the answer is just N.

Time Complexity: O(N) per test case (single linear scan)
Space Complexity: O(1) extra space (excluding input storage)
"""


# ------------------------------------ Solution ------------------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        if '+' not in S and '-' not in S:
            print(N)
            continue
        ans = 0
        last_charge = None
        zeros = 0
        for ch in S:
            if ch == '0':
                zeros += 1
            else:
                if last_charge is not None:
                    if last_charge != ch and zeros % 2 == 1:
                        ans += 1
                last_charge = ch
                zeros = 0
        print(ans)

if __name__ == "__main__":
    solve()
