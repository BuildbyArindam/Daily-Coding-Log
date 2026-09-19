"""
Problem: Chef and Water Bottles
Platform: CodeChef
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/CHEFBOTTLE
Difficulty: 662
Date Solved: 2026-09-19
Topics: Math, Greedy, Basic Programming

Approach:
Chef has N bottles, each with capacity X, and K units of water available.
The number of bottles that can actually be filled is K // X (integer division),
but this can never exceed the total bottles Chef has (N). So the answer is
the minimum of these two values.

Time Complexity: O(1) per test case, O(T) overall
Space Complexity: O(1)
"""


# -------------------------------------- Solution -------------------------------------------------


T = int(input())

for _ in range(T):
    N, X, K = map(int, input().split())
    print(min(N, K // X))
