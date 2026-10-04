/*
 * Problem : 1424. Diagonal Traverse II
 * Platform: LeetCode 
 * Link    : https://leetcode.com/problems/diagonal-traverse-ii/
 * Date    : 2026-10-04
 * Difficulty: Medium
 * Topics  : Array, Sorting, Heap (Priority Queue)
 *
 * Approach:
 *   Elements on the same anti-diagonal share the same i + j. Bucket each
 *   element by i + j while scanning row by row, so each bucket holds its
 *   diagonal in top-to-bottom order. The required output goes bottom-to-top
 *   within a diagonal, so walk each bucket in reverse, in increasing order
 *   of i + j. No sorting or heap is needed.
 *
 * Complexity (N = total number of elements):
 *   Time : O(N)
 *   Space: O(N) for the buckets and result, plus the fixed 100001-bucket table
 */


// ------------------------------------------ Solution -------------------------------------------------


class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        int m = nums.size(), maxSum = 0, size = 0, index = 0;
        std::vector<std::vector<int>> map(100001);
        
        for (int i = 0; i < m; i++) {
            size += nums[i].size();
            for (int j = 0; j < nums[i].size(); j++) {
                int sum = i + j;
                map[sum].push_back(nums[i][j]);
                maxSum = std::max(maxSum, sum);
            }
        }
        
        std::vector<int> res(size);
        for (int i = 0; i <= maxSum; i++) {
            std::vector<int>& cur = map[i];
            for (int j = cur.size() - 1; j >= 0; j--) {
                res[index++] = cur[j];
            }
        }
        
        return res;
    }
};
