"""
Problem   : Insertion Sort
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/insertion-sort_3155179?kunjiRedirection=true
Date      : 2026-08-29
Difficulty: Easy
Topic     : Sorting / Arrays

Approach:
    Classic insertion sort. Iterate from index 1 to n-1, treating arr[i] as
    the 'key' to insert into the already-sorted prefix arr[0..i-1]. Shift
    elements greater than key one position right until the correct spot
    for key is found, then place it there.

Time Complexity : O(n^2) worst/average case (nested shifting), O(n) best case (already sorted)
Space Complexity: O(1) — sorts in place, no extra data structures
"""


# ------------------------ Solution ---------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import List

def insertionSort(n: int, arr: List[int]) -> None:
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
