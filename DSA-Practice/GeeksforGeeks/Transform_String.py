"""
Problem   : Transform String
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/transform-string5648/1
Difficulty: Medium
Topics    : Hashing, Strings, Two Pointer (Greedy)
Date      : 2026-08-21

Approach:
- If Counter(s1) != Counter(s2), the strings can never match (different
  character sets/frequencies) -> return -1.
- Otherwise, walk s1 from the back with pointer i, and s2 from the back
  with pointer j. Whenever s1[i] == s2[j], that character is already in
  correct relative order from the end, so decrement j.
- Characters that never matched form the "unordered prefix" that must be
  moved to the front to align with s2. The count of such characters is
  j + 1, which is exactly the minimum number of move-to-front operations.

Time Complexity : O(n)      -> one pass for Counter comparison, one pass for the pointer walk
Space Complexity: O(1)/O(26)-> Counter over a bounded alphabet (O(n) if alphabet is unbounded/Unicode)
"""


# ------------------------- Solution ------------------------------


class Solution:
    def transform(self, s1, s2): 
        #code here
        from collections import Counter
        if Counter(s1) != Counter(s2):
            return - 1
        n = len(s1)
        j = n - 1
        for i in reversed(range(n)):
            if s1[i] == s2[j]:
                j -= 1
        return j + 1
