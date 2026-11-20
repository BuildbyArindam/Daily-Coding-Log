/*
 * Problem:    577. Employee Bonus
 * Platform:   LeetCode 
 * Difficulty: Easy
 * Topics:     Database
 * Link:       https://leetcode.com/problems/employee-bonus/
 * Solved on:  2026-10-04
 *
 * Approach:
 *   LEFT JOIN Employee to Bonus on empId so employees without a bonus
 *   row are retained (bonus = NULL). Filter for bonus IS NULL (no bonus
 *   record) OR bonus < 1000. The NULL check is required because
 *   comparisons with NULL evaluate to unknown and would drop those rows.
 *
 * Time:  O(N + M) with a hash join, O(N log M) with an index lookup,
 *        where N = rows in Employee, M = rows in Bonus
 * Space: O(1) extra beyond the result set (O(M) if the optimizer builds a hash table)
 */


------------------------------------------ Solution -------------------------------------------------


-- # Write your MySQL query statement below
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b ON e.empId = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;
