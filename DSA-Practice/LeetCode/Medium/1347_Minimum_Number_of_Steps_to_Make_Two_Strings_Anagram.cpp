/*
 * Problem   : 1347. Minimum Number of Steps to Make Two Strings Anagram (LeetCode)
 * Link      : https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
 * Difficulty: Medium
 * Topics    : Hash Table, String, Counting
 * Date      : 2026-10-03
 *
 * Approach:
 *   Count the frequency of each letter in s and t using two 26-sized arrays.
 *   Both strings have equal length, so every surplus character in one string
 *   is matched by a deficit in the other. Summing |count_s[i] - count_t[i]|
 *   counts each mismatch twice (once as surplus, once as deficit), so the
 *   number of replacements needed is that sum divided by 2.
 *
 * Complexity:
 *   Time : O(n), one pass over each string plus a constant 26-letter scan
 *   Space: O(1), fixed-size arrays of 26 integers
 */


// ----------------------------------------- Solution -------------------------------------------------------------


class Solution {
public:
    int minSteps(string s, string t) {
        std::vector<int> count_s(26, 0);
        std::vector<int> count_t(26, 0);
        for (char ch : s) {
            count_s[ch - 'a']++;
        }
        for (char ch : t) {
            count_t[ch - 'a']++;
        }
        int steps = 0;
        for (int i = 0; i < 26; i++) {
            steps += std::abs(count_s[i] - count_t[i]);
        }
        return steps / 2;  
    }
};
