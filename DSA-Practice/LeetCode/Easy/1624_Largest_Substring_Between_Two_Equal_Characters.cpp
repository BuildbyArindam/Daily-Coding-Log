/*
 * Problem : 1624. Largest Substring Between Two Equal Characters
 * Platform: LeetCode
 * Link    : https://leetcode.com/problems/largest-substring-between-two-equal-characters/
 * Difficulty: Easy
 * Topics  : Hash Table, String
 * Date    : 2026-10-03
 *
 * Approach (Brute Force):
 *   Check every pair of indices (left, right) with left < right. When
 *   s[left] == s[right], the substring between them has length
 *   right - left - 1. Keep the maximum, starting from -1 (returned if no
 *   character repeats).
 *
 * Time Complexity : O(n^2)
 * Space Complexity: O(1)
 */


// ------------------------------------- Solution ------------------------------------------------


class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int ans = -1;
        for (int left = 0; left < s.size(); left++) {
            for (int right = left + 1; right < s.size(); right++) {
                if (s[left] == s[right]) {
                    ans = max(ans, right - left - 1);
                }
            }
        }
        
        return ans;
    }
};
