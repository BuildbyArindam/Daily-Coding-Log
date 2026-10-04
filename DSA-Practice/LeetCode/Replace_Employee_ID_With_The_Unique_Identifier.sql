/*
 * Problem   : Replace Employee ID With The Unique Identifier
 * Platform  : LeetCode  
 * Difficulty: Easy
 * Topic     : Database
 * Link      : https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
 * Date      : 2026-10-04
 *
 * Approach  : LEFT JOIN Employees to EmployeeUNI on id. Employees without a
 *             mapping are kept, with unique_id returned as NULL.
 *             ORDER BY is optional here (any order is accepted).
 *
 * Time      : O(N + M) with a hash join, O(N log M) with an index on EmployeeUNI.id
 *             (N = rows in Employees, M = rows in EmployeeUNI)
 * Space     : O(1) extra, excluding the output
 */


---------------------------------------- Solution ---------------------------------------------


-- # Write your MySQL query statement below
SELECT EmployeeUNI.unique_id, Employees.name
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id
ORDER BY Employees.id ASC;
