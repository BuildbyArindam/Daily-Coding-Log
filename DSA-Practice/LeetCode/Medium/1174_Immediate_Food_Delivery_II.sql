/*
 * Problem:    1174. Immediate Food Delivery II
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/immediate-food-delivery-ii/
 * Difficulty: Medium
 * Topics:     Database
 * Date:       2026-10-05
 *
 * Approach:
 *   1. Use a CTE (FirstOrders) to keep only each customer's first order,
 *      identified via a correlated subquery on MIN(order_date).
 *   2. An order is "immediate" if order_date = customer_pref_delivery_date.
 *   3. Percentage = immediate first orders / total first orders * 100,
 *      rounded to 2 decimals.
 *
 * Time Complexity:  O(N^2) worst case for the correlated subquery without an
 *                   index; O(N log N) with an index on (customer_id, order_date).
 * Space Complexity: O(C), where C is the number of customers (CTE rows).
 */


------------------------------------ Solution ---------------------------------------------------


-- # Write your MySQL query statement below
WITH FirstOrders AS (
   SELECT *
   FROM Delivery d
   WHERE d.order_date = (SELECT MIN(order_date) FROM Delivery WHERE customer_id = d.customer_id)
)
SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS immediate_percentage
FROM FirstOrders;
