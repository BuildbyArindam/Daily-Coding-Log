"""
Problem   : Recursive Sums
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/recursive-sums/
Difficulty: Easy
Topics    : Implementation, Math
Date      : 2026-09-05

Approach:
Each test case gives M "digit blocks" (length, digit) pairs, meaning a digit
repeated `length` times. The digital root of a number formed this way only
depends on (sum of digits) % 9 -- since a run of `length` copies of `digit`
contributes (length * digit) to the digit sum, and mod-9 distributes over
that. So track (digit_sum + length*digit) % 9 across all blocks. If the
final result is 0 but the number wasn't all zeros, the digital root is 9
(not 0), matching the standard digital-root edge case.

Complexity:
Time  : O(M) per test case -> O(sum of M) overall
Space : O(1) extra (aside from input)
"""


# --------------------------- Solution ------------------------------


name = input()   
T = int(name)
for _ in range(T):
    M = int(input())
    digit_sum = 0
    has_nonzero = False
    for _ in range(M):
        length, digit = map(int, input().split())
        if digit != 0:
            has_nonzero = True
        digit_sum = (digit_sum + (length % 9) * digit) % 9
    if digit_sum == 0 and has_nonzero:
        print(9)
    else:
        print(digit_sum)
