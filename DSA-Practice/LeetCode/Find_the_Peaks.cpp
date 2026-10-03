/*
 * Problem   : 2951. Find the Peaks
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/find-the-peaks/
 * Difficulty: Easy
 * Topics    : Array, Enumeration
 * Date      : 2026-10-03
 *
 * Approach  : A peak must have two neighbours, so the first and last
 *             elements are skipped. Scan indices 1..n-2 and record i
 *             whenever mountain[i] is strictly greater than both
 *             mountain[i-1] and mountain[i+1].
 *
 * Time      : O(n), single pass
 * Space     : O(1) extra (excluding the output vector)
 */


// ------------------------------------ Solution ----------------------------------------------


class Solution {
public:
    vector<int> findPeaks(vector<int>& mountain) {
        vector<int> peaks;
        for (int i = 1; i < mountain.size() - 1; ++i) {
            if (mountain[i] > mountain[i - 1] && mountain[i] > mountain[i + 1]) {
                peaks.push_back(i);
            }
        }
        return peaks;
    }
};
