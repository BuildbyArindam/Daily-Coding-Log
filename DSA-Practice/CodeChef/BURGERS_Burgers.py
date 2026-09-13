"""
Problem   : Burgers
Platform  : CodeChef
Link      : https://www.codechef.com/problems/BURGERS
Date      : 2026-09-13
Approach  : Each burger needs exactly 1 patty and 1 bun, so the number of
            burgers Chef can make is bottlenecked by whichever ingredient
            he has less of. Answer = min(A, B) per test case.
Time      : O(1) per test case, O(T) overall
Space     : O(1)
"""


# -------------------------- Solution -------------------------------------


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(min(A, B))
