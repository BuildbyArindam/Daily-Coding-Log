"""
Problem   : Identical BSTs
Platform  : Coding360 (Naukri Code360)
Link      : https://www.naukri.com/code360/problems/identical-bsts_920527
Difficulty: Easy
Date      : 2026-08-27

Approach:
    Two insertion sequences produce identical BSTs iff every value ends up
    with the same parent in both trees. Instead of building the trees
    explicitly, simulate insertion order and use a Fenwick tree (BIT) over
    the *rank* of each value to find, at each step, the predecessor
    (largest already-inserted value smaller than x) and successor
    (smallest already-inserted value larger than x) via k-th order
    statistics. Whichever of predecessor/successor was inserted more
    recently becomes the parent of x (standard BST-insertion property).
    Compare the resulting parent maps for arr1 and arr2.

Time complexity : O(n log n)   -- n Fenwick updates + kth-element queries
Space complexity: O(n)         -- Fenwick array, rank map, parent map
"""


# -------------------------- Solution ----------------------------


from os import *
from sys import *
from collections import *
from math import *
from bisect import *

def isIdenticalBST(arr1, arr2, n):
    if len(set(arr1)) != n or len(set(arr2)) != n:
        return False
    if set(arr1) != set(arr2):
        return False
    values = sorted(arr1)
    rank = {value: i + 1 for i, value in enumerate(values)}
    class Fenwick:
        def __init__(self, size):
            self.size = size
            self.bit = [0] * (size + 1)
        def update(self, idx, delta):
            while idx <= self.size:
                self.bit[idx] += delta
                idx += idx & -idx
        def query(self, idx):
            total = 0
            while idx > 0:
                total += self.bit[idx]
                idx -= idx & -idx
            return total
        def kth(self, k):
            idx = 0
            step = 1 << (self.size.bit_length() - 1)
            while step:
                nxt = idx + step
                if nxt <= self.size and self.bit[nxt] < k:
                    idx = nxt
                    k -= self.bit[nxt]
                step >>= 1
            return idx + 1

    def get_parent_map(arr):
        """
        For every node, find its parent in the BST formed by insertion.

        For a newly inserted value x:
        - predecessor = largest inserted value < x
        - successor   = smallest inserted value > x
        The parent is the one of these two that was inserted later.
        """
        bit = Fenwick(n)
        latest = [0] * (n + 1)
        parent = {}
        for i, x in enumerate(arr):
            r = rank[x]
            if i == 0:
                parent[x] = None
                bit.update(r, 1)
                latest[r] = i
                continue
            inserted_before = bit.query(n)
            left_count = bit.query(r - 1)
            predecessor = None
            successor = None
            if left_count > 0:
                pred_rank = bit.kth(left_count)
                predecessor = values[pred_rank - 1]
            if inserted_before - left_count > 0:
                succ_rank = bit.kth(left_count + 1)
                successor = values[succ_rank - 1]
            if predecessor is None:
                parent[x] = successor
            elif successor is None:
                parent[x] = predecessor
            elif latest[rank[predecessor]] > latest[rank[successor]]:
                parent[x] = predecessor
            else:
                parent[x] = successor
            bit.update(r, 1)
            latest[r] = i
        return parent
    return get_parent_map(arr1) == get_parent_map(arr2)
