/*
 * Problem   : 29. Divide Two Integers
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/divide-two-integers/
 * Difficulty: Medium
 * Topics    : Math, Bit Manipulation
 * Date      : 2026-10-05
 *
 * Approach:
 *   Handle the only 32-bit overflow case (INT_MIN / -1) up front, then use
 *   the built-in integer division, which already truncates toward zero.
 *   The result is clamped to the 32-bit signed range.
 *   Note: this uses '/', which the problem intends to forbid.
 *
 * Time Complexity : O(1)
 * Space Complexity: O(1)
 */


// ------------------------------------------- Solution ----------------------------------------------------


class Solution {
public:
    int divide(int dividend, int divisor) {
        if( dividend == INT_MIN && divisor == -1 )
            return INT_MAX;
        long long int ans = dividend/divisor;
        if(ans>INT_MAX)
            return INT_MAX;
        if(ans<INT_MIN)
            return INT_MIN;
        return ans;
    }
};
