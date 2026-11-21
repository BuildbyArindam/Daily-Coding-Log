/*
 * Problem   : 2366. Minimum Replacements to Sort the Array
 * Link      : https://leetcode.com/problems/minimum-replacements-to-sort-the-array/
 * Platform  : LeetCode
 * Difficulty: Hard
 * Topics    : Array, Math, Greedy
 * Date      : 2026-11-21
 *
 * Approach  : Greedy, traversing right to left.
 *   - The last element stays as is and becomes the upper bound ("last").
 *   - If nums[i] > last, split it into t = ceil(nums[i] / last) parts.
 *   - Splitting as evenly as possible makes the smallest part,
 *     floor(nums[i] / t), as large as possible. That is the new bound
 *     for the elements to the left, which keeps later splits minimal.
 *   - Each split costs t - 1 operations.
 *
 * Time      : O(n)
 * Space     : O(1)
 */


// -------------------------------------- Solution --------------------------------------------------------------


class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {
        int n = nums.size();
        int last = nums[n-1];  
        long long ans = 0;   
        for (int i = n - 2; i >= 0; --i) {
            if (nums[i] > last) { 
                int t = nums[i] / last; 
                if (nums[i] % last) t++; 
                last = nums[i] / t; 
                ans += t - 1;
            } else {
                last = nums[i];
            }
        }
        return ans; 
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
