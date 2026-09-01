"""
Problem: Count Small
Platform: Code360
Link: https://www.naukri.com/code360/problems/count-small_6614977?kunjiRedirection=true
Date Solved: 2026-09-01
Difficulty: Medium
Topics: Binary Search, Sorting, Arrays

Approach:
For each element x in array A, count how many elements in array B
are <= x. B is assumed sorted (or sorted here) so bisect_right(B, x)
gives that count directly in O(log m) per query instead of an O(m)
scan.

Time Complexity: O(n log m) — n queries from A, each a binary search
                  over B (sorted once, O(m log m) if not pre-sorted)
Space Complexity: O(1) extra (O(n) for the output list)
"""


# ------------------------ Solution -------------------------------


from bisect import bisect_right

def countS(n: int, m: int, a: [int], b: [int]) -> [int]:
    return [bisect_right(b, x) for x in a]
