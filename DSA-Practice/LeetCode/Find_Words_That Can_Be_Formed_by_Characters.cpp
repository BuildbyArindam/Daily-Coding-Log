/*
 * Problem   : 1160. Find Words That Can Be Formed by Characters
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
 * Difficulty: Easy
 * Topics    : Array, Hash Table, String, Counting
 * Date      : 2026-10-03
 *
 * Approach:
 *   Count the frequency of each character in `chars`. For every word, count its
 *   own character frequencies and check that no letter is needed more times than
 *   `chars` provides. If the word is valid, add its length to the answer.
 *
 * Complexity:
 *   Time : O(m + L), where m = chars.length() and L = total characters across all words
 *   Space: O(1), since the maps hold at most 26 lowercase letters
 */


// --------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
    unordered_map<char, int> char_counts;
    for (char& c : chars) {
      ++char_counts[c];
    }

    int ans = 0;
    for (string& w : words) {
      unordered_map<char, int> word_counts;
      for (char& c : w) {
        ++word_counts[c];
      }

      bool ok = true;
      for (auto& pair : word_counts) {
        if (pair.second > char_counts[pair.first]) {
          ok = false;
          break;
        }
      }

      if (ok) {
        ans += w.size();
      }
    }

    return ans;
    }
};
