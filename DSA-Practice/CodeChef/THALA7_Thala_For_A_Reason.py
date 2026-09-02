"""
Problem   : Thala For A Reason (THALA7)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/THALA7
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic I/O, Conditional Statements, Implementation

Approach:
Read N, print "THALA" if N == 7 else "SADGE".
A single equality check — no loops or data structures needed.

Complexity:
Time  : O(1)
Space : O(1)
"""


# ------------------------- Solution --------------------------------


N = int(input())
if N == 7:
    print("THALA")
else:
    print("SADGE")
