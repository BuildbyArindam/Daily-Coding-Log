"""
Problem   : Values with Equal Array Remainders (K-Modulus Array Element)
Link      : https://www.geeksforgeeks.org/problems/k-modulus-array-element0255/1
Platform  : GeeksforGeeks
Date      : 2026-09-11
Difficulty: Easy
Topic     : Arrays, Mathematics (GCD, Divisors)

Approach:
- If all elements give the same remainder mod k, then k must divide every
  pairwise difference of the array elements.
- So compute g = GCD of |arr[i] - arr[0]| for all i. Any k that divides g
  works, so the answer is the count of divisors of g.
- If g == 0 (all elements identical), no finite k satisfies the condition
  uniquely, so return -1.
- Divisor count is found in O(sqrt(g)) by checking factor pairs.

Time Complexity : O(n + sqrt(g))  -> O(n) to compute GCD, O(sqrt(g)) to count divisors
Space Complexity: O(1)
"""


# --------------------------- Solution ---------------------------------------


from math import gcd

class Solution:
    def sameMod(self, arr):
        # code here
        g = 0
        for i in range(1, len(arr)):
            g = gcd(g, abs(arr[i] - arr[0]))
        if g == 0:
            return -1
        count = 0
        d = 1
        while d * d <= g:
            if g % d == 0:
                count += 1
                if d != g // d:
                    count += 1
            d += 1
        return count
