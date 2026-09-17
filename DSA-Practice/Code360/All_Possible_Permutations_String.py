"""
Problem: All Possible Permutations - String
Platform: Code360 (Naukri)
Link: https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380929
Date solved: 2026-09-17
Difficulty: Easy
Topics: Backtracking, Recursion, Strings

Approach:
Generate all permutations of the string using in-place swapping (Heap's-style
backtracking). At each recursive call, fix the character at `index` by trying
every remaining character in that position (swap it in), recurse on the next
index, then swap back (backtrack) to restore state for the next iteration.
When index reaches the end of the string, a full permutation is complete —
join and record it.

Time Complexity:  O(n * n!)  -- n! permutations, O(n) to join each into a string
Space Complexity: O(n) recursion stack (excluding the O(n * n!) output storage)
"""


# ---------------------------- Solution ----------------------------------------


from os import *
from sys import *
from collections import *
from math import *

def findPermutations(s):
    ans = []
    def backtrack(index):
        if index == len(s):
            ans.append(''.join(s))
            return
        for i in range(index, len(s)):
            s[index], s[i] = s[i], s[index]
            backtrack(index + 1)
            s[index], s[i] = s[i], s[index]
    s = list(s)
    backtrack(0)
    return ans
