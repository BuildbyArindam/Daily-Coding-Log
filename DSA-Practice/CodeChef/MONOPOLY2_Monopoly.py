"""
Problem   : Monopoly
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MONOPOLY2
Difficulty: 578
Topic     : Math, Ad-Hoc, Greedy
Date      : 2026-09-12

Approach:
For each test case, check if any one of the four values (P, Q, R, S)
exceeds the sum of the other three. If so, that player can never be
matched/balanced by the rest combined, so print "YES" (imbalance
exists). Otherwise print "NO".

Time Complexity : O(T) overall, O(1) per test case
Space Complexity: O(1)
"""


# ----------------------------- Solution --------------------------------


T = int(input())
for _ in range(T):
    P, Q, R, S = map(int, input().split())
    if P > Q + R + S or Q > P + R + S or R > P + Q + S or S > P + Q + R:
        print("YES")
    else:
        print("NO")
