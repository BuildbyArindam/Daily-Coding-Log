/*
 * Problem   : 1048. Longest String Chain
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/longest-string-chain/
 * Difficulty: Medium
 * Topics    : Array, Hash Table, Two Pointers, String, Dynamic Programming, Sorting
 * Date      : 2026-10-07
 *
 * Approach  : Sort + DP with hash map
 *   - Sort words by length so every possible predecessor is processed first.
 *   - dp[w] = length of the longest chain ending at word w.
 *   - For each word, delete one character at a time to form every possible
 *     predecessor; dp[w] = 1 + max(dp[predecessor]) (missing predecessors count as 0).
 *   - Answer is the max dp value across all words.
 *
 * Time      : O(n log n + n * L^2)
 *             n = number of words, L = max word length
 *             (L deletions per word, each costing O(L) to build and hash)
 * Space     : O(n * L) for the hash map
 */


// ------------------------------------------ Solution --------------------------------------------------------


class Solution {
public:
    static bool cmp(const string &s1, const string &s2) {
        return s1.length() < s2.length();
    }

    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), cmp);
        unordered_map<string, int> ump;
        int ans = 0;
        for (string w : words) {
            int longest=0;
            for (int i = 0; i < w.length(); i++) {
                string sub = w;
                sub.erase(i, 1);
                longest = max(longest,ump[sub]+1);
            }
            ump[w] = longest;
            ans = max(ans,longest);
        }
        return ans;  
    }
};
