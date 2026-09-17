"""
Problem: Easy Sum Set Problem
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/easy-sum-set-problem-7e6841ca/
Difficulty: Easy
Topics: Algorithms, Searching
Date Solved: 2026-09-17

Approach:
For every candidate b in [1, 100], check whether adding b to every
element of set A lands inside set C. Using a set for C gives O(1)
average membership checks, so this is just a brute-force scan over
the small candidate range for b, validated against a hashed set.

Time Complexity: O(100 * n) ~ O(n), where n = |A| (100 is a constant
    upper bound on b's search range)
Space Complexity: O(n + m), for storing sets A and C
"""


# ------------------------------ Solution -----------------------------------------


n = int(input())
A = set(map(int, input().split()))
m = int(input())
C = set(map(int, input().split()))
answer = []
for b in range(1, 101):
    if all(a + b in C for a in A):
        answer.append(b)
print(*answer)
