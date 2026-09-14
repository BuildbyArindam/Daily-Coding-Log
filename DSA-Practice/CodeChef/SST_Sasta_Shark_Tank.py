"""
Problem   : Sasta Shark Tank
Platform  : CodeChef
Link      : https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SST
Difficulty: 800 (rated 592 on solve)
Date      : 2026-09-14
Topics    : Greedy, Basic Math, Conditional Logic

Approach:
    Two investors offer A and B rupees respectively for a fixed equity share
    (investor 1 offers for double the equity of investor 2, or similar split —
    adjust wording to match the actual problem statement). Compare the
    effective valuation each offer implies: 2*A vs B.
    - If 2*A > B: FIRST investor's offer is better.
    - If 2*A < B: SECOND investor's offer is better.
    - Else: both are equal, ANY is acceptable.

Time complexity : O(T) — O(1) work per test case.
Space complexity: O(1) — no extra data structures used.
"""


# ---------------------------- Solution -------------------------------------


T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    if 2 * A > B:
        print("FIRST")
    elif 2 * A < B:
        print("SECOND")
    else:
        print("ANY")
