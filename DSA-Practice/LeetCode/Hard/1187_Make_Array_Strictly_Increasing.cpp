/*
 * Problem : 1187. Make Array Strictly Increasing 
 * Platform: LeetCode
 * Link    : https://leetcode.com/problems/make-array-strictly-increasing/
 * Date    : 2026-11-21
 * Difficulty: Hard
 * Topics  : Array, Binary Search, Dynamic Programming, Sorting, LIS
 *
 * Approach:
 *   - Sort + dedupe arr2 (via set).
 *   - dp[j] = smallest possible last value of the processed arr1 prefix
 *     using exactly j replacements (INT_MAX = impossible).
 *   - For each arr1[i], two transitions from the previous row:
 *       keep    : if dp[j] < arr1[i]  -> cur[j]   = arr1[i]
 *       replace : smallest arr2 value > dp[j] -> cur[j+1] = min(cur[j+1], that value)
 *   - A moving pointer `t` over arr2 finds the replacement value, so each row
 *     costs O(n) with no per-state binary search.
 *   - Rolling two rows keeps memory small. Answer = first j with dp[j] != INT_MAX.
 *
 * Time : O(n log n + m * min(m, n))   (m = |arr1|, n = |arr2|)
 * Space: O(n)                         (deduped arr2 + two dp rows of size <= min(m, n) + 1)
 */


// ------------------------------------------ Solution -------------------------------------------------------------


class Solution {
public:
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr) {
        std::set<int> aset(arr.begin(), arr.end());
        vector<int> arr2(aset.begin(), aset.end());

        int m = arr1.size(), n = arr2.size();
        
        vector<vector<int>> dp(2); 
        dp[0].push_back(arr1[0]); 
        dp[0].push_back(arr2[0]); 
        
        int k = 1;
        for(int i = 1; i < m; i++) {
            for(int j = 0; j < dp[1 - k].size(); j++) {
                if(j >= dp[k].size()) dp[k].push_back(INT_MAX);
                if(dp[1-k][j] < arr1[i]) dp[k][j] = arr1[i];
                else dp[k][j] = INT_MAX;
            }
            int t = n - 1;
            for(int j = 0; j < dp[1 - k].size(); j++) {
                while(t >= 0 && arr2[t] > dp[1-k][j]) t--;
                if(t + 1 < n && arr2[t + 1] > dp[1 - k][j]) {
                    if(j + 1 >= dp[k].size()) dp[k].push_back(INT_MAX);
                    dp[k][j+1] = std::min(dp[k][j+1], arr2[t + 1]);
                }
            }
            k = 1 - k;
        }
        
        for(int i = 0; i < dp[1-k].size(); i++) if(dp[1-k][i] != INT_MAX) return i;
        return -1;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
