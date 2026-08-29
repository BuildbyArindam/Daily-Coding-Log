"""
Problem   : Equal Buying (EQBUY)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/EQBUY
Date      : 2026-08-29
Difficulty: Cakewalk
Topics    : Basic Math, Parity, Conditional Statements

Approach:
Chef has N kg of flour, made up of an equal number of 1 kg and 2 kg
sacks. If there are k sacks of each, total weight = k*1 + k*2 = 3k.
So the answer is "Yes" iff N is divisible by 3, else "No".

Time complexity : O(1)
Space complexity: O(1)
"""


# -------------------- Solution ------------------------


N = int(input())
if N % 3 == 0:
    print("Yes")
else:
    print("No")
