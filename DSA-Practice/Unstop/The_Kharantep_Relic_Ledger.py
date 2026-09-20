"""
Problem   : The Kharantep Relic Ledger
Platform  : Unstop
Link      : https://unstop.com/code/practice/660868
Date      : 2026-09-20
Difficulty: Hard
Topics    : DSU (Union-Find), Small-to-Large Merging, Leftist Heap (Priority Queue), Graph

Approach:
    Maintain a DSU over nodes where each component tracks its own
    "leftist max-heap" root (heap keyed on relic value, ties broken by
    smaller index). On LINK(u, v), union the two components by size
    (small-to-large) and meld their leftist heaps into one. On the
    query operation, find the component root, peek/pop the max element
    from its heap, and report (index, value) or EMPTY if the heap is empty.

Complexity:
    Time  : O((n + m) log n) — DSU union/find with path halving is
            near O(1) amortized; each meld/pop on a leftist heap is
            O(log n), and small-to-large unioning keeps total heap
            work bounded across all merges.
    Space : O(n) — for DSU arrays, heap left/right/dist/value arrays.
"""


# ------------------------------------- Solution -------------------------------------------------


import sys
input = sys.stdin.readline

class LeftistHeap:
    def __init__(self, n, values):
        self.left = [0] * (n + 1)
        self.right = [0] * (n + 1)
        self.dist = [0] * (n + 1)
        self.value = [0] * (n + 1)
        self.index = list(range(n + 1))
        for i in range(1, n + 1):
            self.value[i] = values[i]
    def better(self, a, b):
        """Return True if heap node a should be above b."""
        if self.value[a] != self.value[b]:
            return self.value[a] > self.value[b]
        return a < b
    def meld(self, a, b):
        """Meld two leftist max-heaps."""
        if a == 0:
            return b
        if b == 0:
            return a
        if not self.better(a, b):
            a, b = b, a
        self.right[a] = self.meld(self.right[a], b)
        if self.dist[self.left[a]] < self.dist[self.right[a]]:
            self.left[a], self.right[a] = self.right[a], self.left[a]
        self.dist[a] = self.dist[self.right[a]] + 1
        return a
    def pop(self, root):
        """Remove and return the maximum node."""
        new_root = self.meld(self.left[root], self.right[root])
        self.left[root] = 0
        self.right[root] = 0
        self.dist[root] = 1
        return new_root

def solve():
    n, m = map(int, input().split())
    values = [0] + list(map(int, input().split()))
    parent = list(range(n + 1))
    size = [1] * (n + 1)
    heap = LeftistHeap(n, values)
    heap_root = [0] * (n + 1)
    for i in range(1, n + 1):
        if values[i] != 0:
            heap_root[i] = i
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    output = []
    for _ in range(m):
        parts = input().split()
        if parts[0] == "LINK":
            u = int(parts[1])
            v = int(parts[2])
            ru = find(u)
            rv = find(v)
            if ru == rv:
                continue
            if size[ru] < size[rv]:
                ru, rv = rv, ru
            parent[rv] = ru
            size[ru] += size[rv]
            heap_root[ru] = heap.meld(heap_root[ru], heap_root[rv])
            heap_root[rv] = 0
        else: 
            x = int(parts[1])
            r = find(x)
            h = heap_root[r]
            if h == 0:
                output.append("EMPTY")
            else:
                output.append(f"{h} {values[h]}")
                heap_root[r] = heap.pop(h)
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    solve()
