/*
 * Problem:    176. Second Highest Salary
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/second-highest-salary/
 * Difficulty: Medium
 * Topics:     Database
 * Date:       2026-10-08
 *
 * Approach:
 *   Find the overall max salary with a scalar subquery, then take the max
 *   of all salaries strictly less than it. That value is the second highest
 *   distinct salary. If no such row exists (e.g. only one distinct salary),
 *   MAX over an empty set returns NULL, which matches the required output.
 *
 * Time Complexity:  O(n) - two scans of the Employee table
 * Space Complexity: O(1) - no extra storage beyond scalar results
 */


----------------------------------------- Solution ----------------------------------------------------


-- # Write your MySQL query statement below
select max(salary) as secondhighestsalary
from employee 
where salary <> (select max(salary) from employee )
