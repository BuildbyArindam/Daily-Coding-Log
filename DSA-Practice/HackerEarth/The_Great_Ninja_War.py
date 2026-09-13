"""
Problem   : The Great Ninja War (Sallu Bhai and IAS)
Platform  : HackerEarth
Link      : https://www.hackerearth.com/problem/algorithm/sallu-bhai-and-ias-8838ac8d/
Date      : 2026-09-13
Difficulty: Medium
Topics    : Counting and Arrangements, Digit DP, Combinatorics

Approach:
- A number is "special" if, using the multiset of its nonzero digits
  (1-9), the sum of d^d over those digits is divisible by the LCM of
  the distinct digits present.
- Precompute (once, independent of queries) every valid frequency
  vector `counts[1..9]` of nonzero digits (with total digits <= 13,
  since 9^9 already needs up to 13 digits to bound any input range)
  that satisfies the "special" condition. This is done via
  backtracking (`generate`) over digits 1..9, tracking running LCM
  and running digit^digit sum, pruned when digit count is exhausted.
- To count special numbers <= X: pad X to MAX_DIGITS with leading
  zeros, then for each precomputed frequency vector, count how many
  permutations of that exact multiset (multiset = frequency vector +
  the implied zero count) are <= X. This is the standard
  "count permutations of a fixed multiset <= X" digit-by-digit walk:
  at each position, try placing a smaller digit than X's digit (using
  factorial/multinomial counts of the remaining slots), then commit to
  X's digit and recurse into the next position.
- Answer per query = count_leq(R) - count_leq(L - 1).

Complexity:
- Precomputation (generate): bounded by the number of ways to
  distribute <=13 identical "digit slots" over 9 digit types
  (~C(21,8) compositions before pruning), done once. Call this S =
  len(special_counts).
- Per query: O(S * MAX_DIGITS) for count_leq, so O(Q * S * 13) total.
- Space: O(S) for special_counts, O(1) auxiliary (fact/power tables).
"""


# ------------------------------- Solution -----------------------------------------


import sys
import math

MAX_DIGITS = 13
fact = [1] * (MAX_DIGITS + 1)
for i in range(1, MAX_DIGITS + 1):
    fact[i] = fact[i - 1] * i
power = [0] * 10
for d in range(1, 10):
    power[d] = d ** d
special_counts = []

def generate(d, remaining, counts, total, req_lcm):
    if d == 10:
        if sum(counts) > 0 and total % req_lcm == 0:
            special_counts.append(tuple(counts))
        return
    p = power[d]
    for cnt in range(remaining + 1):
        counts.append(cnt)
        if cnt == 0:
            new_lcm = req_lcm
        else:
            new_lcm = math.lcm(req_lcm, d)
        generate(
            d + 1,
            remaining - cnt,
            counts,
            total + cnt * p,
            new_lcm
        )
        counts.pop()
generate(1, MAX_DIGITS, [], 0, 1)

def count_leq(x):
    """Number of special positive integers <= x."""
    if x <= 0:
        return 0
    digits = list(map(int, str(x).zfill(MAX_DIGITS)))
    ans = 0
    for freq in special_counts:
        zero_count = MAX_DIGITS - sum(freq)
        counts = [zero_count] + list(freq)
        denom = 1
        for c in counts:
            denom *= fact[c]
        possible = True
        for pos in range(MAX_DIGITS):
            limit = digits[pos]
            remaining = MAX_DIGITS - pos - 1
            for d in range(limit):
                c = counts[d]
                if c > 0:
                    ans += fact[remaining] // (denom // c)
            c = counts[limit]
            if c == 0:
                possible = False
                break
            denom //= c
            counts[limit] -= 1
        if possible:
            ans += 1
    return ans

def main():
    input = sys.stdin.readline
    Q = int(input())
    result = []
    for _ in range(Q):
        L, R = map(int, input().split())
        answer = count_leq(R) - count_leq(L - 1)
        result.append(str(answer))
    sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()
