"""
Problem: Reverse The Number
Link: https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/FLOW007
Platform: CodeChef | Difficulty: 588
Date Solved: 2026-09-14
Topic: Math, String Manipulation

Approach:
Convert each integer to a string, reverse it, and convert back to int
(this also strips any leading zeros that result from the reversal).

Time Complexity: O(D) per test case, where D = number of digits in N
Space Complexity: O(D) for the string representation
"""


# --------------------------- Solution ---------------------------------


T = int(input())

for _ in range(T):
    N = int(input())
    print(int(str(N)[::-1]))
