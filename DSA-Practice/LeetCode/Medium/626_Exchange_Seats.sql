/*
 * Problem   : 626. Exchange Seats
 * Platform  : LeetCode 
 * Link      : https://leetcode.com/problems/exchange-seats/
 * Difficulty: Medium
 * Topics    : Database
 * Date      : 2026-10-08
 *
 * Approach  :
 *   Swap every pair of consecutive seats by remapping ids:
 *     - odd id, not the last row  -> id + 1  (moves to the next seat)
 *     - even id                   -> id - 1  (moves to the previous seat)
 *     - odd id that is the last   -> unchanged (no partner to swap with)
 *   Student names stay attached to their rows; only ids change, then the
 *   result is sorted by the new id.
 *
 * Time      : O(n log n)  (dominated by ORDER BY; the MAX(id) subquery is O(n)
 *                          and evaluated once)
 * Space     : O(n)        (sorting the result set)
 */


--------------------------------------------- Solution ----------------------------------------------------


-- # Write your MySQL query statement below
SELECT 
    CASE 
        WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;
