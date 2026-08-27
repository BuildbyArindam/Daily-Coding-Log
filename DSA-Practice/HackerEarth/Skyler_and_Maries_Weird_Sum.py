"""
Problem   : Skyler and Marie's Weird Sum
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/pallindrome-sum/
Date      : 2026-08-27
Difficulty: Medium
Topics    : Math, Digit Sum, Combinatorics, Modular Arithmetic

Approach  :
    For an N-digit number range, every digit position's contribution to the
    total digit-sum across all N-digit numbers follows a fixed pattern based
    on symmetry (digit d and digit (9-d) mirror across positions) and the
    count of times each position cycles through 0-9. Precompute:
      - first_digit_sum / other_digit_sum: average digit-sum contribution
        for the leading digit vs. other digit positions (leading digit
        can't be 0, so it's handled separately with 45 * 10^(k-1)).
      - geom_sum(a, b): closed-form sum of 10^a + ... + 10^b (mod P) using
        the modular inverse of 9, to fold the per-position multiplier sums
        into O(log MOD) work instead of iterating over all N positions.
    The two halves of the N-digit number (mirrored positions) are combined
    via coefficient sums (coeff_sum) built from geom_sum, giving an O(1)
    (amortized O(log MOD) for modpow) formula per query.

Time complexity : O(log(MOD)) per test case (dominated by pow() calls)
Space complexity: O(1) additional space (excluding input/output buffers)
"""


# --------------------- Solution ----------------------------


import sys

MOD = 10**9 + 7
INV9 = pow(9, MOD - 2, MOD)

def geom_sum(a, b):
    """Return 10^a + 10^(a+1) + ... + 10^b modulo MOD."""
    if a > b:
        return 0
    return (pow(10, b + 1, MOD) - pow(10, a, MOD)) * INV9 % MOD

def solve(N):
    if N == 1:
        return 45
    k = (N + 1) // 2
    first_digit_sum = 45 * pow(10, k - 1, MOD) % MOD
    other_digit_sum = 45 * 9 * pow(10, k - 2, MOD) % MOD
    first_coeff = (pow(10, N - 1, MOD) + 1) % MOD
    if N % 2 == 0:
        coeff_sum = (
            geom_sum(k, 2 * k - 2) +
            geom_sum(1, k - 1)
        ) % MOD
    else:
        coeff_sum = (
            geom_sum(k, 2 * k - 3) +
            geom_sum(1, k - 1)
        ) % MOD
    answer = (
        first_digit_sum * first_coeff +
        other_digit_sum * coeff_sum
    ) % MOD
    return answer

def main():
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        N = int(input())
        out.append(str(solve(N)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
