"""
Platform   : CodeChef
Problem    : XD Subsequences (XDS)
Link       : https://www.codechef.com/problems/XDS
Difficulty : 1813
Topics     : Constructive Algorithms, Math, Strings
Date       : 2026-10-11

Approach:
    Build the shortest string of 'X' and 'D' with exactly N subsequences "XD".
    A string of a X's followed by q D's gives a*q pairs, so the length a+q is
    smallest when a ≈ q ≈ sqrt(N). Take L = ceil(sqrt(4N)) and a = L // 2.
    Write N = a*q + r (0 <= r < a). If r == 0, the answer is 'X'*a + 'D'*q.
    Otherwise put r X's, then one D (it pairs with those r X's, giving r),
    then the remaining a-r X's, then q D's. Each of those q D's sees all
    a X's, so the total is r + a*q = N.

Complexity:
    Time  : O(sqrt(N)) per test case to build the output string
    Space : O(sqrt(N)) for the output string
"""


# -------------------------------------- Solution ---------------------------------------------------


import math

T = int(input())

for _ in range(T):
    N = int(input())
    L = math.isqrt(4 * N)
    if L * L < 4 * N:
        L += 1
    a = L // 2
    q, r = divmod(N, a)
    if r == 0:
        ans = 'X' * a + 'D' * q
    else:
        ans = 'X' * r + 'D' + 'X' * (a - r) + 'D' * q
    print(ans)
