"""
Problem   : Conquer the Fest!! (CLSI)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CLSI
Date      : 2026-08-21
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Logic, Implementation

Approach:
Fest requires attendee IQ (N) to be at least 10x the puzzle
difficulty (B) to solve it. Direct comparison: if N >= 10*B,
answer is YES, else NO. No edge cases beyond the single
inequality check.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------- Solution ---------------------------


N, B = map(int, input().split())
if N >= 10 * B:
    print("YES")
else:
    print("NO")
