/*
 * Problem   : 867. Transpose Matrix
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/transpose-matrix/
 * Difficulty: Easy
 * Topics    : Array, Matrix, Simulation
 * Date      : 2026-10-03
 *
 * Approach  : The transpose swaps rows and columns, so element matrix[i][j]
 *             goes to ans[j][i]. Iterate column by column over the original
 *             matrix, collect each column into a temporary row, and append
 *             that row to the result.
 *
 * Complexity: Time  O(n * m), every element is visited once
 *             Space O(n * m) for the output matrix (O(1) extra beyond it)
 */


// ----------------------------------- Solution -------------------------------------------------


class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> ans;
        for (int j = 0; j < m; j++) {
            vector<int> temp;
            for (int i = 0; i < n; i++) {
                temp.push_back(matrix[i][j]);
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
