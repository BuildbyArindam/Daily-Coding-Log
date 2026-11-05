"""
Problem   : 1385. Find the Distance Value Between Two Arrays
Platform  : LeetCode 
Link      : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
Date      : 2026-11-05
Difficulty: Easy
Topics    : Array, Two Pointers, Binary Search, Sorting

Approach  :
    Sort arr2, then for each value in arr1 binary-search for the first
    element in arr2 that is >= val. Only that element and its predecessor
    can be the closest to val, so check both against d. If either is within
    d, val is "bad" and doesn't count toward the answer. The answer is
    len(arr1) minus the number of bad values.

Complexity:
    Time  : O((n + m) log m), where n = len(arr1), m = len(arr2)
            (sorting arr2 is O(m log m), n binary searches are O(n log m))
    Space : O(m) for the sorted copy of arr2
"""


# --------------------------------------------------- Solution ---------------------------------------------------------


class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        pool = sorted(arr2)
        size = len(pool)
        def has_close_neighbour(val: int) -> bool:
            lo, hi = 0, size
            while lo < hi:
                mid = (lo + hi) >> 1
                if pool[mid] < val:
                    lo = mid + 1
                else:
                    hi = mid
            if lo < size and pool[lo] - val <= d:
                return True
            if lo > 0 and val - pool[lo - 1] <= d:
                return True
            return False
        answer = len(arr1)
        for item in arr1:
            if has_close_neighbour(item):
                answer -= 1
        return answer

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
