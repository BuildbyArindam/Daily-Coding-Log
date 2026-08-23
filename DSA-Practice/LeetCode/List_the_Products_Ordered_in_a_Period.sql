/*
Problem: List the Products Ordered in a Period
Platform: LeetCode
Link: https://leetcode.com/quest/database-quest/quiz/list-the-products-ordered-in-a-period/
Date Solved: 2026-08-23
Difficulty: Easy
Topic: SQL - Aggregation, GROUP BY, HAVING

Approach:
Join Products and Orders on product_id, filter orders to the
February 2020 date range, group by product to sum units ordered,
then keep only products whose total units sold in that window
is >= 100 (HAVING filters on the aggregate).

Time Complexity: O(n) — single pass over Orders joined with Products,
                  plus O(n log n) for the GROUP BY sort/hash step.
Space Complexity: O(n) — intermediate grouping structure sized to
                  distinct product_id count.
*/

--------------------------- Solution -------------------------------

SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o
    ON p.product_id = o.product_id
WHERE o.order_date >= '2020-02-01'
  AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name
HAVING SUM(o.unit) >= 100;
