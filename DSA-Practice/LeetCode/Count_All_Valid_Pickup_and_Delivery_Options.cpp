/*
 * Problem    : 1359. Count All Valid Pickup and Delivery Options
 * Link       : https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
 * Platform   : LeetCode
 * Difficulty : Hard
 * Topics     : Math, Dynamic Programming, Combinatorics
 * Date       : 2026-10-07
 *
 * Approach:
 *   Build the answer incrementally. Suppose there are already n-1 valid
 *   orders, which occupy 2(n-1) slots. To add the n-th pair (P_n, D_n),
 *   the sequence has 2n slots in total:
 *     - P_n can go in any of 2n-1 gaps... counted jointly with D_n, there are
 *       C(2n, 2) = n(2n-1) ways to pick two positions, and D_n must come
 *       after P_n, so each pair of positions gives exactly one valid placement.
 *   Recurrence: f(n) = f(n-1) * n * (2n - 1), with f(1) = 1.
 *   Take the result modulo 1e9 + 7 at each step to avoid overflow.
 *
 * Time  : O(n)
 * Space : O(1)
 */


// ---------------------------------------------- Solution -------------------------------------------------------


class Solution {
public:
    int countOrders(int n) {
        long res = 1, mod = 1e9 + 7;
        for (int i = 1; i <= n; ++i)
            res = res * (i * 2 - 1) * i % mod;
        return res;
    }
};
