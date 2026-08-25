"""
Problem   : Time Machine
Platform  : CodeChef
Link      : https://www.codechef.com/problems/TIMA
Date      : 2026-08-25
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
    Read year X, check if X + 25 crosses/reaches 2050.
    Print YES if the 25-year-later year is >= 2050, else NO.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# --------------------- Solution ---------------------------


import sys

def main():
    X = int(sys.stdin.read().strip())
    if X + 25 >= 2050:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
