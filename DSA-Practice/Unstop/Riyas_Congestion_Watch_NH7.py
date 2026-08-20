"""
Problem   : Riya's Congestion Watch on NH-7
Platform  : Unstop
Link      : https://unstop.com/code/practice/656581
Difficulty: Hard
Date      : 2026-08-20

Approach:
    Segment tree over the traffic-density array supporting three ops:
      1) Range Add       -> add v to every index in [l, r]
      2) Range Max        -> max value in [l, r]
      3) Leftmost > x     -> smallest index in [l, r] whose value exceeds x
    Range updates use lazy propagation (additive lazy tag pushed down
    on descent). The "leftmost greater than x" query prunes any subtree
    whose max <= x, then descends left-first so the first leaf reached
    that intersects [l, r] and exceeds x is guaranteed to be the
    leftmost valid index.

Time Complexity : O((n + q) log n)
                    - build: O(n)
                    - range_add / range_max: O(log n) each
                    - first_greater: O(log n) amortized (each call visits
                      O(log n) nodes since pruned subtrees are cut early)
Space Complexity : O(n) for arr, O(4n) for mx[] and lazy[] segment tree arrays
"""


# ------------------------------- Solution -----------------------------------


import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.buffer.readline
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        size = 4 * self.n
        self.mx = [0] * size
        self.lazy = [0] * size
        self.build(1, 0, self.n - 1, arr)
    def build(self, node, left, right, arr):
        if left == right:
            self.mx[node] = arr[left]
            return
        mid = (left + right) // 2
        self.build(node * 2, left, mid, arr)
        self.build(node * 2 + 1, mid + 1, right, arr)
        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
    def apply(self, node, value):
        self.mx[node] += value
        self.lazy[node] += value
    def push(self, node):
        if self.lazy[node] != 0:
            value = self.lazy[node]
            self.apply(node * 2, value)
            self.apply(node * 2 + 1, value)
            self.lazy[node] = 0
    def range_add(self, ql, qr, value):
        self._range_add(1, 0, self.n - 1, ql, qr, value)
    def _range_add(self, node, left, right, ql, qr, value):
        if ql <= left and right <= qr:
            self.apply(node, value)
            return
        self.push(node)
        mid = (left + right) // 2
        if ql <= mid:
            self._range_add(node * 2, left, mid, ql, qr, value)
        if qr > mid:
            self._range_add(node * 2 + 1, mid + 1, right, ql, qr, value)
        self.mx[node] = max(self.mx[node * 2], self.mx[node * 2 + 1])
    def range_max(self, ql, qr):
        return self._range_max(1, 0, self.n - 1, ql, qr)

    def _range_max(self, node, left, right, ql, qr):
        if ql <= left and right <= qr:
            return self.mx[node]
        self.push(node)
        mid = (left + right) // 2
        result = -10**30
        if ql <= mid:
            result = max(
                result,
                self._range_max(node * 2, left, mid, ql, qr)
            )
        if qr > mid:
            result = max(
                result,
                self._range_max(node * 2 + 1, mid + 1, right, ql, qr)
            )
        return result

    def first_greater(self, ql, qr, x):
        return self._first_greater(1, 0, self.n - 1, ql, qr, x)

    def _first_greater(self, node, left, right, ql, qr, x):
        if right < ql or left > qr:
            return -1
        if self.mx[node] <= x:
            return -1
        if left == right:
            return left
        self.push(node)
        mid = (left + right) // 2
        result = self._first_greater(node * 2, left, mid, ql, qr, x)
        if result != -1:
            return result
        return self._first_greater(node * 2 + 1, mid + 1, right, ql, qr, x)

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    it = iter(data)
    n = next(it)
    arr = [next(it) for _ in range(n)]
    q = next(it)
    seg = SegmentTree(arr)
    out = []
    for _ in range(q):
        t = next(it)
        if t == 1:
            l = next(it) - 1
            r = next(it) - 1
            v = next(it)
            seg.range_add(l, r, v)
        elif t == 2:
            l = next(it) - 1
            r = next(it) - 1
            out.append(str(seg.range_max(l, r)))
        else:  
            l = next(it) - 1
            r = next(it) - 1
            x = next(it)
            ans = seg.first_greater(l, r, x)
            out.append(str(ans + 1 if ans != -1 else -1))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
