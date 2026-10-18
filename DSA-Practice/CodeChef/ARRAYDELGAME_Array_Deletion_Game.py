"""
Problem   : Array Deletion Game (ARRAYDELGAME)
Platform  : CodeChef
Link      : https://www.codechef.com/problems/ARRAYDELGAME
Difficulty: 2006
Date      : 2026-10-18
Topics    : Greedy, Heap / Priority Queue

Approach:
    Scan the array left to right, pushing each element into a min-heap.
    After processing the i-th element, the heap is capped at ceil(i/2)
    elements (i.e. (i + 1) // 2). If it grows past the cap, pop the
    smallest element. The answer is the sum of the heap at the end.

Complexity:
    Time : O(N log N) per test case (one push and at most one pop per element)
    Space: O(N) for the heap (at most ceil(N/2) elements)
"""


# ---------------------------------------------- Solution ---------------------------------------------------


import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    heap = []
    for i, x in enumerate(A, start=1):
        heapq.heappush(heap, x)
        limit = (i + 1) // 2
        if len(heap) > limit:
            heapq.heappop(heap)
    print(sum(heap))
