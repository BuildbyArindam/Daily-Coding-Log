"""
Problem: The Three Topics
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/THREETOPICS
Date Solved: 2026-09-12
Difficulty: 800 (rated as 573)
Topic(s): Conditionals, Brute Force

Approach:
Read four integers A, B, C, X. X represents a topic chosen by a student.
Simply check if X matches any of A, B, or C using an OR condition.
No loops or data structures needed — pure conditional logic.

Time Complexity: O(1) — constant number of comparisons
Space Complexity: O(1) — no extra space used
"""


# ---------------------- Solution --------------------------------------

A, B, C, X = map(int, input().split())
if X == A or X == B or X == C:
    print("Yes")
else:
    print("No")
