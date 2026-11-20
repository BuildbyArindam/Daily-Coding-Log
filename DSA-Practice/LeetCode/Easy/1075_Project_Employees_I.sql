/*
 * Problem:    1075. Project Employees I
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/project-employees-i/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-05
 *
 * Approach:
 *   Join Project with Employee on employee_id to attach each employee's
 *   experience_years to their project. Group by project_id and take the
 *   average of experience_years, rounded to 2 decimal places.
 *
 * Time Complexity:  O(P + E) for the join (hash join) plus O(R log R) for
 *                   grouping/sorting, where R is the number of joined rows.
 * Space Complexity: O(R) for the join result and group aggregates.
 */


---------------------------------- Solution -------------------------------------------------------


-- # Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project p
JOIN Employee e ON p.employee_id = e.employee_id
GROUP BY p.project_id
ORDER BY p.project_id;
