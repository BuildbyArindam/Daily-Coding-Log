/*
 * Problem:    76. Minimum Window Substring
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/minimum-window-substring/
 * Difficulty: Hard
 * Topics:     Hash Table, String, Sliding Window
 * Date:       2026-10-08
 *
 * Approach:
 *   Variable-size sliding window. `count[c]` holds how many more of
 *   character c the window still needs (negative = surplus). `required`
 *   tracks how many characters of t are still unmatched.
 *     - Expand r: decrement count[s[r]]; if it stays >= 0, that char was
 *       needed, so decrement `required`.
 *     - When required == 0 the window is valid: record it if it's the
 *       shortest so far, then shrink from l. Incrementing count[s[l]]
 *       above 0 means we just dropped a needed char, so `required`
 *       goes back up and the shrink loop ends.
 *
 * Time:  O(|s| + |t|)  (each index is visited at most twice by r and l)
 * Space: O(1)          (fixed 128-size array for ASCII)
 */


// ------------------------------------------ Solution -----------------------------------------------


class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> count(128);
    int required = t.length();
    int bestLeft = -1;
    int minLength = s.length() + 1;

    for (const char c : t)
      ++count[c];

    for (int l = 0, r = 0; r < s.length(); ++r) {
      if (--count[s[r]] >= 0)
        --required;
      while (required == 0) {
        if (r - l + 1 < minLength) {
          bestLeft = l;
          minLength = r - l + 1;
        }
        if (++count[s[l++]] > 0)
          ++required;
      }
    }

    return bestLeft == -1 ? "" : s.substr(bestLeft, minLength);
    }
};
