/*
 * Problem   : 1731. The Number of Employees Which Report to Each Employee
 * Platform  : LeetCode
 * Link      : https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
 * Difficulty: Easy
 * Topics    : Database, SQL, Joins, Aggregation
 * Date      : 2026-10-08
 *
 * Approach:
 *   Self-join the Employees table: e2 is the manager, e1 is the direct report
 *   (e1.reports_to = e2.employee_id). Group by manager, count the matched
 *   reports, and take the rounded average of the reports' ages. Managers with
 *   no reports drop out naturally due to the INNER JOIN. Order by employee_id.
 *
 * Time Complexity : O(N log N) - join (hash/index lookup) plus sort for ORDER BY
 * Space Complexity: O(M) - M = number of distinct managers held for grouping
 */


------------------------------------------------ Solution --------------------------------------------------------


-- # Write your MySQL query statement below
select e2.employee_id,e2.name, count(e2.employee_id) as reports_count, round(avg(e1.age *1.00),0) as average_age
from employees e1
inner join employees e2 on e1.reports_to = e2.employee_id
group by  e2.employee_id,e2.name
order by e2.employee_id asc
