"""
Problem   : Lucky Clover (LUCLO)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/LUCLO
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic Math, Pattern Recognition, Implementation

Approach:
The answer follows a direct linear relationship with N — the minimum
count grows by 3 for every unit increase in N, with a fixed offset of 1.
So the closed-form formula 3*N + 1 gives the answer directly with no
iteration or extra logic needed.

Complexity:
Time  : O(1)
Space : O(1)
"""


# --------------------------- Solution ---------------------------------


N = int(input())
print(3 * N + 1)
