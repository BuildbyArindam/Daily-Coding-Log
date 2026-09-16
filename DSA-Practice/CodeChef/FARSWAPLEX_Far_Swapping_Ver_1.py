"""
Problem: Far Swapping (Ver 1)
Platform: CodeChef
Link: https://www.codechef.com/START256D/problems/FARSWAPLEX
Date Solved: 2026-09-16
Difficulty: Medium
Topics: Graph Theory, Topological Sort, Greedy, Priority Queue / Heap

Approach:
For each pair of consecutive values (v, v+1), add a directed edge based on
which one appears earlier (smaller index) in the given array — the earlier
one must come before the later one in the output. This turns the problem
into finding the lexicographically smallest valid topological order of the
resulting DAG on values 1..n. Use Kahn's algorithm with a min-heap (instead
of a FIFO queue) as the ready set, always popping the smallest available
value, to guarantee lexicographic minimality.

Time Complexity: O(n log n) per test case (each of the n-1 edges/nodes is
                  pushed/popped from the heap at most once, each heap op
                  costs O(log n))
Space Complexity: O(n) for adjacency list, indegree array, and heap
"""


# ----------------------------- Solution ----------------------------------------


import sys
import heapq

def solve_case(n, arr):
    where = [0] * (n + 1)
    for idx, val in enumerate(arr):
        where[val] = idx
    children = [[] for _ in range(n + 1)]
    incoming = [0] * (n + 1)
    for val in range(1, n):
        nxt = val + 1
        if where[val] < where[nxt]:
            first, second = val, nxt
        else:
            first, second = nxt, val
        children[first].append(second)
        incoming[second] += 1
    ready = [v for v in range(1, n + 1) if incoming[v] == 0]
    heapq.heapify(ready)
    answer = []
    while ready:
        cur = heapq.heappop(ready)
        answer.append(cur)
        for nb in children[cur]:
            incoming[nb] -= 1
            if incoming[nb] == 0:
                heapq.heappush(ready, nb)
    return answer

def main():
    raw = sys.stdin.buffer.read().split()
    pos = 0
    total = int(raw[pos]); pos += 1
    output_chunks = []
    for _ in range(total):
        n = int(raw[pos]); pos += 1
        values = list(map(int, raw[pos:pos + n]))
        pos += n
        result = solve_case(n, values)
        output_chunks.append(' '.join(map(str, result)))
    sys.stdout.write('\n'.join(output_chunks) + '\n')

if __name__ == "__main__":
    main()
