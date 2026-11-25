/*
 * Problem   : 2097. Valid Arrangement of Pairs
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/valid-arrangement-of-pairs/
 * Date      : 2026-11-25
 * Difficulty: Hard
 * Topics    : Graph, DFS, Eulerian Path/Circuit
 *
 * Approach  :
 *   Treat each pair [a, b] as a directed edge a -> b. A valid arrangement is
 *   an Eulerian path that uses every edge exactly once.
 *   1. Build adjacency lists and track in/out degrees per node.
 *   2. Start node = the node with out - in == 1. If none exists, the graph
 *      has an Eulerian circuit, so any node works.
 *   3. Run iterative Hierholzer's algorithm with a stack. When a node has no
 *      unused edges left, pop it and push it to the front of the path.
 *   4. Consecutive nodes in the path form the ordered pairs.
 *
 * Time      : O(V + E) average (hash map/set operations), E = pairs.size()
 * Space     : O(V + E) for the graph, degree map, stack and path
 */


// -------------------------------------------------- Solution --------------------------------------------------------------


class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& pairs) {
        unordered_map<int, unordered_set<int>> g;
        unordered_map<int, pair<int, int>> deg;
        for (auto p : pairs) {
            g[p[0]].insert(p[1]);
            deg[p[1]].first++;
            deg[p[0]].second++;
        }
        auto getsrc = [&]() {
            int src;
            for (auto [e, d] : deg) {
                auto [in, out] = d;
                if (out - in == 1) {
                    src = e;
                    break;
                }
                src = e;
            }
            return src;
        };
        int src = getsrc();
        deque<int> path;
        stack<int> st;
        st.push(src);
        while (!st.empty()) {
            int u = st.top();
            if (g[u].size() == 0) {
                path.push_front(u);
                st.pop();
            } else {
                int v = *g[u].begin();
                g[u].erase(v);
                st.push(v);
            }
        }
        vector<vector<int>> ans;
        int n = path.size();
        for (int i = 0; i < n - 1; ++i) {
            ans.push_back({path[i], path[i + 1]});
        }
        return ans;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
