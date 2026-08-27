"""
Problem   : Remove Consecutive Duplicates
Platform  : Coding360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/remove-consecutive-duplicates_893195
Date      : 2026-08-27
Difficulty: Easy
Topics    : Recursion, Strings

Approach:
    Recursively process the suffix s[1:] first to get its deduplicated
    version 'remaining'. Since 'remaining' is already free of consecutive
    duplicates, comparing s[0] with remaining[0] tells us whether s[0]
    was part of the same run as the next surviving character:
        - if they match, s[0] is a duplicate -> discard it, return 'remaining'
        - if they differ, s[0] starts a new run -> prepend it

Time Complexity : O(n^2)
    - n recursive calls, and each call does an O(n) slice (s[1:]),
      giving O(n^2) total due to string slicing/copying.
Space Complexity: O(n^2)
    - O(n) recursion depth, plus each stack frame holds a sliced
      substring, so cumulative extra space is O(n^2) (excluding output).
    - Note: an iterative single-pass approach achieves O(n) time and
      O(n) space using a stack/two-pointer technique.
"""


# -------------------------- Solution ---------------------------


def removeDuplicate(n, s):
    if n <= 1:
        return s
    remaining = removeDuplicate(n - 1, s[1:])
    if s[0] == remaining[0]:
        return remaining
    return s[0] + remaining
  
