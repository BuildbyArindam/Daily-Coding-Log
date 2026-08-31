"""
Problem: Rearrange Alternatively
Link: https://www.naukri.com/code360/problems/rearrange-alternatively_873851?kunjiRedirection=true
Platform: Code360
Difficulty: Easy
Date: 2026-08-31
Topics: Arrays, Two Pointers, Partitioning

Approach:
Split the array into two lists — negatives and non-negatives — 
preserving their relative order. Then merge them alternately 
(negative, non-negative, negative, ...) using two pointers, 
appending any leftover elements from the longer list at the end.

Time Complexity: O(n) — single pass to split, single pass to merge
Space Complexity: O(n) — extra lists for negative/non-negative and result
"""


# --------------------------- Solution -----------------------------


from os import *
from sys import *
from collections import *
from math import *

def rearrange(arr):
    negative = []
    non_negative = []
    for num in arr:
        if num < 0:
            negative.append(num)
        else:
            non_negative.append(num)
    result = []
    i = 0
    j = 0
    while i < len(negative) and j < len(non_negative):
        result.append(negative[i])
        i += 1
        result.append(non_negative[j])
        j += 1
    while i < len(negative):
        result.append(negative[i])
        i += 1
    while j < len(non_negative):
        result.append(non_negative[j])
        j += 1
    return result
