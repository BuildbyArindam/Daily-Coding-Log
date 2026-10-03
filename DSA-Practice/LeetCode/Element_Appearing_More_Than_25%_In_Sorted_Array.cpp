/*
 * Problem : 1287. Element Appearing More Than 25% In Sorted Array
 * Platform: LeetCode (Easy)
 * Link    : https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
 * Date    : 2026-10-03
 * Topics  : Array
 *
 * Approach:
 *   The array is sorted, so equal values are contiguous. Let t = n / 4.
 *   An element occurring more than 25% of the time occurs at least t + 1 times,
 *   so it must occupy a contiguous block of length >= t + 1.
 *   Hence arr[i] == arr[i + t] for some i, and that arr[i] is the answer.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */


// ----------------------------------------- Solution -------------------------------------------------------


class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        int n = arr.size();
    int threshold = n / 4;
    for (int i = 0; i < n; ++i) {
      if (i + threshold < n && arr[i] == arr[i + threshold]) {
        return arr[i];
      } else if (i - threshold >= 0 && arr[i] == arr[i - threshold]) {
        return arr[i];
      }
    }
    return -1; 
    }
};
