"""
Problem   : Killjee and Superdromes
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/killjee-and-superdromes-1f1d31c3/
Date      : 2026-08-20
Difficulty: Easy
Topic     : Implementation / Basics

Approach:
  A "superdrome" is a number that is a palindrome in BOTH its decimal
  and binary representations. For each query n, we need the count of
  superdromes in [1, n].
  Since q queries can repeat/overlap ranges, precompute a prefix-count
  array `pref` up to the global limit (1,000,000) once: for every i,
  check decimal palindrome first (cheap string check) and only then
  check binary palindrome (short-circuits most non-palindromic i early).
  Answer each query in O(1) via direct array lookup.

Complexity:
  Precompute : O(LIMIT * D)  where D = avg digit length (~7 decimal, ~20 binary)
  Per query  : O(1) lookup after precompute
  Overall    : O(LIMIT * D + Q)
  Space      : O(LIMIT) for the prefix array
"""


# ---------------------------- Solution -------------------------------


import sys

def precompute_superdromes(limit=1000000):
    pref = [0] * (limit + 1)
    count = 0
    for i in range(1, limit + 1):
        s = str(i)
        if s == s[::-1]:
            b = bin(i)[2:]
            if b == b[::-1]:
                count += 1
        pref[i] = count
    return pref

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    pref = precompute_superdromes(1000000)
    results = []
    for i in range(1, q + 1):
        n = int(input_data[i])
        results.append(str(pref[n]))
    print("\n".join(results))

if __name__ == "__main__":
    main()
