# Problem: Pizza Split (PZSPLIT)
# Link: https://www.codechef.com/problems/PZSPLIT
# Date: 2026-08-25
# Difficulty: Cakewalk
# Topics: Basic Math, Parity, Conditional Statements
#
# Approach:
# A pizza has N slices, split between Chef and Chefina.
# If N is even, 1 pizza suffices (N/2 slices each).
# If N is odd, 1 pizza can't be split evenly -> buy 2 pizzas (2N slices,
# giving N slices each, which is always achievable since 2N is even).
#
# Time Complexity: O(1)
# Space Complexity: O(1)


# ------------------------ Solution ---------------------------


N = int(input().strip())
if N % 2 == 0:
    print(1)
else:
    print(2)
