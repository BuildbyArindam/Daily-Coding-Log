"""
Problem   : Chef and Strange Formula (STFM)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/STFM
Difficulty: 1817
Topics    : Math, Modular Arithmetic, Factorials
Date      : 2026-10-13

Approach:
    The answer is the sum of F(x) mod m over all x in p, where
    F(x) = (x+1)! - 1 + x^2 * (x+1) / 2, using the telescoping identity
    sum(k * k!) = (x+1)! - 1.
    - If m == 1, everything is 0 mod 1, so print 0.
    - If x+1 >= m, then m divides (x+1)!, so the factorial term is 0 mod m.
    - Otherwise, collect the distinct needed values x+1 < m, sort them, and
      build the factorial incrementally in one pass, caching each needed value.
    - The polynomial term is computed with exact integer division before
      taking the mod.

Complexity:
    Time : O(n log n + min(max(p), m)) for sorting and the factorial build
    Space: O(n) for the cached factorials
"""


# ------------------------------------------ Solution ------------------------------------------------------------


import sys

def solve():
    input = sys.stdin.buffer.readline
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    if m == 1:
        print(0)
        return
    needed = sorted(set(x + 1 for x in p if x + 1 < m))
    fact_values = {}
    fact = 1
    k = 1
    for target in needed:
        while k <= target:
            fact = (fact * k) % m
            k += 1
        fact_values[target] = fact
    ans = 0
    for x in p:
        if x + 1 >= m:
            fact_part = 0
        else:
            fact_part = fact_values[x + 1]
        poly = (x * x * (x + 1) // 2) % m
        fx = (fact_part - 1 + poly) % m
        ans = (ans + fx) % m
    print(ans)

if __name__ == "__main__":
    solve()
