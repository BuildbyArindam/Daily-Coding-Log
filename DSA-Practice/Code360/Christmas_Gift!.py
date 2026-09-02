"""
Problem   : Christmas Gifts!
Platform  : Code360
Link      : https://www.naukri.com/code360/problems/christmas-gifts_3167812?kunjiRedirection=true
Difficulty: Hard
Topic     : Greedy, Sorting, Exchange Argument
Date      : 2026-09-02

Approach:
    For each house, visiting it costs `req[i]` energy up front, then
    refunds `amount[i]` energy after. To minimize the worst-case peak
    energy spent, sort houses by (req - amount) descending — this is
    an exchange-argument greedy: if a house with a bigger deficit
    (req - amount) is visited later, swapping it earlier never
    increases the running peak. Then simulate in that order, tracking
    cumulative `spent` and the max prefix cost (spent_so_far + req_i).

Time complexity : O(n log n) per test case (dominated by the sort)
Space complexity: O(n) for the sorted (req, amount) pairs
"""


# --------------------------- Solution ------------------------------------


from os import *
from sys import *
from collections import *
from math import *
from typing import *

def min_energy(n: int, req: List[int], amount: List[int]) -> int:
    houses = sorted(
        zip(req, amount),
        key=lambda x: x[0] - x[1],
        reverse=True
    )
    spent = 0
    ans = 0
    for r, a in houses:
        ans = max(ans, spent + r)
        spent += a
    return ans

def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        req = list(map(int, input().split()))
        amount = list(map(int, input().split()))
        print(min_energy(n, req, amount))

if __name__ == "__main__":
    main()
