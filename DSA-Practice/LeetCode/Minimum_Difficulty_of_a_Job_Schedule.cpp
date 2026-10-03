/*
 * Problem   : Minimum Difficulty of a Job Schedule (LeetCode 1335)
 * Link      : https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
 * Difficulty: Hard
 * Topics    : Array, Dynamic Programming
 * Date      : 2026-10-03
 *
 * Approach:
 *   Bottom-up DP. dp[i][k] = min total difficulty to schedule the first i jobs
 *   in exactly k days. For the last day, try every split point j: jobs j+1..i
 *   go on day k, costing max(jobDifficulty[j..i-1]) (tracked while j moves
 *   left), plus dp[j][k-1] for the earlier days.
 *   dp[i][k] = min over j of (dp[j][k-1] + max(job[j+1..i]))
 *   If n < d, there aren't enough jobs for one per day, so return -1.
 *
 * Time : O(n^2 * d)
 * Space: O(n * d)
 */


// ------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    int minDifficulty(vector<int>& jobDifficulty, int d) {
        const int n = jobDifficulty.size();
    if (n < d)
      return -1;
    vector<vector<int>> dp(n + 1, vector<int>(d + 1, INT_MAX / 2));
    dp[0][0] = 0;
    for (int i = 1; i <= n; ++i)
      for (int k = 1; k <= d; ++k) {
        int maxDifficulty = 0;              
        for (int j = i - 1; j >= k - 1; --j) { 
          maxDifficulty = max(maxDifficulty, jobDifficulty[j]);  
          dp[i][k] = min(dp[i][k], dp[j][k - 1] + maxDifficulty);
        }
      }
    return dp[n][d];
    }
};
