"""
Problem   : Max Digit Sum Number in 1 to n
Link      : https://www.geeksforgeeks.org/problems/biggest-integer-having-maximum-digit-sum1704/1
Platform  : GeeksforGeeks
Difficulty: Easy
Topic     : Mathematics, Numbers
Date      : 2026-09-09

Approach:
    For each prefix position i in n's digit string, try decreasing digit[i]
    by 1 and filling all digits after it with '9'. This generates the
    largest possible number <= n that "gives up" digit sum starting at
    position i. Track the candidate with the maximum digit sum; if two
    candidates tie on digit sum, keep the numerically larger one.
    n itself is always a valid candidate (its own digit sum) and is used
    as the initial answer.

Time Complexity : O(d^2)  -> d = number of digits in n (string slicing/building
                  per position); can be optimized to O(d) with careful
                  index-based construction instead of slicing.
Space Complexity: O(d)    -> for the string representation and candidate strings.
"""


# ----------------------- Solution -----------------------------------


class Solution:
    def findMax(self, n):
        s = str(n)
        m = len(s)
        ans = n
        max_sum = sum(int(ch) for ch in s)
        prefix = 0
        for i in range(m):
            digit = int(s[i])
            if digit > 0:
                candidate_sum = (
                    prefix
                    + (digit - 1)
                    + 9 * (m - i - 1)
                )
                candidate = int(
                    s[:i] + str(digit - 1) + '9' * (m - i - 1)
                )
                if (candidate_sum > max_sum or
                        (candidate_sum == max_sum and candidate > ans)):
                    max_sum = candidate_sum
                    ans = candidate
            prefix += digit
        return ans
