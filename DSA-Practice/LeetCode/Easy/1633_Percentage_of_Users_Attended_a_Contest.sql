/*
 * Problem:    1633. Percentage of Users Attended a Contest
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/percentage-of-users-attended-a-contest/
 * Difficulty: Easy
 * Topics:     Database, Aggregation, Subquery
 * Date:       2026-10-05
 *
 * Approach:
 *   Group the Register table by contest_id and count the distinct users in each
 *   contest. Divide by the total number of users (scalar subquery on Users),
 *   multiply by 100, and round to 2 decimals. Sort by percentage descending,
 *   with contest_id ascending as the tie-breaker.
 *
 * Time Complexity:  O(R + U), one scan of Register for grouping and one count of
 *                   Users. Sorting the C contests adds O(C log C).
 * Space Complexity: O(C) for the per-contest groups (plus the DISTINCT set per group).
 */


---------------------------------------- Solution --------------------------------------------------


-- # Write your MySQL query statement below
SELECT r.contest_id, 
       ROUND(COUNT(DISTINCT r.user_id) / (SELECT COUNT(*) FROM Users) * 100, 2) AS percentage
FROM Register r
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC;
