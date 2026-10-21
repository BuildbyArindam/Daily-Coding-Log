"""
Platform   : CodeChef (Starters 261, Div. unknown)
Problem    : The Prize Ladder (EXPRIZE)
Link       : https://www.codechef.com/START261A/problems/EXPRIZE
Date       : 2026-10-21
Difficulty : Easy
Topics     : Math, Monotonic Search

Approach
--------
The minimum amount needed to reach level k is
    need(k) = k + (k-1)*k*(k+1)/6      (a cubic in k)
Since need(k) is strictly increasing, the answer is the largest k
with need(k) <= n. For large k, need(k) ~ k^3 / 6, so the cube-root
estimate g = round((6n)^(1/3)) lands within a step or two of the
answer. Two small correction loops fix any floating-point error
(step down while need(g) > n, step up while need(g+1) <= n).

Complexity
----------
Time  : O(1) per test case (constant number of corrections), O(T) overall
Space : O(T) for the buffered output
"""


# ----------------------------------------------- Solution -------------------------------------------------------


import sys
from math import isqrt

def need(k):
    return k + (k - 1) * k * (k + 1) // 6

def solve_one(n):
    g = int(round((6.0 * n) ** (1.0 / 3.0)))
    if g < 1:
        g = 1
    while need(g) > n:
        g -= 1
    while need(g + 1) <= n:
        g += 1
    return g

def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    res = [str(solve_one(int(data[i]))) for i in range(1, t + 1)]
    sys.stdout.write("\n".join(res) + "\n")

main()
