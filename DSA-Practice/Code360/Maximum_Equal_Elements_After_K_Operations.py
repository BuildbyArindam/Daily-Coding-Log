"""
Problem   : Maximum Equal Elements After K Operations
Link      : https://www.naukri.com/code360/problems/maximum-equal-elements-after-k-operations_992848
Platform  : Coding360 (Naukri Code360)
Difficulty: Medium
Date      : 2026-08-27

Approach:
    Sort the array. For a contiguous window [left, right] in the sorted
    array, the cost to make every element equal to arr[right] (the window
    max) is: arr[right] * (right - left + 1) - sum(arr[left..right]).
    Use a sliding window (two pointers) — expand `right`, and whenever the
    cost exceeds k, shrink from `left`. Track the max window size seen;
    that's the max count of elements we can make equal using at most k
    increment operations.

Time Complexity : O(n log n)   -> dominated by the sort; the two-pointer
                                   scan itself is O(n) since left/right
                                   each move forward at most n times.
Space Complexity: O(1) extra   -> (ignoring sort's internal space, which
                                   is O(log n) to O(n) depending on the
                                   Python implementation's sort algorithm)
"""


# ----------------------------- Solution ------------------------------


from os import *
from sys import *
from collections import *
from math import *

def maxEqualElements(arr, k):
    arr.sort()
    n = len(arr)
    left = 0
    curr_sum = 0
    ans = 1
    for right in range(n):
        curr_sum += arr[right]
        while (right - left + 1) * arr[right] - curr_sum > k:
            curr_sum -= arr[left]
            left += 1
        ans = max(ans, right - left + 1)
    return ans

def main():
    input = stdin.readline
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        arr = list(map(int, input().split()))
        print(maxEqualElements(arr, k))

if __name__ == "__main__":
    main()
