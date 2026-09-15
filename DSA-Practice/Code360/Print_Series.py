"""
Problem   : Print Series
Platform  : Code360 (Naukri)
Link      : https://www.naukri.com/code360/guided-paths/data-structures-algorithms/content/118522/offering/1380916
Difficulty: Easy
Date      : 2026-09-15
Topics    : Recursion, Backtracking Basics, Time-Space Complexity

Approach:
Recurse downward from n to n-k, n-2k, ... until the value drops to <= 0,
adding each value to the list BEFORE the recursive call (pre-order).
After the base case is hit, each frame appends 'n' again AFTER the
recursive call returns (post-order), so the same descending values are
mirrored back on the way up the call stack.
Net effect: [n, n-k, n-2k, ..., <=0, ..., n-2k, n-k, n]

Time Complexity : O(n/k)  — one recursive call per step of size k
Space Complexity: O(n/k)  — recursion call stack + output list
"""


# --------------------------- Solution -----------------------------------


def printSeries(n, k):
    ans = [n]
    if n <= 0:
        return ans
    ans += printSeries(n - k, k)
    ans.append(n)
    return ans
