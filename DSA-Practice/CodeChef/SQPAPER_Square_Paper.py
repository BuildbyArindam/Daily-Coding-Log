# ---------------------------------------------------------------
# Problem   : Square Paper (SQPAPER)
# Platform  : CodeChef (Starters 247)
# Link      : https://www.codechef.com/problems/SQPAPER
# Date      : 2026-08-19
# Difficulty: Cakewalk
# Topics    : Math, Ad-hoc
#
# Approach:
#   Given an A x B rectangular sheet, the largest square that can be
#   cut from it has side length = min(A, B) (limited by the shorter
#   dimension). Area of that square = min(A, B) ** 2.
#
# Time Complexity : O(1) per test case
# Space Complexity: O(1)
# ---------------------------------------------------------------

# ---------------- Solution -----------------------

A, B = map(int, input().split())
print(min(A, B) ** 2)
