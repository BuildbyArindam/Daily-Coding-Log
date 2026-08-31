"""
Problem   : Make All Elements Equal
Platform  : Code360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/make-all-elements-equal_2099909?kunjiRedirection=true
Date      : 2026-08-31
Difficulty: Medium
Topics    : Arrays, Sorting, Median, Greedy, Math

Approach:
    To make all elements equal with minimum total cost (cost = sum of
    |arr[i] - target| for all i), the optimal target is the MEDIAN of
    the array. This is because the median minimizes the sum of absolute
    deviations (unlike the mean, which minimizes sum of squared
    deviations). Sort the array, pick the middle element as the target,
    then sum the absolute differences of every element from it.

Time Complexity : O(n log n)  -> dominated by the sort
Space Complexity: O(1) extra  -> in-place sort (ignoring sort's internal stack space)
"""


# ----------------------------- Solution --------------------------------


def findMinimumCost(arr, n):
    arr.sort()
    median = arr[n // 2]
    cost = 0
    for num in arr:
        cost += abs(num - median)
    return cost
