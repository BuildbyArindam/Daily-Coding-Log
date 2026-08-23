"""
Problem: Notebook Counting
Platform: CodeChef
Link: https://www.codechef.com/problems/NOTECNT
Date: 2026-08-23

Approach:
Given A boxes with B notebooks each, and each notebook has 100 pages,
total page count is simply A * B * 100. Direct formula computation,
no iteration needed.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ------------------------ Solution ------------------------


A, B = map(int, input().split())
total_lines = A * B * 100
print(total_lines)
