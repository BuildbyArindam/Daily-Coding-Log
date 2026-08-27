"""
Problem   : Regular Cleaning (REGCLN)
Link      : https://www.codechef.com/problems/REGCLN
Date      : 2026-08-27
Platform  : CodeChef
Difficulty: Cakewalk
Topics    : Basic Math, Modular Arithmetic

Approach:
Chef cleans on every multiple of 10. Given today's day number N, the
number of days remaining until the next cleaning day equals 10 minus
the remainder of N when divided by 10 (i.e., 10 - N % 10). This works
even when N itself is a multiple of 10, since the *next* cleaning day
is 10 days later, not today.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------ Slution --------------------------


N = int(input())
ans = 10 - (N % 10)
print(ans)
