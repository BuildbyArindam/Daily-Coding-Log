/*
 * Problem   : 1531. String Compression II
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/string-compression-ii/
 * Date      : 2026-10-03
 * Difficulty: Hard
 * Topics    : String, Dynamic Programming
 *
 * Approach  : Top-down DP with memoization.
 *   State   : dp[i][k] = minimum run-length-encoded length of s[i:]
 *             when at most k characters may be deleted.
 *   Choice  : From index i, extend a block to every j >= i. Inside s[i..j],
 *             keep the most frequent character and delete the rest
 *             (cost = (j - i + 1) - maxFreq deletions). The block encodes to
 *             getLength(maxFreq), then recurse on j + 1 with the remaining k.
 *   Base    : k < 0 is invalid (returns kMax); if i reaches the end, or the
 *             remaining suffix can be fully deleted, the cost is 0.
 *   Length  : 1 -> "c" (1), 2..9 -> "2c" (2), 10..99 -> "10c" (3), 100 -> (4).
 *
 * Time      : O(n^2 * k)  -> n*k states, O(n) transitions each
 *             (plus a 128-sized count array allocated per state)
 * Space     : O(n * k) for the memo table, O(n) recursion depth
 */


// --------------------------------- Solution --------------------------------------------------


class Solution {
public:
    int getLengthOfOptimalCompression(string s, int k) {
    dp.resize(s.length(), vector<int>(k + 1, kMax));
    return compression(s, 0, k);
  }

 private:
  constexpr static int kMax = 101;
  vector<vector<int>> dp;
  int compression(const string& s, int i, int k) {
    if (k < 0)
      return kMax;
    if (i == s.length() || s.length() - i <= k)
      return 0;
    if (dp[i][k] != kMax)
      return dp[i][k];
    int maxFreq = 0;  
    vector<int> count(128);
    for (int j = i; j < s.length(); ++j) {
      maxFreq = max(maxFreq, ++count[s[j]]);
      dp[i][k] = min(dp[i][k],
                     getLength(maxFreq) +
                     compression(s, j + 1, k - (j - i + 1 - maxFreq)));
    }
    return dp[i][k];
  }
  int getLength(int maxFreq) {
    if (maxFreq == 1)
      return 1;  
    if (maxFreq < 10)
      return 2; 
    if (maxFreq < 100)
      return 3;
    return 4;  
    }
};
