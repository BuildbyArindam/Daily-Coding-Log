"""
Problem   : Game of Deletion
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/game-of-destruction-f96cd509/
Difficulty: Medium
Topics    : Basic Programming, Bit Manipulation
Date      : 2026-09-30

Approach:
    For each array, the reward is (sum of elements) - (bitwise OR of all
    elements). Compute it for A and B in one pass each, then compare:
    the larger reward wins and the output is the winner with the
    difference; on a tie, print 1.

Complexity:
    Time  : O(N), one pass per array for the sum and the OR
    Space : O(N) for the input arrays (O(1) extra beyond that)
"""


# ------------------------------------------ Solution -------------------------------------------


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sum_a = sum(A)
or_a = 0
for x in A:
    or_a |= x
sum_b = sum(B)
or_b = 0
for x in B:
    or_b |= x
reward_a = sum_a - or_a
reward_b = sum_b - or_b
if reward_a > reward_b:
    print(1, reward_a - reward_b)
elif reward_b > reward_a:
    print(2, reward_b - reward_a)
else:
    print(1)
