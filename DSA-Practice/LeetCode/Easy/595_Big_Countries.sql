/*
 * Problem:    595. Big Countries
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/big-countries/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-04
 *
 * Approach:
 *   A country is "big" if its area is at least 3,000,000 km² OR its
 *   population is at least 25,000,000. Filter the World table with a
 *   single WHERE clause using OR, and select name, population, area.
 *
 * Time Complexity:  O(n) - one full scan of the World table
 *                   (could be lower with indexes on area/population).
 * Space Complexity: O(1) - extra space; the result set is output only.
 */


------------------------------------------------ Solution ---------------------------------------------


-- # Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE (area >= 3000000 OR population >= 25000000);
