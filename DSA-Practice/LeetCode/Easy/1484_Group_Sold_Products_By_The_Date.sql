/*
 * Problem:    1484. Group Sold Products By The Date
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/group-sold-products-by-the-date/
 * Difficulty: Easy
 * Topics:     Database
 * Solved on:  2026-10-08
 *
 * Approach:
 *   Group rows by sell_date. For each group, COUNT(DISTINCT product) gives
 *   the number of unique products sold, and GROUP_CONCAT(DISTINCT product
 *   ORDER BY product SEPARATOR ',') builds the sorted, comma-separated
 *   product list. Final ORDER BY sell_date returns dates in ascending order.
 *
 * Time Complexity:  O(n log n) - grouping plus sorting the rows and
 *                   the concatenated products within each group
 * Space Complexity: O(n) - intermediate grouped results and concatenated strings
 */


------------------------------------ Solution ------------------------------------------------------


-- # Write your MySQL query statement below
SELECT sell_date,
		COUNT(DISTINCT(product)) AS num_sold, 
		GROUP_CONCAT(DISTINCT product ORDER BY product ASC SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date ASC
