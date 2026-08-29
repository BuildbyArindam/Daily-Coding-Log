"""
Problem: Too Much Homework!
Platform: CodeChef
Link: https://www.codechef.com/problems/HWFIN
Date Solved: 2026-08-29
Difficulty: Cakewalk
Topics: Basic Math, Conditional Statements, Implementation

Approach:
Chef has already solved X questions and can attempt at most 10 more
worksheets, each containing Y questions. Since Chef would solve every
question in each worksheet taken, the maximum total achievable is
X + 10*Y. Compare this against the target of 100 questions and print
"YES" if it's reachable, else "NO".

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------------- Solution ---------------------------------


X, Y = map(int, input().split())
if X + 10 * Y >= 100:
    print("YES")
else:
    print("NO")
