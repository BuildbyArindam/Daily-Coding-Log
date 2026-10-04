/*
 * Problem:    10. Regular Expression Matching
 * Platform:   LeetCode 
 * Link:       https://leetcode.com/problems/regular-expression-matching/
 * Date:       2026-10-04
 * Difficulty: Hard
 * Topics:     String, Dynamic Programming, Recursion
 *
 * Approach:   Bottom-up 2D DP.
 *             dp[i][j] = true if s[0..i-1] matches p[0..j-1].
 *             - p[j-1] is a letter or '.':
 *                 dp[i][j] = chars match && dp[i-1][j-1]
 *             - p[j-1] is '*' (applies to p[j-2]):
 *                 zero occurrences: dp[i][j-2]
 *                 one or more:      chars match && dp[i-1][j]
 *             Base: dp[0][0] = true; dp[0][j] = dp[0][j-2] when p[j-1] == '*'.
 *
 * Time:       O(m * n)
 * Space:      O(m * n)  (can be reduced to O(n) with a rolling row)
 */


// ------------------------------------------ Solution -----------------------------------------------------------


class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length(), n = p.length();
        vector<vector<bool>> dp(m + 1, vector<bool>(n + 1, false));
        dp[0][0] = true;
        for (int i = 1; i <= n; i++) {
            if (p[i - 1] == '*') {
                dp[0][i] = dp[0][i - 2];
            }
        }
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (p[j - 1] == '*') {
                    dp[i][j] = dp[i][j - 2] || (s[i - 1] == p[j - 2] || p[j - 2] == '.') && dp[i - 1][j];
                } else {
                    dp[i][j] = (s[i - 1] == p[j - 1] || p[j - 1] == '.') && dp[i - 1][j - 1];
                }
            }
        }
        return dp[m][n];
    }
};
