"""
Problem   : Spring Cleaning
Platform  : CodeChef
Link      : https://www.codechef.com/problems/SPRCLN
Date      : 2026-08-25
Difficulty: Cakewalk
Topics    : Basic Math, Implementation

Approach:
Read X (spring-cleaning items) and Y (deep-cleaning items). Each X-item
takes 30 minutes, each Y-item takes 60 minutes. Total time is a direct
linear sum — no edge cases beyond input parsing.

Complexity:
Time  : O(1)
Space : O(1)
"""


# ------------------------ Solution ----------------------------


import sys

def main():
    X, Y = map(int, sys.stdin.read().split())
    total_time = (X * 30) + (Y * 60)
    print(total_time)

if __name__ == "__main__":
    main()
