"""
Problem   : Convert One String to Another with Constraints
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/check-if-it-is-possible-to-convert-one-string-into-another-with-given-constraints4116/1
Difficulty: Easy
Topics    : Strings, Greedy, Two Pointers, Constructive
Date      : 2026-10-17

Approach:
  '#' is a blank, so it can be ignored when comparing the strings. After
  skipping blanks, the remaining non-blank characters must match in the
  same order. Use two pointers (i on s1, j on s2) to compare them one by
  one. 'A' can only move left and 'B' can only move right, so:
    - if s1[i] == 'A' and i < j: 'A' would have to move right -> False
    - if s1[i] == 'B' and i > j: 'B' would have to move left  -> False
  If one pointer runs out of characters before the other, the answer is
  False.

Time Complexity : O(n), single pass with two pointers
Space Complexity: O(1)
"""


# ---------------------------------------------- Solution --------------------------------------------------


class Solution:
    def isItPossible(self, s1: str, s2: str) -> bool:
        # code here
        n = len(s1)
        if len(s2) != n:
            return False
        i = j = 0
        while i < n and j < n:
            while i < n and s1[i] == '#':
                i += 1
            while j < n and s2[j] == '#':
                j += 1
            if i == n or j == n:
                return i == n and j == n
            if s1[i] != s2[j]:
                return False
            if s1[i] == 'A' and i < j:
                return False
            if s1[i] == 'B' and i > j:
                return False
            i += 1
            j += 1
        return True
