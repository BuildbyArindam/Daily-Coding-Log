"""
Problem: Optimal Division
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/optimal-division-d75f0043/
Date Solved: 2026-09-18
Difficulty: Medium
Topics: Binary Search, Bitwise OR, Greedy

Approach:
    Binary search on the answer (the minimum possible "max OR of a segment").
    For a candidate limit, greedily partition the array into the fewest
    contiguous segments such that each segment's cumulative OR stays <= limit
    (can_split). Binary search over [max(arr), OR of all elements] to find
    the smallest limit for which the array can be split into <= m segments.
    Edge case: if m >= n, each element can be its own segment, so the answer
    is just max(arr).

Time Complexity:  O(n log(maxOR)) per test case
                   (each binary search step does an O(n) greedy scan)
Space Complexity:  O(n) for storing the array
"""


# -------------------------------- Solution -----------------------------------------------


import sys

def can_split(arr, m, limit):
    segments = 1
    current_or = 0
    for value in arr:
        new_or = current_or | value
        if new_or <= limit:
            current_or = new_or
        else:
            segments += 1
            current_or = value
            if segments > m:
                return False
    return True

def solve():
    input = sys.stdin.readline
    t = int(input())
    answers = []
    for _ in range(t):
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        if m >= n:
            answers.append(str(max(arr)))
            continue
        low = max(arr)
        high = 0
        for x in arr:
            high |= x
        while low < high:
            mid = (low + high) // 2
            if can_split(arr, m, mid):
                high = mid
            else:
                low = mid + 1
        answers.append(str(low))
    sys.stdout.write("\n".join(answers))

if __name__ == "__main__":
    solve()
