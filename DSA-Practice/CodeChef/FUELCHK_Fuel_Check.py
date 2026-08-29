"""
Problem   : Fuel Check
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FUELCHK
Date      : 2026-08-29
Approach  : Read X and Y, compute their product, and compare against
            the threshold 100. Print "Yes" if X * Y >= 100, else "No".
            Pure conditional/arithmetic check — no loops or data structures.
Time      : O(1)
Space     : O(1)
"""


# ------------------------- Solution ------------------------------


X, Y = map(int, input().split())
if X * Y >= 100:
    print("Yes")
else:
    print("No")
