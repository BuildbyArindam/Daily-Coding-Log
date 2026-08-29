"""
Problem: Christmas Greetings
Platform: CodeChef
Link: https://www.codechef.com/problems/CHRISTGREET
Date Solved: 2026-08-29
Difficulty: Cakewalk
Topics: Basic I/O, Conditional Statements, Implementation

Approach:
Read a single integer X. If X equals 25 (Christmas Day), print "CHRISTMAS";
otherwise print "ORDINARY". Direct conditional check, no edge cases beyond
the single comparison.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ------------------------- Solution ----------------------------


X = int(input())
if X == 25:
    print("CHRISTMAS")
else:
    print("ORDINARY")
