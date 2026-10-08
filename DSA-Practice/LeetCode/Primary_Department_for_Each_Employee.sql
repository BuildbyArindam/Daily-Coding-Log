/*
 * Problem:    1789. Primary Department for Each Employee
 * Platform:   LeetCode
 * Link:       https://leetcode.com/problems/primary-department-for-each-employee/
 * Difficulty: Easy
 * Topics:     Database
 * Date:       2026-10-08
 *
 * Approach:
 *   An employee's primary department is either:
 *     (a) the row flagged primary_flag = 'Y', or
 *     (b) their only department, when they belong to just one
 *         (primary_flag is 'N' in that case).
 *   Query 1 selects all rows flagged 'Y'.
 *   Query 2 groups by employee_id and keeps those with exactly one
 *   department. Since employee_id is the group key, department_id is
 *   unambiguous (one row per group).
 *   UNION merges both results and removes duplicates, so a single-department
 *   employee who is also flagged 'Y' appears only once.
 *
 * Time Complexity:  O(n log n), dominated by grouping and the UNION dedupe
 *                   (sort or hash) over n rows.
 * Space Complexity: O(n) for intermediate results and the dedupe step.
 */


--------------------------------------------- Solution ----------------------------------------------------------


-- # Write your MySQL query statement below
select employee_id, department_id from employee
where primary_flag = 'Y' 
UNION
select employee_id, department_id from employee
group by employee_id
having count(department_id) = 1
