"""
Problem   : Chef and Socks (CHEFSOCKS)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/CHEFSOCKS
Date      : 2026-08-30
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
Chef needs A pairs of socks, and already has X pairs and Y single socks
(each single sock can only complete a pair, not form one alone here per
problem constraints — read as: total wearable pairs achievable is X + Y).
Simply check if the total available (X + Y) meets or exceeds the required
amount A. Print "YES" if sufficient, else "NO".

Time Complexity : O(1) — constant-time arithmetic comparison
Space Complexity: O(1) — no extra data structures used
"""


# ----------------------- Solution -----------------------------


A, X, Y = map(int, input().split())
if X + Y >= A:
    print("YES")
else:
    print("NO")
