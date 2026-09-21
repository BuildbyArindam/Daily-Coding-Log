"""
Problem   : Maximum Dance Partners
Platform  : CodeChef (DSAMONDAY021)
Link      : https://www.codechef.com/DSAMONDAY021/problems/MADNER
Date      : 2026-09-21
Difficulty: Medium
Topics    : Greedy, Strings, Two Pointers

Approach:
Scan the string left to right with a single pointer. At each position,
compare the current character with the next one. If they differ, they
form a valid dance pair — count it and jump ahead by 2 (both characters
consumed). If they're the same, they can't pair together, so advance
by 1 and re-check the next character against its neighbor. This greedy
strategy is optimal because pairing two mismatched adjacent characters
as soon as possible never blocks a better future pairing — skipping a
valid pair only wastes a potential match.

Time Complexity : O(n) — single left-to-right scan
Space Complexity: O(1) — only a few scalar variables
"""


# ------------------------------------ Solution ------------------------------------------


class Solution:
    def findMaximumPairs(self, students: str) -> int:
        # write your code here
        total_pairs = 0
        idx = 0
        length = len(students)
        while idx < length - 1:
            first, second = students[idx], students[idx + 1]
            if first != second:
                total_pairs += 1
                idx += 2
            else:
                idx += 1
        return total_pairs
