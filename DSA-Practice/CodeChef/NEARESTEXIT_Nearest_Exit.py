"""
Problem: Nearest Exit
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/NEARESTEXIT
Date: 2026-09-14
Difficulty: 585
Topics: Implementation, Conditionals / Ad-hoc

Approach:
Given a position X on a corridor of length 100 (exits at 0 and 100),
compare X against the midpoint (50). If X <= 50, the LEFT exit is
nearer (or equal distance); otherwise the RIGHT exit is nearer.
Pure constant-time comparison per query — no data structure needed.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# ------------------------- Solution ------------------------------------


T = int(input())
for _ in range(T):
    X = int(input())
    if X <= 50:
        print("LEFT")
    else:
        print("RIGHT")
