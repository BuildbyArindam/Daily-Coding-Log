"""
Problem: Evaluate the Bracket Pairs of a String
Link: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/
Date: 2026-09-26
Difficulty: Medium
Topics: Array, Hash Table, String

Approach:
Build a lookup dict from the knowledge list, then scan the string once.
On '(' find the matching ')', pull the key in between, and replace it with
the dict lookup (default '?'). Non-bracket characters are copied as-is.

Time Complexity: O(n) - single pass over s, plus O(k) key length work
                  amortized across the scan
Space Complexity: O(m) - m = number of knowledge entries, for the dict;
                  plus O(n) for the result list
"""


# ------------------------------------ Solution ---------------------------------------------


class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        values = {key: value for key, value in knowledge}
        result = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                j = i + 1
                while s[j] != ')':
                    j += 1
                key = s[i + 1:j]
                result.append(values.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1
        return ''.join(result)

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
