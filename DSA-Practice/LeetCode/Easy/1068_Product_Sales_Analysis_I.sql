/*
 * Problem:    1068. Product Sales Analysis I
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/product-sales-analysis-i/
 * Difficulty: Easy
 * Topics:     Database, SQL, Joins
 * Date:       2026-10-04
 *
 * Approach:
 *   Sales holds product_id, year, and price, while the product name lives in
 *   Product. Join the two tables on product_id and select product_name, year,
 *   and price. product_id is a foreign key in Sales, so every sale row has a
 *   matching product and an INNER JOIN drops nothing.
 *
 * Time Complexity:  O(N + M) with a hash join, where N = rows in Sales and
 *                   M = rows in Product. O(N log M) with an indexed join on
 *                   Product.product_id.
 * Space Complexity: O(M) for the hash table built on Product (or O(1) extra
 *                   with an index lookup), plus the output rows.
 */


--------------------------------------------- Solution --------------------------------------------------------


-- # Write your MySQL query statement below
SELECT p.product_name, s.year, s.price
FROM Sales s
INNER JOIN Product p ON s.product_id = p.product_id;
