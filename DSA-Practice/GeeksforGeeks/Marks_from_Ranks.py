"""
Problem: Marks from Ranks
Platform: GeeksForGeeks
Link: https://www.geeksforgeeks.org/problems/find-marks-from-ranks/1
Date Solved: 2026-08-30
Difficulty: Medium
Topics: Arrays, Searching (Binary Search on Prefix Sums)

Approach:
Build a prefix-sum array of cumulative rank-range sizes (r[i]-l[i]+1),
so prefix[i] = total ranks covered up to and including block i.
For each query rank k, binary search the prefix array for the first
block whose cumulative count is >= k (the block containing that rank).
Compute the offset within that block (k - ranks covered before it)
and map it back to the corresponding mark via l[i] + offset - 1.

Time Complexity: O((n + q) log n) — n = number of blocks, q = number of queries
Space Complexity: O(n) — for the prefix sum array
"""


# ------------------------ Solution -----------------------------


class Solution:
    def getMarks(self, l, r, rank):
        """code here"""
        prefix = []
        total = 0
        for i in range(len(l)):
            total += r[i] - l[i] + 1
            prefix.append(total)
        ans = []
        for k in rank:
            lo, hi = 0, len(prefix) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] >= k:
                    hi = mid
                else:
                    lo = mid + 1
            i = lo
            before = prefix[i - 1] if i > 0 else 0
            offset = k - before
            ans.append(l[i] + offset - 1)
        return ans
