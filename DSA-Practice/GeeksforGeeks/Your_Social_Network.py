"""
Problem   : Your Social Network
Platform  : GeeksforGeeks
Link      : https://www.geeksforgeeks.org/problems/your-social-network0328/1
Difficulty: Medium
Topics    : Graph
Date      : 2026-10-05

Approach:
    Each new user i (2..n) joins through exactly one existing friend
    arr[i-2], so the network forms a tree rooted at user 1.
    The ancestor list of user i is:
        - the direct friend at distance 1, plus
        - every entry in the friend's ancestor list, with distance + 1.
    Build each list from the parent's list (DP over the tree), sort it by
    user id, and emit [i, user, steps] triples.

Complexity:
    Let D = total (user, ancestor) pairs, which is at most O(n^2) for a chain.
    Time : O(D log n)  -> copying ancestors plus sorting each list
    Space: O(D)        -> stored ancestor lists (same order as the output)
"""


# --------------------------------------- Solution ---------------------------------------------------


class Solution:
    def socialNetwork(self, arr):
        # code here
        n = len(arr) + 1
        result = []
        dist = [[] for _ in range(n + 1)]
        for i in range(2, n + 1):
            friend = arr[i - 2]
            dist[i].append((friend, 1))
            for user, steps in dist[friend]:
                dist[i].append((user, steps + 1))
            dist[i].sort()
            for user, steps in dist[i]:
                result.append([i, user, steps])
        return result
