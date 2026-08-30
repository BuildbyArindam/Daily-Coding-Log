"""
Problem   : Lucky Seven (LUCKYSEVEN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LUCKYSEVEN
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic I/O, String Manipulation, Indexing

Approach:
    Read the input string and print the character at index 6
    (i.e., the 7th character, 0-indexed) directly.

Time Complexity : O(1)  -- single indexing operation
Space Complexity: O(1)  -- no extra space used
"""


# --------------------- Solution -----------------------


S = input().strip()
print(S[6])
