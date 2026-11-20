/*
 * Problem:    1838. Frequency of the Most Frequent Element
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/frequency-of-the-most-frequent-element/
 * Difficulty: Medium
 * Topics:     Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum
 * Date:       2026-10-04
 *
 * Approach:   Sort + sliding window.
 *   After sorting, the best target for any window is its largest element
 *   (nums[right]), since raising smaller elements to it costs the least.
 *   A window [left, right] is valid if the cost to raise everything to
 *   nums[right] fits in k:
 *       nums[right] * windowSize - windowSum <= k
 *   Expand right each step; shrink left while the window is invalid.
 *   The answer is the largest valid window size.
 *
 * Time:  O(n log n)  - sorting dominates; the window pass is O(n)
 * Space: O(1)        - extra space (ignoring sort's internal stack)
 */


// ------------------------------------------- Solution ---------------------------------------------------


class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int left = 0, right = 0;
        long res = 0, total = 0;

        while (right < nums.size()) {
            total += nums[right];

            while (nums[right] * static_cast<long>(right - left + 1) > total + k) {
                total -= nums[left];
                left += 1;
            }

            res = max(res, static_cast<long>(right - left + 1));
            right += 1;
        }

        return static_cast<int>(res);        
    }
};
