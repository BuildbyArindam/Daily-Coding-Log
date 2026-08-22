"""
Problem   : Maximum Equal Sum Stack
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/maximum-equal-sum-stack_1164270
Date      : 2026-08-22
Difficulty: Easy
Topics    : Greedy, Array, Stack, Simulation

Approach:
Compute the total sum of each stack. Repeatedly pop from the stack with the
largest current sum (since popping only reduces a sum, the largest sum must
shrink for the three to ever converge). Stop as soon as all three sums are
equal, or if any stack is exhausted before equality is reached (no valid
answer -> return 0).

Time Complexity : O(n1 + n2 + n3) — each element is popped at most once
Space Complexity: O(1) extra (excluding input storage)
"""


# ---------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *


def maxStackSum(stack1, stack2, stack3):
    sum1 = sum(stack1)
    sum2 = sum(stack2)
    sum3 = sum(stack3)
    i = j = k = 0
    while True:
        if sum1 == sum2 and sum2 == sum3:
            return sum1
        if i == len(stack1) or j == len(stack2) or k == len(stack3):
            return 0
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= stack1[i]
            i += 1
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= stack2[j]
            j += 1
        else:
            sum3 -= stack3[k]
            k += 1
