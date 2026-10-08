/*
 * Problem   : 1321. Restaurant Growth
 * Platform  : LeetCode 
 * Topic     : Database
 * Difficulty: Medium
 * Link      : https://leetcode.com/problems/restaurant-growth/
 * Date      : 2026-10-08
 *
 * Approach  : Use a window function with a RANGE frame over dates. For each
 *             visited_on, SUM(amount) covers the current day and the 6 days
 *             before it (a 7-day window). Customer has several rows per day,
 *             so the window result is identical for rows sharing a date, and
 *             DISTINCT collapses them to one row per day. OFFSET 6 drops the
 *             first 6 days, which don't have a full 7-day window yet. The
 *             average is the 7-day sum / 7, rounded to 2 decimals.
 *             (MySQL requires LIMIT to use OFFSET, hence the large LIMIT.)
 *
 * Time      : O(n log n), from sorting by visited_on for the window
 * Space     : O(n), for the window buffer
 */


---------------------------------------------- Solution -------------------------------------------


-- # Write your MySQL query statement below
SELECT DISTINCT
    visited_on,
    SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
    ROUND(SUM(amount) OVER(ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) / 7, 2) AS average_amount
FROM
    Customer
LIMIT 1000000
OFFSET 6
