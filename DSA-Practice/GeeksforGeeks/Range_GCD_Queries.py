"""
Problem   : Range GCD Queries
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/range-gcd-queries3654/1
Difficulty: Medium
Topics    : Segment Tree, Advanced Data Structure, Number Theory, Mathematics
Date      : 2026-09-28

Approach:
    Iterative (bottom-up) segment tree where each node stores the GCD of its range.
    - Build : the array is padded to a power-of-two size, leaves hold the values,
              and each internal node = gcd(left child, right child).
    - Update: overwrite the leaf, then recompute GCDs up to the root.
    - Query : walk the inclusive range [l, r] bottom-up, collecting the GCD of the
              nodes that cover the left and right boundaries separately, then
              combine them.
    GCD is associative and has identity 0, so unused padding leaves (0) don't
    affect results.

Complexity:
    Time : O(n) build; O(log n) tree steps per query/update, each with a GCD
           call (about O(log A) for values up to A)
    Space: O(n) for the tree (2 * next_power_of_two(n))
"""


# --------------------------------------- Solution ------------------------------------------------------


from math import gcd

class Solution:
    def processQueries(self, arr: list[int], queries: list[list[int]]) -> list[int]:
        # code here
        n = len(arr)
        size = 1
        while size < n:
            size <<= 1
        tree = [0] * (2 * size)
        for i in range(n):
            tree[size + i] = arr[i]
        for i in range(size - 1, 0, -1):
            tree[i] = gcd(tree[2 * i], tree[2 * i + 1])
        def update(index: int, value: int) -> None:
            pos = size + index
            tree[pos] = value
            pos //= 2
            while pos:
                tree[pos] = gcd(tree[2 * pos], tree[2 * pos + 1])
                pos //= 2
        def query(left: int, right: int) -> int:
            left += size
            right += size
            result_left = 0
            result_right = 0
            while left <= right:
                if left & 1:
                    result_left = gcd(result_left, tree[left])
                    left += 1
                if not (right & 1):
                    result_right = gcd(tree[right], result_right)
                    right -= 1
                left //= 2
                right //= 2
            return gcd(result_left, result_right)
        answers = []
        for t, x, y in queries:
            if t == 0:
                answers.append(query(x, y))
            else:
                update(x, y)
        return answers
