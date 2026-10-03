"""
Problem   : The Old Monk
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/the-old-monk/
Difficulty: Easy
Topics    : Binary Search, Two Pointers, Sorting
Date      : 2026-10-03

Approach:
    Both arrays are non-increasing, so for a fixed i the valid j's (B[j] >= A[i])
    form a contiguous prefix of the range starting at i. As i grows, A[i] only
    gets smaller, so the furthest valid j never moves backwards. That allows a
    two-pointer sweep: advance j while B[j] >= A[i], then record (j - 1) - i as
    the best distance for this i. No binary search is needed.

Complexity:
    Time  : O(n) per test case, since i and j each move forward at most n times.
    Space : O(n) for the input arrays, O(1) extra.
"""


# -------------------------------------- Solution -----------------------------------------------


tc = int(input())
for _ in range(tc):
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    j = 0
    ans = 0
    for i in range(n):
        if j < i:
            j = i
        while j < n and B[j] >= A[i]:
            ans = max(ans, j - i)
            j += 1
        if j > 0:
            ans = max(ans, (j - 1) - i)
    print(ans)
