/*
 * Problem   : 1897. Redistribute Characters to Make All Strings Equal
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
 * Difficulty: Easy
 * Topics    : Hash Table, String, Counting
 * Date      : 2026-10-03
 *
 * Approach  : Moving characters between strings is free, so the strings can be
 *             made equal exactly when every letter's total count across all
 *             words is divisible by n (the number of words). Count each letter
 *             in a 26-slot array and check divisibility.
 *
 * Time      : O(L), where L = total number of characters across all words
 * Space     : O(1), fixed 26-element frequency array
 */


// ---------------------------------- Solution --------------------------------------------------------


class Solution {
public:
    bool makeEqual(vector<string>& words) {
        if (words.size() == 1) {
            return true;
        }
        int totalCharCount = 0;
        for (const string& s : words) {
            totalCharCount += s.length();
        }
        if (totalCharCount % words.size() != 0) {
            return false;
        }
        vector<int> myMap(26, 0);
        for (const string& s : words) {
            for (char c : s) {
                myMap[c - 'a']++;
            }
        }
        for (int i : myMap) {
            if (i % words.size() != 0) {
                return false;
            }
        }
        return true;
    }
};
