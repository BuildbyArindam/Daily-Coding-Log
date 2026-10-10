"""
Problem   : Painting The Logo
Platform  : HackerEarth (Algorithms > Searching > Binary Search)
Link      : https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/painting-the-logo/
Difficulty: Medium
Date      : 2026-10-10
Topics    : Binary Search, Sorting

Approach  : Paint needed for a logo of size a is 2*a*(a+1), which grows
            monotonically with a. Sizes are odd (a = 2*mid + 1), so I binary
            search on mid for the largest a with paint <= x, then print
            "a a-1". Small x (< 12 and < 24) are handled as special cases.

Time      : O(T * log(10^8)) overall, about 27 iterations per test case
Space     : O(T) for the input read; O(1) extra per test case
"""


# --------------------------------------- Solution -----------------------------------------------------


import sys

def solve(x):
    if x < 12:
        return "0 0"
    if x < 24:
        return "1 2"
    low, high = 1, 100_000_000
    best = 1
    while low <= high:
        mid = (low + high) // 2
        a = 2 * mid + 1
        paint = 2 * a * (a + 1)
        if paint <= x:
            best = a
            low = mid + 1
        else:
            high = mid - 1
    return f"{best} {best - 1}"

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    for x in data[1:t + 1]:
        print(solve(x))

if __name__ == "__main__":
    main()
