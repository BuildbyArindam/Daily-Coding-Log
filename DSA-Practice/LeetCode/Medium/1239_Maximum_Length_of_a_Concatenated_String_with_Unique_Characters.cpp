/*
 * Problem : 1239. Maximum Length of a Concatenated String with Unique Characters
 * Link    : https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
 * Platform: LeetCode 
 * Difficulty: Medium
 * Topics  : Array, String, Backtracking, Bit Manipulation
 * Date    : 2026-10-03
 *
 * Approach:
 *   Backtracking over subsets. For each index, try appending arr[i] to the
 *   current string if the combined characters stay unique, then recurse on
 *   i + 1. Track the longest valid length seen at any node.
 *
 * Time  : O(2^n * L), n = arr.size(), L <= 26 (cost of each uniqueness check)
 * Space : O(n + L) recursion depth plus the current string
 */


// ---------------------------------------- Solution ----------------------------------------------------------------


class Solution {
public:
    int n = 0;
    int curMax = 0;
    int maxLength(vector<string>& arr) {
        n = arr.size();
        string cur = "";
        dfs(arr, 0, cur);
        return curMax;
    }
    void dfs(vector<string>& arr, int idx, string s) {
        cout << idx << s << endl;
        curMax = max(curMax, (int)s.length());
        for(int i = idx; i < n; i ++) {
            cout << "checking " << s << " " << arr[i] << endl;
            if(check(s, arr[i])) {
                dfs(arr, i+1, s + arr[i]);
            }
        }
    }
    bool check(string s1, string s2) {
        vector<int> count(26, 0);

        for(char c : s1) {
            if(count[c - 'a'] > 0)
                return false;
            count[c - 'a'] ++;
        }
        for(char c : s2) {
            if(count[c - 'a'] > 0)
                return false;
            count[c - 'a'] ++;
        }
        return true;
    }
};
