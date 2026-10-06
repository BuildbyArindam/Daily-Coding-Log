/**
 * Problem   : 1095. Find in Mountain Array
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/find-in-mountain-array/
 * Date      : 2026-10-07
 * Difficulty: Hard
 * Topics    : Array, Binary Search, Interactive
 *
 * Approach  :
 *   1. Binary search for the peak: if arr[mid] < arr[mid+1], the peak is
 *      to the right, otherwise it is at mid or to the left.
 *   2. Binary search the ascending part [0, peak] for the target.
 *   3. If not found, binary search the descending part [peak, n-1]
 *      (comparison direction reversed).
 *   The left side is searched first, so the smallest valid index is returned.
 *
 * Complexity:
 *   Time  : O(log n), about 3 binary searches, which stays within the
 *           100 get() call limit.
 *   Space : O(1)
 */


// -------------------------------------------------- Solution ---------------------------------------------------------


/**
 * // This is the MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * class MountainArray {
 *   public:
 *     int get(int index);
 *     int length();
 * };
 */

class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int maxPosition = -1;
        int left = 1;
        int right = n - 2;
        int mid;

        while (left < right) {
            mid = left + (right - left) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        maxPosition = left;
        left = 0;
        right = maxPosition;
        int me;

        while (left <= right) {
            mid = left + (right - left) / 2;
            me = mountainArr.get(mid);

            if (me == target) return mid;
            if (me > target) right = mid - 1;
            else left = mid + 1;
        }
        left = maxPosition;
        right = n - 1;

        while (left <= right) {
            mid = left + (right - left) / 2;
            me = mountainArr.get(mid);

            if (me == target) return mid;
            if (me < target) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
};
