"""
Problem   : Queries and Attributes
Platform  : HackerEarth (CodeMonk)
Link      : https://www.hackerearth.com/practice/codemonk/7/1504746/
Difficulty: Easy
Topics    : Heap / Priority Queue, Greedy, Dynamic Programming (DP on intervals), Sweep Line / Offline Processing
Date      : 2026-09-11

Approach:
    - Each item i defines an interval [l[i], r[i]] and a cost a[i].
    - Process positions from right (n-1) to left. For every item whose
      right endpoint equals the current position, push (cost + b[dest],
      l[i]) onto a min-heap keyed by total cost.
    - Lazily discard heap entries whose interval start is beyond the
      current position (heap[0][1] > i) since they're not reachable yet.
    - b[i] = cheapest cost to reach the end from position i, computed
      bottom-up via the heap; then take a prefix min so b[] becomes
      monotonic and supports O(1) lookups for arbitrary query positions.
    - Each query (x, y) answers as b[x-1] + y.

Time complexity : O(n log n + q)   (n heap pushes/pops, q O(1) queries)
Space complexity: O(n)             (b, l, r, by_r, heap)
"""


# --------------------------- Solution -------------------------------


import sys
import heapq

def solve():
    input = sys.stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * n
    r = [0] * n
    by_r = [[] for _ in range(n)]
    for i in range(n):
        li, ri = map(int, input().split())
        li -= 1
        ri -= 1
        l[i] = li
        r[i] = ri
        by_r[ri].append(i)
    INF = 10**30
    b = [INF] * n
    heap = []
    for i in range(n - 1, -1, -1):
        if i == n - 1:
            b[i] = 0
        else:
            for j in by_r[i]:
                heapq.heappush(heap, (a[j] + b[j], l[j]))
            while heap and heap[0][1] > i:
                heapq.heappop(heap)
            b[i] = heap[0][0] if heap else INF
    for i in range(1, n):
        b[i] = min(b[i], b[i - 1])
    q = int(input())
    ans = []
    for _ in range(q):
        x, y = map(int, input().split())
        ans.append(str(b[x - 1] + y))
    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    solve()
