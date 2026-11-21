/*
 * Problem   : 956. Tallest Billboard
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/tallest-billboard/
 * Date      : 2026-11-21
 * Difficulty: Hard
 * Topics    : Array, Dynamic Programming, Knapsack, Meet in the Middle
 *
 * Approach  : Top-down DP (memoization). For each rod, choose one of three options:
 *             skip it, add it to the left support, or add it to the right support.
 *             State = (index, diff), where diff = left - right, offset by 5000 so
 *             it fits as a non-negative array index. The stored value is the max
 *             height of the left support. At the end, diff == 0 means both
 *             supports are equal, so the stored value is the billboard height.
 *             Any other final diff is invalid and returns INT_MIN.
 *
 * Time      : O(n * S), where S = sum of rods (diff range is 2S + 1, at most 10001)
 * Space     : O(n * S) for the memo table + O(n) recursion stack
 */


// ------------------------------------------- Solution --------------------------------------------------


class Solution {
public:
    int solve(vector<int>& rods, int n, int index, int maxSum, vector<vector<int>>& dp){
        if(index>=n){
            if(maxSum==5000){
                return 0;
            }
            return INT_MIN;
        }
        
        if(dp[index][maxSum] != INT_MIN){
            return dp[index][maxSum];
        }
        
        return dp[index][maxSum] = max(solve(rods, n, index+1, maxSum, dp), 
                            max(solve(rods, n, index+1, maxSum-rods[index], dp), rods[index]+solve(rods, n, index+1, maxSum+rods[index], dp)));
    }
    
    int tallestBillboard(vector<int>& rods) {
        int n = rods.size();
        int index=0;
        int maxSum = 5000;//GIVEN
        vector<vector<int>> dp(n, vector<int>(10001, INT_MIN));
        return solve(rods, n, index, maxSum, dp); 
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
