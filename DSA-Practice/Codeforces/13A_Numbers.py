"""
Problem   : Numbers
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/13/A
Difficulty: *1000
Topic     : Implementation, Math
Date      : 2026-08-17

Approach:
    For a given integer A, compute the sum of its digits when represented
    in every base from 2 to A-1. Return this total sum divided by (A-2)
    as a reduced fraction (the average digit-sum across all bases).
    - sum_of_digits_in_base(n, base): repeatedly take n % base to get the
      digit and n //= base to shift, accumulating the digit sum.
    - Reduce total_sum / (A-2) using gcd to lowest terms.

Complexity:
    Time  : O(A log A) — for each of the (A-2) bases, digit extraction
            takes O(log_base A) steps, dominated by base=2 → O(log A).
    Space : O(1) — only running totals and counters are kept.
"""


---------------------- Solution -------------------------


import math

def sum_of_digits_in_base(n, base):
    total = 0
    while n > 0:
        total += n % base
        n //= base
    return total

def main():
    import sys
    A = int(sys.stdin.read().strip())
    total_sum = 0
    for base in range(2, A):
        total_sum += sum_of_digits_in_base(A, base)
    count = A - 2
    common_divisor = math.gcd(total_sum, count)
    numerator = total_sum // common_divisor
    denominator = count // common_divisor
    print(f"{numerator}/{denominator}")

if __name__ == "__main__":
    main()
