"""
Problem: Mark The Answer
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/mark-the-answer-1/
Difficulty: Easy
Topics: Data Structures, Arrays, One-dimensional
Date Solved: 2026-08-30

Approach:
Iterate through the array once. Count elements strictly less than X as
correct ("scored") answers. On hitting the first element >= X, treat it
as a skip and continue scanning; on hitting a second such element, stop
immediately (only one skip is allowed before the process ends).

Time Complexity: O(N) — single pass over the array
Space Complexity: O(N) — for storing the input array (O(1) extra)
"""


# -------------------------- Solution --------------------------------


import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    X = int(input_data[1])
    A = [int(x) for x in input_data[2:2+N]]
    score = 0
    skipped = False
    for diff in A:
        if diff < X:
            score += 1
        else:
            if not skipped:
                skipped = True
            else:
                break
    print(score)

if __name__ == '__main__':
    solve()
