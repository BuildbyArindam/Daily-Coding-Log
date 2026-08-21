"""
Problem   : Favorite Words (FAVWD)
Platform  : CodeChef (Starters 245)
Link      : https://www.codechef.com/problems/FAVWD
Date      : 2026-08-21
Topic     : Implementation, Strings
Difficulty: Beginner (School / ~800 CF-equivalent)

Approach:
A word is "liked" by Chef if it starts with 'c' OR ends with 'f'.
Direct O(1) check on the first and last characters of the string.

Time Complexity : O(1)   -- fixed-length (4-char) input, constant work
Space Complexity: O(1)   -- no extra data structures used
"""


# ----------------------- Solution -------------------------


S = input().strip()
print("Yes" if (S[0] == 'c' or S[-1] == 'f') else "No")
