/*
 * Problem   : 1512. Number of Good Pairs
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/number-of-good-pairs/
 * Difficulty: Easy
 * Topics    : Array, Hash Table, Math, Counting
 * Date      : 2026-10-07
 *
 * Approach  : One-pass frequency counting. For each element x, every earlier
 *             occurrence of x forms one good pair with it, so add the
 *             current count of x to the answer, then increment the count.
 *
 * Time      : O(n)
 * Space     : O(k), where k = number of distinct values (k <= n)
 */


// -------------------------------------------- Solution -----------------------------------------------------


class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        int ans = 0;
        unordered_map<int, int> f;
        for (int& x : nums)
            ans += f[x]++;
        return ans;
    }
};
