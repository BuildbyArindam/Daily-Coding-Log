/*
 * Problem :   1204. Last Person to Fit in the Bus
 * Platform:   LeetCode
 * Link    :   https://leetcode.com/problems/last-person-to-fit-in-the-bus/
 * Difficulty: Medium
 * Topics  :   Database, Window Functions
 * Date    :   2026-10-08
 *
 * Approach:
 *   1. Use SUM(weight) OVER (ORDER BY turn) to compute the running total
 *      of weights in boarding order.
 *   2. Among rows where the running total <= 1000, take the largest turn.
 *   3. Return the person_name whose turn matches it.
 *
 * Time Complexity : O(n log n), dominated by sorting on `turn` for the window.
 * Space Complexity: O(n), for the CTE / window computation.
 */


------------------------------------ Solution --------------------------------------------------


-- # Write your MySQL query statement below
-- # Find the maximum number of turns among rows where 'tot_weight <= 1000'.

WITH CTE AS (
    SELECT 
        turn, person_name, weight,
        SUM(weight) OVER(ORDER BY turn ASC) AS tot_weight 
    FROM Queue
    ORDER BY turn
)
SELECT person_name
FROM Queue q
WHERE q.turn = (SELECT MAX(turn) FROM CTE WHERE tot_weight <= 1000);
