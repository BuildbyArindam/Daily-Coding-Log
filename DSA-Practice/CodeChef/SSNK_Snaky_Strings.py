"""
Problem: Snaky Strings (SSNK)
Link: https://www.codechef.com/problems/SSNK
Date: 2026-08-29
Platform: CodeChef
Difficulty: Cakewalk
Topics: Basic String Manipulation, Conditional Statements

Approach:
A string is "snaky" if its first or last character is 's'.
Read the string and check A[0] and A[-1]; print "Yes" if either
matches, else "No".

Time Complexity: O(1)  -- string length is fixed/small, only endpoint checks
Space Complexity: O(1)  -- no extra data structures used
"""


# --------------------- Solution ------------------------


A = input().strip()
if A[0] == 's' or A[-1] == 's':
    print("Yes")
else:
    print("No")
