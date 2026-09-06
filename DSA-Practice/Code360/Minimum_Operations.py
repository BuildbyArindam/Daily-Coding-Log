"""
Problem   : Minimum Operations
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/day-10-minimum-operations_762937?kunjiRedirection=true
Difficulty: Easy
Topic     : Hashing, Frequency Counting
Date      : 2026-09-06

Approach:
Count the frequency of each element using a hash map (Counter).
The array can be made "good" with minimum operations by keeping only
the most frequent element and changing every other element to match it.
So the answer = n - (frequency of the most frequent element).

Time Complexity : O(n)  -> one pass to build frequency map, one pass to find max
Space Complexity: O(n)  -> hash map storing up to n distinct frequencies
"""


# ---------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *

def minimumOperation(arr, n):
    freq = Counter(arr)
    max_freq = max(freq.values())
    return n - max_freq

t = int(input())
while t > 0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(minimumOperation(arr,n))
    t -= 1
