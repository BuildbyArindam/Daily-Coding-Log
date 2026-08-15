"""
Problem   : Numbers Without d as Digit
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/count-numbers2004/1
Difficulty: Hard
Topic     : Mathematical
Date      : 2026-08-15

Approach:
Count integers in [1, n] that do NOT contain the digit d, using
positional/combinatorial digit counting instead of brute force.

1. For every length k < len(str(n)), count all k-digit numbers that
   avoid digit d (handling the leading-digit case separately since
   it can't be 0, and can't be d).
2. For numbers with the same number of digits as n, walk digit by
   digit (like a digit-DP/"tight bound" scan):
   - At each position, count how many smaller digits could be placed
     there (excluding d) while keeping the earlier prefix fixed,
     and multiply by 9^(remaining positions) for the free digits.
   - If n's own digit at this position equals d, n itself (and every
     extension of this prefix) contains d, so stop early and return
     the running count.
3. If the loop completes without hitting d anywhere in n, n itself
   is valid, so add 1.

Time Complexity : O(log10(n))  -- single pass over the digits of n
Space Complexity: O(log10(n))  -- to hold str(n)
"""


# --------------------- Solution -------------------------


class Solution:
    def countWithout(self, n: int, d: int) -> int:
        # code here
        if n <= 0:
            return 0
        ds = str(d)
        s = str(n)
        count = 0
        length = len(s)
        for k in range(1, length):
            first_choices = 9 - (1 if d != 0 else 0)
            other_choices = 10 - 1
            if d == 0:
                first_choices = 9
            else:
                first_choices = 8
            count += first_choices * (9 ** (k - 1))
        for i, ch in enumerate(s):
            digit = int(ch)
            remaining = length - i - 1
            if i == 0:
                smaller = digit - 1
                if d != 0 and digit > d:
                    smaller -= 1
            else:
                smaller = digit
                if digit > d:
                    smaller -= 1
            if smaller > 0:
                count += smaller * (9 ** remaining)
            if digit == d:
                return count
        return count + 1
      
