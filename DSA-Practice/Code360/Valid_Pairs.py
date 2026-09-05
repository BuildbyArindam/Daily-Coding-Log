"""
Problem   : Valid Pairs
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/problems/valid-pairs_625919
Difficulty: Hard
Topics    : Hashing / Frequency Counting, Modular Arithmetic, Number Theory

Approach:
    For every element, only its remainder mod k matters when checking
    if two elements can sum to a multiple of m (mod k). Build a frequency
    array `freq[r]` = count of elements with arr[i] % k == r.
    For each remainder r, its valid pairing partner is (m - r) % k.
        - If r == partner: freq[r] must be even (elements pair among themselves).
        - If r != partner: freq[r] must equal freq[partner] (cross-pairing).
    If any remainder class fails this, a valid pairing is impossible.

Time complexity : O(n + k)   -> O(n) to build freq, O(k) to verify all classes
Space complexity: O(k)       -> frequency array of size k
"""


# ------------------------ Solution --------------------------


from math import *
from collections import *
from sys import *
from os import *

n = int(input())
arr = list(map(int, input().split()))
k = int(input())
m = int(input())
freq = [0] * k
for num in arr:
    freq[num % k] += 1
possible = True
for r in range(k):
    partner = (m - r) % k
    if r == partner:
        if freq[r] % 2 != 0:
            possible = False
            break
    else:
        if freq[r] != freq[partner]:
            possible = False
            break
print("true" if possible else "false")
