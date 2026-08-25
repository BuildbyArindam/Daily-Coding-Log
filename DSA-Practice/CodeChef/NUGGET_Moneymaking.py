"""
Problem: Moneymaking
Platform: CodeChef
Link: https://www.codechef.com/problems/NUGGET
Date: 2026-08-25
Difficulty: Cakewalk
Topics: Basic Math, Implementation, Basic I/O

Approach:
Read X (number of chicken nuggets) and Y (number of gold coins per... 
whatever unit), compute total coins as a direct weighted sum:
total = X*5000 + Y*9800. No loops, no conditionals — pure arithmetic.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution ----------------------


import sys

def main():
    X, Y = map(int, sys.stdin.read().split())
    total_coins = (X * 5000) + (Y * 9800)
    print(total_coins)

if __name__ == "__main__":
    main()
