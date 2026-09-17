"""
Problem: Subsequences of String
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380932
Difficulty: Medium
Topics: Recursion, Backtracking, Subsets
Date Solved: 2026-09-17

Approach:
Generate all subsequences using recursion by making a binary choice at each
index — include the current character or exclude it — until the end of the
string is reached. Each complete path represents one subsequence.

Time Complexity: O(2^n * n)
    - There are 2^n possible subsequences.
    - Building/copying each subsequence (via string concatenation) costs O(n).
Space Complexity: O(2^n * n) for storing all subsequences in the output list,
    plus O(n) for the recursion call stack.
"""


# ------------------------------ Solution --------------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def subsequences(str):
    ans = []
    def generate(index, current):
        if index == len(str):
            if current:
                ans.append(current)
            return
        generate(index + 1, current + str[index])
        generate(index + 1, current)
    generate(0, "")
    return ans
