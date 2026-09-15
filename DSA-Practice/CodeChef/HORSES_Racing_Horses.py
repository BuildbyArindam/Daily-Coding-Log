"""
Problem   : Racing Horses
Platform  : CodeChef
Link      : https://www.codechef.com/problems/HORSES
Difficulty: 1231
Topics    : Sorting, Greedy/Math
Date      : 2026-09-15

Approach:
    Sort the horse speeds. The minimum possible difference between
    any two horses must occur between two horses that are adjacent
    in sorted order (since sorting brings closest values together).
    So just scan adjacent pairs in the sorted array and track the
    minimum difference.

Time Complexity : O(n log n) per test case (dominated by the sort)
Space Complexity: O(n) for storing the input list
"""


# ------------------------- Solution ------------------------------------


t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()
    ans = s[1] - s[0]
    for i in range(1, n):
        ans = min(ans, s[i] - s[i - 1])
    print(ans)
