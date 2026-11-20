/*
 * Problem   : 847. Shortest Path Visiting All Nodes
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/shortest-path-visiting-all-nodes/
 * Date      : 2026-10-07
 * Difficulty: Hard
 * Topics    : BFS, Bitmask, Dynamic Programming, Graph Theory, Bit Manipulation
 *
 * Approach  : Multi-source BFS over states (mask, node), where mask is the set
 *             of visited nodes and node is the current position. Every node is
 *             pushed as a starting state with only its own bit set. Each BFS
 *             level is one edge traversed, and the first state whose mask
 *             equals (1<<n)-1 gives the minimum path length. A visited table
 *             on (mask, node) prevents revisiting states, so nodes and edges
 *             can be reused freely.
 *
 * Time      : O(2^n * n + 2^n * E), i.e. each (mask, node) state is processed
 *             once and expands along its node's edges. With n <= 12 this is fine.
 * Space     : O(2^n * n) for the visited table and queue.
 */


// --------------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int shortestPathLength(vector<vector<int>>& adj) {
        int n = adj.size();
        int end = (1<<n) - 1;
        vector<vector<bool>> vis(1<<n, vector<bool>(n, false));
        queue<pair<int, int>> q;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int m = 0;
            m |= 1 << i;
            q.push({m, i});
            vis[m][i] = true;
        }
        while(!q.empty()) {
            int k = q.size();
            while(k--) {
                auto[set, node] = q.front();
                q.pop();
                if (set == end) {
                    return ans;
                }
                for (int i = 0; i < adj[node].size(); ++i) {
                    int m = set;
                    m |= (1 << adj[node][i]);
                    if (!vis[m][adj[node][i]]) {
                        q.push({m, adj[node][i]});
                        vis[m][adj[node][i]] = true;
                    }
                }
            }
            ++ans;
        }
        return ans;   
    }
};
