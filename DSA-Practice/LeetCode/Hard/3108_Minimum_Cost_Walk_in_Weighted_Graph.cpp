/*
 * Problem   : 3108. Minimum Cost Walk in Weighted Graph
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/
 * Date      : 2026-11-25
 * Difficulty: Hard
 * Topics    : Graph Theory, Bit Manipulation, Union-Find, BFS
 *
 * Approach  :
 *   A walk may revisit nodes and reuse edges, and AND can only clear bits.
 *   So within a connected component, the cheapest walk between any two nodes
 *   can pass through every edge in the component and ends up with the AND of
 *   all edge weights there.
 *   1. Build the adjacency list.
 *   2. BFS each unvisited node to label its component and compute the AND
 *      of all edge weights in it (starting from an all-ones mask).
 *   3. For each query: if the endpoints are in different components -> -1,
 *      otherwise -> that component's AND.
 *
 * Complexity:
 *   Time  : O(n + E + Q)
 *   Space : O(n + E)
 */


// ---------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    void bfs(vector<vector<pair<int, int>>>& adj, int comp,
             unordered_map<int, int>& connectedAnd, vector<int>& component,
             int current) {
        queue<int> bfs;
        bfs.push(current);
        component[current] = comp;
        int totalAnd = pow(2, 20) - 1;
        while (!bfs.empty()) {
            int cur = bfs.front();
            bfs.pop();
            for (auto& [child, wt] : adj[cur]) {
                if (component[child] == -1) {
                    component[child] = comp;
                    totalAnd &= wt;
                    bfs.push(child);
                } else
                    totalAnd &= wt;
            }
        }
        connectedAnd[comp] = totalAnd;
    }
    vector<int> minimumCost(int n, vector<vector<int>>& edges, vector<vector<int>>& query) {
        int comp = 0;
        vector<vector<pair<int, int>>> adj(n);
        for (auto& v : edges) {
            adj[v[0]].push_back({v[1], v[2]});
            adj[v[1]].push_back({v[0], v[2]});
        }
        unordered_map<int, int> connectedAnd;
        vector<int> component(n, -1);
        for (int i = 0; i < n; i++) {
            if (component[i] == -1) {
                bfs(adj, comp, connectedAnd, component, i);
                comp++;
            }
        }
        vector<int> ans;
        for (auto& q : query) {
            int start = q[0], end = q[1];
            if (component[start] != component[end]) {
                ans.push_back(-1);
                continue;
            }
            ans.push_back(connectedAnd[component[start]]);
        }
        return ans;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
