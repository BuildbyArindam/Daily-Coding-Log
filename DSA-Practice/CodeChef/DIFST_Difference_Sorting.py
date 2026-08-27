"""
Problem: Difference Sorting
Platform: CodeChef
Link: https://www.codechef.com/problems/DIFST
Date Solved: 2026-08-27

Approach:
Treat the array as a permutation p[1..n]. For every index i where p[i] != i,
push (|i - p[i]|, i) onto a min-heap keyed by displacement distance. Repeatedly
pop the smallest-distance pair (a, b = p[a]); if it's still valid (distance
unchanged, not already fixed), swap p[a] and p[b] and record the swap. After
each swap, re-push 'a' if it's still displaced. Greedily resolving the
smallest-displacement pairs first minimizes/orders the swap sequence needed
to sort the permutation.

Time Complexity: O(n log n)  — each element can be pushed/popped from the
                                heap a bounded number of times.
Space Complexity: O(n)       — heap and permutation arrays.
"""


# --------------------------- Solution ----------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.readline
    T = int(input())
    out = []
    for _ in range(T):
        n = int(input())
        p = [0] + list(map(int, input().split()))
        heap = []
        for i in range(1, n + 1):
            if p[i] != i:
                heap.append((abs(i - p[i]), i))
        heapq.heapify(heap)
        ans = []
        while heap:
            d, a = heapq.heappop(heap)
            b = p[a]
            if b == a or abs(a - b) != d:
                continue
            c = p[b]
            ans.append((a, b))
            p[a], p[b] = p[b], p[a]
            if p[a] != a:
                heapq.heappush(heap, (abs(a - p[a]), a))
        out.append(str(len(ans)))
        out.extend(f"{a} {b}" for a, b in ans)
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()
