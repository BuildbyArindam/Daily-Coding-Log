"""
Problem   : Shubham and Xor
Platform  : HackerEarth 
Link      : https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/shubham-and-xor-8526868e/
Date      : 2026-10-16
Difficulty: Easy
Topics    : Algorithms, Bubble Sort, Searching, Sorting

Approach  : a ^ b == 0 only when a == b, so the task reduces to counting
            pairs of equal elements. Sort the array so equal values sit
            next to each other, then for each run of length r add
            r * (r - 1) / 2 pairs.

Complexity: Time  O(n log n), dominated by the sort
            Space O(1) extra beyond the input (in-place sort)
"""


# ---------------------------------------------------- Solution ------------------------------------------------


import sys

def tally(values):
    values.sort()
    total = 0
    run = 1
    for k in range(1, len(values)):
        if values[k] == values[k - 1]:
            run += 1
        else:
            total += run * (run - 1) // 2
            run = 1
    total += run * (run - 1) // 2
    return total

def main():
    tokens = sys.stdin.read().split()
    size = int(tokens[0])
    nums = list(map(int, tokens[1:size + 1]))
    print(tally(nums))

main()
