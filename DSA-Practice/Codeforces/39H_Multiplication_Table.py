"""
Problem   : Multiplication Table
Platform  : Codeforces
Link      : https://codeforces.com/problemset/problem/39/H
Difficulty: *1300
Topic     : Implementation
Date      : 2026-09-06

Approach:
    Print a (k-1) x (k-1) multiplication table where entry (i, j) = i*j,
    but each product is expressed in base-k notation instead of base-10.
    A helper `to_base(n, base)` repeatedly divides n by `base`, collecting
    remainders, then reverses them to build the base-k digit string.

Time complexity : O(k^2 * log_k(k^2)) ~ O(k^2 log k) 
    - k^2 products, each converted to base-k in O(log_k(value)) digit steps
Space complexity: O(k^2) for the output rows (O(k) per row before printing)
"""


# -------------------------- Solution ----------------------------


k = int(input())
def to_base(n, base):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(reversed(digits))
for i in range(1, k):
    row = []
    for j in range(1, k):
        row.append(to_base(i * j, k))
    print(' '.join(row))
