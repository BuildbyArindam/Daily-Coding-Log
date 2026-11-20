/*
 * Problem : 2433. Find The Original Array of Prefix Xor
 * Platform: LeetCode
 * Link    : https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
 * Date    : 2026-10-07
 * Difficulty: Medium
 * Topics  : Array, Bit Manipulation
 *
 * Approach:
 *   pref[i] = pref[i-1] ^ arr[i]. XOR both sides with pref[i-1] and the
 *   pair cancels (x ^ x = 0), giving arr[i] = pref[i-1] ^ pref[i].
 *   The first element is the same in both arrays: arr[0] = pref[0].
 *
 * Time Complexity : O(n), single pass
 * Space Complexity: O(n) for the output array (O(1) extra)
 */


// --------------------------------------- Solution -----------------------------------------------------


class Solution {
    public int[] findArray(int[] pref) {
        int n = pref.length;
        int arr[] = new int[n];
        arr[0] = pref[0];

        for(int i=1; i<n; i++){
            arr[i] = pref[i-1]^pref[i];
        }
        return arr;
    }
}
