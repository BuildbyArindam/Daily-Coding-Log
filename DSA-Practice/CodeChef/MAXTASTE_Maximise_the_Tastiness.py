"""
Problem   : Maximise the Tastiness
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MAXTASTE
Date      : 2026-09-18
Difficulty: 627
Topics    : Greedy, Math, Implementation, Ad-hoc

Approach:
For each test case we're given two pairs (a, b) and (c, d). To maximise
the total tastiness we independently pick the larger value from each
pair and sum them — max(a, b) + max(c, d). Since the two pairs are
independent choices, picking greedily within each pair is optimal
(no exchange argument needed since there's no shared constraint).

Time complexity : O(T) — O(1) work per test case
Space complexity: O(1) — no extra data structures beyond input vars
"""


# -------------------------------- Solution -----------------------------------------


T = int(input())

for _ in range(T):
    a, b, c, d = map(int, input().split())
    
    ans = max(a, b) + max(c, d)
    print(ans)
