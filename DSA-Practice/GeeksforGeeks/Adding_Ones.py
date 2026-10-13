"""
Problem   : Adding Ones
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/adding-ones3628/1
Difficulty: Easy
Topics    : Arrays, Prefix Sum
Date      : 2026-10-13

Approach:
    Each update j adds 1 to every element from index j (1-based) to the end.
    Instead of looping over that range for every update, mark only the start
    point (arr[j-1] += 1), then take a running prefix sum. Each position
    then holds the number of updates whose start index is at or before it.

Time Complexity : O(n + u)   where u = len(updates)
Space Complexity: O(n)       for the result array
"""


# --------------------------------------------- Solution --------------------------------------------------------


class Solution:
    def update(self, n: int, updates: list[int]) -> list[int]:
        # code here
        arr = [0] * n
        for j in updates:
            arr[j - 1] += 1
        for i in range(1, n):
            arr[i] += arr[i - 1]
        return arr
