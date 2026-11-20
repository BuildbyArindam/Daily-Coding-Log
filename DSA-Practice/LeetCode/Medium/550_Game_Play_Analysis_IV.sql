/*
 * Problem   : 550. Game Play Analysis IV
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/game-play-analysis-iv/
 * Difficulty: Medium
 * Topics    : Database
 * Solved on : 2026-10-05
 *
 * Approach:
 *   1. Subquery: find each player's first login date (MIN(event_date) GROUP BY player_id).
 *   2. Keep rows where (player_id, event_date - 1 day) matches a (player_id, first_login)
 *      pair, which means the player logged in the day after their first login.
 *   3. Count those distinct players, divide by the total distinct players,
 *      and ROUND to 2 decimals.
 *
 * Time  : O(N log N) worst case (grouping/sorting N rows); ~O(N) with hash aggregation
 * Space : O(P), where P = number of distinct players (first-login results)
 */


---------------------------------------------- Solution -----------------------------------------------------


-- # Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN (SELECT player_id, MIN(event_date) AS first_login FROM ACTIVITY GROUP BY player_id)
