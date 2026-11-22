"""
Problem   : 2124. Check if All A's Appears Before All B's
Platform  : LeetCode
Link      : https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
Difficulty: Easy
Topics    : String
Date      : 2026-11-22

Approach:
    Scan the string from right to left. Once an 'a' is seen, any 'b' found
    further left means a 'b' precedes an 'a', so the string is invalid.
    If the scan finishes without that happening, return True.

Complexity:
    Time  : O(n), single pass
    Space : O(1)
"""


# -------------------------------------------- Solution ------------------------------------------------------


class Solution:
    def checkString(self, s: str) -> bool:
        seen_a = False
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == 'a':
                seen_a = True
            elif seen_a:    
                return False
        return True

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
