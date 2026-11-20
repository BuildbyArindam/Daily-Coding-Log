/*
 * Problem   : 1685. Sum of Absolute Differences in a Sorted Array
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
 * Date      : 2026-10-04
 * Difficulty: Medium
 * Topics    : Array, Math, Prefix Sum
 *
 * Approach:
 *   Since nums is sorted, for index i every element on the left is <= nums[i]
 *   and every element on the right is >= nums[i], so the absolute values can
 *   be dropped:
 *     left  = nums[i] * (i + 1)      - prefix[i]
 *     right = (prefix[n-1] - prefix[i]) - nums[i] * (n - 1 - i)
 *     answer[i] = left + right
 *   A prefix-sum array gives each range sum in O(1).
 *
 * Time  : O(n)
 * Space : O(n) for the prefix array (O(1) extra if the output is not counted
 *         and a running prefix is used instead)
 */


// ---------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    vector<int> getSumAbsoluteDifferences(vector<int>& nums) {
        int sz = nums.size();
        vector<int> result(sz);
        vector<long long> prefSum(sz);
        for(int indx = 0; indx < sz; indx++){
            if(indx == 0)prefSum[indx] = nums[indx];
            else prefSum[indx] = prefSum[indx-1] + nums[indx]; 
        }
        for(int indx = 0; indx < sz; indx++){
             int currNum = nums[indx];
             int leftSum = currNum * (indx+1) - prefSum[indx];
             int rightSum = (prefSum[sz - 1] - prefSum[indx] - (sz - 1 - indx)  * currNum);
             result[indx] = leftSum + rightSum;
        }
        return result;
    }
};
