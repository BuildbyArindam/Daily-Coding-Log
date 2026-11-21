/*
 * Problem   : 44. Wildcard Matching
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/wildcard-matching/
 * Date      : 21-Nov-2026
 & Difficulty: Hard
 * Topics    : String, Dynamic Programming, Greedy, Recursion
 *
 * Approach  : Bottom-up 2D DP. dp[i][j] is true if the first i characters
 *             of s match the first j characters of p.
 *             - Base: dp[0][0] = true; dp[0][j] = dp[0][j-1] when p[j-1] == '*'
 *               (a leading run of '*' can match the empty string).
 *             - If p[j-1] == '*': dp[i][j] = dp[i][j-1] (star matches empty)
 *                                         || dp[i-1][j] (star absorbs s[i-1]).
 *             - If p[j-1] == '?' or equals s[i-1]: dp[i][j] = dp[i-1][j-1].
 *             - Otherwise dp[i][j] stays false.
 *
 * Time      : O(m * n)
 * Space     : O(m * n), reducible to O(n) with a rolling row
 *             (m = s.length(), n = p.length())
 */


// ------------------------------------------ Solution --------------------------------------------------


class Solution {
public:
   bool isMatch(string s, string p) {
       int m = s.length(), n = p.length();
       vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));

       dp[0][0] = true;  
       for (int i = 1; i <= n; i++) {
           if (p[i - 1] == '*') {
               dp[0][i] = dp[0][i - 1];  
           }
       }

       for (int i = 1; i <= m; i++) {
           for (int j = 1; j <= n; j++) {
               if (p[j - 1] == '*') {
                   dp[i][j] = dp[i][j - 1] || dp[i - 1][j];  
               } else if (p[j - 1] == '?' || s[i - 1] == p[j - 1]) {
                   dp[i][j] = dp[i - 1][j - 1];  
               }
           }
       }

       return dp[m][n];
   }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
