/*
 * Problem   : 446. Arithmetic Slices II - Subsequence
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
 * Date      : 2026-10-03
 * Difficulty: Hard
 * Topics    : Array, Dynamic Programming
 *
 * Approach  :
 *   dp[i][j] = number of arithmetic subsequences (length >= 2) whose last two
 *   elements are nums[j], nums[i] (j < i). The common difference is
 *   d = nums[i] - nums[j]. Such a subsequence extends one that ends at
 *   (nums[k], nums[j]) with nums[k] = 2*nums[j] - nums[i] and k < j.
 *   A hash map from value -> list of indices finds all valid k.
 *   Transition: dp[i][j] += dp[j][k] + 1  (the +1 is the new pair [k, j]
 *   extended by i, i.e. the length-3 base case).
 *   The answer sums dp[i][j] over all pairs, which counts only length >= 3.
 *
 * Time      : O(n^2 * m), where m is the max number of indices sharing one
 *             value (worst case O(n^3), e.g. all elements equal)
 * Space     : O(n^2) for dp + O(n) for the index map
 */


// -------------------------------------- Solution ----------------------------------------------------------


class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        const int n = nums.size();
    int ans = 0;
    vector<vector<int>> dp(n, vector<int>(n));
    unordered_map<long, vector<int>> numToIndices;
    for (int i = 0; i < n; ++i)
      numToIndices[nums[i]].push_back(i);
    for (int i = 0; i < n; ++i)
      for (int j = 0; j < i; ++j) {
        const long target = nums[j] * 2L - nums[i];
        if (numToIndices.count(target))
          for (const int k : numToIndices[target])
            if (k < j)
              dp[i][j] += (dp[j][k] + 1);
        ans += dp[i][j];
      }
    return ans;
    }
};
