"""
Problem   : Balancing with Distinct Powers
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/balancing-pan5038/1
Difficulty: Easy
Topics    : Mathematics
Date      : 2026-10-10

Approach:
    Weights are a^0, a^1, a^2, ..., each usable at most once, on either pan.
    This is equivalent to writing b in base `a` with every digit in {-1, 0, 1}.
    At each step look at the last base-a digit r = b % a:
      - r == 0      -> no weight needed at this power; b //= a
      - r == 1      -> put the weight on the opposite pan; b = (b - 1) // a
      - r == a - 1  -> put the weight on the same pan as the object (digit -1,
                       carry 1); b = (b + 1) // a
      - otherwise   -> a digit outside {-1, 0, 1} is unavoidable -> False

Time Complexity : O(log_a b)  (b shrinks by a factor of a each iteration)
Space Complexity: O(1)
"""


# ------------------------------------------- Solution -------------------------------------------------------


class Solution:
    def balancePan(self, a, b):
        # code here
        while b > 0:
            r = b % a
            if r == 0:
                b //= a
            elif r == 1:
                b = (b - 1) // a
            elif r == a - 1:
                b = (b + 1) // a
            else:
                return False
        return True
