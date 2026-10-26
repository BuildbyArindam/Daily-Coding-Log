"""
Problem   : Minimum number of Flips (MINFLIPS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/MINFLIPS
Difficulty: 781
Topics    : Math, Arrays, Greedy
Date      : 2026-10-26

Approach:
    The array holds only 1 and -1, and each flip changes the total sum by 2.
    The goal is a sum of 0, which needs an equal count of 1s and -1s.
    - Odd length: impossible, so the answer is -1.
    - Otherwise: answer = |count(1) - count(-1)| / 2.

Time Complexity : O(N) per test case (single pass to count)
Space Complexity: O(N) for the input array
"""


# --------------------------------------------------- Solution -----------------------------------------------------


import sys

def solve_case(arr):
    length = len(arr)
    if length & 1:
        return -1
    ones = arr.count(1)
    minus = length - ones
    return abs(ones - minus) >> 1

def main():
    tokens = sys.stdin.read().split()
    ptr = 0
    cases = int(tokens[ptr])
    ptr += 1
    results = []
    for _ in range(cases):
        n = int(tokens[ptr])
        ptr += 1
        arr = [int(x) for x in tokens[ptr:ptr + n]]
        ptr += n
        results.append(str(solve_case(arr)))
    sys.stdout.write("\n".join(results) + "\n")

main()
