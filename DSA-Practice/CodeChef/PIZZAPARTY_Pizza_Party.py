"""
Problem: Pizza Party (PIZZAPARTY)
Platform: CodeChef
Link: https://www.codechef.com/problems/PIZZAPARTY
Date Solved: 2026-09-02
Difficulty: Cakewalk
Topics: Basic Math, Ceiling Division, Implementation

Approach:
Each adult (A) eats 4 slices, and there are A+1 adults (A adults + 1 host/self,
per problem statement) — hence (A + 1) * 4. Each child (B) eats 3 slices,
contributing B * 3. Total slices needed = (A + 1)*4 + B*3. Since each pizza
has 8 slices, the number of pizzas required is the ceiling of
total_slices / 8, computed via math.ceil.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# -------------------------- Solution -----------------------------


import math
A, B = map(int, input().split())
total_slices = (A + 1) * 4 + B * 3
pizzas = math.ceil(total_slices / 8)
print(pizzas)
