"""
Problem   : Triangles
Link      : https://www.codechef.com/problems/TRIANGLE7
Date      : 2026-08-18
Difficulty: Cakewalk
Topics    : Math, Ad-hoc, Geometry (Angle Sum Property)

Approach:
Given two angles A and B of a triangle, the third angle C satisfies
A + B + C = 180 (angle sum property of a triangle).
So simply compute C = 180 - (A + B) and print it.

Time Complexity : O(1) per test case
Space Complexity: O(1)
"""


# ----------------------- Solution ---------------------------


A, B = map(int, input().split())
third_angle = 180 - (A + B)
print(third_angle)
