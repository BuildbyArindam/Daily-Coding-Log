/*
 * Problem   : 1657. Determine if Two Strings Are Close
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/determine-if-two-strings-are-close/
 * Date      : 2026-10-03
 * Difficulty: Medium
 * Topics    : Hash Table, String, Sorting, Counting
 *
 * Approach  :
 *   The two allowed operations (swap any two characters, and swap the
 *   identities of two existing characters) mean two strings are "close" iff:
 *     1. They have the same length.
 *     2. They use exactly the same set of distinct characters
 *        (tracked with a 26-bit mask).
 *     3. The sorted frequency counts match, so the frequencies can be
 *        redistributed among characters.
 *
 * Time      : O(n + 26 log 26) ~ O(n)
 * Space     : O(1)  (fixed-size 26-element arrays)
 */


// -------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    bool closeStrings(string word1, string word2) {
        if (word1.size() != word2.size()) {
            return false;
        }
        int a[26] = {0}, b[26] = {0}, mask1 = 0, mask2 = 0;
        for (int i = 0; i < word1.size(); i++) {
            a[word1[i] - 'a']++;
            b[word2[i] - 'a']++;
            mask1 |= 1 << (word1[i] - 'a');
            mask2 |= 1 << (word2[i] - 'a');
        };
        if (mask1 != mask2) {
            return false;
        }
        sort(begin(a), end(a));
        sort(begin(b), end(b));
        
        for (int i = 0; i < 26; i++) {
            if (a[i] != b[i]) return false;
        } 
        return true;
    }
};
