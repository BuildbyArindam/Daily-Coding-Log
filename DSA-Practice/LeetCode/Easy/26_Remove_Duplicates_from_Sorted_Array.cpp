/*
 * Problem   : 26. Remove Duplicates from Sorted Array
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
 * Date      : 2026-10-05
 * Difficulty: Easy
 * Topics    : Array, Two Pointers
 *
 * Approach  : Two pointers. `readIndex` scans the array, while `writeIndex`
 *             marks where the next unique value goes. Since the array is
 *             sorted, a value is new if it differs from the last unique
 *             value written (nums[writeIndex - 1]). Overwrite in place and
 *             return writeIndex as the count of unique elements.
 *
 * Time      : O(n), single pass
 * Space     : O(1), in-place
 */


// -------------------------------------- Solution --------------------------------------------------


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty()) return 0; 
        int writeIndex = 1;
        for (int readIndex = 1; readIndex < nums.size(); ++readIndex) {
            if (nums[readIndex] != nums[writeIndex - 1]) {
                nums[writeIndex++] = nums[readIndex];
            }
        }
        return writeIndex;
    }
};
