"""
Problem   : Search In The Array
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/search-in-the-array_1116099?kunjiRedirection=true
Difficulty: Easy
Date      : 2026-08-24
Topics    : Sorting, Prefix Sum, Binary Search

Approach:
  For each query, we need the sum of all array elements <= query.
  1. Sort the array so elements are in increasing order.
  2. Build a prefix-sum array over the sorted array.
  3. For each query, binary search for the rightmost index whose
     value is <= query (a bisect_right-style search).
  4. The prefix sum up to that index is the answer; if no such
     index exists, the answer is 0.

Time Complexity : O((n + q) log n)   [sort: O(n log n), each query: O(log n)]
Space Complexity: O(n)               [prefix array]
"""


# ---------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *

def searchInTheArray(arr, queries, n, q):
    arr.sort()
    prefix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]
    ans = []
    for query in queries:
        left = 0
        right = n - 1
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= query:
                index = mid
                left = mid + 1
            else:
                right = mid - 1
        if index == -1:
            ans.append(0)
        else:
            ans.append(prefix[index])
    return ans
