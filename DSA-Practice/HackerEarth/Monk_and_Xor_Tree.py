"""
Problem: Monk and Xor Tree
Platform: HackerEarth (CodeMonk)
Link: https://www.hackerearth.com/practice/codemonk/8/1483400/
Date Solved: 2026-09-23
Difficulty: Easy
Topics; Trees, XOR

Approach:
Rooted tree with values on nodes. For each node u, compute prefix XOR
from root to u. Count pairs (u, v) on the same root-to-node path where
prefix[u] XOR prefix[v] == K, using an offline DFS + hashmap:
  - Iterative DFS (stack-based, avoids recursion depth issues) tracks
    a running frequency map of prefix-XOR values seen on the current
    root-to-node path.
  - On entering node u: compute prefix[u], look up freq[prefix[u] ^ K]
    to count valid ancestor matches, then add prefix[u] to freq.
  - On leaving u (post-order): decrement freq[prefix[u]] to remove it
    once its subtree is fully processed, keeping the map scoped to
    the current path only.

Time Complexity:  O(N)      -- each node pushed/processed twice
Space Complexity: O(N)      -- prefix array, freq map, stack, adjacency list
"""


# --------------------------------------- Solution -------------------------------------------


import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
children = [[] for _ in range(N + 1)]
parents = [0] * (N + 1)
parent_list = list(map(int, input().split()))
for i in range(2, N + 1):
    p = parent_list[i - 2]
    parents[i] = p
    children[p].append(i)
prefix = [0] * (N + 1)
freq = {0: 1} 
answer = 0
stack = [(1, 0)]
while stack:
    u, state = stack.pop()
    if state == 0:
        prefix[u] = prefix[parents[u]] ^ A[u]
        target = prefix[u] ^ K
        answer += freq.get(target, 0)
        freq[prefix[u]] = freq.get(prefix[u], 0) + 1
        stack.append((u, 1))
        for v in reversed(children[u]):
            stack.append((v, 0))
    else:
        freq[prefix[u]] -= 1
        if freq[prefix[u]] == 0:
            del freq[prefix[u]]
print(answer)
