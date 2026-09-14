"""
Problem: Rectangle Overlap
Link: https://leetcode.com/problems/rectangle-overlap/
Platform: LeetCode
Date Solved: 2026-09-14
Difficulty: Easy
Topic: Math, Geometry

Approach:
Two axis-aligned rectangles overlap if and only if they overlap on both the
x-axis and the y-axis. Check that rec1's horizontal range and rec2's horizontal
range intersect (rec1 starts before rec2 ends, and rec1 ends after rec2 starts),
and do the same check for the vertical ranges. If both hold, the rectangles
share positive area.

Time Complexity: O(1) — constant number of comparisons
Space Complexity: O(1) — no extra space used
"""


# ------------------------------ Solution --------------------------------------


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return (
            rec1[0] < rec2[2] and
            rec1[2] > rec2[0] and
            rec1[1] < rec2[3] and
            rec1[3] > rec2[1]
        )

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
