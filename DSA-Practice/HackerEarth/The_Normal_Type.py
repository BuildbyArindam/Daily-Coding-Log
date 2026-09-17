"""
Problem   : The Normal Type
Platform  : HackerEarth
Link      : https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/the-normal-type/
Date      : 2026-09-17
Difficulty: Medium
Topics    : Two Pointers, Searching, Sets

Approach:
    Sliding window / two-pointer technique. First compute total_distinct,
    the number of distinct elements in the full array. Expand a window
    with pointer `right`, tracking per-element frequency and a running
    count of distinct elements currently in the window. Once the window
    contains all `total_distinct` elements, shrink from the left as far
    as possible while still retaining all distinct elements (i.e. while
    the leftmost element has frequency > 1, it's "redundant" and can be
    dropped). At that point, every subarray ending at `right` and
    starting anywhere in [0, left] also contains all distinct elements,
    so add (left + 1) to the answer.

Time Complexity : O(N)  — each index enters/leaves the window at most once
Space Complexity: O(N)  — frequency dict + distinct-elements set
"""


# ----------------------------------- Solution ----------------------------------------------


import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
total_distinct = len(set(A))
freq = {}
distinct = 0
left = 0
ans = 0
for right in range(N):
    x = A[right]
    freq[x] = freq.get(x, 0) + 1
    if freq[x] == 1:
        distinct += 1
    if distinct == total_distinct:
        while freq[A[left]] > 1:
            freq[A[left]] -= 1
            left += 1
        ans += left + 1
print(ans)
