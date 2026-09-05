"""
Problem   : Strings
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/strings-1/
Difficulty: Easy
Topics    : Approved, Combinatorics, Math, Open, String Manipulation
Date      : 2026-09-05

Approach:
For each test case, read n and m as strings. Two "strings" are considered
equal under this problem's rule if they're identical, OR if one is "2" and
the other is "4" (a special-case equivalence defined by the problem).
Print YES if either condition holds, else NO.

Time complexity : O(1) per test case -> O(T) overall
Space complexity: O(1) extra space
"""


# ------------------------- Solution ---------------------------------


t = int(input())
for _ in range(t):
    n, m = input().split()
    if n == m or (n == "2" and m == "4") or (n == "4" and m == "2"):
        print("YES")
    else:
        print("NO")
