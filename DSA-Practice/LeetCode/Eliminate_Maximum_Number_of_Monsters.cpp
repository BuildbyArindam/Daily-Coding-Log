/*
 * Problem : 1921. Eliminate Maximum Number of Monsters
 * Platform: LeetCode 
 * Link    : https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
 * Date    : 2026-10-04
 * Difficulty: Medium
 * Topics  : Array, Greedy, Sorting
 *
 * Approach:
 *   Compute each monster's arrival time = ceil(dist / speed) and sort.
 *   The weapon kills one monster per minute, so the monster at sorted
 *   index i must be killed by minute i. If two neighbouring monsters
 *   share an arrival time and the elapsed minutes already reach it, a
 *   monster gets through, so return the count killed so far. If no
 *   monster gets through, return n.
 *
 * Time : O(n log n)  (sorting dominates)
 * Space: O(n)        (arrival-time array)
 */


// ----------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int eliminateMaximum(vector<int>& dist, vector<int>& speed) {
        int x = 1;
        int n = dist.size();
        vector<pair<int,int>>vp;
        vector<int> ans;
        for(int i = 0;i<n;i++){
            ans.push_back(ceil((double)dist[i]/speed[i]));
        }
        sort(ans.begin(), ans.end());
        for(int i = 0;i<n;i++){
            cout << ans[i] << " ";
        }
        cout << endl;
        for(int i = 0;i<n-1;i++){
            if(ans[i]==ans[i+1]&&x>=ans[i+1]){
                return x;
            }
            x++;
        }
        return x;
    }
};
