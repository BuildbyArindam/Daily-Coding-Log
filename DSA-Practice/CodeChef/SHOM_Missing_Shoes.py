"""
Problem   : Missing Shoes (SHOM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SHOM
Date      : 2026-08-19
Difficulty: Cakewalk
Topics    : Basic Math, Ad-Hoc / Implementation

Approach:
Chef has L left shoes and R right shoes. Each pair needs exactly one
left + one right shoe. The number of complete pairs is min(L, R), so
whichever side has more shoes leaves the surplus unpaired. That surplus
is simply |L - R|.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution ---------------------------


L, R = map(int, input().split())
print(abs(L - R))
