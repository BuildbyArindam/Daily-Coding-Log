"""
Problem   : Bob And The Magic Count
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/bob-and-the-magic-count-d016bec6/
Difficulty: Easy
Topics    : Greedy, Number Theory, Bitmask DP
Date      : 2026-11-23

Approach:
  1. Compute G = gcd of the whole array. If G == 1, cost is 0.
     (All zeros is a special case: answer is min(n, 3).)
  2. Factor G into its distinct primes p_1..p_k. Only these primes
     matter, since they are what must be eliminated.
  3. For each index idx, build a bitmask of the primes that do NOT
     divide idx. Scanning idx from n down to 1, keep only the first
     (cheapest, cost n - idx + 1) index seen for each mask.
  4. Bitmask DP over subsets of primes: table[state] is the minimum
     cost to cover `state`. Combine states with the cheapest option
     per mask until all k primes are covered (state == full).

Complexity:
  Time  : O(n log A) for the gcd + O(sqrt(G)) for factoring
          + O(n * k) to build masks + O(2^k * M) for the DP,
          where M <= min(n, 2^k) is the number of distinct masks.
          k is tiny, since G has few distinct prime factors.
  Space : O(2^k + M) per test case, plus O(n) for the input array.
"""


# ---------------------------------------------- Solution -------------------------------------------------------------


import sys
from math import gcd

def distinct_primes(val):
    found = []
    f = 2
    while f * f <= val:
        if val % f == 0:
            found.append(f)
            while val % f == 0:
                val //= f
        f += 1 if f == 2 else 2
    if val > 1:
        found.append(val)
    return found

def best_cost(n, arr):
    total_g = 0
    for v in arr:
        total_g = gcd(total_g, v)
    if total_g == 1:
        return 0
    if total_g == 0:
        return min(n, 3)
    pr = distinct_primes(total_g)
    k = len(pr)
    full = (1 << k) - 1
    cheapest = {}
    for idx in range(n, 0, -1):     
        m = 0
        for b in range(k):
            if idx % pr[b] != 0:
                m |= 1 << b
        if m and m not in cheapest:
            cheapest[m] = n - idx + 1
    INF = float('inf')
    table = [INF] * (full + 1)
    table[0] = 0
    options = list(cheapest.items())
    for state in range(full + 1):
        cur = table[state]
        if cur == INF:
            continue
        for mk, c in options:
            nxt = state | mk
            if cur + c < table[nxt]:
                table[nxt] = cur + c
    return table[full]

def main():
    tokens = sys.stdin.buffer.read().split()
    pos = 0
    tc = int(tokens[pos]); pos += 1
    out = []
    for _ in range(tc):
        n = int(tokens[pos]); pos += 1
        arr = [int(x) for x in tokens[pos:pos + n]]
        pos += n
        out.append(str(best_cost(n, arr)))
    print("\n".join(out))

main()
