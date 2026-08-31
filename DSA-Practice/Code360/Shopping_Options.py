"""
Problem   : Shopping Options
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/shopping-options_1538511?kunjiRedirection=true
Difficulty: Easy
Date      : 2026-08-31
Topics: Brute Force, Recursion (implicit via nested loops), Cartesian Product, Arrays

Approach:
Brute-force enumeration of all possible combinations of one item from each
category (pants, shirts, shoes, skirts). For every combination, check if the
total cost is within the given budget, and count valid combinations.

Time Complexity : O(P * S * Sh * K)  -- P, S, Sh, K = sizes of the 4 lists
Space Complexity: O(1) additional space (excluding input lists)
"""


# ---------------------------- Solution ---------------------------------


def shoppingOptions(pants, shirts, shoes, skirts, budget):
    count = 0
    for p in pants:
        for s in shirts:
            for sh in shoes:
                for sk in skirts:
                    if p + s + sh + sk <= budget:
                        count += 1
    return count
