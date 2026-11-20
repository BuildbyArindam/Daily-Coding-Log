/*
 * Problem:    1269. Number of Ways to Stay in the Same Place After Some Steps
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
 * Difficulty: Hard
 * Topics:     Dynamic Programming
 * Date:       2026-10-07
 *
 * Approach:
 *   Bottom-up DP where dp[pos][step] = number of ways to be at index `pos`
 *   after `step` moves. Each state comes from staying, or moving from the
 *   left or right neighbour on the previous step:
 *       dp[pos][step] = dp[pos][step-1] + dp[pos-1][step-1] + dp[pos+1][step-1]
 *   The pointer must return to index 0, so it can never usefully go farther
 *   than steps/2 from the start. The position range is therefore capped at
 *   min(steps/2, arrLen-1). Results are taken modulo 1e9+7.
 *
 * Time Complexity:  O(steps * min(steps/2, arrLen))
 * Space Complexity: O(steps * min(steps/2, arrLen))
 *                   (reducible to O(min(steps/2, arrLen)) with rolling arrays)
 */


// ------------------------------------------------ Solution ---------------------------------------------------


class Solution {
    public int numWays(int steps, int arrLen) {
        int mod = 1000000007;
        
        // Calculate the maximum number of steps that you can take and still be within the array
        int maxSteps = Math.min(steps / 2, arrLen - 1);
        
        // Create a 2D array to store the number of ways to reach each position at each step
        int[][] dp = new int[maxSteps + 1][steps + 1];
        
        // Initialize the base case
        dp[0][0] = 1;
        
        for (int step = 1; step <= steps; step++) {
            for (int position = 0; position <= maxSteps; position++) {
                dp[position][step] = dp[position][step - 1];
                if (position > 0) {
                    dp[position][step] = (dp[position][step] + dp[position - 1][step - 1]) % mod;
                }
                if (position < maxSteps) {
                    dp[position][step] = (dp[position][step] + dp[position + 1][step - 1]) % mod;
                }
            }
        }
        
        return dp[0][steps];
    }
}
