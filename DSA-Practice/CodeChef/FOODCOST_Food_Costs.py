"""
Problem   : Food Costs
Platform  : CodeChef
Link      : https://www.codechef.com/problems/FOODCOST
Date      : 2026-08-25
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
Given X plates (each costing 6) and an extra fixed cost Y,
total cost = 6*X + Y. Direct formula computation, no loops needed.

Time Complexity : O(1)
Space Complexity: O(1)
"""


# -------------------- Soluion ----------------------------


import sys

def main():
    X, Y = map(int, sys.stdin.read().split())
    total_cost = (6 * X) + Y
    print(total_cost)

if __name__ == "__main__":
    main()
