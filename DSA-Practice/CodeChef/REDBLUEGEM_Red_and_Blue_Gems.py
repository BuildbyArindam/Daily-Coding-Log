"""
Problem   : Red and Blue Gems
Platform  : CodeChef
Link      : https://www.codechef.com/problems/REDBLUEGEM
Date      : 2026-08-28
Difficulty: Cakewalk
Topics    : Basic Math / Greedy / Implementation

Approach:
Given R red gems each worth P and B blue gems each worth Q,
compare total value of taking all red gems vs all blue gems
and pick the maximum. Since values are uniform per color,
the optimal strategy is simply max(R*P, B*Q).

Time Complexity : O(1)
Space Complexity: O(1)
"""


# ------------------------- Solution ------------------------------

R, B, P, Q = map(int, input().split())
red_coins = R * P
blue_coins = B * Q
print(max(red_coins, blue_coins))
