/*
 * Problem : 1759. Count Number of Homogenous Substrings
 * Link    : https://leetcode.com/problems/count-number-of-homogenous-substrings/
 * Platform: LeetCode 
 * Difficulty: Medium
 * Topics  : Math, String, Two Pointers
 * Date    : 2026-10-04
 *
 * Approach:
 *   Sliding window over runs of equal characters. `left` marks the start of the
 *   current run. For each index `right`, every substring ending at `right` that
 *   stays inside the run is homogenous, which gives (right - left + 1) new
 *   substrings. When s[right] differs from the run's character, a new run
 *   starts at `right` and contributes just 1 (the single character).
 *   Equivalent to summing k*(k+1)/2 over each run of length k.
 *   The sum is kept in a long long (max ~5e9 for n = 1e5) and reduced mod 1e9+7
 *   once at the end.
 *
 * Time : O(n)
 * Space: O(1)
 */


// ----------------------------------------- Solution ---------------------------------------------------------------


class Solution {
public:
    int countHomogenous(string s) {
        int left = 0;
        long long res = 0;
        
        for (int right = 0; right < s.length(); right++) {
            if (s[left] == s[right]) {
                res += right - left + 1;
            } else {
                res += 1;
                left = right;
            }
        }
        return (int) (res % (1000000007));     
    }
};
