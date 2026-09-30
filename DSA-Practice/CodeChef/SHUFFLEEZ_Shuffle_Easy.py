"""
Problem   : Shuffle (Easy) - SHUFFLEEZ
Platform  : CodeChef (Starters 258, Div B)
Link      : https://www.codechef.com/START258B/problems/SHUFFLEEZ
Date      : 2026-09-30
Difficulty: Medium
Topics    : Combinatorics, Modular Arithmetic

Approach:
  The answer has a closed form: k^(n-k+1) * (k-1)! mod 998244353.
  The array values are never needed, so they are skipped while parsing.
  Read all test cases first, precompute factorials once up to the largest
  k, then answer each case with one modular exponentiation and one lookup.

Complexity:
  Time  : O(max_k + T log n)  - factorial precompute + fast pow per test
  Space : O(max_k + T)        - factorial table + stored queries/output
"""


# ------------------------------------- Solution ---------------------------------------------


import sys
MOD = 998244353

def build_factorials(limit):
    fact = [1] * (limit + 1)
    for idx in range(2, limit + 1):
        fact[idx] = fact[idx - 1] * idx % MOD
    return fact

def solve_all(data):
    ptr = 0
    total_cases = int(data[ptr]); ptr += 1
    n_vals = []
    k_vals = []
    max_k = 0
    for _ in range(total_cases):
        n = int(data[ptr]); k = int(data[ptr + 1]); ptr += 2
        n_vals.append(n)
        k_vals.append(k)
        if k > max_k:
            max_k = k
        ptr += n
    fact_table = build_factorials(max_k + 1)
    out_lines = []
    for n, k in zip(n_vals, k_vals):
        exponent = n - k + 1
        base_power = pow(k, exponent, MOD)
        combined = base_power * fact_table[k - 1] % MOD
        out_lines.append(str(combined))
    return "\n".join(out_lines)

def main():
    raw = sys.stdin.buffer.read().split()
    result = solve_all(raw)
    sys.stdout.write(result + "\n")

if __name__ == "__main__":
    main()
