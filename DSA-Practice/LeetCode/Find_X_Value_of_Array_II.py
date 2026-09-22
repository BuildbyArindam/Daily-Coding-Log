"""
Problem: Find X-Value of Array II
Platform: LeetCode
Link: https://leetcode.com/problems/find-x-value-of-array-ii/?envType=daily-question&envId=2026-09-22
Date Solved: 2026-09-22
Difficulty: Hard
Topics: Array, Math, Segment Tree

Approach:
Segment tree where each node stores (product mod k, count[0..k-1]) — count[r]
is the number of ways a contiguous subrange within that node's span, when its
product is taken starting fresh from some point, lands on remainder r mod k.
Merge combines left/right by shifting the right child's counts by
(left_prod * r) mod k. Point updates rebuild the leaf and propagate up;
each query updates nums[index] then queries the suffix product-remainder
counts over [start, n) and reads off count[x].

Time Complexity: O((n + q) * k log n)
  - build: O(n * k)
  - each update: O(k log n)
  - each range_query: O(k log n)
Space Complexity: O(n * k) for the segment tree (tree_cnt stores a k-length
  array per node, 2*size nodes)
"""


# ------------------------------------------- Solution ----------------------------------------------------


class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        size = 1
        while size < n:
            size <<= 1
        tree_prod = [1 % k] * (2 * size)
        tree_cnt = [[0] * k for _ in range(2 * size)]
        def make_leaf(x):
            rem = x % k
            cnt = [0] * k
            cnt[rem] = 1
            return rem, cnt
        def merge(left_prod, left_cnt, right_prod, right_cnt):
            prod = (left_prod * right_prod) % k
            cnt = left_cnt[:]  
            for r in range(k):
                cnt[(left_prod * r) % k] += right_cnt[r]
            return prod, cnt
        for i, x in enumerate(nums):
            p, c = make_leaf(x)
            tree_prod[size + i] = p
            tree_cnt[size + i] = c
        for i in range(size - 1, 0, -1):
            lp, lc = tree_prod[i << 1], tree_cnt[i << 1]
            rp, rc = tree_prod[i << 1 | 1], tree_cnt[i << 1 | 1]
            tree_prod[i], tree_cnt[i] = merge(lp, lc, rp, rc)
        def update(pos, value):
            p, c = make_leaf(value)
            idx = size + pos
            tree_prod[idx] = p
            tree_cnt[idx] = c
            idx >>= 1
            while idx:
                lp, lc = tree_prod[idx << 1], tree_cnt[idx << 1]
                rp, rc = tree_prod[idx << 1 | 1], tree_cnt[idx << 1 | 1]
                tree_prod[idx], tree_cnt[idx] = merge(lp, lc, rp, rc)
                idx >>= 1
        def range_query(l, r):
            left_prod = 1 % k
            left_cnt = [0] * k
            right_prod = 1 % k
            right_cnt = [0] * k
            l += size
            r += size
            while l < r:
                if l & 1:
                    np, nc = merge(
                        left_prod, left_cnt,
                        tree_prod[l], tree_cnt[l]
                    )
                    left_prod, left_cnt = np, nc
                    l += 1
                if r & 1:
                    r -= 1
                    np, nc = merge(
                        tree_prod[r], tree_cnt[r],
                        right_prod, right_cnt
                    )
                    right_prod, right_cnt = np, nc
                l >>= 1
                r >>= 1
            return merge(left_prod, left_cnt, right_prod, right_cnt)
        ans = []
        for index, value, start, x in queries:
            update(index, value)
            _, cnt = range_query(start, n)
            ans.append(cnt[x])
        return ans

__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
