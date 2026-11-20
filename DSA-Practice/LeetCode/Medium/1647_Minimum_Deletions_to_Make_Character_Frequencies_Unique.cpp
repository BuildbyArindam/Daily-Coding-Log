/*
 * Problem   : 1647. Minimum Deletions to Make Character Frequencies Unique
 * Link      : https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
 * Platform  : LeetCode
 * Difficulty: Medium
 * Topics    : Hash Table, String, Greedy, Sorting
 * Date      : 2026-10-07
 *
 * Approach:
 *   Count the frequency of each letter and sort the 26 counts ascending.
 *   Walk from the second-largest to the smallest. Each count must be
 *   strictly less than the count to its right (after adjustment), so if
 *   freq[i] >= freq[i+1], lower it to max(0, freq[i+1] - 1) and add the
 *   difference to the deletion total. Counts that reach 0 are fine to repeat.
 *
 * Time Complexity : O(n + 26 log 26) = O(n)
 * Space Complexity: O(1)  (fixed-size array of 26)
 */


// -------------------------------------------------- Solution ------------------------------------------------------


class Solution {
public:
    int minDeletions(string s) {
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++; 
        }
        sort(freq.begin(), freq.end());
        int del = 0;
        for (int i = 24; i >= 0; i--) {
            if (freq[i] == 0) {
                break;
            }
            if (freq[i] >= freq[i + 1]) {
                int prev = freq[i];
                freq[i] = max(0, freq[i + 1] - 1);
                del += prev - freq[i];
            }
        }
        return del;
    }
};
