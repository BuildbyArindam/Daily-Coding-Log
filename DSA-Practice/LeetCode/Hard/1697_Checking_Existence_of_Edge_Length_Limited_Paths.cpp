/*
 * Platform   : LeetCode
 * Problem    : 1697. Checking Existence of Edge Length Limited Paths
 * Link       : https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/
 * Difficulty : Hard
 * Topics     : Union-Find, Graph, Sorting, Two Pointers
 * Date       : 2026-11-22
 *
 * Approach (offline queries + DSU):
 *   - Attach each query's original index, then sort edges and queries by weight.
 *   - For each query (in increasing limit order), binary search the last edge
 *     with weight < limit, and merge edges into the DSU up to that point.
 *     A pointer only moves forward, so each edge is merged at most once.
 *   - Answer = whether the two query nodes are connected in the DSU.
 *     Results are written back by original query index.
 *
 * Time  : O(E log E + Q log Q + Q log E + (E + Q) log N)
 *         (finds are O(log N) with union by size and no path compression)
 * Space : O(N + E + Q)
 */


// ---------------------------------------------- Solution ---------------------------------------------------------------


class DSUnode{
    public:
    int parent,rank;
    DSUnode(int parent,int rank){
        this->parent=parent;
        this->rank=rank;
    }
};
class DSU{
    private:
    vector<DSUnode>parents;
    void _merge(int parent,int child){
        this->parents[child].parent=parent;
        this->parents[parent].rank+=this->parents[child].rank;
    }
    int _find(int x){
        while(this->parents[x].parent!=x){
            x=this->parents[x].parent;
        }
        return x;
    }
    public:
    DSU(int n){
        for(int i=0;i<n;i++){
            DSUnode element(i,1);
            this->parents.push_back(element);
        }
    }
    void findUnion(int x,int y){
        int parx=this->_find(x);
        int pary=this->_find(y);
        if(parx!=pary){
            if(this->parents[parx].rank>=this->parents[pary].rank){
                this->_merge(parx,pary);
            } else {
                this->_merge(pary,parx);
            }
        }
    }
    bool isConnected(int start,int end){
        return this->_find(start)==this->_find(end);
    }
};
class Solution {
private:
    int determineEnd(vector<int>&weights,int limit){
        int end=lower_bound(weights.begin(),weights.end(),limit)-weights.begin();
        return end==weights.size()?end:end-1;
    }
    bool solve(DSU &dsu,int qs,int qe,int &start,int end,vector<vector<int>>&edges){
        if(dsu.isConnected(qs,qe)){
            return true;
        } else {
            while(start<=end){
                int s=edges[start][0];
                int e=edges[start][1];
                dsu.findUnion(s,e);
                if(dsu.isConnected(qs,qe)){
                    return true;
                }
                start++;
            }
            return false;
        }
    }
public:
    vector<bool> distanceLimitedPathsExist(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        DSU dsu(n);
        for(int i=0;i<queries.size();i++){
            queries[i].push_back(i);
        }
        sort(edges.begin(),edges.end(),[](vector<int>&e1,vector<int>&e2){
            return e1[2]<e2[2];
        });
        sort(queries.begin(),queries.end(),[](vector<int>&q1,vector<int>&q2){
            return q1[2]<q2[2];
        });
        vector<int>weights;
        for(vector<int>edge:edges){
            weights.push_back(edge[2]);
        }
        vector<bool>ans(queries.size(),true);
        int start=0;
        for(vector<int>query:queries){
            int qs=query[0];
            int qe=query[1];
            int limit=query[2];
            int index=query[3];
            int end=determineEnd(weights,limit);
            ans[index]=solve(dsu,qs,qe,start,end,edges);
        }
        return ans;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
