/*
 * Problem   : 338. Counting Bits
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/counting-bits/
 * Difficulty: Easy
 * Topics    : Dynamic Programming, Bit Manipulation
 * Date      : 2026-10-07
 *
 * Approach:
 *   DP on the binary representation. For any i, right-shifting by one
 *   (i >> 1) drops the last bit, so:
 *       bits(i) = bits(i >> 1) + (i & 1)
 *   The answer for i >> 1 is already computed because i >> 1 < i.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1) extra (O(n) for the output array)
 */


// -------------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> ans(n+1, 0);
        for(int i=1; i<=n; i++){
            ans[i]=ans[i>>1]+(i&1);
        }
        return ans;
    }
};
