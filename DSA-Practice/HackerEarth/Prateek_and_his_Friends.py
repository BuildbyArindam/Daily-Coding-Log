"""
Problem: Prateek and his Friends
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/prateek-and-his-friends/
Difficulty: Easy
Topic: Ad-Hoc, Open
Date Solved: 2026-09-04

Approach:
    Sliding window / two pointers over the cost array. Expand the window by
    adding costs[right] each step; while the running sum exceeds X, shrink
    from the left. If current_sum ever equals X exactly, a contiguous set
    of friends' gifts sums to X, so answer is YES.
    (Relies on all costs being non-negative, which lets the window sum
    move monotonically — that's what makes shrink-on-overflow valid.)

Time Complexity: O(N) per test case — each index enters/leaves the window once
Space Complexity: O(N) for the costs list, O(1) auxiliary
"""


# ------------------------------ Soolution ------------------------------


T = int(input())
for _ in range(T):
    N, X = map(int, input().split())
    costs = [int(input()) for _ in range(N)]
    left = 0
    current_sum = 0
    found = False
    for right in range(N):
        current_sum += costs[right]
        while current_sum > X and left <= right:
            current_sum -= costs[left]
            left += 1
        if current_sum == X:
            found = True
            break
    print("YES" if found else "NO")
