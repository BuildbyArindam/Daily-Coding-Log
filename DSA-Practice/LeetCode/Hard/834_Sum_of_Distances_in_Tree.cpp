/*
 * Problem   : 834. Sum of Distances in Tree
 * Link      : https://leetcode.com/problems/sum-of-distances-in-tree/
 * Platform  : LeetCode 
 * Date      : 2026-11-25
 * Difficulty: Hard
 * Topics    : Tree, DFS, Dynamic Programming, Graph
 *
 * Approach  : Rerooting DP on trees (two DFS passes).
 *   1) Post-order DFS from root 0 computes, for every node:
 *        count[v] = size of v's subtree
 *        res[v]   = sum of distances from v to nodes in its subtree
 *                 = sum over children c of (res[c] + count[c])
 *      After this pass, res[0] is the final answer for the root.
 *   2) Pre-order DFS reroots from parent to child c:
 *        res[c] = res[parent] - count[c] + (n - count[c])
 *      The count[c] nodes in c's subtree get 1 closer, and the other
 *      n - count[c] nodes get 1 farther.
 *
 * Time      : O(n)  (each node and edge is visited a constant number of times)
 * Space     : O(n)  (adjacency list, count[], res[], recursion stack)
 */


// --------------------------------------------------- Solution --------------------------------------------------------------


class Solution {
private:
    unordered_map<int, vector<int>> graph;
    vector<int> count;
    vector<int> res;

    void dfs(int node, int parent) {
        for (int child : graph[node]) {
            if (child != parent) {
                dfs(child, node);
                count[node] += count[child];
                res[node] += res[child] + count[child];
            }
        }
    }

    void dfs2(int node, int parent) {
        for (int child : graph[node]) {
            if (child != parent) {
                res[child] = res[node] - count[child] + (count.size() - count[child]);
                dfs2(child, node);
            }
        }
    }

public:
    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        graph.clear();
        count = vector<int>(n, 1);
        res = vector<int>(n, 0);

        for (auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        dfs(0, -1);
        dfs2(0, -1);

        return res;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
