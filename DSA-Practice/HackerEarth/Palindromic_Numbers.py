"""
Problem: Palindromic Numbers
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/palindromic-numbers-7/
Difficulty: Easy
Topic: Ad-Hoc, Algorithms, Basic Programming
Date: 2026-09-11

Approach:
    For each query range [A, B], iterate through every number N in the range,
    convert it to a string, and check if it reads the same forwards and
    backwards (palindrome check via string reversal). Count all such N.

Time Complexity:  O(T * (B - A) * D)  where D = number of digits in N
                   (each number requires an O(D) palindrome check)
Space Complexity: O(D) per check (for the string representation)
"""


# ---------------------------- Solution ----------------------------------


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    count = 0
    for N in range(A, B + 1):
        s = str(N)
        if s == s[::-1]:
            count += 1
    print(count)
