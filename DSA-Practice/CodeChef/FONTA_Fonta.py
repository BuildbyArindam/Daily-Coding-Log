"""
Problem   : Fonta (FONTA)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FONTA
Date      : 2026-08-29
Difficulty: Cakewalk
Topics    : String Manipulation, Suffix Checking, Basic Implementation

Approach:
A drink is "fanta-like" if its name ends with the suffix "nta".
Read the string, check it with str.endswith("nta"), and print
YES/NO accordingly. Single pass, no extra data structures needed.

Complexity:
Time  : O(N) where N = length of the string (endswith scan)
Space : O(1) extra space
"""


# ---------------------- Solution --------------------------------


S = input().strip()
if S.endswith("nta"):
    print("YES")
else:
    print("NO")
