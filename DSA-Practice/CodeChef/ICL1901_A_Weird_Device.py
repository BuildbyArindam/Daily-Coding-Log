"""
Problem   : A Weird Device (ICL1901)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ICL1901
Difficulty: 1810
Topics    : Math, Implementation
Date      : 2026-10-11

Approach:
    For each test case, only k matters (n is read but unused).
    Collect the distinct digits of k in a set, let d = size of that set,
    and print d^3.

Complexity (per test case):
    Time  : O(len(k)) to scan the digits of k
    Space : O(1), since the set holds at most 10 digits
"""


# --------------------------------------------- Solution --------------------------------------------------------


t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    digits = set(str(k))
    d = len(digits)
    print(d ** 3)
