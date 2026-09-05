"""
Problem: New game of Oz
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/new-game-of-oz/
Difficulty: Easy
Topics: Ad-Hoc, Approved, Open, Sorting
Date: 2026-09-05

Approach:
    Sort the array, then scan for maximal runs of consecutive integers
    (arr[i] == arr[i-1] + 1). Within a run of length L, elements can be
    paired off from the front two at a time (greedy), leaving ceil(L/2)
    unpaired/group segments -> contributes (L + 1) // 2 to the answer.
    Sum this over all runs.

Time Complexity:  O(N log N) per test case (dominated by the sort)
Space Complexity: O(N) for the input array
"""


# ---------------------------- Solution ----------------------------


name = input() 
T = int(name)
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    answer = 0
    length = 1
    for i in range(1, N):
        if arr[i] == arr[i - 1] + 1:
            length += 1
        else:
            answer += (length + 1) // 2
            length = 1
    answer += (length + 1) // 2
    print(answer)
