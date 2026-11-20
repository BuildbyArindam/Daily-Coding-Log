/*
 * Problem:    197. Rising Temperature (LeetCode)
 * Link:       https://leetcode.com/problems/rising-temperature/
 * Difficulty: Easy
 * Topics:     Database, SQL, Self Join
 * Solved on:  2026-10-04
 *
 * Approach:
 *   Self-join the Weather table on itself, pairing each row (w) with the
 *   row from the previous calendar day (w_prev). Matching on
 *   w.recordDate = DATE_ADD(w_prev.recordDate, INTERVAL 1 DAY) ensures we
 *   compare consecutive dates rather than consecutive rows, so gaps in the
 *   data are handled correctly. Filter where w.temperature is higher.
 *
 * Complexity:
 *   Time:  O(n) with an index on recordDate (hash/index join),
 *          O(n^2) worst case without one.
 *   Space: O(1) extra (O(n) if the engine materializes the join).
 */


------------------------------------------- Solution ----------------------------------------------------


-- # Write your MySQL query statement below
SELECT w.id
FROM Weather w
INNER JOIN Weather w_prev ON w.recordDate = DATE_ADD(w_prev.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > w_prev.temperature;
