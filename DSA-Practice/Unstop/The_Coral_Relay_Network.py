"""
Problem: The Coral Relay Network
Platform: Unstop
Link: https://unstop.com/code/practice/659694
Date Solved: 2026-09-14
Difficulty: Hard
Topics: Tree, Centroid Decomposition, Sorting, Two Pointers, Distance Calculation, Divide and Conquer

Approach:
Centroid Decomposition on the tree. For each centroid, gather distances from
the centroid to every node in its current component (via DFS/collect_distances),
then count pairs (u, v) whose path distance <= D using a sort + two-pointer scan
(count_pairs) — plus a binary-search-based incremental variant while merging
subtree distance lists to avoid double counting pairs within the same subtree.
Recurse into each remaining subtree after removing the centroid, so the tree
is repeatedly split into balanced halves (O(log n) levels).

Time Complexity: O(n log^2 n)
    - O(log n) centroid decomposition levels
    - O(n log n) work per level (sorting/binary search over distances)
Space Complexity: O(n)
    - graph adjacency list, recursion stack, and per-level distance arrays
"""


# ---------------------------------- Solution --------------------------------------


import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

def solve():
    n, D = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append((v, w))
        graph[v].append((u, w))
    removed = [False] * n
    subtree = [0] * n
    def find_centroid(start):
        parent = [-1] * n
        order = [start]
        parent[start] = -2
        for u in order:
            for v, _ in graph[u]:
                if removed[v] or v == parent[u]:
                    continue
                parent[v] = u
                order.append(v)
        for u in reversed(order):
            subtree[u] = 1
            for v, _ in graph[u]:
                if removed[v] or parent[v] != u:
                    continue
                subtree[u] += subtree[v]
        total = len(order)
        centroid = start
        while True:
            nxt = -1
            for v, _ in graph[centroid]:
                if removed[v]:
                    continue
                if parent[v] == centroid:
                    part = subtree[v]
                elif parent[centroid] == v:
                    part = total - subtree[centroid]
                else:
                    continue
                if part > total // 2:
                    nxt = v
                    break
            if nxt == -1:
                return centroid
            centroid = nxt
    def collect_distances(start, parent, initial_dist):
        result = []
        stack = [(start, parent, initial_dist)]
        while stack:
            u, p, dist = stack.pop()
            result.append(dist)
            for v, w in graph[u]:
                if removed[v] or v == p:
                    continue
                stack.append((v, u, dist + w))
        return result
    def count_pairs(arr):
        arr.sort()
        left = 0
        right = len(arr) - 1
        count = 0
        while left < right:
            if arr[left] + arr[right] <= D:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
    answer = 0
    def decompose(start):
        nonlocal answer
        centroid = find_centroid(start)
        all_distances = [0]
        for v, w in graph[centroid]:
            if removed[v]:
                continue
            distances = collect_distances(v, centroid, w)
            for dist in distances:
                if dist <= D:
                    lo, hi = 0, len(all_distances)
                    limit = D - dist
                    while lo < hi:
                        mid = (lo + hi) // 2
                        if all_distances[mid] <= limit:
                            lo = mid + 1
                        else:
                            hi = mid
                    answer += lo
            all_distances.extend(distances)
        removed[centroid] = True
        for v, _ in graph[centroid]:
            if not removed[v]:
                decompose(v)
    decompose(0)
    print(answer)

if __name__ == "__main__":
    solve()
