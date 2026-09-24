"""
Problem   : Maximum Height Disc Stack
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/stacking-up-discs1315/1
Difficulty: Hard
Topics    : Dynamic Programming, Sorting, Fenwick Tree (BIT)
Date      : 2026-09-24

Approach:
    Weighted LIS variant: a disc can sit on another only if both its radius
    and height are strictly greater than the one below it.
    1. Sort discs by radius.
    2. Process discs in groups of equal radius, so discs of the same radius
       never stack on each other.
    3. For each disc, query a max-Fenwick tree (indexed by height) for the
       best stack ending at a height < current height. The disc's stack
       height is that value plus its own height.
    4. After the whole radius group is processed, update the tree with the
       group's results. Deferring updates prevents same-radius stacking.
    5. The answer is the maximum stack height seen.

Complexity:
    Time : O(n log n) for the sort plus O(n log H) for BIT operations
           (H = max disc height, 1000 here)
    Space: O(n + H)
"""


# ---------------------------------------- Solution -----------------------------------------------


class Solution:
    def maxStackHeight(self, r, h):
        # code here
        discs = list(zip(r, h))
        discs.sort()
        size = 1000
        bit = [0] * (size + 1)
        def query(x):
            ans = 0
            while x > 0:
                ans = max(ans, bit[x])
                x -= x & -x
            return ans
        def update(x, value):
            while x <= size:
                bit[x] = max(bit[x], value)
                x += x & -x
        answer = 0
        i = 0
        n = len(discs)
        while i < n:
            j = i
            current = []
            while j < n and discs[j][0] == discs[i][0]:
                radius, height = discs[j]
                best_below = query(height - 1)
                current.append((height, best_below + height))
                answer = max(answer, best_below + height)
                j += 1
            for height, stack_height in current:
                update(height, stack_height)
            i = j
        return answer
