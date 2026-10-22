"""
Platform   : CodeChef
Problem    : Balanced Ingredients (BAIN)
Link       : https://www.codechef.com/problems/BAIN
Difficulty : 850
Topics     : Brute Force, Subsets 
Date       : 2026-10-22

Approach:
    The input is only 4 integers, so brute force is enough. Try every
    non-empty subset (largest first) and return "Yes" as soon as one
    sums to 0, otherwise "No".

Complexity:
    Time  : O(2^4 * 4) = O(1), since the input size is fixed
    Space : O(1)
"""


# ---------------------------------------------- Solution ---------------------------------------------------------


import sys
from itertools import combinations as pick

def solve(vals):
    n = len(vals)
    for size in range(n, 0, -1):
        for grp in pick(vals, size):
            if sum(grp) == 0:
                return "Yes"
    return "No"

def main():
    raw = sys.stdin.read().split()
    nums = [int(tok) for tok in raw[:4]]
    print(solve(nums))

main()
