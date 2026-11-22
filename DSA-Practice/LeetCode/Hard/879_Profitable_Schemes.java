/**
 * Problem: 879. Profitable Schemes
 * Link: https://leetcode.com/problems/profitable-schemes/
 * Platform: LeetCode 
 * Difficulty: Hard
 * Date: 2026-11-22
 * Topics: Array, Dynamic Programming, Knapsack Problem, 0-1 Knapsack
 *
 * Approach: 3D DP (0-1 knapsack with two constraints).
 *   dp[i][j][k] = number of ways to choose among the first i crimes
 *   using exactly j members and earning at least k profit (k is capped at minProfit).
 *   Transition for crime i (needs `members`, yields `earn`):
 *     - skip it:  dp[i-1][j][k]
 *     - take it:  dp[i-1][j-members][max(0, k-earn)]   (if j >= members)
 *   Base: dp[0][0][0] = 1. Answer = sum of dp[len][j][minProfit] over j in [0, n].
 *   Results are taken modulo 1e9+7.
 *
 * Time:  O(len * n * minProfit)
 * Space: O(len * n * minProfit)  (can be reduced to O(n * minProfit) with a rolling 2D array)
 */


// ------------------------------------------ Solution -------------------------------------------------------


class Solution {
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int len = group.length, MOD = (int)1e9 + 7;
        int[][][] dp = new int[len + 1][n + 1][minProfit + 1];
        dp[0][0][0] = 1;
        for (int i = 1; i <= len; i++) {
            int members = group[i - 1], earn = profit[i - 1];
            for (int j = 0; j <= n; j++) {
                for (int k = 0; k <= minProfit; k++) {
                    if (j < members) {
                        dp[i][j][k] = dp[i - 1][j][k];
                    } else {
                        dp[i][j][k] = (dp[i - 1][j][k] + dp[i - 1][j - members][Math.max(0, k - earn)]) % MOD;
                    }
                }
            }
        }
        int sum = 0;
        for (int j = 0; j <= n; j++) {
            sum = (sum + dp[len][j][minProfit]) % MOD;
        }
        return sum;
    }
}
