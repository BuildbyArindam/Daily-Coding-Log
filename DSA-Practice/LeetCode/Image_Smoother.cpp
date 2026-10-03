/*
 * Problem   : 661. Image Smoother (LeetCode)
 * Link      : https://leetcode.com/problems/image-smoother/
 * Difficulty: Easy
 * Topics    : Array, Matrix
 * Date      : 2026-10-03
 *
 * Approach:
 *   For every cell, scan its 3x3 neighborhood, clamping the row and column
 *   bounds to the grid so edge and corner cells only use valid neighbors.
 *   Accumulate the sum and count of valid cells, then store the floor of
 *   sum / count (integer division) in a separate result matrix, so the
 *   original values aren't overwritten mid-computation.
 *
 * Time Complexity : O(R * C), at most 9 cells visited per cell
 * Space Complexity: O(1) extra, excluding the O(R * C) output matrix
 */


// --------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        int rows = img.size();
        int cols = img[0].size();
        vector<vector<int>> result(rows, vector<int>(cols, 0));
        for (int i = 0; i < rows; ++i) 
        {
            for (int j = 0; j < cols; ++j) 
            {
                int total_sum = 0;
                int count = 0;

                for (int l = max(0, i-1); l < min(rows, i+2); ++l) 
                {
                    for (int k = max(0, j-1); k < min(cols, j+2); ++k) 
                    {
                        total_sum += img[l][k];
                        count += 1;
                    }
                }
                result[i][j] = total_sum / count;
            }
        }
        return result;
    }
};
