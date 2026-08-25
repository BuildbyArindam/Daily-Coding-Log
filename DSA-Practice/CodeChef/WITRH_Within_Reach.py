"""
Problem: Within Reach
Platform: CodeChef
Link: https://www.codechef.com/problems/WITRH
Date: 2026-08-25
Difficulty: Cakewalk
Topics: Basic Math / Conditional Statements / Implementation

Approach:
    Two points X and Y are "within reach" if the distance between
    them does not exceed K. Since we're on a 1D number line, the
    distance is just |X - Y|. Compare this directly against K and
    print YES/NO accordingly.

Time Complexity:  O(1)  — single arithmetic comparison
Space Complexity: O(1)  — no extra data structures
"""


# --------------------------- Solution ------------------------------


X, Y, K = map(int, input().split())
if abs(X - Y) <= K:
    print("YES")
else:
    print("NO")
