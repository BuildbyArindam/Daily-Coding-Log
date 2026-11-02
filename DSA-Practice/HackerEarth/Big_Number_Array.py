"""
Problem   : Big Number Array
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/data-structures/advanced-data-structures/segment-trees/practice-problems/algorithm/big-number-array-043361b7/
Date      : 2026-11-02
Difficulty: Medium
Topics    : Fenwick tree (BIT), Segment trees, Hashing

Approach  :
  Each range update (x..y, with value interval [lo, hi]) is reduced to a
  64-bit XOR tag: scramble(lo) ^ scramble(hi + 1). A Fenwick tree stores XOR
  range updates (XOR at x and y+1), so a prefix-XOR query gives the combined
  hash of everything applied to a position. Two positions are equal iff their
  hashes match. scramble() is a salted SplitMix64-style mixer, so the hash is
  randomized per run and can't be hacked with fixed inputs.

Complexity:
  Time  : O((N + Q) log N) overall; each update/query is O(log N)
  Space : O(N) for the Fenwick tree per test case
  Note  : Probabilistic. Collision chance is about 2^-64 per comparison.
"""


# -------------------------------------------------------- Solution --------------------------------------------------------------


import sys
import random

MASK = (1 << 64) - 1
SALT = random.getrandbits(64)

def scramble(v):
    v = (v + SALT + 0x9E3779B97F4A7C15) & MASK
    v = ((v ^ (v >> 30)) * 0xBF58476D1CE4E5B9) & MASK
    v = ((v ^ (v >> 27)) * 0x94D049BB133111EB) & MASK
    return v ^ (v >> 31)

def main():
    tokens = sys.stdin.buffer.read().split()
    cur = 0
    cases = int(tokens[cur]); cur += 1
    answers = []
    for _ in range(cases):
        n = int(tokens[cur]); q = int(tokens[cur + 1]); cur += 2
        tree = [0] * (n + 2)
        for _ in range(q):
            kind = tokens[cur]
            if kind == b'1':
                x = int(tokens[cur + 1]); y = int(tokens[cur + 2])
                lo = int(tokens[cur + 3]); hi = int(tokens[cur + 4])
                cur += 5
                tag = scramble(lo) ^ scramble(hi + 1)
                i = x
                while i <= n:
                    tree[i] ^= tag
                    i += i & -i
                i = y + 1
                while i <= n:
                    tree[i] ^= tag
                    i += i & -i
            else:
                a = int(tokens[cur + 1]); b = int(tokens[cur + 2])
                cur += 3
                ha = 0
                i = a
                while i > 0:
                    ha ^= tree[i]
                    i -= i & -i
                hb = 0
                i = b
                while i > 0:
                    hb ^= tree[i]
                    i -= i & -i
                answers.append("YES" if ha == hb else "NO")
    sys.stdout.write("\n".join(answers) + ("\n" if answers else ""))

main()
