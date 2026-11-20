/*
 * Problem   : 629. K Inverse Pairs Array
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/k-inverse-pairs-array/
 * Date      : 2026-10-08
 * Difficulty: Hard
 * Topics    : Dynamic Programming
 *
 * Approach  : dp[i][j] = number of permutations of 1..i with exactly j inverse pairs.
 *             Inserting the i-th element into a permutation of i-1 elements creates
 *             between 0 and i-1 new inversions, so
 *             dp[i][j] = sum(dp[i-1][j-x]) for x in [0, min(j, i-1)].
 *             Base case: dp[0][0] = 1. Answer is dp[n][k] modulo 1e9+7.
 *
 * Time      : O(n * k * min(n, k))
 * Space     : O(n * k)  (fixed 1001 x 1001 table)
 */


// ------------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int kInversePairs(int n, int k) {
        int dp[1001][1001] = {1};  
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= k; j++) {
                for (int x = 0; x <= min(j, i - 1); x++) {
                    
                    if (j - x >= 0) {
                        dp[i][j] = (dp[i][j] + dp[i - 1][j - x]) % 1000000007;
                    }
                }
            }
        }

        return dp[n][k];
    }
};
