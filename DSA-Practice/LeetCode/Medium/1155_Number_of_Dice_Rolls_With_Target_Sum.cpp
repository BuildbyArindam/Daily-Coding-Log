/*
 * Problem   : 1155. Number of Dice Rolls With Target Sum
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
 * Difficulty: Medium
 * Topics    : Dynamic Programming, Memoization
 * Date      : 2026-10-03
 *
 * Approach:
 *   Top-down DP with memoization. State dp[n][target] is the number of ways
 *   to reach `target` using exactly `n` dice. For each state, try every face
 *   value 1..k on one die and recurse on (n - 1, target - face).
 *   Base cases: (n == 0 && target == 0) -> 1; (n == 0 || target <= 0) -> 0.
 *   All additions are taken modulo 1e9 + 7.
 *
 * Complexity:
 *   Time : O(n * target * k)  -> n * target states, k transitions each
 *   Space: O(n * target)      -> memo table, plus O(n) recursion stack
 */


// ------------------------------------ Solution --------------------------------------------------------


class Solution {
public:
    const int mod = (int)pow(10, 9) + 7;
    int numRollsToTarget(int n, int k, int target) {
        vector<vector<int>> dp(n + 1, vector<int>(target + 1, -1));
        return recursion(dp, n, k, target);
    }

private:
    int recursion(vector<vector<int>>& dp, int n, int k, int target) {
        if (target == 0 && n == 0) return 1;
        if (n == 0 || target <= 0) return 0;
        if (dp[n][target] != -1) return dp[n][target] % mod;
        int ways = 0; 
        for (int i = 1; i <= k; i++) {
            ways = (ways + recursion(dp, n - 1, k, target - i)) % mod;
        }
        dp[n][target] = ways % mod;
        return dp[n][target];
    }
};
