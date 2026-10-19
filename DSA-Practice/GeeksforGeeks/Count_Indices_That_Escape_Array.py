"""
Problem   : Count Indices That Escape Array
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/good-stones--170647/1
Difficulty: Medium
Topics    : Greedy, Dynamic Programming, Graph, DFS
Date      : 2026-10-19

Approach:
    Treat each index i as a node with a single outgoing edge to i + arr[i].
    An index "escapes" if following the edges leads outside the array.
    Walk from each unvisited index, marking nodes with a state:
        0 = unvisited, 1 = on the current path, 2 = escapes, 3 = stuck (cycle).
    The walk stops when it leaves the array, reaches a node already resolved
    (2 or 3), or reaches a node on the current path (a cycle). Every node on
    the path then gets the same final state, so each index is resolved once.
    The answer is the count of nodes with state 2.

Time Complexity : O(n), each index is visited and resolved at most once.
Space Complexity: O(n), for the state array and the path list.
"""


# --------------------------------------------------- Solution ---------------------------------------------------------------------


class Solution:
    def goodIndices(self, arr):
        # code here
        n = len(arr)
        state = [0] * n
        for i in range(n):
            if state[i] != 0:
                continue
            path = []
            curr = i
            while 0 <= curr < n and state[curr] == 0:
                state[curr] = 1
                path.append(curr)
                curr += arr[curr]
            if curr < 0 or curr >= n or (
                0 <= curr < n and state[curr] == 2
            ):
                result = 2
            else:
                result = 3
            for node in path:
                state[node] = result
        return state.count(2)
