/*
 * Problem    : 1934. Confirmation Rate
 * Platform   : LeetCode
 * Link       : https://leetcode.com/problems/confirmation-rate/
 * Difficulty : Medium
 * Topics     : Database
 * Date       : 2026-10-05
 *
 * Approach:
 *   LEFT JOIN Signups -> Confirmations so users with no confirmation
 *   requests are kept. Group by user_id; (action = 'confirmed') evaluates
 *   to 1/0, so SUM(...) / COUNT(*) gives the confirmed ratio. Users with
 *   no requests get NULL from SUM, which IFNULL turns into 0. Round to 2
 *   decimals.
 *
 * Time  : O(S + C) for the join and aggregation (plus O(S log S) for ORDER BY)
 * Space : O(S) for the grouped result
 *         (S = rows in Signups, C = rows in Confirmations)
 */


------------------------------------------- Solution ----------------------------------------------------


-- # Write your MySQL query statement below
SELECT s.user_id,
      ROUND(
          IFNULL(SUM(c.action = 'confirmed') / COUNT(*), 0)
          , 2) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c ON s.user_id = c.user_id
GROUP BY s.user_id
ORDER BY s.user_id;
