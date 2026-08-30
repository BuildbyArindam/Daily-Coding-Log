# Problem: Payment Scheme
# Platform: CodeChef
# Link: https://www.codechef.com/problems/PAYSC
# Date: 2026-08-30
# Difficulty: Cakewalk
# Topics: Basic Math, Conditional Statements, Implementation
#
# Approach:
#   Two payment schemes are available:
#     Scheme 1: flat 100 + 4 per unit of X
#     Scheme 2: flat 300, regardless of X
#   The optimal choice is simply the minimum of the two costs.
#
# Time Complexity: O(1)
# Space Complexity: O(1)


# ---------------------- Solution ---------------------------


X = int(input())
scheme1 = 100 + 4 * X
scheme2 = 300
print(min(scheme1, scheme2))
