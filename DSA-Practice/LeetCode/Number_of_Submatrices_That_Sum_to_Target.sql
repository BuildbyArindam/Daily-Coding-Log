/*
 * Problem:    1074. Number of Submatrices That Sum to Target
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
 * Difficulty: Hard
 * Topics:     Array, Hash Table, Matrix, Prefix Sum
 * Date:       2026-10-08
 *
 * Approach:
 *   1. Build row-wise prefix sums so the sum of any row segment [i..j]
 *      can be read in O(1).
 *   2. Fix a pair of left/right column boundaries (i, j). This collapses
 *      the 2D problem into a 1D one: for each row k, the value is the sum
 *      of that row between columns i and j.
 *   3. Solve the 1D "subarray sum equals target" problem with a running
 *      sum and a hash map of previously seen prefix sums. Each time
 *      (cur - target) has been seen, every occurrence is the top edge of
 *      a valid submatrix ending at row k.
 *
 * Time:  O(n^2 * m)  - n^2 column pairs, m rows scanned for each
 * Space: O(m)        - hash map holds at most m + 1 prefix sums
 *                      (the matrix is modified in place for row prefix sums)
 */


-------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& A, int target) {
        int res = 0, m = A.size(), n = A[0].size();

        // Row-wise prefix sums (in place)
        for (int i = 0; i < m; i++)
            for (int j = 1; j < n; j++)
                A[i][j] += A[i][j - 1];

        unordered_map<int, int> counter;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                counter = {{0, 1}};
                int cur = 0;
                for (int k = 0; k < m; k++) {
                    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
                    auto it = counter.find(cur - target);
                    if (it != counter.end()) res += it->second;
                    counter[cur]++;
                }
            }
        }
        return res;
    }
};
