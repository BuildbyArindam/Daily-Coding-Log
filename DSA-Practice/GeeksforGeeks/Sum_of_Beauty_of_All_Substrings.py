"""
Problem   : Sum of Beauty of All Substrings
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/sum-of-beauty-of-all-substrings-1662962118/1
Difficulty: Easy
Topics    : Strings
Date      : 2026-10-25

Approach:
    Beauty of a substring = (max char frequency) - (min non-zero char frequency).
    Fix every start index and extend the end index one character at a time,
    keeping a 26-slot frequency array. The running max is updated in O(1)
    as each character is added, and the min non-zero frequency is found by
    scanning the 26 slots. Add (max - min) to the answer for every substring.

Time Complexity : O(26 * n^2), n^2 substrings, 26 work per substring
Space Complexity: O(1), fixed 26-size frequency array
"""


# ------------------------------------------------ Solution ----------------------------------------------------------


class Solution:
    def beautySum(self, s: str) -> int:
        # code here
        size = len(s)
        answer = 0
        begin = size
        while begin > 0:
            begin -= 1
            bucket = [0] * 26
            top = 0
            for end in range(begin, size):
                slot = ord(s[end]) - 97
                bucket[slot] += 1
                if bucket[slot] > top:
                    top = bucket[slot]
                low = size + 1
                for cnt in bucket:
                    if 0 < cnt < low:
                        low = cnt
                answer += top - low
        return answer
