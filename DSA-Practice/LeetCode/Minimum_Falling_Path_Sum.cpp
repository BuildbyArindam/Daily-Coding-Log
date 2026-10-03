/*
 * Problem   : 931. Minimum Falling Path Sum (LeetCode)
 * Link      : https://leetcode.com/problems/minimum-falling-path-sum/
 * Difficulty: Medium
 * Topics    : Array, Dynamic Programming, Matrix
 * Date      : 2026-10-03
 *
 * Approach  : Bottom-up DP, done in place on the input matrix.
 *             A[i][j] becomes the minimum falling path sum ending at (i, j).
 *             Each cell can be reached from the three cells above it
 *             (j-1, j, j+1), so A[i][j] += min(A[i-1][j-1..j+1]).
 *             The answer is the minimum value in the last row.
 *
 * Time      : O(n^2)  (each of the n^2 cells checks at most 3 neighbours)
 * Space     : O(1)    extra (the input matrix is modified in place)
 */


// ---------------------------------------- Solution ---------------------------------------------------------


class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& A) {
        const int n = A.size();

    for (int i = 1; i < n; ++i)
      for (int j = 0; j < n; ++j) {
        int mini = INT_MAX;
        for (int k = max(0, j - 1); k < min(n, j + 2); ++k)
          mini = min(mini, A[i - 1][k]);
        A[i][j] += mini;
      }
    return *min_element(begin(A[n - 1]), end(A[n - 1]));
    }
};
