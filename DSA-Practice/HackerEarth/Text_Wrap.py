"""
Problem: Text Wrap
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/minimum-width-3ae6ed73/
Date: 2026-09-18
Difficulty: Medium
Topics: Binary Search, Input/Output, Basic Programming

Approach:
Binary search on the answer (line width W). For a candidate W, greedily
pack words into lines and check whether the text fits within M lines
(can_fit helper). Search space is [max(word length), sum(lengths)+gaps].
Monotonic property: if W works, any W' > W also works, so binary search
on the smallest feasible W is valid.

Time Complexity: O(N log(sum(L))) — binary search over width range,
                  each feasibility check is O(N)
Space Complexity: O(N) — for storing the list of word lengths
"""


# ---------------------------- Solution -----------------------------------------


import sys
input = sys.stdin.readline
N, M = map(int, input().split())
L = list(map(int, input().split()))

def can_fit(W):
    """Return True if all words fit in at most M lines of width W."""
    lines = 1
    current_width = 0
    for length in L:
        if length > W:
            return False
        if current_width == 0:
            current_width = length
        elif current_width + 1 + length <= W:
            current_width += 1 + length
        else:
            lines += 1
            current_width = length
            if lines > M:
                return False
    return True

low = max(L)
high = sum(L) + (N - 1)
while low < high:
    mid = (low + high) // 2
    if can_fit(mid):
        high = mid
    else:
        low = mid + 1
print(low)
