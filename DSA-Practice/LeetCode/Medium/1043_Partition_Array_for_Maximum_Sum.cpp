/*
 * Problem : 1043. Partition Array for Maximum Sum
 * Platform: LeetCode 
 * Link    : https://leetcode.com/problems/partition-array-for-maximum-sum/
 * Date    : 2026-10-08
 * Difficulty: Medium
 * Topics  : Array, Dynamic Programming
 *
 * Approach:
 *   Bottom-up DP where dp[i] is the max sum obtainable from the suffix
 *   arr[i..N-1]. For each start i, try every first-subarray length
 *   1..k, tracking the running max. Every element in that subarray
 *   becomes that max, so the candidate is:
 *       currMax * len + dp[i + len]
 *   Only the last k+1 states are ever needed, so dp is a circular
 *   buffer of size k+1 indexed by (i % (k+1)).
 *
 * Time : O(N * k)
 * Space: O(k)
 */


// --------------------------------------------- Solution ------------------------------------------------


class Solution {
public:
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int N = arr.size();
        int K = k + 1;

        int dp[k + 1];
        memset(dp, 0, sizeof(dp));

        for (int start = N - 1; start >= 0; start--) {
            int currMax = 0;
            int end = min(N, start + k);
            
            for (int i = start; i < end; i++) {
                currMax = max(currMax, arr[i]);
                dp[start % K] = max(dp[start % K], dp[(i + 1) % K] + currMax * (i - start + 1));
            }
        }
        return dp[0];
    }
};
