"""
Problem   : Two Pairs with Same Sum
Platform  : GeeksforGeeks 
Link      : https://www.geeksforgeeks.org/problems/satisfy-the-equation5847/1
Date      : 2026-11-24
Difficulty: Medium
Topics    : Hash, Sorting, Map

Approach  : Enumerate every pair (i, j) with i < j and bucket the index
            pairs by their sum in a hash map. Pairs are inserted in
            lexicographic order, so within each bucket the first two
            index-disjoint pairs found give the smallest answer for that
            sum. Take the lexicographic minimum across all buckets, or
            return [-1, -1, -1, -1] if no bucket has two disjoint pairs.

Time      : O(n^2) to build the buckets. The disjoint-pair scan inside a
            bucket exits early, so it stays near O(n^2) overall.
Space     : O(n^2) for the map holding all pair indices.
"""


# ---------------------------------------------------- Solution -----------------------------------------------------------


from collections import defaultdict

class Solution:
    def findPairs(self, arr: list[int]) -> list[int]:
        # code here
        n = len(arr)
        buckets = defaultdict(list)
        for i in range(n - 1):
            base = arr[i]
            for j in range(i + 1, n):
                buckets[base + arr[j]].append((i, j))
        best = None
        for group in buckets.values():
            m = len(group)
            if m < 2:
                continue
            found = None
            for p in range(m - 1):
                x, y = group[p]
                for q in range(p + 1, m):
                    u, v = group[q]
                    if x != u and x != v and y != u and y != v:
                        found = (x, y, u, v)
                        break
                if found:
                    break
            if found and (best is None or found < best):
                best = found
        return list(best) if best else [-1, -1, -1, -1]
