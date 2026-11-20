/*
 * Problem   : 377. Combination Sum IV
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/combination-sum-iv/
 * Difficulty: Medium
 * Topics    : Array, Dynamic Programming
 * Date      : 2026-10-07
 *
 * Approach  : Bottom-up DP (unbounded knapsack, counting ordered sequences).
 *             dp[i] = number of ordered combinations that sum to i.
 *             dp[0] = 1; for each i, dp[i] = sum of dp[i - num] over all num <= i.
 *             The target loop is outer and the nums loop is inner, which
 *             counts different orderings as distinct combinations.
 *             unsigned int avoids signed overflow on intermediate values;
 *             the answer is guaranteed to fit in a 32-bit int.
 *
 * Time      : O(target * n), where n = nums.size()
 * Space     : O(target)
 */


// --------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target+1, 0);
        dp[0] = 1;
        
        for(int i=1;i<=target;i++){
            for(int j=0;j<nums.size();j++){
                if(i-nums[j]>=0 && dp[i]< INT_MAX){
                dp[i] += dp[i-nums[j]];
                }
            }
        }
        return dp[target];
    }
};
