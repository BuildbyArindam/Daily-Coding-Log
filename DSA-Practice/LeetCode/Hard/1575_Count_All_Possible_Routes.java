/*
 * Problem   : 1575. Count All Possible Routes
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/count-all-possible-routes/
 * Date      : 2026-11-21
 * Difficulty: Hard
 * Topics    : Array, Dynamic Programming, Memoization
 *
 * Approach  : Top-down DP (memoized DFS). State is (city i, remaining fuel k) =
 *             number of ways to reach `finish` starting at city i with k fuel.
 *             - Prune: if k < |loc[i] - loc[finish]|, finish is unreachable -> 0.
 *             - Count 1 if i == finish (stopping here is a valid route), then
 *               add the ways from every other city j after spending |loc[i] - loc[j]|.
 *             - Results taken modulo 1e9 + 7 and cached in f[i][k].
 *
 * Time      : O(n^2 * fuel)  -> n * fuel states, O(n) transitions each
 * Space     : O(n * fuel)    -> memo table + recursion depth up to O(fuel)
 */


// -------------------------------------------- Solution ------------------------------------------------


class Solution {
    private int[] locations;
    private int finish;
    private int n;
    private Integer[][] f;
    private final int mod = (int) 1e9 + 7;

    public int countRoutes(int[] locations, int start, int finish, int fuel) {
        n = locations.length;
        this.locations = locations;
        this.finish = finish;
        f = new Integer[n][fuel + 1];
        return dfs(start, fuel);
    }

    private int dfs(int i, int k) {
        if (k < Math.abs(locations[i] - locations[finish])) {
            return 0;
        }
        if (f[i][k] != null) {
            return f[i][k];
        }
        int ans = i == finish ? 1 : 0;
        for (int j = 0; j < n; ++j) {
            if (j != i) {
                ans = (ans + dfs(j, k - Math.abs(locations[i] - locations[j]))) % mod;
            }
        }
        return f[i][k] = ans;
    }
}
