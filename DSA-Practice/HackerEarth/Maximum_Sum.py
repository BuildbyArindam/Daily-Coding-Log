"""
Problem: Maximum Sum
Platform: HackerEarth
Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/
Date Solved: 2026-09-17
Difficulty: Easy
Topics: Algorithms, Searching

Approach:
Single pass over the array. Sum and count all positive elements.
Separately count zeros. If there's at least one positive number,
the answer is (sum of positives, count of positives + zeros) —
since including zeros doesn't change the sum but they're valid
"non-negative" picks. If there are no positives but there are
zeros, answer is (0, count of zeros). If the array is all
negative, fall back to the single largest (least negative)
element as the answer, since you must pick at least one number.

Time Complexity: O(n) — one linear scan
Space Complexity: O(1) extra (excluding input storage)
"""


# ----------------------------- Solution -------------------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    a = [int(x) for x in data[1:]]
    positive_sum = 0
    positive_count = 0
    zero_count = 0
    max_element = a[0]
    for x in a:
        if x > 0:
            positive_sum += x
            positive_count += 1
        elif x == 0:
            zero_count += 1
        if x > max_element:
            max_element = x
    if positive_count > 0:
        total_sum = positive_sum
        total_count = positive_count + zero_count
        print(f"{total_sum} {total_count}")
    elif zero_count > 0:
        print(f"0 {zero_count}")
    else:
        print(f"{max_element} 1")

if __name__ == '__main__':
    solve()
