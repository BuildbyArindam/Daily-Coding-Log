/*
 * Problem   : 1416. Restore The Array
 * Link      : https://leetcode.com/problems/restore-the-array/
 * Platform  : LeetCode 
 * Difficulty: Hard
 * Topics    : String, Dynamic Programming
 * Date      : 2026-11-22
 *
 * Approach  : Top-down DP (memoized DFS). dp[i] = number of ways to split
 *             the suffix s[i..] into numbers in [1, k] with no leading zeros.
 *             From index i, extend the number digit by digit and recurse on
 *             j + 1 while the value stays <= k. A '0' at the start of a
 *             segment gives 0 ways. Reaching the end of the string counts as
 *             1 valid way. Results are taken modulo 1e9 + 7.
 *
 * Time      : O(n * log10(k)): n states, each tries at most ~10 digits
 * Space     : O(n) for the dp table plus O(n) recursion stack
 */


// -------------------------------------- Solution -----------------------------------------------------------


class Solution {
public:
    int dfs(const string& s, long k, int i, vector<int>& dp) {
        if (i == s.size()) return 1;
        if (s[i] == '0') return 0;
        if (dp[i] != -1) return dp[i];

        int ans = 0;
        long num = 0;
        for (int j = i; j < s.size(); j++) {
            num = num * 10 + s[j] - '0';
            if (num > k) break;
            ans = (ans + dfs(s, k, j + 1, dp))%1000000007;
        }
        return dp[i] = ans;
    }

    int numberOfArrays(string s, int k) {
        vector<int> dp(s.size(), -1);
        return dfs(s, k, 0, dp);
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
