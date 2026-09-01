"""
Problem: The Ides of March
Platform: CodeChef
Link: https://www.codechef.com/problems/IDESM
Date: 2026-09-01
Difficulty: Cakewalk
Topics: Basic Math / Conditional Statements / Implementation

Approach:
Read integer n. The Ides of March corresponds to the 15th, so simply
check if n == 15 and print "Yes"/"No" accordingly.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# -------------------------- Solution -------------------------------


n = int(input())
if n == 15:
    print("Yes")
else:
    print("No")
