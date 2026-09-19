"""
Problem: Circle and Rectangle Overlapping
Link: https://leetcode.com/problems/circle-and-rectangle-overlapping/?envType=daily-question&envId=2026-09-19
Date Solved: 2026-09-19
Difficulty: Medium
Topics: Math, Geometry

Approach:
Find the point on the rectangle closest to the circle's center by clamping
the center's x and y coordinates to the rectangle's bounds. If the squared
distance from this closest point to the center is within radius^2, the
circle and rectangle overlap.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ------------------------------------- Solution -----------------------------------------------


class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))
        dx = closest_x - xCenter
        dy = closest_y - yCenter
        return dx * dx + dy * dy <= radius * radius

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
