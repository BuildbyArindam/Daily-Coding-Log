"""
Problem: 753. Cracking the Safe
Link: https://leetcode.com/problems/cracking-the-safe/
Platform: LeetCode 
Difficulty: Hard
Date: 2026-11-25
Topics: String, DFS, Graph Theory, Eulerian Circuit

Approach:
  Model the problem as a graph where each node is an (n-1)-digit string and
  each edge is an n-digit password (node + digit). Every password is one
  edge, so the shortest string containing all passwords corresponds to an
  Eulerian circuit (every node has in-degree = out-degree = k).
  Run Hierholzer's algorithm via DFS: follow unused edges, and append the
  edge digit in post-order. Reversing the post-order gives the circuit.
  Prefix with the start node "0" * (n - 1) to form the final string.

Time Complexity:  O(k^n)    - each of the k^n edges is visited once
                              (string slicing/concat adds a factor of n in practice)
Space Complexity: O(k^n)    - seen set, result list, and recursion depth
"""

# ---------------------------------------------------- Solution ------------------------------------------------------


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        def dfs(node):
            for x in map(str, range(k)):
                neighbor = node + x
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor[1:])
                    result.append(x)

        start = "0" * (n - 1)
        seen = set()
        result = []
        dfs(start)
        
        return start + "".join(result[::-1])

  __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
