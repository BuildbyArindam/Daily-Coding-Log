"""
Platform   : CodeChef
Problem    : NASA (PALIXOR)
Link       : https://www.codechef.com/problems/PALIXOR
Difficulty : 2014
Solved on  : 2026-10-24
Topics     : Bit Manipulation, Counting, Frequency Array, Palindromes

Approach
--------
Count pairs (i <= j) whose XOR is a palindromic number (0 counts as one).
Values are below 2^15, so every XOR is also below 2^15. Only about 426
palindromes fit in that range, so:
  1. Precompute all nonzero palindromes below 2^15 once.
  2. Per test, build a frequency array over the values.
  3. Equal values (XOR = 0): each value with count w gives w*(w+1)/2 pairs
     (i == j included).
  4. For each nonzero palindrome p, sum freq[v] * freq[v ^ p] over the
     distinct values v. This counts each unordered pair twice, so halve it.
  5. answer = equal-value pairs + (ordered sum / 2).

Complexity
----------
Time  : O(S log S) precompute once (S = 2^15), then O(N + P * K) per test,
        where P ≈ 426 palindromes and K = distinct values (K <= min(N, S)).
        The inner loop over K is vectorised with NumPy.
Space : O(S) for the frequency array and palindrome list.
"""


# ---------------------------------------------- Solution ----------------------------------------------------------


import sys
import numpy as np

def build_pals(limit):
    out = []
    for k in range(1, limit):
        s = str(k)
        if s == s[::-1]:
            out.append(k)
    return out

def main():
    tokens = sys.stdin.buffer.read().split()
    SZ = 1 << 15
    nz_pals = np.array(build_pals(SZ), dtype=np.int64)
    ptr = 1
    answers = []
    for _ in range(int(tokens[0])):
        n = int(tokens[ptr]); ptr += 1
        arr = np.array(tokens[ptr:ptr + n], dtype=np.int64)
        ptr += n
        freq = np.bincount(arr, minlength=SZ).astype(np.int64)
        keys = np.nonzero(freq)[0]
        w = freq[keys]
        total = int((w * (w + 1) // 2).sum())
        ordered = 0
        for p in nz_pals:
            ordered += int((w * freq[keys ^ p]).sum())
        answers.append(total + ordered // 2)
    print("\n".join(map(str, answers)))

main()
