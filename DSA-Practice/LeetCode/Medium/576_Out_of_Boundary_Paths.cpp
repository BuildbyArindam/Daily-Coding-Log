/*
 * Problem : 576. Out of Boundary Paths 
 * Link    : https://leetcode.com/problems/out-of-boundary-paths/
 * Date    : 2026-10-08
 * Difficulty: Medium
 * Topics  : Dynamic Programming
 *
 * Approach:
 *   Bottom-up DP over the number of moves. dp[i][j] holds the number of ways
 *   to be at cell (i, j) after the current number of moves. Before each move,
 *   every boundary cell adds dp[i][j] to the answer once per edge it touches
 *   (corners count twice, and a 1-wide grid counts both sides), since each
 *   such edge is a distinct way to step out. Then dp is rolled forward by
 *   summing the four neighbours into a fresh grid. All sums are taken mod 1e9+7.
 *
 * Time    : O(N * m * n)
 * Space   : O(m * n)  (two grids, current and next)
 */


// ---------------------------------------------- Solution -------------------------------------------------


class Solution {
public:
    int findPaths(int m, int n, int N, int x, int y) {
        const int M = 1000000000 + 7;
        vector<vector<int>> dp(m, vector<int>(n, 0));
        dp[x][y] = 1;
        int count = 0;

        for (int moves = 1; moves <= N; moves++) {
            vector<vector<int>> temp(m, vector<int>(n, 0));

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i == m - 1) count = (count + dp[i][j]) % M;
                    if (j == n - 1) count = (count + dp[i][j]) % M;
                    if (i == 0) count = (count + dp[i][j]) % M;
                    if (j == 0) count = (count + dp[i][j]) % M;
                    temp[i][j] = (
                        ((i > 0 ? dp[i - 1][j] : 0) + (i < m - 1 ? dp[i + 1][j] : 0)) % M +
                        ((j > 0 ? dp[i][j - 1] : 0) + (j < n - 1 ? dp[i][j + 1] : 0)) % M
                    ) % M;
                }
            }
            dp = temp;
        }

        return count;  
    }
};
