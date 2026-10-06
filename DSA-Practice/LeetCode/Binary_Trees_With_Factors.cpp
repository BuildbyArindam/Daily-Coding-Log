/*
 * Problem   : 823. Binary Trees With Factors
 * Link      : https://leetcode.com/problems/binary-trees-with-factors/
 * Platform  : LeetCode 
 * Difficulty: Medium
 * Date      : 2026-10-07
 * Topics    : Array, Hash Table, Dynamic Programming, Sorting
 *
 * Approach:
 *   Sort the array. Let dp[i] = number of valid trees with arr[i] as root.
 *   Every node starts with 1 (the single-node tree). For each arr[i], use two
 *   pointers p, q over the smaller elements to find pairs with
 *   arr[p] * arr[q] == arr[i]:
 *     - p == q : adds dp[p] * dp[q]
 *     - p != q : adds 2 * dp[p] * dp[q]   (left/right children can swap)
 *   The answer is the sum of all dp[i] mod 1e9+7.
 *
 * Time : O(n^2)  (sort O(n log n) + two-pointer scan per element)
 * Space: O(n)    (dp array)
 */


// ----------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    const int mod = 1e9 + 7;
    int numFactoredBinaryTrees(vector<int>& arr) {
        int n = arr.size();
        sort(arr.begin(), arr.end());
        vector<long> dp(n);
        dp[0] = 1;
        int res = 0;
        for (int i = 1; i < n; i++)
        {
            int target = arr[i];
            int p = 0, q = i - 1; 
            long ways = 1;
            while(p <= q)
            {
                long mul = (((long)arr[p]) * (arr[q]));
                if (mul == target) 
                {
                    if (p == q) ways += (dp[p] * dp[q]) % mod;
                    else ways += ((dp[p] * dp[q]) * 2) % mod;
                    p++;
                    q--;
                }
                else if (mul < target) p++;
                else if (mul > target) q--;
            }
            dp[i] = ways;
            res  = (int)((res + dp[i]) % mod);
        }
        return res + 1;
    }
};
