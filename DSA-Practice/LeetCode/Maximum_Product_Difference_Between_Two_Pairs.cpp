/*
 * Problem : 1913. Maximum Product Difference Between Two Pairs
 * Platform: LeetCode 
 * Link    : https://leetcode.com/problems/maximum-product-difference-between-two-pairs/
 * Date    : 2026-10-03
 8 Difficulty: Easy
 * Topics  : Array, Sorting
 *
 * Approach:
 *   Sort the array. The product difference (a*b - c*d) is maximised when
 *   (a, b) are the two largest values and (c, d) are the two smallest.
 *   After sorting, return nums[n-1]*nums[n-2] - nums[0]*nums[1].
 *
 * Time Complexity : O(n log n), dominated by sorting
 * Space Complexity: O(1) extra (in-place sort, ignoring sort's internal stack)
 */


// ---------------------------------- Solution -----------------------------------------


class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n= nums.size()-1;
        int result= nums[n] *nums[n-1]-nums[0]*nums[1];
        return result;   
    }
};
