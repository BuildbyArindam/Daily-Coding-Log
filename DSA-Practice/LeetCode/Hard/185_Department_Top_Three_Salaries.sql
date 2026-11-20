/*
 * Problem   : 185. Department Top Three Salaries
 * Platform  : LeetCode 
 * Difficulty: Hard 
 * Topic     : Database
 * Link      : https://leetcode.com/problems/department-top-three-salaries/
 * Date      : 2026-10-08
 *
 * Approach  : Join Employee with Department, then use DENSE_RANK() partitioned
 *             by department and ordered by salary DESC. DENSE_RANK (not RANK or
 *             ROW_NUMBER) ensures ties share a rank and no distinct salary
 *             value is skipped, so "top 3 unique salaries" is rank <= 3.
 *             The outer query filters to rank <= 3.
 *
 * Time      : O(N log N) - join plus sorting within each partition
 * Space     : O(N) - intermediate ranked result set
 */


------------------------------------------ Solution -------------------------------------------------


-- # Write your MySQL query statement below
SELECT Department, Employee, Salary
FROM (
    SELECT 
        d.name AS Department,
        e.name AS Employee,
        e.salary AS Salary,
        DENSE_RANK() OVER (PARTITION BY d.name ORDER BY Salary DESC) AS rnk
    FROM Employee e
    JOIN Department d
    ON e.departmentId = d.id
) AS rnk_tbl
WHERE rnk <= 3;
