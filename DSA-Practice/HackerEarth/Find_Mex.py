# Problem: Find Mex
# Platform: HackerEarth (Easy)
# Link: https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/find-mex-62916c25/
# Date: 2026-08-31
# Topic: Algorithms, Brute Force, Implementation, Linear Search, Iterators
#
# Approach:
#   Maintain a running set of seen elements and a running MEX pointer as we
#   iterate through the array. After inserting each new element, advance the
#   MEX pointer while it's present in the seen set. Since MEX is
#   non-decreasing as elements are added, each pointer advance is amortized
#   O(1) across the whole array (it only ever moves forward).
#
# Time Complexity:  O(n) amortized — each element inserted once, MEX pointer
#                    advances at most n times total across the loop.
# Space Complexity: O(n) — for the `seen` set and result list.


# --------------------------- Solution -----------------------------------


import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    n = int(data[0])
    arr = [int(x) for x in data[1:n+1]]
    seen = set()
    mex = 0
    result = []
    for num in arr:
        seen.add(num)
        while mex in seen:
            mex += 1
        result.append(mex)
    print(*(result))

if __name__ == '__main__':
    solve()
