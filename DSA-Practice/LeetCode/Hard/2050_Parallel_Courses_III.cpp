/*
 * Problem   : 2050. Parallel Courses III
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/parallel-courses-iii/
 * Date      : 2026-10-07
 * Difficulty: Hard
 * Topics    : Array, DP, Graph, Topological Sort, DAG
 *
 * Approach  : Kahn's algorithm (BFS topological sort) with DP on the DAG.
 *             maxTime[v] = earliest finish time of course v
 *                        = time[v] + max(maxTime[u]) over all prerequisites u.
 *             Courses with indegree 0 start at maxTime = time[i]. When
 *             processing node u, relax each neighbour v with
 *             max(maxTime[v], maxTime[u] + time[v]). Answer is the max
 *             of maxTime over all courses.
 *
 * Time      : O(V + E)
 * Space     : O(V + E)  (adjacency list + indegree + maxTime + queue)
 */


// --------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<int>adj[n];
        vector<int>indegree(n,0);
        for(auto relation:relations){
            int u = relation[0]-1;
            int v = relation[1]-1;
            adj[u].push_back(v);
            indegree[v]++;
        }
        queue<int>q;
        vector<int>maxTime(n,0);
        for(int i=0;i<n;i++){
            if(indegree[i]==0){
                maxTime[i] = time[i];
                q.push(i);
            }
        }
        while(q.empty()==false){
            int size = q.size();
            for(int i=0;i<size;i++){
                auto node = q.front();q.pop();
                for(int x:adj[node]){
                    maxTime[x] = max(maxTime[x],time[x]+maxTime[node]);
                    indegree[x]--;
                    if(indegree[x]==0)q.push(x);
                }
            }
        }
        int maxi = 0;
        for(int i=0;i<n;i++){
            maxi = max(maxi,maxTime[i]);
        }
        return maxi ;
    }
};
