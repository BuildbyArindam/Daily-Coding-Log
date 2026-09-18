"""
Problem   : Jenga Night
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/JENGA
Difficulty: 613
Date      : 2026-09-18
Topics    : Math, Number Theory, Divisibility

Approach:
For each test case, check whether X is exactly divisible by N.
If X % N == 0, print "YES", otherwise print "NO".

Time Complexity : O(T) — O(1) per test case
Space Complexity: O(1)
"""


# ------------------------------ Solution --------------------------------------------


T = int(input())

for _ in range(T):
    N, X = map(int, input().split())

    if X % N == 0:
        print("YES")
    else:
        print("NO")
