/*
 * Problem   : 332. Reconstruct Itinerary
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/reconstruct-itinerary/
 * Difficulty: Hard
 * Date      : 2026-10-07
 * Topics    : Graph, DFS, Eulerian Path, Sorting
 *
 * Approach:
 *   Build an adjacency list where each airport maps to a multiset of
 *   destinations, so they stay sorted lexicographically and duplicate
 *   tickets are kept. Run Hierholzer's algorithm from "JFK": repeatedly
 *   take the smallest unused outgoing edge and recurse. When an airport
 *   has no edges left, append it to the result (post-order). Reverse the
 *   result at the end to get the itinerary.
 *
 * Complexity:
 *   Time : O(E log E), E = number of tickets (multiset insert/erase)
 *   Space: O(E) for the adjacency list, plus O(E) recursion depth
 *          and result
 */


// ---------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    void dfs(unordered_map<string, multiset<string>>& adj, vector<string>& result, string s){
        while(adj[s].size()){
            string v = *(adj[s].begin());
            adj[s].erase(adj[s].begin());
            dfs(adj, result, v);
        }
        result.push_back(s);
    }
public:
    vector<string> findItinerary(vector<vector<string>>& tickets) {
        unordered_map<string, multiset<string>> adj;
        for(vector<string>& t: tickets)
            adj[t[0]].insert(t[1]);
      
        vector<string> result;
        dfs(adj, result, "JFK");
        reverse(result.begin(), result.end());
        return result;   
    }
};
