"""
Problem   : Small Factorials
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FCTRL2
Difficulty: 648
Date      : 2026-09-19
Topics    : Math, Big Integers, Basic Simulation

Approach:
    For each test case, compute N! iteratively by multiplying from 1 to N.
    Python's int type supports arbitrary precision natively, so no custom
    big-integer logic is needed (unlike C++/Java, where this problem tests
    bignum handling).

Complexity:
    Time  : O(N) multiplications per test case (each multiplication itself
            costs more than O(1) as the number grows, but standard analysis
            treats it as O(N) per case).
    Space : O(1) extra space, excluding the size of the output integer itself.
"""


# --------------------------------- Solution --------------------------------------------


t = int(input())

for _ in range(t):
    n = int(input())

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    print(factorial)
