"""
Problem: Selling Coins
Platform: CodeChef
Link: https://www.codechef.com/problems/SELLCOIN
Date Solved: 2026-09-01
Difficulty: Cakewalk
Topics: Basic Math, Implementation

Approach:
Each silver coin sells for 1 rupee, and each gold coin converts into
2 silver coins (worth 2 rupees). Total earnings = A*1 + B*2.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# --------------------------- Solution -------------------------------


A, B = map(int, input().split())
answer = A + 2 * B
print(answer)
