"""
Problem: Election
Platform: CodeChef
Link: https://www.codechef.com/problems/ELECTION1
Date: 2026-09-05
Difficulty: Cakewalk
Topics: Basic Math, Greedy, Implementation

Approach:
Majority requires floor(N/2)+1 votes. Given K votes already secured,
the extra votes needed is max(0, majority - K). No loop needed —
pure O(1) arithmetic.

Time Complexity: O(1)
Space Complexity: O(1)
"""


# ----------------------- Solution -----------------------------


N, K = map(int, input().split())
majority = N // 2 + 1
answer = max(0, majority - K)
print(answer)
