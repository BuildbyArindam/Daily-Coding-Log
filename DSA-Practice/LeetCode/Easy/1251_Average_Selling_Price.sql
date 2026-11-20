/*
 * Problem    : 1251. Average Selling Price
 * Platform   : LeetCode
 * Link       : https://leetcode.com/problems/average-selling-price/
 * Difficulty : Easy
 * Topics     : Database
 * Date       : 2026-10-05
 *
 * Approach:
 *   LEFT JOIN Prices to UnitsSold on product_id, keeping only sales whose
 *   purchase_date falls within the price's [start_date, end_date] range.
 *   The date condition goes in the ON clause (not WHERE) so products with
 *   no sales still appear. Group by product and compute
 *   SUM(units * price) / SUM(units), rounded to 2 decimals.
 *   IFNULL turns the NULL average (no sales) into 0.
 *
 * Time  : O(P + U) with a hash/indexed join (worst case O(P * U) for a
 *         nested-loop join), plus grouping over the joined rows
 * Space : O(P) for the grouped results
 */


------------------------------------------- Solution ------------------------------------------------------


-- # Write your MySQL query statement below
SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id
