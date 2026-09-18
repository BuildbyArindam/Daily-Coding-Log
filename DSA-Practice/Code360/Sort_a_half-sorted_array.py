"""
Problem   : Sort a Half-Sorted Array
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118822/offering/1382142
Difficulty: Easy
Topics    : Arrays, Merging, Two Pointers, Sorting
Date      : 2026-09-18

Approach:
    The array consists of two sorted (ascending) segments concatenated
    together, with exactly one point where arr[i] > arr[i+1]. Find that
    split index, then merge the two sorted halves (standard merge-sort
    merge step) back into the array.

Time complexity : O(n)  -- one pass to find split, one pass to merge
Space complexity: O(n)  -- temporary left/right sub-lists during merge
"""


# ------------------------------- Solution --------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def sortHalfSorted(arr:list):
	n = len(arr)
	if n <= 1:
		return
	split = -1
	for i in range(n - 1):
		if arr[i] > arr[i + 1]:
			split = i + 1
			break
	if split == -1:
		return
	left = arr[:split]
	right = arr[split:]
	i = j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1from os import *
from sys import *
from collections import *
from math import *

def sortHalfSorted(arr:list):
	n = len(arr)
	if n <= 1:
		return
	split = -1
	for i in range(n - 1):
		if arr[i] > arr[i + 1]:
			split = i + 1
			break
	if split == -1:
		return
	left = arr[:split]
	right = arr[split:]
	i = j = 0
	k = 0
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1
		else:
			arr[k] = right[j]
			j += 1
		k += 1
	while i < len(left):
		arr[k] = left[i]
		i += 1
		k += 1
	while j < len(right):
		arr[k] = right[j]
		j += 1
		k += 1
