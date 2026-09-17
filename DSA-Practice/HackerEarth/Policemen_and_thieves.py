"""
Problem: Policemen and Thieves (Joker and Thieves)
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/joker-and-thieves-53e59f4a/
Platform: HackerEarth
Date: 2026-09-17
Difficulty: Medium
Topics: Two Pointer, Searching

Approach:
    For each row of the grid, separate positions of 'P' (policemen) and
    'T' (thieves) into two lists. Use a two-pointer sweep across both
    sorted-by-construction lists: if a policeman and thief are within K
    columns of each other, count a catch and advance both pointers;
    otherwise advance whichever pointer points to the smaller column
    index. Sum catches across all rows.

Time Complexity:  O(N^2) per test case (N rows x N columns scanned once,
                   plus O(N) two-pointer sweep per row)
Space Complexity: O(N) per row for the policemen/thieves index lists
"""


# -------------------------------- Solution ----------------------------------------


def solution(A, K):
    total = 0
    N = len(A)
    for row in range(N):
        policemen = []
        thieves = []
        for col in range(N):
            if A[row][col] == 'P':
                policemen.append(col)
            elif A[row][col] == 'T':
                thieves.append(col)
        i = 0
        j = 0
        while i < len(policemen) and j < len(thieves):
            if abs(policemen[i] - thieves[j]) <= K:
                total += 1
                i += 1
                j += 1
            elif policemen[i] < thieves[j]:
                i += 1
            else:
                j += 1
    return total

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().split())
    out_ = solution(A, K)
    print(out_)
