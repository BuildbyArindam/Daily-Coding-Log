/*
 * Problem   : 455. Assign Cookies
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/assign-cookies/
 * Difficulty: Easy
 * Topics    : Array, Two Pointers, Greedy, Sorting
 * Date      : 2026-10-03
 *
 * Approach  : Greedy + two pointers.
 *   Sort greed factors (g) and cookie sizes (s). Walk through the cookies
 *   from smallest to largest, and give each cookie to the least greedy
 *   child who is still unsatisfied. If the cookie is big enough
 *   (g[i] <= s[j]), that child is content and we move to the next child.
 *   Otherwise the cookie is too small for every remaining child, so skip it.
 *   The number of children satisfied is i.
 *
 * Time      : O(n log n + m log m)  (sorting dominates; the scan is O(n + m))
 * Space     : O(1) extra (ignoring the sort's O(log n) stack space; sorts in place)
 */


// ---------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int i = 0;
        for(int j=0; i<g.size() && j<s.size(); j++)
          if(g[i]<=s[j]) i++;
        return i;
    }
};
