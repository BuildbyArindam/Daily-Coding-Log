/*
 * Problem:    27. Remove Element
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/remove-element/
 * Difficulty: Easy
 * Topics:     Array, Two Pointers
 * Date:       2026-10-05
 *
 * Approach:   Two pointers (read/write). readIndex scans every element;
 *             whenever nums[readIndex] != val, copy it to nums[writeIndex]
 *             and advance writeIndex. The first writeIndex elements end up
 *             holding all values not equal to val, in original order.
 *
 * Time:       O(n)  - single pass over the array
 * Space:      O(1)  - in-place, no extra storage
 */


// ------------------------------------------ Solution -----------------------------------------------------


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int writeIndex = 0;
        for (int readIndex = 0; readIndex < nums.size(); ++readIndex) {
            if (nums[readIndex] != val) {
                nums[writeIndex++] = nums[readIndex];
            }
        }
        return writeIndex;
    }
};
