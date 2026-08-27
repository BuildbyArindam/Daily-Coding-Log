"""
Problem   : Flower Reversal
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FLREV
Date      : 2026-08-27

Approach:
For a binary string, "beauty" = count of adjacent equal-character pairs
= (N-1) - (count of 01 transitions) - (count of 10 transitions).
Reversing exactly one substring can merge/eliminate transitions:
 - If either transition type occurs >= 2 times, one reversal can remove
   2 transitions (gain = 2).
 - If both 01 and 10 occur at least once (but not >=2 of either), one
   reversal can remove 1 transition (gain = 1).
 - Otherwise (string is already uniform or has at most 1 transition
   total), no reversal helps (gain = 0).
Answer = beauty + gain.

Time Complexity : O(N) per test case, O(sum of N) overall
Space Complexity: O(1) extra (excluding input string storage)
"""


# -------------------------- Solution -------------------------------


import sys

def solve():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input().strip()
        c01 = 0
        c10 = 0
        for i in range(N - 1):
            if S[i] == '0' and S[i + 1] == '1':
                c01 += 1
            elif S[i] == '1' and S[i + 1] == '0':
                c10 += 1
        beauty = (N - 1) - c01 - c10
        if c01 >= 2 or c10 >= 2:
            gain = 2
        elif c01 > 0 and c10 > 0:
            gain = 1
        else:
            gain = 0
        print(beauty + gain)

if __name__ == "__main__":
    solve()
