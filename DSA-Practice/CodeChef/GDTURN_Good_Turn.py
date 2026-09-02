"""
Problem   : Good Turn (GDTURN)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/GDTURN
Date      : 2026-09-02
Difficulty: Cakewalk
Topics    : Basic Math, Conditional Statements, Implementation

Approach:
For each test case, read two integers x and y. A "turn" is good if
their sum exceeds 6. Directly compare (x + y) to 6 and print YES/NO
accordingly — no data structures or precomputation needed.

Complexity:
Time  : O(T)   -- one O(1) check per test case
Space : O(1)   -- no extra storage beyond input variables
"""


# -------------------------- Solution -------------------------------


t = int(input())
for i in range(0, t):
    x, y = map(int, input().split())
    if x + y > 6:
        print("YES")
    else:
        print("NO")
