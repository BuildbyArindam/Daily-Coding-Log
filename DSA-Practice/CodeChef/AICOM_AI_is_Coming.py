"""
Problem   : AI is Coming
Platform  : CodeChef
Link      : https://www.codechef.com/problems/AICOM
Date      : 2026-08-22
Difficulty: Easy
Topics    : Implementation, Conditionals

Approach:
Read a single integer X and check it against a fixed threshold (60).
Print "YES" if X <= 60, else "NO". Straightforward one-pass conditional
check with no data structures involved.

Complexity:
Time  : O(1)
Space : O(1)
"""


# --------------------------- Solution --------------------------------


X = int(input())
if X <= 60:
    print("YES")
else:
    print("NO")
