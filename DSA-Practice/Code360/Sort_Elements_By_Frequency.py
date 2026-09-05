"""
Problem: Sort Elements By Frequency
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/problems/sort-elements-by-frequency_1280138?kunjiRedirection=true
Difficulty: Easy
Topics: Hashing, Frequency Counting, Sorting
Date: 2026-09-05

Approach:
Count frequency of each element with Counter. Track the first-occurrence
index of each distinct element to break ties for equal frequencies
(stable order = order of first appearance). Sort distinct elements by
(-frequency, first_occurrence), then expand each element by its frequency
to build the final result.

Time Complexity: O(n log n) — dominated by sorting the distinct elements
Space Complexity: O(n) — for frequency map, first-occurrence map, and result
"""


# ------------------------ Solution -------------------------------


from os import *
from sys import *
from collections import *
from math import *

def sortByFrequency(nums):
    frequency = Counter(nums)
    first_occurrence = {}
    for i, num in enumerate(nums):
        if num not in first_occurrence:
            first_occurrence[num] = i
    elements = list(frequency.keys())
    elements.sort(key=lambda x: (-frequency[x], first_occurrence[x]))
    result = []
    for num in elements:
        result.extend([num] * frequency[num])
    return result
