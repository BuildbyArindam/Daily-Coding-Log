"""
Problem   : Shil and Lucky String
Platform  : HackerEarth (Easy)
Link      : https://www.hackerearth.com/practice/algorithms/sorting/merge-sort/practice-problems/algorithm/shil-and-lucky-string-1/
Date      : 2026-11-01
Topics    : Algorithms, Implementation, Sorting

Approach:
    Split the string into a left half and a right half, then compute the
    minimum number of changes for each of three target conditions and
    take the smallest:
      1. Equal    : halves become anagrams -> len - multiset overlap (Counter).
      2. Smaller  : every left char < its matched right char. Sort both
                    halves and greedily two-pointer match. Left 'z' and
                    right 'a' can never satisfy it, so the answer is
                    max(pairs - good, stuck).
      3. Greater  : mirror of case 2 by flipping the alphabet (a<->z) and
                    reusing the "smaller" routine.

Complexity:
    Time  : O(N log N) for the sorts (O(N) with counting sort, since the
            alphabet is only 26 letters).
    Space : O(N)
"""


# ------------------------------------------- Solution -------------------------------------------------------------


import sys
from collections import Counter

FLIP = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")

def cost_equal(left, right):
    cl, cr = Counter(left), Counter(right)
    kept = sum(min(cl[ch], cr[ch]) for ch in cl)
    return len(left) - kept

def cost_smaller(left, right):
    pairs = len(left)
    stuck = left.count('z') + right.count('a')
    lo = sorted(ch for ch in left if ch != 'z')
    hi = sorted(ch for ch in right if ch != 'a')
    ptr = good = 0
    for ch in hi:
        if ptr < len(lo) and lo[ptr] < ch:
            good += 1
            ptr += 1
    return max(pairs - good, stuck)

def cost_greater(left, right):
    return cost_smaller(left.translate(FLIP), right.translate(FLIP))

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1]
    mid = n // 2
    a, b = s[:mid], s[mid:]
    print(min(cost_equal(a, b), cost_smaller(a, b), cost_greater(a, b)))

main()
