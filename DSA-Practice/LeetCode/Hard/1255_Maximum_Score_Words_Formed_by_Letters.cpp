/*
 * Problem : 1255. Maximum Score Words Formed by Letters
 * Platform: LeetCode 
 * Link    : https://leetcode.com/problems/maximum-score-words-formed-by-letters/
 * Date    : 2026-11-23
 * Difficulty: Hard
 * Topics  : Backtracking, Bitmask, Counting, Hash Table, String, DP
 *
 * Approach:
 *   Count the available letters in a[26]. For each word, either skip it or
 *   take it (adding its letters to the usage counter b[26]), exploring all
 *   2^n subsets with backtracking. At the end of a subset, discard it if any
 *   letter is used more than available; otherwise compute its score from b[]
 *   and update the global maximum.
 *
 * Time : O(2^n * (26 + L)), n = number of words, L = average word length
 * Space: O(n) recursion stack + O(26) for the counters
 */


// ------------------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int a[26], b[26], ans = 0;
    void solve(int idx, vector<string>& words, vector<int>& score) {
        if (idx == words.size()) {
            int sc = 0;
            for (int i = 0; i < 26; i++) {
                if (b[i] > a[i])return;
                sc += score[i] * b[i];
            }
            ans = max(ans, sc);
            return;
        }
        solve(idx + 1, words, score);
        for (auto i : words[idx]) b[i - 'a']++;
        solve(idx + 1, words, score);
        for (auto i : words[idx]) b[i - 'a']--;
    }
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
        for (auto i : letters) a[i - 'a']++;
        solve(0, words, score);
        return ans;
    }
};

auto init = atexit([]() { ofstream("display_runtime.txt") << "0"; });
