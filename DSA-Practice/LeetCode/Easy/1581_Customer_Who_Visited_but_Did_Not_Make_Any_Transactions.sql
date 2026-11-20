/*
 * Problem:    1581. Customer Who Visited but Did Not Make Any Transactions
 * Platform:   LeetCode 
 * Difficulty: Easy
 * Topic:      Database
 * Link:       https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
 * Date:       2026-10-04
 *
 * Approach:
 *   LEFT JOIN Visits to Transactions on visit_id. Visits with no matching
 *   transaction have NULL on the Transactions side, so filter with
 *   t.visit_id IS NULL. Group by customer_id and COUNT(*) to get the
 *   number of transaction-free visits per customer.
 *
 * Time:  O(V + T) with a hash join (O(V log T) with an index lookup),
 *        plus O(K log K) for ORDER BY over K distinct customers.
 * Space: O(K) for the grouped result (plus the join's hash table).
 *
 * Note: ORDER BY is optional here, since the problem accepts any order.
 */


--------------------------------------- Solution -----------------------------------------------------------


-- # Write your MySQL query statement below
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id
ORDER BY v.customer_id ASC;
