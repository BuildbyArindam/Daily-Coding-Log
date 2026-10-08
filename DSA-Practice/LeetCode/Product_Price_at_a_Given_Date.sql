/*
 * Problem:    1164. Product Price at a Given Date
 * Link:       https://leetcode.com/problems/product-price-at-a-given-date/
 * Platform:   LeetCode 
 * Difficulty: Medium
 * Topic:      Database
 * Solved on:  2026-10-08
 *
 * Approach:
 *   1. CTE: keep only price changes on or before 2019-08-16, then rank each
 *      product's changes by change_date DESC. Rank 1 = latest price as of that date.
 *   2. Select rank-1 rows -> products that had a price change by the cutoff.
 *   3. UNION with products whose changes all happened after the cutoff
 *      (absent from the CTE) and assign the default price of 10.
 *
 * Complexity:
 *   Time:  O(n log n), dominated by the window function's partition sort.
 *   Space: O(n) for the CTE and window buffers.
 */


----------------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below
WITH cte AS (
  SELECT *, 
  RANK() OVER(
    PARTITION BY product_id 
    ORDER BY change_Date DESC
  ) price_priority 
  FROM Products 
  WHERE change_date <= '2019-08-16'
)

SELECT product_id, new_price AS price 
FROM cte
WHERE price_priority = 1

UNION

SELECT product_id, 10 AS price 
FROM Products
WHERE product_id NOT in (
  SELECT product_id
  FROM cte
)
