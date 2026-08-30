# Platform: CodeChef
# Problem: Move Grid (MOVEMENT)
# Link: https://www.codechef.com/problems/MOVEMENT
# Date: 2026-08-30
# Difficulty: Cakewalk
# Topics: Basic Math, Implementation, Coordinate Geometry
# Approach: Given two points (A,B) and (C,D), the required move vector
#           is simply the difference of coordinates: dx = A-C, dy = B-D.
#           Direct O(1) arithmetic, no loops or conditionals needed.
# Time Complexity: O(1)
# Space Complexity: O(1)


# ------------------------- Solution --------------------------


A, B, C, D = map(int, input().split())
x = A - C
y = B - D
print(x, y)
