/*
 * Problem   : 1211. Queries Quality and Percentage
 * Platform  : LeetCode (Easy) 
 * Topic     : Database
 * Link      : https://leetcode.com/problems/queries-quality-and-percentage/
 * Date      : 2026-10-05
 *
 * Approach  :
 *   Group rows by query_name and compute two aggregates per group:
 *   - quality: AVG(rating / position), rounded to 2 decimals.
 *   - poor_query_percentage: share of rows with rating < 3, i.e.
 *     SUM(rating < 3) / COUNT(*) * 100, rounded to 2 decimals.
 *   The query_name IS NOT NULL filter drops rows with no query name.
 *
 * Time      : O(n) for the scan and aggregation (n = rows in Queries)
 * Space     : O(k) for the groups (k = distinct query_name values)
 */


------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below
SELECT 
   query_name, ROUND(AVG(rating/position), 2) AS quality,
   ROUND(
     SUM(IF(rating < 3, 1, 0))/COUNT(rating)*100,2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name;
